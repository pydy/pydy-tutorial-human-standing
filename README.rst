Introduction
============

This is the material for a tutorial on analyzing multibody dynamics with
scientific Python tools. It was first given as "Simulation and Control of
Biomechanical Systems with Python" at the `Midwest American Society of
Biomechanics Regional meeting
<http://www.uakron.edu/engineering/BME/ASB2014/>`_ on March 4th, 2014 in Akron,
Ohio and then a slightly modified version will be given as "`Dynamics and
Control with Python <https://us.pycon.org/2014/schedule/presentation/132/>`_"
at PYCON on April 9th, 2014 in Montreal.

Register for the PYCON tutorial here:

https://us.pycon.org/2014/

We will cover these main topics:

- Symbolic derivation of equations of motion for multibody systems.
- Numerical simulation of the system.
- 2D and 3D visualization of the motion of the system.
- Basic feedback control for stabilization.

The attendees will be exposed to various functionality of these Python tools:

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
students should have a working 3-link 2D inverted pendulum model of a human
that can be used for balancing studies. The free body diagram of the model is
shown below:

.. image:: notebooks/figures/human_balance_diagram.png

Installation
============

Python Packages
---------------

To run these notebooks the `SciPy Stack`_ is required. To obtain the needed
packages, we are recommending users install the `Anaconda Scientific Python
Distribution`_ which contains most of the necessary software and eases cross
platform installation. You should install Anaconda to your home directory. The
installation directory can simply be deleted when the tutorial is over if you
no longer want the files.

.. _SciPy Stack: http://www.scipy.org/stackspec.html
.. _Anaconda Scientific Python Distribution: https://store.continuum.io/cshop/anaconda/

First, `download and install Anaconda <http://continuum.io/downloads>`_ for
your operating system.

Then in a terminal (Anaconda CMD prompt on Windows) upgrade to SymPy 0.7.5 by
typing and executing::

   pip install --upgrade sympy

Then install PyDy with::

   pip install pydy

Note that this tutorial only runs on Python 2.7.

Web Browser
-----------

If you want to see the 3D visualizations you must use a WebGL compliant
browser. Visit http://get.webgl.org/ to see if your current browser supports
WebGL. If not, you will need to upgrade or install another browser. Visit
http://caniuse.com/webgl to choose a suitable browser. We've only confirmed the
following:

**Linux**

Latest versions of Firefox and Chrome work.

**Mac OSX**

Latest version Firefox works.

**Windows**

Latest version of Chrome works and IE 11 works.

We know that some OS browser combinations do not work. See
https://github.com/pydy/pydy-viz/issues/113 for more details.

Advanced SciPy Stack Installation
---------------------------------

There are many methods to installing the SciPy Stack. If you know what you are
doing then feel free to install relatively recent versions of NumPy (>= 1.6),
SciPy (>= 0.9), matplotlib (>= 0.10), and IPython (>=0.13) however you like.
Keep in mind that the tutorial will be tested to work with the versions
provided in Anaconda 1.9 (Python 2.7.6), SymPy 0.7.5, and PyDy 0.1.0. You can
find `various instructions for installing the SciPy stack`_ on the SciPy
website.

.. _various instructions for installing the SciPy stack: http://www.scipy.org/install.html

Use
===

Download the latest zipped tutorial materials from:

http://tinyurl.com/pycon-pydy-tutorial

and then extract the zip file. Open a terminal window in the ``notebooks``
directory and type::

   ipython notebook

Your web browser should open and you see a list of all the notebooks and can
click to open them and execute.

Notebooks
=========

These are the notebooks for the tutorial.

- [15 min] n00_python_intro.ipynb_
- [10 min] n01_dynamics_overview.ipynb_
- [3 min] n02_problem_introduction.ipynb_
- [28 min] n03_kinematics.ipynb_
- [13 min] n04_inertia.ipynb_
- [18 min] n05_kinetics.ipynb_
- [18 min] n06_equations_of_motion.ipynb_
- [23 min] n07_simulation.ipynb_
- [18 min] n08_visualization.ipynb_
- [20 min] n09_control.ipynb_

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
