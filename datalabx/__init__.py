"""
<img src="assets/datalabx_logo.png" alt="datalabx logo" height: "80" style="display:block; margin: 20px auto;">

"datalabx v0.1.0b9 : Flexible Data Loading & Refined Missing Data Handling"

"""
__version__ = '0.1.0b9'

import importlib

_subpackages = ['tabular']

__all__ = []

for package in _subpackages:
    module = importlib.import_module(f'{__name__}.{package}')
    
    for name in getattr(module, '__all__', []):
        alias = f'{package}_{name}' if name in globals() else name
        globals()[alias] = getattr(module, name)
        __all__.append(alias)
