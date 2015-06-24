#!/usr/bin/env python

# Controller Design

from numpy import matrix, dot, asarray
from numpy.linalg import inv
from scipy.linalg import solve_continuous_are
from sympy import Matrix

parameter_dict = dict(zip(constants, numerical_constants))

linearizer = kane.to_linearizer()
linearizer.r = Matrix(specified)
A, B = linearizer.linearize(op_point=[equilibrium_dict, parameter_dict],
                            A_and_B=True)

A = matrix(A).astype(float)
B = matrix(B).astype(float)

S = solve_continuous_are(A, B, Q, R)

K = inv(R) * B.T * S

def controller(x, t):
    return -dot(K, x)

y = odeint(right_hand_side, x0, t, args=(controller, numerical_constants))
