"""Allows conversion from Pandas DataFrame <-> Polars DataFrame."""

import pandas as pd
import polars as pl

class BackendConverter:
    """
    Initializing the Backend Converter.

    Parameters
    -----------
    df: pd.DataFrame or pl.DataFrame
        A pandas DataFrame or a polars DataFrame.

    columns: list, optional
        A list of columns you wish to convert, default is None.

    """

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

    def polars_to_pandas(self, array_type: str='auto', conversion_threshold: int=None)-> pd.DataFrame:
        """
        Converts a polars DataFrame to a pandas DataFrame

        Parameters
        -----------
        array_type: str
    
            Determines the array/backend type used in pandas operations, by default 'auto'.

            Options are:

            - 'numpy' -> usual NumPy backend (slower for very large datasets with object types)
            - 'pyarrow' -> PyArrow backend for better performance on large datasets
            - 'auto' -> automatically selects backend based on input and dataset size 

        conversion_threshold: int
            The number of rows at which the conversion from Polars to pandas switches to Arrow-backed pandas arrays for performance, default is 100000.
            Users can increase or decrease this threshold depending on their dataset size and memory availability.
        
        Returns
        -------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            Use this function to convert datasets quickly without having to do manual conversions and remembering parameters.
            Polars -> pandas conversion ensures efficient memory usage and stability, even on low-RAM systems.

        Considerations
        ---------------
            Adjust array_type and conversion_threshold for very large datasets to optimize performance and memory usage.
        """

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

    def pandas_to_polars(self, include_index:bool=False)-> pl.DataFrame:
        """
        Converts a pandas DataFrame to a polars DataFrame

        Parameters
        -----------
        include_index: bool, optional
            Whether you would like to include index during conversion from pandas to polars, by default False
        
        Returns
        -------
        pl.DataFrame
            A polars DataFrame
            
        Considerations
        ---------------
            Polars do not have the concept of index like pandas does, hence, you can adjust include_index depending on your requirement.
        """
        
        if not isinstance(include_index, bool):
            raise TypeError(f'include_index must be either True or False, got {type(include_index).__name__}')

        polars_df = pl.from_pandas(self.df, include_index = include_index)

        return polars_df

