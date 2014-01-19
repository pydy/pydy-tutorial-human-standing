#!/usr/bin/env python

import numpy as np


def controllable(a, b):
    """Returns true if the system is controllable and false if not.

    Parameters
    ----------
    a : numpy.Matrix, shape(n,n)
        The state matrix.
    b : numpy.Matrix, shape(n,r)
        The input matrix.

    Returns
    -------
    controllable : boolean

    """
    n = a.shape[0]
    controllability_matrix = []
    for i in range(n):
        controllability_matrix.append(a ** i * b)
    controllability_matrix = np.hstack(controllability_matrix)

    return np.linalg.matrix_rank(controllability_matrix) == n
