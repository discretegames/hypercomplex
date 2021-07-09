"""Provides the types and tools to create arbitrary-dimension hypercomplex numbers following the Cayley-Dickson construction."""

from mathdunders import mathdunders
from numbers import Number
from math import sqrt


class Numeric(Number):
    """A parent class for Real and Hypercomplex for shared behaviors."""

    def copy(self):
        return self.__class__(self)

    def inverse(self):
        """Returns the multiplicative inverse of the number."""
        return self.conjugate() / self.norm_squared()

    def norm_squared(self):  # Returns base type.
        """Returns the square of the norm of the number as the base type."""
        return (self.conjugate() * self).real_coefficient()

    def norm(self):  # Returns base type.
        """Returns the norm of the number as the base type."""
        return sqrt(self.norm_squared())

    def __abs__(self):  # Returns base type.
        return self.norm()

    def __len__(self):
        return self.dimensions

    def __getitem__(self, index):
        return self.coefficients()[index]

    def __contains__(self, obj):
        return obj in self.coefficients()

    def __str__(self):
        return format(self)

    def __repr__(self):
        return str(self)

    def __format__(self, format_spec):
        if not format_spec:
            format_spec = "g"
        coefficients = [f"{c:{format_spec}}" for c in self.coefficients()]
        return "(" + ' '.join(coefficients) + ")"

    @classmethod
    def e(cls, index):
        """Returns the unit hypercomplex number at the given subscript index."""
        base = cls.base()
        coefficients = [base()] * cls.dimensions
        coefficients[index] = base(1)
        return cls(*coefficients)

    @classmethod
    def e_matrix(cls, string=True, raw=False, e="e"):
        """Creates a table of e(i)*e(j)'s akin to the ones found e.g. at wikipedia.org/wiki/Octonion."""
        def format_cell(cell):
            if not raw:
                i, c = next(((i, c)
                            for i, c in enumerate(cell.coefficients()) if c))
                cell = f"{e}{i}"
                if c < 0:
                    cell = "-" + cell
            return cell

        ees = list(map(cls.e, range(cls.dimensions)))
        matrix = [[format_cell(i * j) for j in ees] for i in ees]

        if string:
            matrix = [list(map(str, row)) for row in matrix]
            length = max(len(cell) for row in matrix for cell in row)
            offset = length - max(len(row[0]) for row in matrix)
            rows = [' '.join(cell.rjust(length)
                             for cell in row)[offset:] for row in matrix]
            return '\n'.join(rows) + '\n'
        return matrix


def reals(base=float):
    """Creates a type that represents real numbers based on a numeric type base."""
    if not issubclass(base, Number):
        raise ValueError("The base type must be derived from numbers.Number.")

    @mathdunders(base=base)
    class Real(Numeric, base):
        """A class that represents a real number, level 0 of the Cayley-Dickson construction."""
        dimensions = 1

        @staticmethod
        def base():
            """Returns the base type these numbers were based on."""
            return base

        def real_coefficient(self):  # Returns base type.
            """Returns the real (leftmost) coefficient of the hypercomplex number as the base type."""
            return base(self)

        def coefficients(self):  # Returns tuple of base types.
            """Returns a tuple of base types of all the coefficients of the hypercomplex number."""
            return (self.real_coefficient(),)

        def conjugate(self):
            """Returns the conjugate of the hypercomplex number."""
            return Real(self)

        # For simplicity, use the base's hash rather than hash of coefficients tuple.
        def __hash__(self):
            return hash(base(self))

    return Real


