Introduction
============

This is the material for a tutorial on rigid body dynamics with scientific
Python tools. It will first be given as "Simulation and Control of
Biomechanical Systems with Python" at the `Midwest American Society of
Biomechanics Regional meeting
<http://www.uakron.edu/engineering/BME/ASB2014/>`_ on March 4th, 2014 in Akron,
Ohio and then a slightly modified version will be given as "`Dynamics and
Control with Python <https://us.pycon.org/2014/schedule/presentation/132/>`_"
at PYCON on April 9th, 2014 in Montreal.

Register for the MASB tutorial here (only 35 seats):

http://www.uakron.edu/engineering/BME/ASB2014/asb-2014-program-.dot

Register for the PYCON tutorial here:

https://us.pycon.org/2014/

We will cover these main topics:

- Symbolic derivation of equations of motion for rigid body systems.
- Numerical simulation of the system.
- 2D and 3D visualization of the motion of the system.
- Basic feedback control for stabilization.

The attendees will exposed to various functionality of these Python tools:

- Python_
- The SciPy Stack: SymPy_, NumPy_, SciPy_, matplotlib_, IPython_
- PyDy_

.. _Python: http://www.python.org
.. _SymPy: http://www.sympy.org
.. _NumPy: http://numpy.scipy.org
.. _SciPy: http://www.scipy.org/scipylib/index.html
.. _matplotlib: http://matplotlib.org
.. _IPython: http://www.ipython.org
.. _PyDy: http://www.pydy.org

License
=======

All materials herein are licensed under `Create Commons Attribution 4.0`_.

.. _Create Commons Attribution 4.0: http://creativecommons.org/licenses/by/4.0/

Example Problem
===============

The tutorial will work through the PyDy workflow in small steps. At the end the
students should have a working 3 link 2D inverted pendulum model of a human
that can be used for balancing studies. The free body diagram of the model is
shown below:

.. image:: notebooks/figures/human_balance_diagram.png

Installation
============

To run these notebooks the `SciPy Stack`_ is required. To obtain the needed
packages, we are recommending users install the `Anaconda Scientific Python
Distribution`_ which contains most of the necessary software and eases cross
platform installation.

.. _SciPy Stack: http://www.scipy.org/stackspec.html
.. _Anaconda Scientific Python Distribution: https://store.continuum.io/cshop/anaconda/

First, `download and install Anaconda <http://continuum.io/downloads>`_ for
your operating system.

Then in an Anaconda terminal (Anaconda CMD prompt on Windows) upgrade to
SymPy 0.7.5 by typing and executing::

   pip install --upgrade sympy

Then install PyDy with::

   pip install pydy

Advanced SciPy Stack Installation
---------------------------------

There are many methods to installing the SciPy Stack. If you know what you are
doing then feel free to install relatively recent versions of NumPy (>= 1.6),
SciPy (>= 0.9), matplotlib (>= 0.10), and IPython (>=0.13) however you like.
Keep in mind that the tutorial wil be expected to work with the versions
provided in Anaconda 1.9, SymPy 0.7.5, and PyDy 0.1.0. You can find `various
instructions for installing the SciPy stack`_ on the SciPy website.

.. _various instructions for installing the SciPy stack: http://www.scipy.org/install.html

Use
===

Download and extract the tutorial materials from:

https://github.com/PythonDynamics/pydy-tutorial-pycon-2014/archive/master.zip

Open a terminal window in the ``notebooks`` directory and type::

   ipython notebook

Your browser should open and you see a list of all the notebooks and can click
to open them and execute.

Notebooks
=========

These are the notebooks for the tutorial.

- n00_python_intro.ipynb_
- n01_dynamics_overview.ipynb_
- n02_problem_introduction.ipynb_
- n03_kinematics.ipynb_
- n04_inertia.ipynb_
- n05_kinetics.ipynb_
- n06_equations_of_motion.ipynb_
- n07_simulation.ipynb_
- n08_visualization.ipynb_
- n09_control.ipynb_

.. _n00_python_intro.ipynb: http://nbviewer.ipython.org/github/PythonDynamics/pydy-tutorial-pycon-2014/blob/master/notebooks/n00_python_intro.ipynb
.. _n01_dynamics_overview.ipynb: http://nbviewer.ipython.org/github/PythonDynamics/pydy-tutorial-pycon-2014/blob/master/notebooks/n01_dynamics_overview.ipynb
.. _n02_problem_introduction.ipynb: http://nbviewer.ipython.org/github/PythonDynamics/pydy-tutorial-pycon-2014/blob/master/notebooks/n02_problem_introduction.ipynb
.. _n03_kinematics.ipynb: http://nbviewer.ipython.org/github/PythonDynamics/pydy-tutorial-pycon-2014/blob/master/notebooks/n03_kinematics.ipynb
.. _n04_inertia.ipynb: http://nbviewer.ipython.org/github/PythonDynamics/pydy-tutorial-pycon-2014/blob/master/notebooks/n04_inertia.ipynb
.. _n05_kinetics.ipynb: http://nbviewer.ipython.org/github/PythonDynamics/pydy-tutorial-pycon-2014/blob/master/notebooks/n05_kinetics.ipynb
.. _n06_equations_of_motion.ipynb: http://nbviewer.ipython.org/github/PythonDynamics/pydy-tutorial-pycon-2014/blob/master/notebooks/n06_equations_of_motion.ipynb
.. _n07_simulation.ipynb: http://nbviewer.ipython.org/github/PythonDynamics/pydy-tutorial-pycon-2014/blob/master/notebooks/n07_simulation.ipynb
.. _n08_visualization.ipynb: http://nbviewer.ipython.org/github/PythonDynamics/pydy-tutorial-pycon-2014/blob/master/notebooks/n08_visualization.ipynb
.. _n09_control.ipynb: http://nbviewer.ipython.org/github/PythonDynamics/pydy-tutorial-pycon-2014/blob/master/notebooks/n09_control.ipynb
