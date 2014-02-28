upper_leg_torque = (upper_leg_frame, knee_torque * inertial_frame.z - hip_torque * inertial_frame.z)

torso_torque = (torso_frame, hip_torque * inertial_frame.z)