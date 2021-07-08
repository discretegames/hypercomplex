"""This package provides a way to work with hypercomplex number algebras following the Cayley-Dickson construction."""

__all__ = """
reals
cayley_dickson_construction cd_construction
cayley_dickson_algebra cd_algebra
CD0 R Real
CD1 C Complex
CD2 Q Quaternion
CD3 O Octonion
CD4 S Sedenion
CD5 P Pathion
CD6 X Chingon
CD7 U Routon
CD8 V Voudon
""".split()

from hypercomplex.hypercomplex import \
    reals, \
    cayley_dickson_construction, cd_construction, \
    cayley_dickson_algebra, cd_algebra, \
    CD0, R, Real,\
    CD1, C, Complex, \
    CD2, Q, Quaternion, \
    CD3, O, Octonion, \
    CD4, S, Sedenion, \
    CD5, P, Pathion, \
    CD6, X, Chingon, \
    CD7, U, Routon, \
    CD8, V, Voudon
