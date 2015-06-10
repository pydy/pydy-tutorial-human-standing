#!/usr/bin/env python

from distutils.version import LooseVersion

for module in ['IPython', 'sympy', 'pydy', 'numpy', 'scipy', 'matplotlib']:
    try:
        __import__(module)
    except ImportError:
        print('Error: {} not installed'.format(module))

import IPython
import sympy
import pydy

if LooseVersion(sympy.__version__) < LooseVersion('0.7.6'):
    msg = ("Error: SymPy >= 0.7.6 is required for correct notebook "
           + "printing, please upgrade.")
    print(msg)

if LooseVersion(IPython.__version__) < LooseVersion('3.0.0'):
    msg = ("Error: IPython >= 3.0.0 is required for the 3D visualizations.")
    print(msg)

if LooseVersion(pydy.__version__) < LooseVersion('0.3.0'):
    print("Error: PyDy >= 0.3.0 is required, please upgrade.")
