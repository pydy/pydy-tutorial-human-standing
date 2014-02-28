F_B = forcing_vector.jacobian(specified)
F_B = F_B.subs(equilibrium_dict).subs(parameter_dict)
F_B = array(F_B.tolist(), dtype=float)
F_B