#!/usr/bin/env python

from distutils.version import LooseVersion

for module in ['IPython', 'sympy', 'pydy', 'numpy', 'scipy', 'matplotlib']:
    try:
        __import__(module)
    except ImportError:
        print('Error: {} not installed'.format(module))

try:
    import sympy
except ImportError:
    pass
else:
    if LooseVersion(sympy.__version__) < LooseVersion('0.7.6'):
        msg = ("Error: SymPy >= 0.7.6 is required for correct notebook "
               "printing, please upgrade.")
        print(msg)

try:
    import IPython
except ImportError:
    pass
else:
    if LooseVersion(IPython.__version__) < LooseVersion('3.0.0'):
        msg = ("Error: IPython >= 3.0.0 is required for the 3D visualizations.")
        print(msg)

    if LooseVersion(IPython.__version__) >= LooseVersion('4.0.0'):
        try:
            __import__('ipywidgets')
        except ImportError:
            print('Error: ipywidgets is required for IPython >= 4.0')

try:
    import pydy
except ImportError:
    pass
else:
    if LooseVersion(pydy.__version__) < LooseVersion('0.3.0'):
        print("Error: PyDy >= 0.3.0 is required, please upgrade.")
