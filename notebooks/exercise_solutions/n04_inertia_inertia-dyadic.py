upper_leg_inertia_dyadic = inertia(upper_leg_frame, 0, 0, upper_leg_inertia)
upper_leg_inertia_dyadic.to_matrix(upper_leg_frame)

upper_leg_central_inertia = (upper_leg_inertia_dyadic, upper_leg_mass_center)

torso_inertia_dyadic = inertia(torso_frame, 0, 0, torso_inertia)
torso_inertia_dyadic.to_matrix(torso_frame)

torso_central_inertia = (torso_inertia_dyadic, torso_mass_center)