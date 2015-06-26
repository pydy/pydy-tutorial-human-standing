#!/usr/bin/env python

from pydy.viz.shapes import Cylinder, Sphere
from pydy.viz.visualization_frame import VisualizationFrame
from pydy.viz.scene import Scene

from .simulation import *

ankle_shape = Sphere(color='black', radius=0.1)
knee_shape = Sphere(color='black', radius=0.1)
hip_shape = Sphere(color='black', radius=0.1)
head_shape = Sphere(color='black', radius=0.125)

ankle_viz_frame = VisualizationFrame(inertial_frame, ankle, ankle_shape)
knee_viz_frame = VisualizationFrame(inertial_frame, knee, knee_shape)
hip_viz_frame = VisualizationFrame(inertial_frame, hip, hip_shape)

head = Point('N')  # N for Noggin
head.set_pos(hip, 2 * torso_com_length * torso_frame.y)
head_viz_frame = VisualizationFrame(inertial_frame, head, head_shape)

constants_dict = dict(zip(constants, numerical_constants))

lower_leg_center = Point('l_c')
upper_leg_center = Point('u_c')
torso_center = Point('t_c')

lower_leg_center.set_pos(ankle, lower_leg_length / 2 * lower_leg_frame.y)
upper_leg_center.set_pos(knee, upper_leg_length / 2 * upper_leg_frame.y)
torso_center.set_pos(hip, torso_com_length * torso_frame.y)

lower_leg_shape = Cylinder(radius=0.08,
                           length=constants_dict[lower_leg_length],
                           color='blue')
lower_leg_viz_frame = VisualizationFrame('Lower Leg', lower_leg_frame,
                                         lower_leg_center, lower_leg_shape)

upper_leg_shape = Cylinder(radius=0.08,
                           length=constants_dict[upper_leg_length],
                           color='green')
upper_leg_viz_frame = VisualizationFrame('Upper Leg', upper_leg_frame,
                                         upper_leg_center, upper_leg_shape)

torso_shape = Cylinder(radius=0.08,
                       length=2 * constants_dict[torso_com_length],
                       color='red')

torso_viz_frame = VisualizationFrame('Torso', torso_frame, torso_center,
                                     torso_shape)

scene = Scene(inertial_frame, ankle,
              ankle_viz_frame, knee_viz_frame, hip_viz_frame, head_viz_frame,
              lower_leg_viz_frame, upper_leg_viz_frame, torso_viz_frame)

scene.constants = constants_dict
scene.states_symbols = coordinates + speeds
scene.states_trajectories = y
