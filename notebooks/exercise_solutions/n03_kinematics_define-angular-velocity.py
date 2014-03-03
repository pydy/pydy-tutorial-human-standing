lower_leg_frame.set_ang_vel(inertial_frame, omega1 * inertial_frame.z)
lower_leg_frame.ang_vel_in(inertial_frame)

upper_leg_frame.set_ang_vel(lower_leg_frame, omega2 * inertial_frame.z)
upper_leg_frame.ang_vel_in(inertial_frame)

torso_frame.set_ang_vel(upper_leg_frame, omega3 * inertial_frame.z)
torso_frame.ang_vel_in(inertial_frame)