"""This package provides a way to work with hypercomplex number algebras following the Cayley-Dickson construction."""

__all__ = """
reals
cayley_dickson_construction cd_construction
cayley_dickson_algebra cd_algebra
CD1 R Real
CD2 C Complex
CD4 Q Quaternion
CD8 O Octonion
CD16 S Sedenion
CD32 P Pathion
CD64 X Chingon
CD128 U Routon
CD256 V Voudon
CD
""".split()

from hypercomplex.hypercomplex import \
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
