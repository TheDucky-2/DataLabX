"""Base class for Computation"""

import pandas as pd

class Computation:
    """
    Initializing Computation.

    Parameters
    -----------
    df: pd.DataFrame
        A pandas dataframe you wish to diagnose

    columns: list, optional
        A list of columns you wish to apply computations on, default is None.
    """
    def __init__(self, df:pd.DataFrame, columns:list=None):

        if not isinstance(df, pd.DataFrame):
            raise TypeError(f'df must be a pandas DataFrame, got {type(df).__name__}')

        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be a list of strings or type None, got {type(columns).__name__}')

        # creating a copy of the original dataframe
        self.df = df.copy()  

        # if user passes a list of columns
        if columns is None: 
            # columns would default to all of the columns of the dataframe
            self.columns = df.columns.tolist()
        else:
            # columns would be the list of columns passed
            self.columns = [column for column in columns if column in self.df.columns]

        # Just making sure that the datatypes of the columns passed are numeric.
        if not all(pd.api.types.is_numeric_dtype(self.df[col]) for col in self.columns):
            raise ValueError('All columns passed for computation must be numeric')

    def validate_columns(self):
        """
        This function just makes sure that the columns passed by the user
        actually exist in the dataframe.
        """ 
        # if the column passed by the user is not in dataframe
        missing_columns = [column for column in self.columns if column not in self.df.columns] 

        if missing_columns:
            raise TypeError(f'Columns not found in dataframe: {missing_columns}')