def cayley_dickson_construction(basis):
    """Creates a type for the Cayley-Dickson algebra with twice the dimensions of the given Hypercomplex or Real basis."""
    if not hasattr(basis, 'coefficients'):
        raise ValueError(
            "The basis type must be Real or Hypercomplex. (No coefficients found.)")

    class Hypercomplex(Numeric):
        """A class that represents a hypercomplex number, level > 0 of the Cayley-Dickson construction."""
        dimensions = 2 * basis.dimensions

        def __init__(self, *args, pair=False):
            if pair:
                # a is the "real" left half. b is the "imaginary" right half.
                self.a, self.b = map(basis, args)
            else:
                if len(args) == 1:
                    if hasattr(args[0], 'coefficients'):
                        args = args[0].coefficients()
                    elif isinstance(args[0], complex):
                        args = args[0].real, args[0].imag
                if len(args) > len(self):
                    raise TypeError(
                        f"Too many args. Got {len(args)} expecting at most {len(self)}.")
                if len(self) != len(args):
                    args += (Hypercomplex.base()(),) * (len(self) - len(args))
                self.a = basis(*args[:len(self) // 2])
                self.b = basis(*args[len(self) // 2:])

        @staticmethod
        def coerce(other):
            """Attempts to coerce other to this Hypercomplex type."""
            try:
                return Hypercomplex(other)
            except TypeError:
                return None

        @staticmethod
        def base():
            """Returns the base type these numbers were based on."""
            return basis.base()

        @property
        # Added so Hypercomplex numbers behave like other Python number types.
        def real(self):
            """The real (leftmost) coefficient of the hypercomplex number as the base type."""
            return self.real_coefficient()

        @property
        # Added so Hypercomplex numbers behave like other Python number types.
        def imag(self):
            """Returns the imaginary (second leftmost) coefficient of the hypercomplex number as the base type."""
            if len(self) == 2:
                return Hypercomplex.base()(self.b)
            return self.a.imag

        def real_coefficient(self):  # Returns base type.
            """Returns the real (leftmost) coefficient of the hypercomplex number as the base type."""
            return self.a.real_coefficient()

        def coefficients(self):  # Returns tuple of base types.
            """Returns a tuple of base types of all the coefficients of the hypercomplex number."""
            return self.a.coefficients() + self.b.coefficients()

        def conjugate(self):
            """Returns the conjugate of the hypercomplex number."""
            return Hypercomplex(self.a.conjugate(), -self.b, pair=True)

        def __hash__(self):
            return hash(self.coefficients())

        def __bool__(self):
            return bool(self.a) or bool(self.b)

        def convert(self, to_type, dimensions=1):
            """Attempts to convert self to to_type. Raises an error if the conversion is impossible."""
            coefficients = self.coefficients()
            if any(coefficients[dimensions:]):
                raise TypeError(
                    f"Can't convert {self.__class__.__name__}[{self.dimensions}] to {to_type.__name__} when there are non-zero incompatible coefficients.")
            return to_type(*coefficients[:dimensions])

        def __int__(self):
            return self.convert(int)

        def __float__(self):
            return self.convert(float)

        def __complex__(self):
            return self.convert(complex, 2)

        def __eq__(self, other):
            coerced = Hypercomplex.coerce(other)
            if coerced is None:
                self = other.__class__.coerce(self)
            else:
                other = coerced
            return self.a == other.a and self.b == other.b

        # Unary Math Dunders:

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
            # Should never encounter a TypeError.
            return Hypercomplex(other) + self

        def __mul__(self, other):
            other = Hypercomplex.coerce(other)
            if other is None:
                return NotImplemented
            a = self.a * other.a - other.b.conjugate() * self.b
            b = other.b * self.a + self.b * other.a.conjugate()
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
            # Short circuit base type to avoid infinite recursion in inverse().
            if isinstance(other, base):
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
    """Creates the type for the Cayley-Dickson algebra with 2**level dimensions. e.g. 0 for Real, 1 for Complex, 2 for Quaternion."""
    if not isinstance(level, int) or level < 0:
        raise ValueError("The level must be a positive integer.")
    numbers = reals(base)
    for _ in range(level):
        numbers = cayley_dickson_construction(numbers)
    return numbers


cd_construction = cayley_dickson_construction
cd_algebra = cayley_dickson_algebra

# Names and letters taken from https://www.mapleprimes.com/DocumentFiles/124913/419426/Figure1.JPG
CD1 = R = Real = reals()
CD2 = C = Complex = cayley_dickson_construction(CD1)
CD4 = Q = Quaternion = cayley_dickson_construction(CD2)
CD8 = O = Octonion = cayley_dickson_construction(CD4)
CD16 = S = Sedenion = cayley_dickson_construction(CD8)
CD32 = P = Pathion = cayley_dickson_construction(CD16)
CD64 = X = Chingon = cayley_dickson_construction(CD32)
CD128 = U = Routon = cayley_dickson_construction(CD64)
CD256 = V = Voudon = cayley_dickson_construction(CD128)
CD = CD1, CD2, CD4, CD8, CD16, CD32, CD64, CD128, CD256
