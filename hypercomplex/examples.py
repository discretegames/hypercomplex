from hypercomplex import cayley_dickson_algebra


# q1 = Quaternion(1, 2, 3, 4)
# print(2 * q1)

# q2 = Quaternion(0, 0, 1, 0)
# print(q1 * q2)
# print(q2 * q1)


# print(Octonion.e_matrix())
# print(Octonion.e(6))


# from decimal import Decimal
# # RealDecimal = reals(Decimal)
from hypercomplex import reals
from decimal import Decimal

RDecimal = reals(Decimal)
print(RDecimal(3) * RDecimal(9))
print(RDecimal(10) / 4)
