"""
<img src="assets/DataLab_logo.png" alt="DataLab logo" height: "80" style="display:block; margin: 20px auto;">

"DataLab v0.1.0b7

Beta release with critical bug fixes for non-Jupyter environments, improved documentation, contributions workflow, and enhanced stability for data diagnosis and visualization workflows."

"""
__version__ = '0.1.0b7'

import importlib

_subpackages = ['tabular']

__all__ = []

for package in _subpackages:
    module = importlib.import_module(f'{__name__}.{package}')
    
    for name in getattr(module, '__all__', []):
        alias = f'{package}_{name}' if name in globals() else name
        globals()[alias] = getattr(module, name)
        __all__.append(alias)
