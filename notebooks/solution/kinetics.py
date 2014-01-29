#!/usr/bin/env python

from .inertia import *

# Gravity
# =======

g = symbols('g')

lower_leg_grav_force = (lower_leg_mass_center,
                        -lower_leg_mass * g * inertial_frame.y)
upper_leg_grav_force = (upper_leg_mass_center,
                        -upper_leg_mass * g * inertial_frame.y)
torso_grav_force = (torso_mass_center, -torso_mass * g * inertial_frame.y)

# Joint Torques
# =============

ankle_torque, knee_torque, hip_torque = dynamicsymbols('T_a, T_k, T_h')

lower_leg_torque = (lower_leg_frame,
                    ankle_torque * inertial_frame.z - knee_torque *
                    inertial_frame.z)

upper_leg_torque = (upper_leg_frame,
                    knee_torque * inertial_frame.z - hip_torque *
                    inertial_frame.z)

torso_torque = (torso_frame, hip_torque * inertial_frame.z)
