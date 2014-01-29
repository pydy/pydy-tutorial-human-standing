#!/usr/bin/env python

from pydy_viz.shapes import Cylinder, Sphere
from pydy_viz.visualization_frame import VisualizationFrame
from pydy_viz.scene import Scene

from .simulation import *

ankle_shape = Sphere(color='blue', radius=0.04)
knee_shape = Sphere(color='red', radius=0.04)
hip_shape = Sphere(color='green', radius=0.04)
torso_com_shape = Sphere(color='orange', radius=0.04)

ankle_viz_frame = VisualizationFrame(inertial_frame, ankle, ankle_shape)
knee_viz_frame = VisualizationFrame(inertial_frame, knee, knee_shape)
hip_viz_frame = VisualizationFrame(inertial_frame, hip, hip_shape)
torso_com_viz_frame = VisualizationFrame(inertial_frame, torso_mass_center,
                                         torso_com_shape)

lower_leg_shape = Cylinder('Lower Leg Cylinder', radius=0.08,
                           length=numerical_constants[0], color='red')
lower_leg_viz_frame = VisualizationFrame('Lower Leg', lower_leg,
                                         lower_leg_shape)


upper_leg_shape = Cylinder('Upper Leg Cylinder', radius=0.08,
                           length=numerical_constants[4], color='blue')
upper_leg_viz_frame = VisualizationFrame('Upper Leg', upper_leg,
                                         upper_leg_shape)


torso_shape = Cylinder('Torso Cylinder', radius=0.1,
                       length=numerical_constants[8], color='green')
torso_viz_frame = VisualizationFrame('Torso', torso, torso_shape)

scene = Scene(inertial_frame, ankle,
              knee_viz_frame, hip_viz_frame)#, torso_com_viz_frame,
              #lower_leg_viz_frame, upper_leg_viz_frame, torso_viz_frame)

scene.generate_visualization_json(coordinates + speeds, constants, y,
                                  numerical_constants)
