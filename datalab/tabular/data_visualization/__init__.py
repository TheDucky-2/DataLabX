def set_visualization_backend():
    import matplotlib

    try:
        env_shell = get_ipython().__class__.__name__

        if env_shell == "ZMQInteractiveShell":
            matplotlib.use('module://matplotlib_inline.backend_inline')
        else:
            matplotlib.use('agg')
    except NameError:
        matplotlib.use('agg')

set_visualization_backend()

from .CategoricalVisualizer import CategoricalVisualizer
from .NumericalVisualizer import NumericalVisualizer
from .MissingnessVisualizer import MissingnessVisualizer


__all__ = ['CategoricalVisualizer', 'NumericalVisualizer', 'MissingnessVisualizer']