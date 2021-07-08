"""This package provides a way to work with hypercomplex number algebras following the Cayley-Dickson construction."""

__all__ = """
reals
cayley_dickson_construction cd_construction
cayley_dickson_algebra cd_algebra
R Real CD1
C Complex CD2
Q Quaternion CD4
O Octonion CD8
S Sedenion CD16
P Pathion CD32
X Chingon CD64
U Routon CD128
V Voudon CD256
""".split()

from hypercomplex.hypercomplex import \
    reals, \
    cayley_dickson_construction, cd_construction, \
    cayley_dickson_algebra, cd_algebra, \
    R, Real, CD1,\
    C, Complex, CD2, \
    Q, Quaternion, CD4, \
    O, Octonion, CD8, \
    S, Sedenion, CD16, \
    P, Pathion, CD32, \
    X, Chingon, CD64, \
    U, Routon, CD128, \
    V, Voudon, CD256
