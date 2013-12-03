Outline
=======

We will work through two parallel but similar problems in the tutorial. The
first will be a demonstration problem in which the full solutions will be shown
and each step will be explained, the second will be a similar problem that the
attendees will work on in pairs to come up with the solution. I’ll introduce
each stage of the problem derivation and development in short ~5 minute
sections and then have the attendees complete the derivation of their problem
using the software tools that have been presented.

1. [00:00] Introduction

   - A wee bit about the presenter
   - Attendees introduce themselves to their neighbor and pair up

2. [00:05] Brief introduction to multibody systems and controls

   - Newton’s Laws, reference frames, velocity, acceleration, forces/torques
   - Ordinary differential equations and their solutions
   - Applications: robots, vehicles, etc

3. [00:10] Brief intro to the software stack (SymPy, SciPy, python-control)

   - SymPy and the Mechanics package
   - NumPy for array computations
   - SciPy for ODE integration (scipy.integrate.odeint)
   - matplotlib for 2D plotting and basic animation
   - IPython Notebook for interactive work
   - PyDy: Mechanics, CodeGen, Viz
   - Check to see everyone can import all of these and the versions are high
     enough

4. [00:15] Derivation of a simple two body 2D problem by hand (the example
   problem)

   - This will be done on a chalkboard, whiteboard, large paper, or overhead
     projector

5. [00:25] Exercise: Draw free body diagram of a two body 2D problem (the
   exercise problem)
6. [00:40] Intro to SymPy Mechanics with a derivation of the simple 2D two body
   problem with SymPy Mechanics
7. [00:50] Exercise: Derive equations of motion of simple 2D problem using SymPy
   Mechanics
8. [01:05] ODE integration routine overview and various Python packages (scipy,
   assimulo, pydstool, sundials, etc)
9. [01:15] Simulate the example problem with SciPy
10. [01:25] Exercise: Simulate the exercise problem
11. [01:35] Break
11. [01:50] 2D plotting of the state trajectories with matplotlib
12. [01:55] Excercise: Plot the simulation results of the exercise problem
13. [02:05] Demonstrate 2D animation the free motion of the example model with
    matplotlib
14. [02:20] Exercise: Animate the 2D exercise problem
15. [02:40] 3D animation of the example problem with PyDyViz
16. [02:45] Exercise: Animate the exercist problem with PyDyViz
17. [02:55] Demonstrate example of 3D dimensional problem, automation with
    Kane’s method and Lagrange’s method

I will also have some sessions on implementing controllers for the dynamic
systems if the class is exceptionally fast.
