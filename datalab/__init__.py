"""
<img src="assets/logo.png" alt="DataLab" style="height: 24px;">

"DataLab v0.1.0b4 - Beta Pre-release: Structured dirty data diagnosis, Polars + Backend optimization, and Enhanced data visualization."
"""
__version__ = '0.1.0b4'

import importlib

_subpackages = ['tabular']

__all__ = []

for package in _subpackages:
    module = importlib.import_module(f'{__name__}.{package}')
    
    for name in getattr(module, '__all__', []):
        alias = f'{package}_{name}' if name in globals() else name
        globals()[alias] = getattr(module, name)
        __all__.append(alias)
