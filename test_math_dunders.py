from math_dunders import math_dunders
import unittest
from math import ceil, floor, trunc


@math_dunders
class r(float):  # Real number.
    pass


class TestMathDunders(unittest.TestCase):
    def assertTypes(self, a, b, a_type=r, b_type=None):
        if a_type is not None:
            self.assertEqual(type(a), a_type)
        if b_type is not None:
            self.assertEqual(type(b), b_type)

    def assertEq(self, a, b, a_type=r, b_type=None):
        self.assertEqual(a, b)
        self.assertTypes(a, b, a_type, b_type)

    def assertNeq(self, a, b, a_type=r, b_type=None):
        self.assertNotEqual(a, b)
        self.assertTypes(a, b, a_type, b_type)

    # Miscellaneous Tests:

    def test_zero(self):
        self.assertEq(r(), 0)
        self.assertEq(r(), 0.0)
        self.assertEq(r(), r())
        self.assertEq(r(), r(0))
        self.assertEq(r(), r(0.0))
        self.assertEq(r(), r("0.0"))

    def test_init(self):
        self.assertEq(r(3.1), 3.1)
        self.assertEq(r(-3.7), r(-3.7))
        self.assertEq(r(3.0), r(3))
        self.assertEq(r("3"), r(3))
        self.assertEq(r(-3), -3)

        self.assertNeq(r(-1), r(1))
        self.assertNeq(r(2), r(3))

    # Unary Dunder Tests:

    def test_abs(self):
        self.assertEq(abs(r(0)), 0)
        self.assertEq(abs(r(4)), 4)
        self.assertEq(abs(r(-4)), 4)

    def test_ceil(self):
        raise NotImplementedError

    def test_floor(self):
        raise NotImplementedError

    def test_neg(self):
        raise NotImplementedError

    def test_pos(self):
        raise NotImplementedError

    def test_round(self):
        raise NotImplementedError

    def test_trunc(self):
        raise NotImplementedError

    # Binary Dunder Tests:

    def test_add(self):
        raise NotImplementedError

    def test_floordiv(self):
        raise NotImplementedError

    def test_mod(self):
        raise NotImplementedError

    def test_mul(self):
        raise NotImplementedError

    def test_pow(self):
        raise NotImplementedError

    def test_sub(self):
        raise NotImplementedError

    def test_truediv(self):
        raise NotImplementedError


if __name__ == "__main__":
    try:
        unittest.main()
    except SystemExit:
        pass
