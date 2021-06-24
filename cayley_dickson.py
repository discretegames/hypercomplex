from decimal import Decimal
from math_dunders import math_dunders


class Number:
    def copy(self):
        return self.__class__(self)

    def norm_squared(self):
        return self.conjugate() * self

    def inverse(self):
        pass  # todo

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

        def conjugate(self):
            return self.copy()

    return Real


def cayley_dicksonize(basis):
    class Hypercomplex(Number):
        dimensions = 2 * basis.dimensions  # TODO use dimensions for type casting

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

        def coefficients(self):
            return self.a.coefficients() + self.b.coefficients()

        def conjugate(self):
            return Hypercomplex(self.a.conjugate(), -self.b, pair=True)

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
            a = self.a * other.a - other.b.conjugate() * self.b
            b = other.b * self.a + self.b * other.a.conjugate()
            return Hypercomplex(a, b, pair=True)

        def __sub__(self, other):
            return Hypercomplex(self.a - other.a, self.b - other.b, pair=True)

        def __truediv__(self, other):
            return self * other.inverse()  # TODO

        # TODO radd rmul rsub rtruediv

    return Hypercomplex


Real = reals(float)
Complex = cayley_dicksonize(Real)
Quaternion = cayley_dicksonize(Complex)
Octonion = cayley_dicksonize(Quaternion)
Sedenion = cayley_dicksonize(Octonion)
Trigintaduonion = cayley_dicksonize(Sedenion)

r = Trigintaduonion(1, 2, 3)
#r = Real(9)

r2 = r.copy()

print(r.norm_squared())
# print(type(r.conjugate()))


# x = Complex(2, 3)
# print(x * x)

# q = Quaternion(1, 2, 3, 4)
# q2 = Quaternion(q)
# print(q2 * q2)


# r1 = Complex(8.344, -1)
# r2 = r1.copy()
# print(r1, r1 is r2)

# print(Trigintaduonion.base())
# q2 = q
# print(q)
# print(q is q2)
# print(q + q)
# print(Octonion())
# o1 = Octonion(1, 2, 3, 4, 5, 6, 7, 8)
# print(bool(o1), bool(Octonion()))
# o2 = Octonion(1, 1, 1, 1, 1, 1, 1, 1)
# print(o1.conj)
