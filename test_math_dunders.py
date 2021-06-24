from math_dunders import math_dunders, unary, binary
import unittest
from math import ceil, floor, trunc


@math_dunders()
class r(float):  # Real number.
    pass


class TestMathDunders(unittest.TestCase):
    def check(self, a, b, a_type=r, b_type=None):
        self.assertEqual(a, b)
        if a_type is not None:
            self.assertEqual(type(a), a_type)
        if b_type is not None:
            self.assertEqual(type(b), b_type)

    # Miscellaneous Tests:

    def test_lists(self):
        u = ['__abs__', '__ceil__', '__floor__', '__neg__', '__pos__', '__round__', '__trunc__']
        b = ['__add__', '__floordiv__', '__mod__', '__mul__', '__pow__', '__sub__', '__truediv__',
             '__radd__', '__rfloordiv__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__']
        self.assertEqual(sorted(unary), sorted(u))
        self.assertEqual(sorted(binary), sorted(b))

    def test_zero(self):
        self.check(r(), 0)
        self.check(r(), 0.0)
        self.check(r(), r())
        self.check(r(), r(0))
        self.check(r(), r(0.0))
        self.check(r(), r("0.0"))

    def test_init(self):
        self.check(r(3.1), 3.1)
        self.check(r(-3.7), r(-3.7))
        self.check(r(3.0), r(3))
        self.check(r("3"), r(3))
        self.check(r(-3), -3)
        self.check(r(1092837675), 1092837675)

    def test_casts(self):
        self.check(str(r(-64)), "-64.0", str)
        self.check(int(r(-50)), -50, int)
        self.check(float(r(9.8)), 9.8, float)
        self.check(bool(r()), False, bool)
        self.check(bool(r(1)), True, bool)
        self.check(bool(r(0.00001)), True, bool)

    # Unary Dunder Tests:

    def test_abs(self):
        self.check(abs(r(0)), 0)
        self.check(abs(r(4)), 4)
        self.check(abs(r(-4)), 4)

    def test_ceil(self):
        self.check(ceil(r(1.5)), 2)
        self.check(ceil(r(-1.5)), -1)

    def test_floor(self):
        self.check(floor(r(1.5)), 1)
        self.check(floor(r(-1.5)), -2)

    def test_neg(self):
        self.check(-r(0), 0)
        self.check(-r(4), -4)
        self.check(-r(-4), 4)

    def test_pos(self):
        self.check(+r(0), 0)
        self.check(+r(4), 4)
        self.check(+r(-4), -4)

    def test_round(self):
        self.check(round(r(1.5)), 2)
        self.check(round(r(-1.5)), -2)
        self.check(round(r(2.5)), 2)
        self.check(round(r(-2.5)), -2)
        self.check(round(r(9.1)), 9)
        self.check(round(r(-9.1)), -9)
        self.check(round(r(9.9)), 10)
        self.check(round(r(-9.9)), -10)

    def test_trunc(self):
        self.check(trunc(r(1.5)), 1)
        self.check(trunc(r(-1.5)), -1)
        self.check(trunc(r(2.5)), 2)
        self.check(trunc(r(-2.5)), -2)
        self.check(trunc(r(9.1)), 9)
        self.check(trunc(r(-9.1)), -9)
        self.check(trunc(r(9.9)), 9)
        self.check(trunc(r(-9.9)), -9)

    # Binary Dunder Tests: TODO

    def test_add(self):
        self.check(r(9) + 8, 17)

    def test_floordiv(self):
        pass

    def test_mod(self):
        pass

    def test_mul(self):
        pass

    def test_pow(self):
        pass

    def test_sub(self):
        pass

    def test_truediv(self):
        pass


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit:
        pass
