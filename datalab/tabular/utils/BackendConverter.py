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
                self.columns = self.df.columns.to_list()

            else:
                self.columns = [column for column in columns if column in self.df.columns]

        elif isinstance (df, pl.DataFrame):
            
            self.df = df.clone()

            if columns is None:
                self.columns = self.df.columns

            else:
                self.columns = [column for column in columns if column in self.df.columns]

    def polars_to_pandas(self, array_type='auto', conversion_threshold: int=None)-> pd.DataFrame:

        if not isinstance(self.df, pl.DataFrame):
            raise TypeError(f'Expected a polars DataFrame, got {type(self.df).__name__}')

        if not isinstance(array_type, str):
            raise TypeError(f'array type must be a string, got {type(array_type).__name__}')
        
        if not isinstance(conversion_threshold, (int, type(None))):
            raise TypeError(f'conversion threshold must be an integer or type None, got {type(conversion_threshold).__name__}')

        if conversion_threshold is None:
            conversion_threshold = 100_000

        df_size = self.df.height

        if array_type == 'auto':
            # if rows more than or equal to conversion threshold
            if df_size >= conversion_threshold:
                return self.df.to_pandas(use_pyarrow_extension_array=True)
            else:
                return self.df.to_pandas()

        if array_type == 'numpy':
            
            pandas_df = self.df.to_pandas()
            return pandas_df

        elif array_type == 'pyarrow':

            pandas_df = self.df.to_pandas(use_pyarrow_extension_array=True)

            return pandas_df 

    def pandas_to_polars(self: pd.DataFrame, include_index=False)-> pl.DataFrame:
        
        if not isinstance(include_index, bool):
            raise TypeError(f'include_index must be either True or False, got {type(include_index).__name__}')

        polars_df = pl.from_pandas(self.df, include_index=include_index)

        return polars_df

