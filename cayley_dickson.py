from math_dunders import math_dunders


class Number:
    def copy(self):
        return self.__class__(self)

    def norm_squared(self):  # Returns base type.
        return (self.conj() * self).real_coefficient()

    def inverse(self):
        return self.conj() / self.norm_squared()

    def __len__(self):
        return self.dimensions

    @classmethod
    # Creates a table akin to the one at wikipedia.org/wiki/Octonion#Definition.
    def e_matrix(cls, table=True, raw=False, e="e"):
        base = cls.base()
        zero, one = base(), base(1)
        args = [zero] * cls.dimensions
        ees = []
        for i in range(cls.dimensions):
            args[i] = one
            ees.append(cls(*args))
            args[i] = zero

        def format(cell):
            if not raw:
                i, c = next(((i, c) for i, c in enumerate(cell.coefficients()) if c))
                cell = f"{e}{i}"
                if c < 0:
                    cell = "-" + cell
            return cell

        matrix = [[format(i * j) for j in ees] for i in ees]

        if table:
            matrix = [[*map(str, row)] for row in matrix]
            length = max(len(cell) for row in matrix for cell in row)
            return '\n'.join(' '.join(cell.rjust(length) for cell in row)[1:] for row in matrix) + '\n'
        return matrix


def reals(base=float):
    @ math_dunders(base=base)
    class Real(Number, base):
        dimensions = 1

        @ staticmethod
        def base():
            return base

        def real_coefficient(self):  # Returns base type.
            return base(self)

        def coefficients(self):  # Returns tuple of base type.
            return (self.real_coefficient(),)

        def conj(self):
            return self.copy()

        def __str__(self):
            return f"{self:g}"

        def __repr__(self):
            return str(self)

    return Real


def cayley_dicksonize(basis):
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

        @ staticmethod
        def coerce(other):
            try:
                return Hypercomplex(other)
            except TypeError:
                return None

        @ staticmethod
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

        def __str__(self):
            coefficients = [f"{c:g}" for c in self.coefficients()]
            return "(" + ' '.join(coefficients) + ")"

        def __repr__(self):
            return f"{Hypercomplex.__name__}[{len(self)}]" + str(self)

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
            if type(other) is base:  # Short circuit base type to avoid infinite recursion in inverse().
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
        numbers = cayley_dicksonize(numbers)
    return numbers


Real = reals()                                                            # level 0 = 1 dimension
Complex = cayley_dicksonize(Real)                                         # level 1 = 2 dimensions
Quaternion = cayley_dicksonize(Complex)                                   # level 2 = 4 dimensions
Octonion = cayley_dicksonize(Quaternion)                                  # level 3 = 8 dimensions
Sedenion = cayley_dicksonize(Octonion)                                    # level 4 = 16 dimensions
Trigintaduonion = cayley_dicksonize(Sedenion)                             # level 5 = 32 dimensions
Sexagintaquatronions = cayley_dicksonize(Trigintaduonion)                 # level 6 = 64 dimensions
Centumduodetrigintanions = cayley_dicksonize(Sexagintaquatronions)        # level 7 = 128 dimensions
Ducentiquinquagintasexions = cayley_dicksonize(Centumduodetrigintanions)  # level 8 = 256 dimensions

# Todo e matrix
print(Real.e_matrix())
print(Complex.e_matrix())
print(Quaternion.e_matrix())
print(cayley_dickson_algebra(5).e_matrix(table=False, e=""))
