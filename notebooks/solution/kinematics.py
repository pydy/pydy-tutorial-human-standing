#!/usr/bin/env python

from sympy import symbols
from sympy.physics.mechanics import dynamicsymbols, ReferenceFrame, Point

# Orientations
# ============

theta1, theta2, theta3 = dynamicsymbols('theta1, theta2, theta3')

inertial_frame = ReferenceFrame('I')

lower_leg_frame = ReferenceFrame('L')

lower_leg_frame.orient(inertial_frame, 'Axis', (theta1, inertial_frame.z))

upper_leg_frame = ReferenceFrame('U')

upper_leg_frame.orient(lower_leg_frame, 'Axis', (theta2, lower_leg_frame.z))

torso_frame = ReferenceFrame('T')

torso_frame.orient(upper_leg_frame, 'Axis', (theta3, upper_leg_frame.z))

# Point Locations
# ===============

# Joints
# ------

lower_leg_length, upper_leg_length = symbols('l_L, l_U')

ankle = Point('A')

knee = Point('K')
knee.set_pos(ankle, lower_leg_length * lower_leg_frame.y)

hip = Point('H')
hip.set_pos(knee, upper_leg_length * upper_leg_frame.y)

# Center of mass locations
# ------------------------

lower_leg_com_length, upper_leg_com_length, torso_com_length = symbols('d_L, d_U, d_T')

lower_leg_mass_center = Point('L_o')
lower_leg_mass_center.set_pos(ankle, lower_leg_com_length * lower_leg_frame.y)

upper_leg_mass_center = Point('U_o')
upper_leg_mass_center.set_pos(knee, upper_leg_com_length * upper_leg_frame.y)

torso_mass_center = Point('T_o')
torso_mass_center.set_pos(hip, torso_com_length * torso_frame.y)

# Define kinematical differential equations
# =========================================

omega1, omega2, omega3 = dynamicsymbols('omega1, omega2, omega3')

time = symbols('t')

kinematical_differential_equations = [omega1 - theta1.diff(time),
                                      omega2 - theta2.diff(time),
                                      omega3 - theta3.diff(time)]

# Angular Velocities
# ==================

lower_leg_frame.set_ang_vel(inertial_frame, omega1 * inertial_frame.z)

upper_leg_frame.set_ang_vel(lower_leg_frame, omega2 * lower_leg_frame.z)

torso_frame.set_ang_vel(upper_leg_frame, omega3 * upper_leg_frame.z)

# Linear Velocities
# =================

ankle.set_vel(inertial_frame, 0)

lower_leg_mass_center.v2pt_theory(ankle, inertial_frame, lower_leg_frame)

knee.v2pt_theory(ankle, inertial_frame, lower_leg_frame)

upper_leg_mass_center.v2pt_theory(knee, inertial_frame, upper_leg_frame)

hip.v2pt_theory(knee, inertial_frame, upper_leg_frame)

torso_mass_center.v2pt_theory(hip, inertial_frame, torso_frame)
