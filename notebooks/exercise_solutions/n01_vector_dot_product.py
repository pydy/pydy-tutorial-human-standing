from sympy import acos

N = ReferenceFrame('N')

v1 = a * N.x + b * N.y + a * N.z
v2 = b * N.x + a * N.y + b * N.z

acos(v1.dot(v2) / (v1.magnitude() * v2.magnitude()))
