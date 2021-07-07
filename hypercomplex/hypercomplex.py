from mathdunders import dunders, mathdunders


class Number:
    def copy(self):
        return self.__class__(self)

    def norm_squared(self):  # Returns base type.
        return (self.conj() * self).real_coefficient()

    def inverse(self):
        return self.conj() / self.norm_squared()

    def __len__(self):
        return self.dimensions

    def __getitem__(self, index):
        return self.coefficients()[index]

    def __str__(self):
        return format(self)

    def __repr__(self):
        return f"{self.__class__.__name__}[{len(self)}]" + str(self)

    def __format__(self, format_spec):
        if not format_spec:
            format_spec = "g"
        coefficients = [f"{c:{format_spec}}" for c in self.coefficients()]
        return "(" + ' '.join(coefficients) + ")"

    @classmethod
    def e(cls, index):
        base = cls.base()
        coefficients = [base()] * cls.dimensions
        coefficients[index] = base(1)
        return cls(*coefficients)

    @classmethod
    # Creates a table akin to the one at wikipedia.org/wiki/Octonion#Definition.
    def e_matrix(cls, table=True, raw=False, e="e"):
        def format_cell(cell):
            if not raw:
                i, c = next(((i, c) for i, c in enumerate(cell.coefficients()) if c))
                cell = f"{e}{i}"
                if c < 0:
                    cell = "-" + cell
            return cell

        ees = list(map(cls.e, range(cls.dimensions)))
        matrix = [[format_cell(i * j) for j in ees] for i in ees]

        if table:
            matrix = [list(map(str, row)) for row in matrix]
            length = max(len(cell) for row in matrix for cell in row)
            offset = length - max(len(row[0]) for row in matrix)
            rows = [' '.join(cell.rjust(length) for cell in row)[offset:] for row in matrix]
            return '\n'.join(rows) + '\n'
        return matrix


def reals(base=float):
    @mathdunders(base=base)
    class Real(Number, base):
        dimensions = 1

        @staticmethod
        def base():
            return base

        def real_coefficient(self):  # Returns base type.
            return base(self)

        def coefficients(self):  # Returns tuple of base type.
            return (self.real_coefficient(),)

        def conj(self):
            return self.copy()

    return Real


