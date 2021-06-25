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
            elif len(args) == 1 and args[0].__class__ is Hypercomplex:
                self.a, self.b = basis(args[0].a), basis(args[0].b)
            else:
                base = self.base()
                args += (base(),) * (len(self) - len(args))
                self.a = basis(*args[:len(self)//2])
                self.b = basis(*args[len(self)//2:])

        # Core Methods:

        @staticmethod
        def base():
            return basis.base()

        def real(self):
            return self.a.real()

        def coefficients(self):
            return self.a.coefficients() + self.b.coefficients()

        def conj(self):
            return Hypercomplex(self.a.conj(), -self.b, pair=True)

        def inverse(self):
            return Hypercomplex(self.conj())  # TODO

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
            return Hypercomplex(self.a + other.a, self.b + other.b, pair=True)

        def __mul__(self, other):
            a = self.a * other.a - other.b.conj() * self.b
            b = other.b * self.a + self.b * other.a.conj()
            return Hypercomplex(a, b, pair=True)

        def __pow__(self, other):  # Only valid if other is an integer.
            pass  # todo

        def __sub__(self, other):
            return Hypercomplex(self.a - other.a, self.b - other.b, pair=True)

        def __truediv__(self, other):
            return self * other.inverse()  # TODO?

        # TODO radd rmul rsub rtruediv

    return Hypercomplex


Real = reals(float)
Complex = cayley_dicksonize(Real)
Quaternion = cayley_dicksonize(Complex)
Octonion = cayley_dicksonize(Quaternion)
Sedenion = cayley_dicksonize(Octonion)
Trigintaduonion = cayley_dicksonize(Sedenion)

r = Octonion(1, 2, 3, 5, -9.8)
print(r.conj())
print(r*r)

print(r.norm_squared())
print(type(Real().conj()))
