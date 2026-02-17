"""Loads pandas DataFrame from a tabular dataset"""

import pandas as pd
from pathlib import Path
import polars as pl

def load_tabular(file_path: str, 
                 file_type: str|None = None,
                 array_type: str ='auto',
                 conversion_threshold:int|None = None,
                 load_as_string = False,
                 **kwargs:dict) -> pd.DataFrame:

    """
    Use this function for loading your tabular data as a pandas DataFrame.

    Parameters
    ------------

    file_path: str
        Path of your data file or just file name
  
    file_type: str, optional

        Supported File Types:
        
        - 'csv' (default)
        - 'excel'
        - 'parquet'
        - 'JSON'

    load_as_strings: bool, optional 
    
        Whether you would like to load your data as strings, instead of original datatypes, default is False

    array_type: str, optional

        Determines the array/backend type used in pandas operations, by default 'auto'.

        Options are:

        - 'numpy' -> usual NumPy backend (slower for very large datasets with object types)
        - 'pyarrow' -> PyArrow backend for better performance on large datasets
        - 'auto' -> automatically selects backend based on input and dataset size 
            
    conversion_threshold: int, optional

        The number of rows at which the conversion from Polars to pandas switches to Arrow-backed pandas arrays for performance, default is 100000.
        Users can increase or decrease this threshold depending on their dataset size and memory availability.
       
    kwargs: dict, optional

        Extra arguments you want to pass into pandas file readers (for excel files only).
     
    Returns
    ---------
    pd.DataFrame

        A pandas DataFrame
    
    Usage Recommendation
    ---------------------

        Use this function to load datasets quickly without memorizing multiple read functions.
        Polars -> pandas conversion ensures efficient memory usage and stability, even on low-RAM systems.

    Considerations
    ---------------

        Adjust array_type and conversion_threshold for very large datasets to optimize performance and memory usage.

    Example
    --------
    
    >>> # Load a CSV file (default parameters)
        df1 = load_tabular('example.csv')

    >>> # Load an Excel file
        df2 = load_tabular('example.xlsx', file_type='excel')             

    >>> # Load a Parquet file using PyArrow backend
        df3 = load_tabular('example.parquet', array_type='pyarrow')

    >>> # Load a large CSV file with custom conversion threshold
        df4 = load_tabular('large_dataset.csv', conversion_threshold=2000000)

    >>> # Load a JSON file from a subdirectory with auto array backend
        df5 = load_tabular('some/path/to/data.json')
    """

    if not isinstance(file_path, (str, Path)):
        raise TypeError(f'file path must be a string or a file path, got {type(file_path).__name__}')

    if not isinstance(file_type, (str, type(None))):
        raise TypeError(f'file type must be a string, got {type(file_type).__name__}')     
        
    if not isinstance(array_type, str):
            raise TypeError(f'array type must be a string, got {type(array_type).__name__}')
    
    if not isinstance(conversion_threshold,(int, type(None))):
        raise TypeError(f'conversion threshold must be an integer, got {type(conversion_threshold).__name__} ')

    if file_type is None:
        file_type = file_path.split('.')[-1].lower()
    else:
        file_type = file_type.lower()

    if conversion_threshold is None:
        conversion_threshold = 100_000 

    if file_type == 'csv':
        if load_as_string:
            polars_df = pl.read_csv(file_path, infer_schema_length=0)
        else:
            polars_df = pl.read_csv(file_path)

    elif file_type == 'parquet':
        polars_df = pl.read_parquet(file_path)
    elif file_type == 'json':
        polars_df = pl.read_json(file_path)
    elif file_type in ['xlsx', 'xls']:
        return pd.read_excel(file_path, **kwargs)
    else:
        raise ValueError(f'Unsupported file type: {file_type}')

    df_size = polars_df.height

    if array_type == 'auto':
        if df_size > conversion_threshold:
            return polars_df.to_pandas(use_pyarrow_extension_array=True)
        else:
            return polars_df.to_pandas()

    elif array_type == 'numpy':
        return polars_df.to_pandas()

    elif array_type == 'pyarrow':
        return polars_df.to_pandas(use_pyarrow_extension_array=True)

    else:
        raise ValueError(f'Unsupported array type: {array_type}')
