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


def reals(base=float):
    @math_dunders(base=base)
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

        # Core Methods:

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
            if other == 0:
                return Hypercomplex(Hypercomplex.base()(1))

            pass  # Todo later

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

# Todo e matrix


def cayley_dickson_algebra(level, base=float):
    if not isinstance(level, int) or level < 1:
        raise ValueError("The level must be a positive integer.")
    numbers = reals(base)
    for _ in range(level - 1):
        numbers = cayley_dicksonize(numbers)
    return numbers


Real = reals()  # 1
Complex = cayley_dicksonize(Real)  # 2
Quaternion = cayley_dicksonize(Complex)  # 4
Octonion = cayley_dicksonize(Quaternion)  # 8
Sedenion = cayley_dicksonize(Octonion)  # 16
Trigintaduonion = cayley_dicksonize(Sedenion)  # 32
Sexagintaquatronions = cayley_dicksonize(Trigintaduonion)  # 64
Centumduodetrigintanions = cayley_dicksonize(Sexagintaquatronions)  # 128
Ducentiquinquagintasexions = cayley_dicksonize(Centumduodetrigintanions)  # 256


q = Quaternion(99, 0)
t = Ducentiquinquagintasexions(q)

a = Ducentiquinquagintasexions(90)
b = cayley_dickson_algebra(True)(90)

print(a == b)

print(99 == q == t)
# print(q == 2)


# print(r.norm_squared())
# print(type(r.norm_squared()))

# a = 2
# b = 3
# x = a + b * (1j)

# c = Complex(2, 3)
# q = Quaternion(1, 2, 3, 4)
# o = Octonion(-2)

# print(o)
# o *= 200
# print(o)

# print(x/x)
# print(c/c)


# print(q - q)
# print(q - 9)
# print(q - Real(100))
# print(q**2)
# print(o - q)
# print(1-q)
# print(-q)


# print(q * c)
# print(c * q)
# print(q + 11.0)
# print(q + Real(11))
# print(Real(11) + q + 2 + Complex(Real(2), Real(3)))
# print(Complex(Real(2), Real(3)) + q + q)
# print(Quaternion(Real(3), Real(3), Real(3), Real(3)))
# print(o + 34)
# print(q)
# print(Real(Real(9)))

# r = Octonion(1, 2, 3, 4, 5, 6, 7, 8)

# s = Sedenion(r)
# print(s)
# print(r)
