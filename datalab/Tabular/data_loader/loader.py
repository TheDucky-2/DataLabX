import pandas as pd
from pathlib import Path

def load_tabular(file_path: str, file_type: str = None, **kwargs) -> pd.DataFrame:

    '''
    ----- Welcome to the first step of this workflow -------------

    Use this function for loading your tabular data as a pandas DataFrame.
    
    Parameters:
    
    file_path: str
        Path of your data file
        ------------------------------
    file_type: str, default is 'csv'
        Supported File Types: 'csv', 'excel, 'parquet', 'JSON'
        ------------------------------
    kwargs: dict
        Extra arguments you want to pass into pandas file readers.
        ------------------------------

    Returns:
        pd.DataFrame (a pandas DataFrame)
    
    Usage Recommendation:
        Use this function for loading your dataset without having to memorize multiple functions for reading different data files.

    Note: 
        If you get an error while reading parquet file, use **kwargs: engine = 'fastparquet' 
        E.g: load_tabular_data('your_file_name.parquet', engine='fastparquet')

    Example Usage:
    >>>   load_tabular_data('example.csv')   
    >>>   load_tabular_data('example.xlsx')
    >>>   load_tabular_data('some/path/to/my/csv/file.csv')
    >>>   load_tabular_data('example.json')
    
    '''
    if not isinstance(file_path, (str, Path)):
        raise TypeError('file path must be a string or a file path')

    if file_type is None:
        file_type = file_path.split('.')[-1].lower()
    else:
        file_type = file_type.lower()
        print(file_type)

    if file_type == 'csv':
        df = pd.read_csv(file_path, **kwargs)
    
    elif file_type in ['xlsx', 'xls']:
        df = pd.read_excel(file_path, **kwargs)
    
    elif file_type == 'parquet':
        df = pd.read_parquet(file_path, **kwargs)
    
    elif file_type == 'json':
        df = pd.read_json(file_path, **kwargs)

    else:
        raise ValueError(f'Unsupported file type: {file_type}')
    
    return df