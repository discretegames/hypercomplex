from decimal import Decimal
from math_dunders import math_dunders


class Number:
    def copy(self):
        return self.__class__(self)

    def norm_squared(self):
        return self.conj() * self

    def __len__(self):
        return self.dimensions


def reals(base=float):
    @math_dunders(base=base)
    class Real(Number, base):
        dimensions = 1

        @staticmethod
        def base():
            return base

        def coefficients(self):
            return (base(self),)

        def real(self):
            return base(self)  # todo should this be copy?

        def inverse(self):
            pass  # todo

        def conj(self):
            return self.copy()

    return Real


def cayley_dicksonize(basis):
    class Hypercomplex(Number):
        dimensions = 2 * basis.dimensions  # TODO use dimensions for type casting?

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

        # Core Methods:

        @staticmethod
        def coerce(other):
            try:
                return Hypercomplex(other)
            except TypeError:
                return None

        @staticmethod
        def base():
            return basis.base()

        # TODO Consider making real, coefficients, conj, inverse all properties

        def real(self):
            return self.a.real()

        def coefficients(self):
            return self.a.coefficients() + self.b.coefficients()

        def conj(self):
            return Hypercomplex(self.a.conj(), -self.b, pair=True)

        def inverse(self):
            return self.conj() / self.norm_squared()

        def __bool__(self):
            return bool(self.a) or bool(self.b)

        def __eq__(self, other):
            return self.a == other.a and self.b == other.b

        def __str__(self):
            coefficients = [f"{c:g}" for c in self.coefficients()]
            return "(" + ' '.join(coefficients) + ")"

        def __repr__(self):
            return f"{Hypercomplex.__name__}[{len(self)}]" + str(self)

        # Unary Mathematical Dunders:

        def __abs__(self):
            pass  # todo

        def __neg__(self):
            return Hypercomplex(-self.a, -self.b, pair=True)

        def __pos__(self):
            return self.copy()

        # Binary Mathematical Dunders:

        def __add__(self, other):
            other = Hypercomplex.coerce(other)
            if other is None:
                return NotImplemented
            return Hypercomplex(self.a + other.a, self.b + other.b, pair=True)

        def __radd__(self, other):
            return Hypercomplex(other) + self  # Should never raise TypeError.

        def __mul__(self, other):
            a = self.a * other.a - other.b.conj() * self.b
            b = other.b * self.a + self.b * other.a.conj()
            return Hypercomplex(a, b, pair=True)

        def __pow__(self, other):  # Only valid if other is an integer.
            pass  # todo

        def __sub__(self, other):
            return Hypercomplex(self.a - other.a, self.b - other.b, pair=True)

        def __truediv__(self, other):
            if not Number.is_hypercomplex(other):
                other = Hypercomplex(other)
            elif len(other) > len(self):
                return NotImplemented
            return self * other.inverse()
            if type(other) is Hypercomplex:
                return self * other.inverse()  # TODO?
            return Hypercomplex(self.a / other, self.b / other, pair=True)

        def __rtruediv__(self, other):

            print(other, 'OTH')
            pass

        # TODO radd rmul rsub rtruediv

    return Hypercomplex

# TODO test += methods


Real = reals(float)
Complex = cayley_dicksonize(Real)
Quaternion = cayley_dicksonize(Complex)
Octonion = cayley_dicksonize(Quaternion)
Sedenion = cayley_dicksonize(Octonion)
Trigintaduonion = cayley_dicksonize(Sedenion)

c = Complex(100, 200)
q = Quaternion(1, 2, 3, 4)
o = Octonion(1)
print(q + c)
print(c + q)
print(q + 11.0)
print(q + Real(11))
print(Real(11) + q + 2 + Complex(Real(2), Real(3)))
print(Complex(Real(2), Real(3)) + q + q)
print(Quaternion(Real(3), Real(3), Real(3), Real(3)))
print(o + 34)
# print(q)
# print(Real(Real(9)))

# r = Octonion(1, 2, 3, 4, 5, 6, 7, 8)

# s = Sedenion(r)
# print(s)
# print(r)
