['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__',
    '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__set_format__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']


# abs add bool eq float floordiv format int le totalorder mod mul neg pos pow radd

def reals(basis=float):
    class Real:
        dimensions = 1

        def __init__(self, val=None):
            self.val = basis() if val is None else basis(val)

        @property
        def conjugate(self):
            return Real(self.val)

        def __add__(self, other):
            return Real(self.val + other)


# definitely need conjugate, coefficients, dimensions


def cayley_dicksonize(number_type=float):
    # todo Hypercomplex(float)? does that even make sense? maybe a 3rd version is in order
    class Hypercomplex:  # TODO use dimensions for type casting? #
        if hasattr(number_type, "dimensions"):
            dimensions = 2 * number_type.dimensions
        else:
            dimensions = 2

        """TODO div abs rmul? radd? pow? norm floordiv?"""

        # a is the "real" part, b the "imaginary"
        def __init__(self, *coefficients, pair=False):
            if pair:
                self.a, self.b = map(copy, coefficients)
            elif len(coefficients) == 1 and coefficients[0].__class__ is self.__class__:
                self.a, self.b = copy(coefficients[0].a), copy(coefficients[0].b)
            else:
                zero = Hypercomplex.basis()()
                coefficients += (zero,) * (len(self) - len(coefficients))
                self.a = number_type(*coefficients[:len(self)//2])
                self.b = number_type(*coefficients[len(self)//2:])

        @classmethod
        def basis(cls):
            if cls.dimensions == 2:
                return number_type
            return number_type.basis

        @staticmethod
        def safe_conj(number):
            if hasattr(number, 'conj'):
                return number.conj
            return number

        @property
        def coefficients(self):
            if len(self) == 2:
                return self.a, self.b
            return self.a.coefficients + self.b.coefficients

        @property
        def conj(self):
            return Hypercomplex(Hypercomplex.safe_conj(self.a), -self.b, pair=True)

        def __copy__(self):  # todo use number_type more and see of e can avoid the copy stuff
            return Hypercomplex(self.a, self.b, pair=True)

        def __abs__(self):  # todo
            self * self.conj

        def inverse(self):  # todo
            pass

        def __str__(self):
            parts = [f"{part:g}" for part in self.coefficients]
            return "(" + ' '.join(parts) + ")"

        def __repr__(self):
            return f"{Hypercomplex.__name__}[{len(self)}]" + str(self)

        def __len__(self):
            return self.dimensions

        def __bool__(self):
            return bool(self.a) or bool(self.b)

        def __eq__(self, other):
            return self.a == other.a and self.b == other.b

        def __add__(self, other):
            return Hypercomplex(self.a + other.a, self.b + other.b, pair=True)

        def __pos__(self):
            return Hypercomplex(self.a, self.b, pair=True)

        def __neg__(self):
            return Hypercomplex(-self.a, -self.b, pair=True)

        def __sub__(self, other):
            return self + (-other)

        def __mul__(self, other):
            a = self.a * other.a - Hypercomplex.safe_conj(other.b) * self.b
            b = other.b * self.a + self.b * Hypercomplex.safe_conj(other.a)
            return Hypercomplex(a, b, pair=True)

        def __truediv__(self, other):
            pass

    return Hypercomplex


Complex = cayley_dicksonize(Real)
Quaternion = cayley_dicksonize(Complex)
Octonion = cayley_dicksonize(Quaternion)
Sedenion = cayley_dicksonize(Octonion)

c = Complex(1, 2)
q = Quaternion(c, c, pair=True)
c.a = 99

#q = Quaternion(1, 2, 3, 88)
#q2 = q
print(q)
#print(q is q2)
# print(q + q)
# print(Octonion())
# o1 = Octonion(1, 2, 3, 4, 5, 6, 7, 8)
# print(bool(o1), bool(Octonion()))
# o2 = Octonion(1, 1, 1, 1, 1, 1, 1, 1)
# print(o1.conj)

# TODO build a test suite out of this?
