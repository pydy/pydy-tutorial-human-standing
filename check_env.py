#!/usr/bin/env python

from distutils.version import LooseVersion

for module in ['IPython', 'sympy', 'pydy', 'numpy', 'scipy', 'matplotlib']:
    try:
        __import__(module)
    except ImportError:
        print('Error: {} not installed'.format(module))

import sympy
import pydy

if LooseVersion(sympy.__version__) < LooseVersion('0.7.5'):
    msg = ("Error: SymPy >= 0.7.5 is required for correct notebook "
           + "printing, please upgrade.")
    print(msg)

if LooseVersion(pydy.__version__) < LooseVersion('0.2.0'):
    print("Error: PyDy > 0.2.0 is required, please upgrade.")
