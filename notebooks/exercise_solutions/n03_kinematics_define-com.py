upper_leg_mass_center = Point('U_o')
upper_leg_mass_center.set_pos(knee, upper_leg_com_length * upper_leg_frame.y)
upper_leg_mass_center.pos_from(ankle)

torso_mass_center = Point('T_o')
torso_mass_center.set_pos(hip, torso_com_length * torso_frame.y)
torso_mass_center.pos_from(ankle)