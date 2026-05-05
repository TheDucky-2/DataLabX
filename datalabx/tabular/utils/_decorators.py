"""Includes internal decorators used within DataLabX modules"""

from functools import wraps


## decorator for handlingsetting and resetting of index column
def handle_index(func):
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