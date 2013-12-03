Outline
=======

We will work through two parallel but similar problems in the tutorial. The
first will be a demonstration problem in which the full solutions will be shown
and each step will be explained, the second will be a similar problem that the
attendees will work in pairs to come up with the solution. I’ll introduce each
stage of the problem derivation and development in short ~5-10 minute sections
and then have the attendees complete the derivation of their problem using the
software tools that have been presented.

1. [00:00] Introduction

   - A wee bit about the presenter
   - Attendees introduce themselves to their neighbor and pair up

2. [00:05] Brief introduction to multibody systems and controls

   - Newton’s Laws, reference frames, velocity, acceleration, forces/torques
   - Ordinary differential equations and their solutions
   - Briefly mention control, but detail it later in talk.
   - Applications: robots, vehicles, etc

3. [00:10] Brief intro to the software stack (SymPy, SciPy, python-control)

   - SymPy and the Mechanics package
   - SciPy for ODE integration (scipy.ode)
   - matplotlib for 2D plotting and basic animation
   - IPython Notebook for interactive work
   - python-control for control design
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
11. [01:40] 2D plotting of the state trajectories with matplotlib
12. [01:45] Excercise: Plot the simulation results of the exercise problem
13. [01:55] Demonstrate 2D animation the free motion of the example model with
    matplotlib
14. [02:10] Exercise: Animate the 2D exercise problem
15. [02:25] Explain linearization about an equilibrium point and demo with the
    example problem
16. [02:35] Exercise: Linearize the exercise problem
17. [02:45] Brief introduction to control theory and python-control
18. [02:55] Build a controller for the sample problem with python control
19. [03:05] Exercise: make controller for the exercise problem
20. [03:20] Add tracking control to the problem
21. [03:30] Exercise: add tracking control to student’s problem
22. [03:45] Demonstrate example of 3D dimensional problem, automation with
    Kane’s method and Lagrange’s method
