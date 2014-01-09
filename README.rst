Folks Involved
==============

- Jason: will be at PyCon and is leading the charge on this. I'm planning to be
  the main presenter of the tutorial (especially if I'm the only one there!).
- Tarun: We are trying to get funding for Tarun to come, but he will be helping
  prepare regardless.
- Gilbert: Is going to try to attend and will be helping prepare.
- Obinna (grad student in Jason's lab): Is going to try to attend and will be
  helping prepare.
- Chris: Probably not coming but said he could help out in preparation.

Goals
=====

- The tutorial must be accesible to people that have general technical degrees
  (not necessarily engineering). Many will be computer scientists, some will be
  makers/hackers, and others will be scientists of various backgrounds that are
  strong in programming skills. Most people will have good software development
  skills.
- We'd like to give people a way to model basic systems, understand their
  motion through simulation/visualization, and maybe allow them to control
  their system.
- We'd like to the students to complete an example problem that relates
  somewhat to the hacker/maker robotics world. This could be a robot arm, and
  RC car, or a heli/quad-copter, etc.
- I am likely going to be able to do the tutorial at a Biomechanics meeting in
  Akron in March so if the topic can be bio-mechanics that would be preferable.
- Software installation on all platforms should work (and we need VirtualBox or
  Wakari backup plans in case it doesn't).
- The tutorial must fit into 2 hours and 45 minutes.

Problem Ideas
=============

2D planar 2 DoF arm
-------------------

We'd have an "arm" that has a shoulder joint and an elbow joint. This arm would
be on a flat table an can slide along the table. The upper and lower arm rigid
bodies will have inertial properties of a human arm. There will be a joint
torque at each revolute joint. The equations of motion will be derived with the
two joints angles as the generalized coordinates. Equations for the x and y
locations of the "hand" will generated as output equations. We'd then simulate
the system with varying joint torque inputs. Then we'd create a controller to
cause the hand to track the time parameterized path of a cursive signature.
This system would model making a robot that can "write".

Tractor Trailer Truck
---------------------

A 2D model of a truck with trailer using the "bicycle" model of a car. The
lateral tire forces would be simple linear functions of the slip angle. We'd
make a controller to track a road path. This is very relevant to car video game
designs.

Balancing a pendulum
--------------------

Classic problem.

Sections
========

These sections could potentially be broken up into seperate notebooks but we'd
like to ensure that each new section builds on the previously completed
section.

Intro to tools
--------------

SymPy: symbols, functions, expressions, derivatives
SymPy mechanices: dynamicsymbols, vectors, reference frames
NumPy: basic array creation
SciPy: odeint
Matlplotlib: Maybe some 2D plotting

Intro to dynamics concepts
--------------------------

- Vectors, Reference Frames
- Rotations, direction cosine matrices
- mass, mass center, Inertia
- Position, Velocity, Acceleration
- Forces, Moments
- Equations of Motion
- Ordinary differential equations

Problem Definition
------------------

Describe the problem and the goals they are trying to achieve.

Kinematics
----------

Simply reference frame rotations. Location of points.

Dynamics
--------

Definition of forces and moments.

Output equations
----------------

Derive equations for any output variables.

Code Generation
---------------

Convert symbolic EoMs and output variables to numerical functions.

Simulation
----------

Simulate with odeint.

Visualization
-------------

Use PyDy viz and/or Matplotlib to animate the results.

Extra Sections
==============

Control
-------

If there is time we could make a controller and simulate/visualize the results.

Tasks
=====

- [ ] Create example problem to see if it works.
- [ ] Fix the PyDy website! (or make a new Sphinx or Jekyll based Github pages
  one).
- [ ] Make a PyDy package that includes sympy.physics.mechanics, pydy-viz, and
  pydy-code-gen. Release to PyPi and ensure it installs in Anaconda based
  enviroments (at least, can check more too) on all three main OS's.
