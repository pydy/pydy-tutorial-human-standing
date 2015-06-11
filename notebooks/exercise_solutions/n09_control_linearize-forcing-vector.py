F_B = forcing_vector.jacobian(specified)
F_B = F_B.subs(equilibrium_dict).subs(parameter_dict)
F_B = matrix2numpy(F_B, dtype=float)
F_B
