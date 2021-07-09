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


# %% 1. Initialization can be done in various ways, including using Python's built in complex numbers. Unspecified coefficients become 0.
print(R(-1.5))
print(C(2, 3))
print(C(2 + 3j))
print(Q(4, 5, 6, 7))
print(Q(4 + 5j, C(6, 7), pair=True))
print(P())


# %% 2. Numbers can be added and subtracted. The result will be the type with more dimensions.
print(Q(0, 1, 2, 2) + C(9, -1))
print(100.1 - O(0, 0, 0, 0, 1.1, 2.2, 3.3, 4.4))


# %% 3. Numbers can be multiplied. The result will be the type with more dimensions.
print(10 * S(1, 2, 3))
print(Q(1.5, 2.0) * O(0, -1))

# notice quaternions are non-commutative
print(Q(1, 2, 3, 4) * Q(1, 0, 0, 1))
print(Q(1, 0, 0, 1) * Q(1, 2, 3, 4))


# %% 4. Numbers can be divided and `inverse` gives the multiplicative inverse.
print(100 / C(0, 2))
print(C(2, 2) / Q(1, 2, 3, 4))
print(C(2, 2) * Q(1, 2, 3, 4).inverse())
print(R(2).inverse(), 1 / R(2))


# %% 5. `conjugate` gives the conjugate of the number.
print(R(9).conjugate())
print(C(9, 8).conjugate())
print(Q(9, 8, 7, 6).conjugate())


# %% 6. `norm` gives the absolute value as the base type (`float` by default). There is also `norm_squared`.
print(O(3, 4).norm(), type(O(3, 4).norm()))
print(abs(O(3, 4)))
print(O(3, 4).norm_squared())


# %% 7. Numbers are considered equal if their coefficients all match. Non-existent coefficients are 0.
print(R(999) == V(999))
print(C(1, 2) == Q(1, 2))
print(C(1, 2) == Q(1, 2, 0.1))


# %% 8. `coefficients` gives a tuple of the components of the number in their base type (`float` by default). The properties `real` and `imag` are shortcuts for the first two components. Indexing can also be used (but is inefficient).
print(R(100).coefficients())
q = Q(2, 3, 4, 5)
print(q.coefficients())
print(q.real, q.imag)
print(q[0], q[1], q[2], q[3])


# %% 9. `e(index)` of a number class gives the unit hypercomplex number where the index coefficient is 1 and all others are 0.
print(C.e(0))
print(C.e(1))
print(O.e(3))


# %% 10. `e_matrix` of a number class gives the multiplication table of `e(i)*e(j)`. Set `string=False` to get a 2D list instead of a string. Set `raw=True` to get the raw hypercomplex numbers.
print(O.e_matrix())
print(C.e_matrix(string=False, raw=True))


# %% 11. A number is considered truthy if it has has non-zero coefficients. Conversion to `int`, `float` and `complex` are only valid when the coefficients beyond the dimension of those types are all 0.
print(bool(Q()))
print(bool(Q(0, 0, 0.01, 0)))

print(complex(Q(5, 5)))
print(int(V(9.9)))
# print(float(C(1, 2))) <- invalid


# %% 12. Any usual format spec for the base type can be given in an f-string.
o = O(0.001, 1, -2, 3.3333, 4e5)
print(f"{o:.2f}")
print(f"{R(23.9):04.0f}")


# %% 13. The `len` of a number is its hypercomplex dimension, i.e. the number of components or coefficients it has.
print(len(R()))
print(len(C(7, 7)))
print(len(U()))


# %% 14. Using `in` behaves the same as if the number were a tuple of its coefficients.
print(3 in Q(1, 2, 3, 4))
print(5 in Q(1, 2, 3, 4))


# %% 15. `copy` can be used to duplicate a number (but should generally not be needed).
x = O(9, 8, 7)
y = x.copy()
print(x == y)
print(x is y)


# %% 16. `base` on a number class will return the base type the entire numbers are built upon.
print(R.base())
print(V.base())
A = cayley_dickson_algebra(20, int)
print(A.base())


# %%
