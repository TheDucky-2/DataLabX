"""Includes internal decorators used within DataLabX modules"""

from functools import wraps
import time
from .Logger import datalabx_logger

logger = datalabx_logger(name = "DataLabX")

def handle_index(func):
    """Decorator for handling setting and resetting of index column"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):

        input_df = self.df.reset_index()
        result = func(self, *args, **kwargs)

        for col in result:
            for key in result[col]:
                self.df = result[col][key]
                if 'index' in self.df.columns:
                    self.df.set_index("index", inplace=True)

        return result
    return wrapper

def measure(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start = time.perf_counter()
        result = func(self,*args, **kwargs)
        end = time.perf_counter()
        logger.info(f"Time taken: {(end-start)*1000:.3f} ms")
        return result

    return wrapper

