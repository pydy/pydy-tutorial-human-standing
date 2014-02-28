upper_leg_length = symbols('l_U')
hip = Point('H')
hip.set_pos(knee, upper_leg_length * upper_leg_frame.y)
hip.pos_from(ankle)