def cayley_dickson_construction(basis):
    class Hypercomplex(Number):
        dimensions = 2 * basis.dimensions

        # a is the "real" half. b is the "imaginary" half.
        def __init__(self, *args, pair=False):
            if pair:
                self.a, self.b = map(basis, args)
            else:
                if len(args) == 1 and hasattr(args[0], 'coefficients'):
                    args = args[0].coefficients()
                if len(args) > len(self):
                    raise TypeError(f"Too many args. Got {len(args)} expecting at most {len(self)}.")
                if len(self) != len(args):
                    args += (Hypercomplex.base()(),) * (len(self) - len(args))
                self.a = basis(*args[:len(self)//2])
                self.b = basis(*args[len(self)//2:])

        @staticmethod
        def coerce(other):
            try:
                return Hypercomplex(other)
            except TypeError:
                return None

        @staticmethod
        def base():
            return basis.base()

        def real_coefficient(self):  # Returns base type.
            return self.a.real_coefficient()

        def coefficients(self):  # Returns tuple of base type.
            return self.a.coefficients() + self.b.coefficients()

        def conj(self):
            return Hypercomplex(self.a.conj(), -self.b, pair=True)

        def __bool__(self):
            return bool(self.a) or bool(self.b)

        def __eq__(self, other):
            coerced = Hypercomplex.coerce(other)
            if coerced is None:
                self = other.__class__.coerce(self)
            else:
                other = coerced
            return self.a == other.a and self.b == other.b

        # Unary Math Dunders:

        def __abs__(self):  # Returns base type.
            return self.norm_squared()**0.5

        def __neg__(self):
            return Hypercomplex(-self.a, -self.b, pair=True)

        def __pos__(self):
            return Hypercomplex(+self.a, +self.b, pair=True)

        # Binary Math Dunders:

        def __add__(self, other):
            other = Hypercomplex.coerce(other)
            if other is None:
                return NotImplemented
            return Hypercomplex(self.a + other.a, self.b + other.b, pair=True)

        def __radd__(self, other):
            return Hypercomplex(other) + self  # Should never raise TypeError.

        def __mul__(self, other):
            other = Hypercomplex.coerce(other)
            if other is None:
                return NotImplemented
            a = self.a * other.a - other.b.conj() * self.b
            b = other.b * self.a + self.b * other.a.conj()
            return Hypercomplex(a, b, pair=True)

        def __rmul__(self, other):
            return Hypercomplex(other) * self

        def __pow__(self, other):  # Only valid if other is an integer.
            if not isinstance(other, int):
                return NotImplemented

            value = Hypercomplex(Hypercomplex.base()(1))
            if other:
                multiplier = self if other > 0 else self.inverse()
                for _ in range(abs(other)):
                    value *= multiplier
            return value

        def __sub__(self, other):
            other = Hypercomplex.coerce(other)
            if other is None:
                return NotImplemented
            return Hypercomplex(self.a - other.a, self.b - other.b, pair=True)

        def __rsub__(self, other):
            return Hypercomplex(other) - self

        def __truediv__(self, other):
            base = Hypercomplex.base()
            if isinstance(other, base):  # Short circuit base type to avoid infinite recursion in inverse().
                other = base(1) / other
            else:
                other = Hypercomplex.coerce(other)
                if other is None:
                    return NotImplemented
                other = other.inverse()
            return self * other

        def __rtruediv__(self, other):
            return Hypercomplex(other) / self

    return Hypercomplex


def cayley_dickson_algebra(level, base=float):
    if not isinstance(level, int) or level < 0:
        raise ValueError("The level must be a positive integer.")
    numbers = reals(base)
    for _ in range(level):
        numbers = cayley_dickson_construction(numbers)
    return numbers


cd_construction = cayley_dickson_construction
cd_algebra = cayley_dickson_algebra

# Named based on https://www.mapleprimes.com/DocumentFiles/124913/419426/Figure1.JPG
R = Real = CD1 = reals()                               # level 0 -> 1 dimension
C = Complex = CD2 = cayley_dickson_construction(R)     # level 1 -> 2 dimensions
Q = Quaternion = CD4 = cayley_dickson_construction(C)  # level 2 -> 4 dimensions
O = Octonion = CD8 = cayley_dickson_construction(Q)    # level 3 -> 8 dimensions
S = Sedenion = CD16 = cayley_dickson_construction(O)   # level 4 -> 16 dimensions
P = Pathion = CD32 = cayley_dickson_construction(S)    # level 5 -> 32 dimensions
X = Chingon = CD64 = cayley_dickson_construction(P)    # level 6 -> 64 dimensions
U = Routon = CD128 = cayley_dickson_construction(X)    # level 7 -> 128 dimensions
V = Voudon = CD256 = cayley_dickson_construction(U)    # level 8 -> 256 dimensions


# # http://sites.science.oregonstate.edu/coursewikis/GO/book/go/sedenions.html
# e = Sedenion(Octonion(0), Octonion(1), pair=True)
# e2 = Sedenion(Octonion(1), Octonion(0), pair=True)
# p = Octonion(1, 2, 3, 4, 5, 6, 7, 8)

# # print(p * e2 == p)
# # print(p * e)  # it works!

# # print(Trigintaduonion.e_matrix())

# i = Sedenion.e(1)
# j = Sedenion.e(2)
# k = Sedenion.e(3)
# l = Sedenion.e(4)

# p = i*l + j*e
# q = j*l + i*e

# p = Quaternion(0, 1.234, 5, -6)

# # p = Real(900)

# print(p)
# print(str(p))
# print(repr(p))
# print(f"{p:0.05f}")
# print(format(p))
# exit()

# print(f'{e = !s}')
# print(f'{i = !s}')
# print(f'{j = !s}')
# # print(f'{k = !s}')6
# print(f'{l = !s}')
# print()

# print(f'{p = !s}')
# print(f'{q = !s}')
# print(f'{p*q = !s}')
# print(f'{1/p = !s}')
# print(f'{1/q = !s}')
# # print(f'{-2/p == p }')
# print(f'{(1/p)*(1/q) = !s}')

# # il = Sedenion.e(5)
# # il = Sedenion.e(9)
# # je = Sedenion.e()
# # jl = Sedenion.e()
# # ie = Sedenion.e()


# TODO
# contains
# handle complex nums nicely, use real part of others
# test suite
# method documentation
# tox?
# .real and .imag ? rename conjugate
# check for and descend from import numbers ... isinstance(x, Number)?
