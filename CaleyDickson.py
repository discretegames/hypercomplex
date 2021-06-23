from abc import ABC, abstractmethod


class Number(ABC):
    @property
    @abstractmethod
    def size(self):
        pass

    @property
    @abstractmethod
    def parts(self):
        pass

    @property
    @abstractmethod
    def conj(self):
        pass


class Real(Number):
    @property
    def parts(self):
        return (Real(self),)

    @property
    def conj(self):
        return Real(self)

    def __add__(self, other):
        return Real(self + other)


def cayley_dicksonize(number_type):
    class Hypercomplex(Number):
        """TODO add sub mul div abs neg rmul? radd? conj"""

        def __init__(self, *parts, inline=True):
            if inline:
                self.real = number_type(*parts[:len(parts)//2])
                self.imag = number_type(*parts[len(parts)//2:])
            else:
                self.real, self.imag = parts

        @property  # TODO remove?
        def size(self):
            return self.real.size + self.imag.size

        @property
        def parts(self):  # Try to avoid using parts. Use recursive definitions for the elegance.
            return self.real.parts + self.imag.parts

        @property
        def conj(self):
            pass  # todo

        def __str__(self):
            parts = [f"{part:g}".replace("-0", "-").lstrip("0") for part in self.parts]
            return "(" + ' '.join(parts) + ")"

        def __repr__(self):
            return f"{self.__class__.__name__}[{self.size}]" + str(self)

        def __eq__(self, other):
            return self.real == other.real and self.imag == other.imag

        def __add__(self, other):
            real = self.real + other.real
            imag = self.imag + other.imag
            return self.__class__(real, imag, inline=False)

    return Hypercomplex


Complex = cayley_dicksonize(Real)
Quaternion = cayley_dicksonize(Complex)
Octonion = cayley_dicksonize(Quaternion)
Sedenion = cayley_dicksonize(Octonion)

c = Complex(1, 2)
print(c + c)
q = Quaternion(1, 2, 3, 4)
# print(repr(q))
#print(q == q)
o = Octonion(1, 2, 0.3, -0.3, 0.1, 90000.9, 7, 8)
# print(o)
