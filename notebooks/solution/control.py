#!/usr/bin/env python

# Controller Design

from numpy import zeros, matrix, eye, dot, asarray
from numpy.linalg import inv
from scipy.linalg import solve_continuous_are

from .utils import controllable
from .visualization import *

equilibrium_point = zeros(len(coordinates + speeds))
equilibrium_dict = dict(zip(coordinates + speeds, equilibrium_point))
parameter_dict = dict(zip(constants, numerical_constants))

linear_state_matrix, linear_input_matrix, inputs = \
    kane.linearize(new_method=True, A_and_B=True)
f_A_lin = linear_state_matrix.subs(parameter_dict).subs(equilibrium_dict)
f_B_lin = linear_input_matrix.subs(parameter_dict).subs(equilibrium_dict)
m_mat = mass_matrix.subs(parameter_dict).subs(equilibrium_dict)

A = matrix(m_mat.inv() * f_A_lin).astype(float)
B = matrix(m_mat.inv() * f_B_lin).astype(float)

assert controllable(A, B)

Q = matrix(eye(6))

R = matrix(eye(3))

S = solve_continuous_are(A, B, Q, R)

K = inv(R) * B.T * S

# This is an annoying little issue. We specified the order of things when
# creating the rhs function, but the linearize function returns the F_B
# matrix in the order corresponding to whatever order it finds the joint
# torques. This would also screw things up if we specified a different
# ordering of the coordinates and speeds as the standard kane._q + kane._u

K = K[[0, 2, 1], :]


def controller(x, t):
    return -asarray(dot(K, x)).flatten()

y = odeint(right_hand_side, x0, t, args=(controller, numerical_constants))
