from decimal import Decimal
from math_dunders import math_dunders
from math import ceil, floor, trunc


def reals(base=float):
    @math_dunders(base=base)
    class Real(base):
        dimensions = 1

        @staticmethod
        def base():
            return base

        def copy(self):
            return Real(self)

        def coefficients(self):
            return (base(self),)

        def conjugate(self):
            return self.copy()

        def __len__(self):
            return self.dimensions

        # possibly todo: inverse, basis, norm?

    return Real


def cayley_dicksonize(basis):

    def make_unary_dunder(func):
        def dunder(self):
            return Hypercomplex(func(self.a), func(self.b), pair=True)
        return dunder

    class Hypercomplex:
        dimensions = 2 * basis.dimensions  # TODO use dimensions for type casting

        # TODO all the mathy dunders, int, float, complex?

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

        def copy(self):
            return Hypercomplex(self)

        def coefficients(self):
            return self.a.coefficients() + self.b.coefficients()

        def conjugate(self):
            return Hypercomplex(self.a.conjugate(), -self.b, pair=True)

        def __len__(self):
            return self.dimensions

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

        def __abs__(self):  # todo
            pass

        __ceil__ = make_unary_dunder(ceil)
        __floor__ = make_unary_dunder(floor)
        __neg__ = make_unary_dunder(lambda x: -x)
        __pos__ = make_unary_dunder(lambda x: +x)
        __round__ = make_unary_dunder(round)
        __trunc__ = make_unary_dunder(trunc)

        # Binary Mathematical Dunders:

        def __add__(self, other):
            return Hypercomplex(self.a + other.a, self.b + other.b, pair=True)

        def __sub__(self, other):
            return self + (-other)

        def __mul__(self, other):
            a = self.a * other.a - other.b.conjugate() * self.b
            b = other.b * self.a + self.b * other.a.conjugate()
            return Hypercomplex(a, b, pair=True)

        def __truediv__(self, other):
            pass

    return Hypercomplex


Real = reals(float)
Complex = cayley_dicksonize(Real)
Quaternion = cayley_dicksonize(Complex)
Octonion = cayley_dicksonize(Quaternion)
Sedenion = cayley_dicksonize(Octonion)
Trigintaduonion = cayley_dicksonize(Sedenion)

r = Sedenion(3.9, 2.8, 9.9)

print(-ceil(r))
print(floor(r))

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
