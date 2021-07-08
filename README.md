# Hypercomplex

**A Python package for working with arbitrary-dimension [hypercomplex numbers][1] following the [Cayley-Dickson construction][2] of algebras.**

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

## Example Usage

See [examples.py](examples.py). TODO 5-6 separated examples.

## Package Contents

Three functions form the core of the package:

- `reals(base)` - Given a base type (`float` by default), generates a class that represents numbers with 1 hypercomplex dimension, i.e. [real numbers](https://en.wikipedia.org/wiki/Real_number). This class can then be extended into complex numbers and beyond with `cayley_dickson_construction`.

    Any usual math operations on instances of the class returned by `reals` behave as instances of `base` would but their type remains the reals class. By default they are printed with the `g` [format-spec][7] and surrounded by parentheses, e.g. `(1)`, to remain consistent with the format of higher dimension hypercomplex numbers.

    Python's [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html) might be another likely choice for `base`.

    ```py
    # reals example:
    from hypercomplex import reals
    from decimal import Decimal
    
    RDecimal = reals(Decimal)
    print(RDecimal(3) * RDecimal(9)) # -> (27)
    print(RDecimal(10) / 4)          # -> (2.5)
    ```

- `cayley_dickson_construction(basis)` (alias `cd_construction`) generates a new class of hypercomplex numbers with twice the dimension of the given `basis`, which must be another hypercomplex number class or class returned from `reals`. The new class of numbers is defined recursively on the basis according the [Cayley-Dickson construction][2]. Normal math operations may be done upon its instances and with instances of other numeric types.

    TODO possibly an example here.

- `cayley_dickson_algebra(level, base)` (alias `cd_algebra`) is a helper function that repeatedly applies `cayley_dickson_construction` to the given `base` type `level` number of times. That is, `cayley_dickson_algebra` returns the class for the Cayley-Dickson algebra of hypercomplex numbers with `2**level` dimensions.

    TODO possibly an example here.

For convenience, nine internal number types are already defined, built off of each other:

| Name | Aliases | Description |
| ---- | ---- | ----------- |
| `Real` | `R`, `CD0` | [Real numbers](https://en.wikipedia.org/wiki/Real_number) with 1 hypercomplex dimension based on `float`.
| `Complex` | `C`, `CD1` | [Complex numbers](https://en.wikipedia.org/wiki/Complex_number) with 2 hypercomplex dimensions based on `Real`.
| `Quaternion` | `Q`, `CD2` | [Quaternion numbers](https://en.wikipedia.org/wiki/Quaternion) with 4 hypercomplex dimensions based on `Complex`.
| `Octonion` | `O`, `CD3` | [Octonion numbers](https://en.wikipedia.org/wiki/Octonion) with 8 hypercomplex dimensions based on `Quaternion`.
| `Sedenion` | `S`, `CD4` | [Sedenion numbers](https://en.wikipedia.org/wiki/Sedenion) with 16 hypercomplex dimensions based on `Octonion`.
| `Pathion` | `P`, `CD5` | Pathion numbers with 32 hypercomplex dimensions based on `Sedenion`.
| `Chingon` | `X`, `CD6` | Chingon numbers with 64 hypercomplex dimensions based on `Pathion`.
| `Routon` | `U`, `CD7` | Routon numbers with 128 hypercomplex dimensions based on `Chingon`.
| `Voudon` | `V`, `CD8` | Voudon numbers with 256 hypercomplex dimensions based on `Routon`.

**Example of using the built-in types:**

```py
from hypercomplex import *
print(Real(4))              # -> (4)
print(C(3-7j))              # -> (3 -7)
print(CD3(1.1, -2.2, 3.3))  # -> (1.1 -2.2 3.3 0 0 0 0 0)
```

The names and letter-abbreviations were taken from [this image][3] ([mirror][4]) found in Micheal Carter's paper [*Visualization of the Cayley-Dickson Hypercomplex Numbers Up to the Chingons (64D)*](https://www.mapleprimes.com/posts/124913-Visualization-Of-The-CayleyDickson) but they also may be known according to their [Latin naming conventions][6].

## About

This package was built for the novelty of it as a math and programming exercise. The operations it can perform on hypercomplex numbers are not particularly efficient due to the recursive nature of the Cayley-Dickson construction.

I, the author, am not a mathematician, only a math hobbyist, and apologize if there are glaring issues with the implementations or descriptions I have provided.

[1]: https://en.wikipedia.org/wiki/Hypercomplex_number
[2]: https://en.wikipedia.org/wiki/Cayley%E2%80%93Dickson_construction
[3]: https://www.mapleprimes.com/DocumentFiles/124913/419426/Figure1.JPG
[4]: https://github.com/discretegames/hypercomplex/blob/ed3c47fb909e85736b7b5a147a39981e6e87fa57/hypercomplex_names.png
[5]: https://www.mapleprimes.com/posts/124913-Visualization-Of-The-CayleyDickson
[6]: https://english.stackexchange.com/q/234607
[7]: https://docs.python.org/3/library/string.html#format-specification-mini-language
