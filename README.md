# Hypercomplex

**A Python package for working with quaternions, octonions, sedenions, and beyond following the Cayley-Dickson construction of hypercomplex numbers.**

As many know, the [complex numbers](https://en.wikipedia.org/wiki/Complex_number) may be viewed as an extension of the everyday [real numbers](https://en.wikipedia.org/wiki/Real_number). A complex number has two real-number coefficients, one multiplied by 1, the other multiplied by [i](https://en.wikipedia.org/wiki/Imaginary_unit).

In a similar way, a [quaternion](https://en.wikipedia.org/wiki/Quaternion), which has 4 components, can be constructed by combining two complex numbers. Likewise, two quaternions can construct an [octonion](https://en.wikipedia.org/wiki/Octonion) (8 components), and two octonions can construct a [sedenion](https://en.wikipedia.org/wiki/Sedenion) (16 components).

The method for this construction is known as the [Cayley-Dickson construction][2] and the resulting classes of numbers are types of [hypercomplex numbers][1]. There is no limit to the number of times you can repeat the Cayley-Dickson construction to create new types of hypercomplex numbers, doubling the number of components each time.

This Python 3 package allows the creation of number classes at any repetition level of Cayley-Dickson constructions, and has built-ins for the smaller, named levels such as quaternion, octonion, and sedenion.

## Installation

```text
pip install hypercomplex
```

[View on PyPI](https://pypi.org/project/hypercomplex) - [View on GitHub](https://github.com/discretegames/hypercomplex)

This package was built in Python 3.9.6 but should be compatible with most earlier Python 3 versions.

## Package Contents

Three functions form the core of the package:

- `reals(base)` - Given a base type (`float` by default), generates a class that represents numbers with 1 hypercomplex dimension, i.e. [real numbers](https://en.wikipedia.org/wiki/Real_number). This class can then be extended into complex numbers and beyond with `cayley_dickson_construction`.

    Any usual math operations on instances of the class returned by `reals` behave as instances of `base` would but their type remains the reals class. By default they are printed with the `g` [format-spec][7] and surrounded by parentheses, e.g. `(1)`, to remain consistent with the format of higher dimension hypercomplex numbers.

    Python's [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html) might be another likely choice for `base`.

    ```py
    # reals example:
    from hypercomplex import reals
    from decimal import Decimal
    
    D = reals(Decimal)
    print(D(10) / 4)   # -> (2.5)
    print(D(3) * D(9)) # -> (27)
    ```

- `cayley_dickson_construction(basis)` (alias `cd_construction`) generates a new class of hypercomplex numbers with twice the dimension of the given `basis`, which must be another hypercomplex number class or class returned from `reals`. The new class of numbers is defined recursively on the basis according the [Cayley-Dickson construction][2]. Normal math operations may be done upon its instances and with instances of other numeric types.

    ```py
    # cayley_dickson_construction example:
    from hypercomplex import *
    RealNum = reals()
    ComplexNum = cayley_dickson_construction(RealNum)
    QuaternionNum = cayley_dickson_construction(ComplexNum)

    q = QuaternionNum(1, 2, 3, 4)
    print(q)         # -> (1 2 3 4)
    print(1 / q)     # -> (0.0333333 -0.0666667 -0.1 -0.133333)
    print(q + 1+2j)  # -> (2 4 3 4)
    ```

- `cayley_dickson_algebra(level, base)` (alias `cd_algebra`) is a helper function that repeatedly applies `cayley_dickson_construction` to the given `base` type (`float` by default) `level` number of times. That is, `cayley_dickson_algebra` returns the class for the Cayley-Dickson algebra of hypercomplex numbers with `2**level` dimensions.

    ```py
    # cayley_dickson_algebra example:
    from hypercomplex import *
    OctonionNum = cayley_dickson_algebra(3)

    o = OctonionNum(8, 7, 6, 5, 4, 3, 2, 1)
    print(o)              # -> (8 7 6 5 4 3 2 1)
    print(2 * o)          # -> (16 14 12 10 8 6 4 2)
    print(o.conjugate())  # -> (8 -7 -6 -5 -4 -3 -2 -1)
    ```

For convenience, nine internal number types are already defined, built off of each other:

| Name | Aliases | Description |
| ---- | ---- | ----------- |
| `Real` | `R`, `CD1`, `CD[0]` | [Real numbers](https://en.wikipedia.org/wiki/Real_number) with 1 hypercomplex dimension based on `float`.
| `Complex` | `C`, `CD2`, `CD[1]` | [Complex numbers](https://en.wikipedia.org/wiki/Complex_number) with 2 hypercomplex dimensions based on `Real`.
| `Quaternion` | `Q`, `CD4`, `CD[2]` | [Quaternion numbers](https://en.wikipedia.org/wiki/Quaternion) with 4 hypercomplex dimensions based on `Complex`.
| `Octonion` | `O`, `CD8`, `CD[3]` | [Octonion numbers](https://en.wikipedia.org/wiki/Octonion) with 8 hypercomplex dimensions based on `Quaternion`.
| `Sedenion` | `S`, `CD16`, `CD[4]` | [Sedenion numbers](https://en.wikipedia.org/wiki/Sedenion) with 16 hypercomplex dimensions based on `Octonion`.
| `Pathion` | `P`, `CD32`, `CD[5]` | Pathion numbers with 32 hypercomplex dimensions based on `Sedenion`.
| `Chingon` | `X`, `CD64`, `CD[6]` | Chingon numbers with 64 hypercomplex dimensions based on `Pathion`.
| `Routon` | `U`, `CD128`, `CD[7]` | Routon numbers with 128 hypercomplex dimensions based on `Chingon`.
| `Voudon` | `V`, `CD256`, `CD[8]` | Voudon numbers with 256 hypercomplex dimensions based on `Routon`.

```py
# built-in types example:
from hypercomplex import *
print(Real(4))               # -> (4)
print(C(3-7j))               # -> (3 -7)
print(CD4(.1, -2.2, 3.3e3))  # -> (0.1 -2.2 3300 0)
print(CD[3](1, 0, 2, 0, 3))  # -> (1 0 2 0 3 0 0 0)
```

The names and letter-abbreviations were taken from [this image][3] ([mirror][4]) found in Micheal Carter's paper [*Visualization of the Cayley-Dickson Hypercomplex Numbers Up to the Chingons (64D)*](https://www.mapleprimes.com/posts/124913-Visualization-Of-The-CayleyDickson), but they also may be known according to their [Latin naming conventions][6].

## Usage Examples

This list follows [examples.py](https://github.com/discretegames/hypercomplex/blob/main/hypercomplex/examples.py) exactly and documents nearly all the things you can do with the hypercomplex numbers created by this package.

Every example assumes the appropriate imports are already done, e.g. `from hypercomplex import *`.

1. Initialization can be done in various ways, including using Python's built in complex numbers. Unspecified coefficients become 0.

    ```py
    print(R(-1.5))                        # -> (-1.5)
    print(C(2, 3))                        # -> (2 3)
    print(C(2 + 3j))                      # -> (2 3)
    print(Q(4, 5, 6, 7))                  # -> (4 5 6 7)
    print(Q(4 + 5j, C(6, 7), pair=True))  # -> (4 5 6 7)
    print(P())                            # -> (0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
    ```

2. Numbers can be added and subtracted. The result will be the type with more dimensions.

    ```py
    print(Q(0, 1, 2, 2) + C(9, -1))                   # -> (9 0 2 2)
    print(100.1 - O(0, 0, 0, 0, 1.1, 2.2, 3.3, 4.4))  # -> (100.1 0 0 0 -1.1 -2.2 -3.3 -4.4)
    ```

3. Numbers can be multiplied. The result will be the type with more dimensions.

    ```py
    print(10 * S(1, 2, 3))                    # -> (10 20 30 0 0 0 0 0 0 0 0 0 0 0 0 0)
    print(Q(1.5, 2.0) * O(0, -1))             # -> (2 -1.5 0 0 0 0 0 0)
    
    # notice quaternions are non-commutative
    print(Q(1, 2, 3, 4) * Q(1, 0, 0, 1))      # -> (-3 5 1 5)
    print(Q(1, 0, 0, 1) * Q(1, 2, 3, 4))      # -> (-3 -1 5 5)
    ```

4. Numbers can be divided and `inverse` gives the multiplicative inverse.

    ```py
    print(100 / C(0, 2))                      # -> (0 -50)
    print(C(2, 2) / Q(1, 2, 3, 4))            # -> (0.2 -0.0666667 0.0666667 -0.466667)
    print(C(2, 2) * Q(1, 2, 3, 4).inverse())  # -> (0.2 -0.0666667 0.0666667 -0.466667)
    print(R(2).inverse(), 1 / R(2))           # -> (0.5) (0.5)
    ```

5. Numbers can be raised to integer powers, a shortcut for repeated multiplication or division.

    ```py
    q = Q(0, 3, 4, 0)
    print(q**5)               # -> (0 1875 2500 0)
    print(q * q * q * q * q)  # -> (0 1875 2500 0)
    print(q**-1)              # -> (0 -0.12 -0.16 0)
    print(1 / q)              # -> (0 -0.12 -0.16 0)
    print(q**0)               # -> (1 0 0 0)
    ```

6. `conjugate` gives the conjugate of the number.

    ```py
    print(R(9).conjugate())           # -> (9)
    print(C(9, 8).conjugate())        # -> (9 -8)
    print(Q(9, 8, 7, 6).conjugate())  # -> (9 -8 -7 -6)
    ```

7. `norm` gives the absolute value as the base type (`float` by default). There is also `norm_squared`.

    ```py
    print(O(3, 4).norm(), type(O(3, 4).norm()))  # -> 5.0 <class 'float'>
    print(abs(O(3, 4)))                          # -> 5.0
    print(O(3, 4).norm_squared())                # -> 25.0
    ```

8. Numbers are considered equal if their coefficients all match. Non-existent coefficients are 0.

    ```py
    print(R(999) == V(999))         # -> True
    print(C(1, 2) == Q(1, 2))       # -> True
    print(C(1, 2) == Q(1, 2, 0.1))  # -> False
    ```

9. `coefficients` gives a tuple of the components of the number in their base type (`float` by default). The properties `real` and `imag` are shortcuts for the first two components. Indexing can also be used (but is inefficient).

    ```py
    print(R(100).coefficients())   # -> (100.0,)
    q = Q(2, 3, 4, 5)
    print(q.coefficients())        # -> (2.0, 3.0, 4.0, 5.0)
    print(q.real, q.imag)          # -> 2.0 3.0
    print(q[0], q[1], q[2], q[3])  # -> 2.0 3.0 4.0 5.0
    ```

10. `e(index)` of a number class gives the unit hypercomplex number where the index coefficient is 1 and all others are 0.

    ```py
    print(C.e(0))  # -> (1 0)
    print(C.e(1))  # -> (0 1)
    print(O.e(3))  # -> (0 0 0 1 0 0 0 0)
    ```

11. `e_matrix` of a number class gives the multiplication table of `e(i)*e(j)`. Set `string=False` to get a 2D list instead of a string. Set `raw=True` to get the raw hypercomplex numbers.

    ```py
    print(O.e_matrix())                        # -> e1  e2  e3  e4  e5  e6  e7
                                               #   -e0  e3 -e2  e5 -e4 -e7  e6
                                               #   -e3 -e0  e1  e6  e7 -e4 -e5
                                               #    e2 -e1 -e0  e7 -e6  e5 -e4
                                               #   -e5 -e6 -e7 -e0  e1  e2  e3
                                               #    e4 -e7  e6 -e1 -e0 -e3  e2
                                               #    e7  e4 -e5 -e2  e3 -e0 -e1
                                               #   -e6  e5  e4 -e3 -e2  e1 -e0
                                               #
    print(C.e_matrix(string=False, raw=True))  # -> [[(1 0), (0 1)], [(0 1), (-1 0)]]
    ```

12. A number is considered truthy if it has has non-zero coefficients. Conversion to `int`, `float` and `complex` are only valid when the coefficients beyond the dimension of those types are all 0.

    ```py
    print(bool(Q()))                    # -> False
    print(bool(Q(0, 0, 0.01, 0)))       # -> True
    
    print(complex(Q(5, 5)))             # -> (5+5j)
    print(int(V(9.9)))                  # -> 9
    # print(float(C(1, 2))) <- invalid
    ```

13. Any usual format spec for the base type can be given in an f-string.

    ```py
    o = O(0.001, 1, -2, 3.3333, 4e5)
    print(f"{o:.2f}")                 # -> (0.00 1.00 -2.00 3.33 400000.00 0.00 0.00 0.00)
    print(f"{R(23.9):04.0f}")         # -> (0024)
    ```

14. The `len` of a number is its hypercomplex dimension, i.e. the number of components or coefficients it has.

    ```py
    print(len(R()))      # -> 1
    print(len(C(7, 7)))  # -> 2
    print(len(U()))      # -> 128
    ```

15. Using `in` behaves the same as if the number were a tuple of its coefficients.

    ```py
    print(3 in Q(1, 2, 3, 4))  # -> True
    print(5 in Q(1, 2, 3, 4))  # -> False
    ```

16. `copy` can be used to duplicate a number (but should generally never be needed as all operations create a new number).

    ```py
    x = O(9, 8, 7)
    y = x.copy()
    print(x == y)   # -> True
    print(x is y)   # -> False
    ```

17. `base` on a number class will return the base type the entire numbers are built upon.

    ```py
    print(R.base())                      # -> <class 'float'>
    print(V.base())                      # -> <class 'float'>
    A = cayley_dickson_algebra(20, int)
    print(A.base())                      # -> <class 'int'>
    ```

18. Hypercomplex numbers are weird, so be careful! Here two non-zero sedenions multiply to give zero because sedenions and beyond have zero devisors.

    ```py
    s1 = S.e(5) + S.e(10)
    s2 = S.e(6) + S.e(9)
    print(s1)                                    # -> (0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0)
    print(s2)                                    # -> (0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0)
    print(s1 * s2)                               # -> (0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
    print((1 / s1) * (1 / s2))                   # -> (0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0)
    # print(1/(s1 * s2)) <- zero division error
    ```

## About

I wrote this package for the novelty of it and as a math and programming exercise. The operations it can perform on hypercomplex numbers are not particularly efficient due to the recursive nature of the Cayley-Dickson construction.

I am not a mathematician, only a math hobbyist, and apologize if there are issues with the implementations or descriptions I have provided.

[1]: https://en.wikipedia.org/wiki/Hypercomplex_number
[2]: https://en.wikipedia.org/wiki/Cayley%E2%80%93Dickson_construction
[3]: https://www.mapleprimes.com/DocumentFiles/124913/419426/Figure1.JPG
[4]: https://github.com/discretegames/hypercomplex/blob/ed3c47fb909e85736b7b5a147a39981e6e87fa57/hypercomplex_names.png
[5]: https://www.mapleprimes.com/posts/124913-Visualization-Of-The-CayleyDickson
[6]: https://english.stackexchange.com/q/234607
[7]: https://docs.python.org/3/library/string.html#format-specification-mini-language
