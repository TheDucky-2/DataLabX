"""
<img src="assets/datalabx_logo.png" alt="datalabx logo" height: "80" style="display:block; margin: 20px auto;">

"DataLabX v0.1.0b12 - Improved Missingness Detection, Stability Fixes & Extended Data Loading."

"""
__version__ = '0.1.0b12'

import importlib

_subpackages = ['tabular']

__all__ = []

for package in _subpackages:
    module = importlib.import_module(f'{__name__}.{package}')
    
    for name in getattr(module, '__all__', []):
        alias = f'{package}_{name}' if name in globals() else name
        globals()[alias] = getattr(module, name)
        __all__.append(alias)
