torso_frame.orient(upper_leg_frame, 'Axis', (theta3, upper_leg_frame.z))
simplify(torso_frame.dcm(inertial_frame))