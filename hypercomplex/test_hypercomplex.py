"""Test suite for hypercomplex.py based on code from README.md and examples.py."""

import unittest
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


# This isn't the most thorough test suite ever but it covers the basics in Python 3.6+ with tox.
class TestHypercomplex(unittest.TestCase):

    def assertEqualT(self, a, b):
        self.assertEqual(a, b)
        self.assertEqual(type(a), type(b))

    # Tests from README.md:

    def test_basics(self):
        c = Complex(0, 7)
        self.assertEqual(str(c), "(0 7)")
        self.assertEqual(c, 7j)

        q = Quaternion(1.1, 2.2, 3.3, 4.4)
        self.assertEqual(str(2 * q), "(2.2 4.4 6.6 8.8)")

        self.assertEqual(Quaternion.e_matrix(),
                         "e0  e1  e2  e3\ne1 -e0  e3 -e2\ne2 -e3 -e0  e1\ne3  e2 -e1 -e0\n")

        o = Octonion(0, 0, 0, 0, 8, 8, 9, 9)
        self.assertEqual(o + q, O(1.1, 2.2, 3.3, 4.4, 8, 8, 9, 9))

        v = Voudon()
        self.assertEqual(v, 0)
        self.assertEqual(len(v), 256)

        BeyondVoudon = cayley_dickson_construction(Voudon)
        self.assertEqual(len(BeyondVoudon()), 512)

    def test_reals(self):
        from decimal import Decimal
        D = reals(Decimal)
        self.assertEqual(D(10) / 4, 2.5)
        self.assertEqual(D(3) * D(9), 27)

    def test_cd_construction(self):
        RealNum = reals()
        ComplexNum = cayley_dickson_construction(RealNum)
        QuaternionNum = cd_construction(ComplexNum)

        q = QuaternionNum(1, 2, 3, 4)
        self.assertEqual(q, Q(1, 2, 3, 4))
        self.assertEqual(str(1 / q), "(0.0333333 -0.0666667 -0.1 -0.133333)")
        self.assertEqual(q + 1 + 2j, Q(2, 4, 3, 4))

    def test_cd_algebra(self):
        OctonionNum = cayley_dickson_algebra(3)
        o = OctonionNum(8, 7, 6, 5, 4, 3, 2, 1)
        self.assertEqual(o, O(8, 7, 6, 5, 4, 3, 2, 1))
        self.assertEqual(2 * o, O(16, 14, 12, 10, 8, 6, 4, 2))
        self.assertEqual(o.conjugate(), O(8, -7, -6, -5, -4, -3, -2, -1))

    def test_types(self):
        self.assertEqual(Real(4), cd_algebra(0)(4))
        self.assertEqual(C(3 - 7j), cd_algebra(1)(3 - 7j))
        self.assertEqual(CD4(.1, -2.2, 3.3e3), cd_algebra(2)(.1, -2.2, 3.3e3))
        self.assertEqual(CD[3](1, 0, 2, 0, 3), cd_algebra(3)(1, 0, 2, 0, 3))
        self.assertEqual(len(CD), 9)

    # Tests from examples.py:

    def test_init(self):
        self.assertEqual(R(-1.5), -1.5)
        self.assertEqual(C(2, 3), 2 + 3j)
        self.assertEqual(C(2 + 3j), 2 + 3j)
        self.assertEqual(repr(Q(4, 5, 6, 7)), "(4 5 6 7)")
        self.assertEqual(Q(4 + 5j, C(6, 7), pair=True), Q(4, 5, 6, 7))
        self.assertEqual(P(), 0)
        self.assertRaises(TypeError, C, 1, 2, 3)

    def test_add_subtract(self):
        self.assertEqual(Q(0, 1, 2, 2) + C(9, -1), Q(9, 0, 2, 2))
        self.assertEqual(100.1 - O(0, 0, 0, 0, 1.1, 2.2, 3.3, 4.4),
                         O(100.1, 0, 0, 0, -1.1, -2.2, -3.3, -4.4))

    def test_multiply(self):
        self.assertEqual(10 * S(1, 2, 3), Q(10, 20, 30))
        self.assertEqual(Q(1.5, 2.0) * O(0, -1), C(2, -1.5))
        self.assertEqual(Q(1, 2, 3, 4) * Q(1, 0, 0, 1), Q(-3, 5, 1, 5))
        self.assertEqual(Q(1, 0, 0, 1) * Q(1, 2, 3, 4), Q(-3, -1, 5, 5))

    def test_divide(self):
        self.assertEqual(100 / C(0, 2), C(0, -50))
        inv = Q(1 / 5, -1 / 15, 1 / 15, -7 / 15)
        self.assertAlmostEqual(C(2, 2) / Q(1, 2, 3, 4), inv)
        self.assertAlmostEqual(C(2, 2) * Q(1, 2, 3, 4).inverse(), inv)
        self.assertEqual(R(2).inverse(), 0.5)
        self.assertEqual(1 / R(2), 0.5)

    def test_power(self):
        q = Q(0, 3, 4, 0)
        q5 = Q(0, 1875, 2500, 0)
        self.assertEqual(q**5, q5)
        self.assertEqual(q * q * q * q * q, q5)
        q1 = Q(0, -0.12, -0.16, 0)
        self.assertEqual(q**-1, q1)
        self.assertEqual(1 / q, q1)
        self.assertEqual(q**0, Q(1, 0, 0, 0))

    def test_conjugate(self):
        self.assertEqual(R(9).conjugate(), (9).conjugate())
        self.assertEqual(C(9, 8).conjugate(), (9 + 8j).conjugate())
        self.assertEqual(Q(9, 8, 7, 6).conjugate(), Q(9, -8, -7, -6))

    def test_norm(self):
        o = O(3, 4)
        self.assertEqualT(o.norm(), 5.0)
        self.assertEqual(abs(o), 5)
        self.assertEqual(o.norm_squared(), 25.0)

    def test_equals(self):
        self.assertEqual(R(999), V(999))
        self.assertEqual(C(1, 2), Q(1, 2))
        self.assertNotEqual(C(1, 2), Q(1, 2, 0.1))
        self.assertNotEqual(C(0, 0.1), C(0.1, 1))

    def test_coefficients(self):
        self.assertEqual(R(100).coefficients(), (100.0,))
        q = Q(2, 3, 4, 5)
        self.assertEqual(q.coefficients(), (2, 3, 4, 5))
        self.assertEqual(q.real, 2.0)
        self.assertEqual(q.imag, 3.0)
        self.assertEqual((q[0], q[1], q[2], q[3]), (2, 3, 4, 5))
        self.assertEqual(tuple(q), (2, 3, 4, 5))
        self.assertEqual(list(q), [2, 3, 4, 5])

    def test_e(self):
        self.assertEqual(C.e(0), C(1, 0))
        self.assertEqual(C.e(1), C(0, 1))
        self.assertEqual(O.e(3), O(0, 0, 0, 1, 0, 0, 0, 0))

    def test_e_matrix(self):
        self.assertEqual(R.e_matrix(), 'e0\n')
        self.assertEqual(C.e_matrix(False, True), [[1, 1j], [1j, -1]])

    def test_conversion(self):
        self.assertFalse(bool(Q()))
        self.assertTrue(bool(Q(0, 0, 0.01, 0)))
        self.assertEqualT(complex(Q(5, 5)), 5 + 5j)
        self.assertEqualT(int(V(9.9)), 9)
        self.assertRaises(TypeError, float, C(1, 2))

    def test_format(self):
        o = O(0.001, 1, -2, 3.3333, 4e5)
        self.assertEqual(
            f"{o:.2f}", "(0.00 1.00 -2.00 3.33 400000.00 0.00 0.00 0.00)")
        self.assertEqual(f"{R(23.9):04.0f}", "(0024)")

    def test_len(self):
        self.assertEqual(len(R()), 1)
        self.assertEqual(len(C(7, 7)), 2)
        self.assertEqual(len(U()), 128)

    def test_in(self):
        self.assertTrue(3 in Q(1, 2, 3, 4))
        self.assertFalse(5 in Q(1, 2, 3, 4))

    def test_copy(self):
        x = O(9, 8, 7)
        y = x.copy()
        self.assertTrue(x == y)
        self.assertFalse(x is y)

    def test_base(self):
        self.assertEqual(R.base(), float)
        self.assertEqual(V.base(), float)
        A = cayley_dickson_algebra(20, int)
        self.assertEqual(A.base(), int)

    def test_zero_divisors(self):
        s1 = S.e(5) + S.e(10)
        s2 = S.e(6) + S.e(9)
        self.assertEqual(s1, S(0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0))
        self.assertEqual(s2, S(0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0))
        self.assertEqual(s1 * s2, 0)
        self.assertEqual((1 / s1) * (1 / s2), 0)
        self.assertRaises(ZeroDivisionError, lambda: 1 / (s1 * s2))


if __name__ == "__main__":
    print('Running tests from main...')
    try:
        unittest.main()
    except SystemExit:  # So debugger doesn't trigger.
        pass
