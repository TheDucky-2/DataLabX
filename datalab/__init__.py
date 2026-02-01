"""
<img src="assets/DataLab_logo.png" alt="DataLab logo" height: "80" style="display:block; margin: 20px auto;">

"DataLab v0.1.0b6 - Beta Pre-release

A stabilization release focused on API reliability, type safety, improved tests, and clearer documentation."
"""
__version__ = '0.1.0b6'

import importlib

_subpackages = ['tabular']

__all__ = []

for package in _subpackages:
    module = importlib.import_module(f'{__name__}.{package}')
    
    for name in getattr(module, '__all__', []):
        alias = f'{package}_{name}' if name in globals() else name
        globals()[alias] = getattr(module, name)
        __all__.append(alias)
