from hypercomplex import Real, Complex, Quaternion, Sedenion

# %% 1. Initialization can be done in various ways, including using Python's built in complex numbers. Unspecified coefficients become 0.
print(Real(-1.5))
print(Complex(2, 3))
print(Complex(2 + 3j))
print(Quaternion(4, 5, 6, 7))
print(Quaternion(4 + 5j, Complex(6, 7), pair=True))
print(Sedenion())

# %% 2. Test
print(999)


# %% 3. Test3
print(9996)
