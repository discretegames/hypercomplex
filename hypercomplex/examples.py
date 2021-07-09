# %% 0. Imports
from hypercomplex import \
    reals, \
    cayley_dickson_construction, cd_construction, \
    cayley_dickson_algebra, cd_algebra, \
    CD1, R, Real,\
    CD2, C, Complex, \
    CD4, Q, Quaternion, \
    CD8, O, Octonion, \
    CD16, S, Sedenion, \
    CD32, P, Pathion, \
    CD64, X, Chingon, \
    CD128, U, Routon, \
    CD256, V, Voudon, \
    CD
# %%

# %% 1. Initialization can be done in various ways, including using Python's built in complex numbers. Unspecified coefficients become 0.
print(Real(-1.5))
print(Complex(2, 3))
print(Complex(2 + 3j))
print(Quaternion(4, 5, 6, 7))
print(Quaternion(4 + 5j, Complex(6, 7), pair=True))
print(Sedenion())


# %% 2. Numbers can be added and subtracted.
print(complex(Q()))


# %%

# TODO other examples
