#!/usr/bin/env python

from sympy.physics.mechanics import inertia, RigidBody

from .kinematics import *

# Mass
# ====

lower_leg_mass, upper_leg_mass, torso_mass = symbols('m_L, m_U, m_T')

# Inertia
# =======

lower_leg_inertia, upper_leg_inertia, torso_inertia = symbols('I_Lz, I_Uz, I_Tz')

lower_leg_inertia_dyadic = inertia(lower_leg_frame, 0, 0, lower_leg_inertia)

lower_leg_central_inertia = (lower_leg_inertia_dyadic, lower_leg_mass_center)

upper_leg_inertia_dyadic = inertia(upper_leg_frame, 0, 0, upper_leg_inertia)

upper_leg_central_inertia = (upper_leg_inertia_dyadic, upper_leg_mass_center)

torso_inertia_dyadic = inertia(torso_frame, 0, 0, torso_inertia)

torso_central_inertia = (torso_inertia_dyadic, torso_mass_center)

# Rigid Bodies
# ============

lower_leg = RigidBody('Lower Leg', lower_leg_mass_center, lower_leg_frame,
                      lower_leg_mass, lower_leg_central_inertia)

upper_leg = RigidBody('Upper Leg', upper_leg_mass_center, upper_leg_frame,
                      upper_leg_mass, upper_leg_central_inertia)

torso = RigidBody('Torso', torso_mass_center, torso_frame,
                  torso_mass, torso_central_inertia)
