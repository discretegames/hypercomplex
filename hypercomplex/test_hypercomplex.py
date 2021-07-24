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


class TestHypercomplex(unittest.TestCase):
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

    def test_init(self):
        self.assertEqual(R(-1.5), -1.5)
        self.assertEqual(C(2, 3), 2 + 3j)
        self.assertEqual(C(2 + 3j), 2 + 3j)
        self.assertEqual(repr(Q(4, 5, 6, 7)), "(4 5 6 7)")
        self.assertEqual(Q(4 + 5j, C(6, 7), pair=True), Q(4, 5, 6, 7))
        self.assertEqual(P(), 0)

    def test_addsub(self):
        pass  # todo
        # self.assertEqual(Q(0, 1, 2, 2) + C(9, -1),


if __name__ == "__main__":
    print('Running tests from main...')
    try:
        unittest.main()
    except SystemExit:  # So debugger doesn't trigger.
        pass
