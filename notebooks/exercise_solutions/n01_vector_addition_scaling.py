from sympy import sin, cos, pi
from sympy.abc import l, theta

N = ReferenceFrame('N')

v1 = l * cos(pi / 4) * N.x + l * sin(pi / 4) * N.y
v2 = -10 * N.y
v3 = l * cos(theta) * N.x + l * sin(theta) * N.y

v1 + v2 - 5 * v3
