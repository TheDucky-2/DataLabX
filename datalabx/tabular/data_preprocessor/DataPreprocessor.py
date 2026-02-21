"""Base Preprocessor class"""
import pandas as pd

class DataPreprocessor:

    def __init__(self, df: pd.DataFrame, columns: list = None):
        import pandas as pd
        import numpy as np
        
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f'df must be a pandas DataFrame, got {type(df).__name__}')

        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be a list of column name/s or type None, got {type(columns).__name__}')

        self.df = df.copy()

        if columns is None:
            self.columns = self.df.columns
        else:
            self.columns = [column for column in columns if column in self.df.columns]

    def validate_columns(self):

        missing_columns = [column for column in self.columns if column not in self.df.columns]

        if missing_columns:
            raise ValueError(f'The following columns are not in the dataframe: {missing_columns}')



