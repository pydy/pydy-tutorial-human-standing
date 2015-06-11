def controller(x, t):
    """Returns the output of the controller, i.e. the joint torques, given
    the current state."""
    return -dot(K, x)
