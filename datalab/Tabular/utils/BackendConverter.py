import pandas as pd
import polars as pl


class BackendConverter:

    def __init__(self, df:pd.DataFrame|pl.DataFrame, columns:list=None):
        
        if not isinstance(df, (pd.DataFrame, pl.DataFrame)):
            raise TypeError(f'Backend Converter expects a pandas DataFrame or a polars DataFrame, got {type(df).__name__}')

        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be a list or type None, got {type(df).__name__}')

        if isinstance(df, pd.DataFrame):
            self.df = df.copy()

            if columns is None:
                self.columns = df.columns.to_list()

            else:
                self.columns = [column for column in columns if column in df.columns]

        elif isinstance (df, pl.DataFrame):
            
            self.df = df.clone()

            if columns is None:
                self.columns = df.columns

            else:
                self.columns = [column for column in columns if column in df.columns]

    def polars_to_pandas(self:pd.DataFrame, array_type='numpy')-> pd.DataFrame:

        if not isinstance(array_type, str):
            raise TypeError(f'array type must be a string, got {type(array_type).__name__}')

        if array_type == 'numpy':
            
            pandas_df = self.df.to_pandas()
            return pandas_df

        elif array_type == 'pyarrow':

            pandas_df = self.df.to_pandas(use_pyarrow_extension_array=True)

            return pandas_df 

    def pandas_to_polars(self, include_index=False)-> pl.DataFrame:
        
        if not isinstance(include_index, bool):
            raise TypeError(f'include_index must be either True or False, got {type(include_index).__name__}')

        polars_df = pl.from_pandas(self.df, include_index=include_index)

        return polars_df

