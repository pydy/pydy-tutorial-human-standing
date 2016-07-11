from sympy import pi
from sympy.abc import l, w

keyboard_frame = ReferenceFrame('K')
intermediate_frame = ReferenceFrame('I')
screen_frame = ReferenceFrame('S')

intermediate_frame.orient(keyboard_frame, 'Axis', (theta, -keyboard_frame.z))
screen_frame.orient(intermediate_frame, 'Axis', (pi, intermediate_frame.y))

v = l * keyboard_frame.y + w * keyboard_frame.z - l * screen_frame.y
v.express(keyboard_frame)
