#!/usr/bin/env python

from sympy.physics.mechanics import KanesMethod

from .kinetics import *

# Equations of Motion
# ===================

coordinates = [theta1, theta2, theta3]

speeds = [omega1, omega2, omega3]

kane = KanesMethod(inertial_frame,
                   coordinates,
                   speeds,
                   kinematical_differential_equations)

loads = [lower_leg_grav_force,
         upper_leg_grav_force,
         torso_grav_force,
         lower_leg_torque,
         upper_leg_torque,
         torso_torque]

bodies = [lower_leg, upper_leg, torso]

fr, frstar = kane.kanes_equations(loads, bodies)

mass_matrix = kane.mass_matrix_full
forcing_vector = kane.forcing_full
