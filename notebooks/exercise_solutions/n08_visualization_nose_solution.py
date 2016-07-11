from pydy.viz.shapes import Cone

nose_frame=ReferenceFrame("S")
from sympy import pi
nose_frame.orient(torso_frame, 'Axis', (pi/2, inertial_frame.z))
nose_shape = Cone(radius=0.0675, length=.25, color='yellow')
nose=Point("S") #S for schnooze
nose.set_pos(head, -0.25*nose_frame.y)
nose_viz_frame = VisualizationFrame("Nose",nose_frame, nose, nose_shape)

scene2 = Scene(inertial_frame, ankle)
scene2.visualization_frames = [ankle_viz_frame,
                              knee_viz_frame,
                              hip_viz_frame,
                              head_viz_frame,
                              nose_viz_frame,
                              lower_leg_viz_frame,
                              upper_leg_viz_frame,
                              torso_viz_frame]
scene2.states_symbols = coordinates + speeds
scene2.constants = constants_dict
scene2.states_trajectories = y

scene2.display_ipython()
