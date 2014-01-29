Introduction
============

This is the material for a tutorial on "Dynamics and Control with Python". It
will be first given at the Midwest American Society of Biomechanics Regional
meeting on March 4th, 2014 in Akron, Ohio and then slightly modified version
will be given to at PYCON on April 9th, 2014 in Montreal.

We will cover these topics:

- Symbolic derivation of equations of motion for rigid body systems
- Numerical simulation of the system
- 2D and 3D visualization of the motion of the system
- Using feedback control for stablization.

We will learn how to use some of these Python packages:

- Python
- SymPy
- NumPy
- SciPy
- matplotlib
- PyDy

Folks Involved
==============

- Jason: will be at MSASB and PyCon and is leading the charge on this. I'm
  planning to be the main presenter of the tutorial (especially if I'm the only
  one there!).
- Tarun: We are trying to get funding for Tarun to come to PYCON, but he will
  be helping prepare regardless.
- Gilbert: Is going to try to attend PYCON and will be helping prepare.
- Obinna (grad student in Jason's lab): Is going to attend MASB and probably
  PYCON and will be helping prepare.
- Chris: Probably not coming but said he could help out in preparation.

Goals
=====

- The MASB version of the tutorial should be accessible to graduate students
  (and above) in biomechanical engineering related fields.
- The PYCON version of the tutorial must be accesible to people that have
  general technical degrees (not necessarily engineering). Many will be
  computer scientists, some will be makers/hackers, and others will be
  scientists of various backgrounds that are strong in programming skills. Most
  people will have good software development skills.
- We'd like to give people a way to model basic systems, understand their
  motion through simulation/visualization, and maybe allow them to control
  their system.
- We'd like to the students to complete an example problem that relates
  somewhat to the hacker/maker robotics world. This could be a robot arm, and
  RC car, or a heli/quad-copter, etc. Note: We are going to give the tutorial
  at a Biomechanics meeting in Akron on March 4th so I'm heavily leaning to a
  biomechanical influenced example problem that is applicable to robotics too.
- Software installation on all platforms should work (and we need VirtualBox or
  Wakari backup plans in case it doesn't).
- The tutorial must fit into 2 hours and 45 minutes.


Installation
============

Recommend Method
----------------

Download and install Anaconda for your operating system.

Then in a terminal type::

   pip install -U pydy

Download and extract the tutorial materials from:

https://github.com/PythonDynamics/pydy-tutorial-pycon-2014/archive/master.zip

Open a terminal window in the notebooks directory and type::

   ipython notebook

You should see a list of all the notebooks and can click to open them and
execute.

Example Problem
===============

The tutorial will work through the PyDy workflow in small steps. At the end the
students should have a working 3 link 2D inverted pendulum model of a human
that can be used for balancing studies.

Notebooks
---------

- n00_python_intro.ipynb
- n01_dynamics_overview.ipynb
- n02_problem_introduction.ipynb
- `n03_kinematics.ipynb <http://nbviewer.ipython.org/github/PythonDynamics/pydy-tutorial-pycon-2014/blob/master/notebooks/n03_kinematics.ipynb>`_
- n04_inertia.ipynb
- n05_kinetics.ipynb
- n06_equations_of_motion.ipynb
- n07_simulation.ipynb
- n08_visualization.ipynb
- n09_control.ipynb
