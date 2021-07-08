from hypercomplex import Real, Complex, Quaternion, Sedenion

# %% 1. Initialization can be done in various ways, including using Python's built in complex numbers. Unspecified coefficients become 0.
Real(-1.5)
Complex(2, 3)
Complex(2 + 3j)
Quaternion(4, 5, 6, 7)
Quaternion(4 + 5j, Complex(6, 7), pair=True)
Sedenion()
# %%


"""examples todo

quaternions noncommutative
octonions nonassociative
Pathion zero divisors

inverse
norm_squared
norm
abs
len
getitem
contains
format custom

e
e_matrix

base
real_coeff
coefficients
conjugate
real
imag
complex
equality
negate
add
mul
pow
sub
div

copy"""
