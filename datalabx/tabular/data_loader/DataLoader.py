"""Loads pandas DataFrame from a tabular dataset"""

import pandas as pd
from pathlib import Path
import polars as pl

from datalabx.tabular.utils.Logger import datalabx_logger

logger = datalabx_logger(name = __name__.split('.')[-1])


# Inheriting from Exception class

class _FileTypeMismatchError(Exception):

    """Internal exception raised during file type mismatches."""

    def __init__(self, expected_type: str, received_type:str, file_path:str):

        if not isinstance(expected_type, str):
            raise TypeError(f'expected_type must be a string, got {type(expected_type).__name__}')     
            
        if not isinstance(received_type, str):
                raise TypeError(f'received_type must be a string, got {type(received_type).__name__}')
        
        if not isinstance(file_path, str):
            raise TypeError(f'file_path must be a string, got {type(file_path).__name__} ')

        self.expected_type = expected_type
        self.received_type = received_type
        self.file_path = file_path

        super().__init__(
        f"File type mismatch: expected: {self.expected_type}, received: {self.received_type} from file: {self.file_path}"
        )

### ------- DATA LOADER ---------

class DataLoader:
    """
    Parameters
    ------------

    file_path: str
        Path of your data file or just file name
  
    file_type: str, optional
        Type of file user passed in the Data Loader (Automatically detected)

        Supported File Types:
        
        - 'csv' 
        - 'excel'
        - 'parquet'
        - 'JSON'
    """
    def __init__(
        self,
        file_path:str,
        file_type: str|None = None):

        if not isinstance(file_path, (str, Path)):
            raise TypeError(f'file path must be a string or a file path, got {type(file_path).__name__}')

        if not isinstance(file_type, (str, type(None))):
            raise TypeError(f'file type must be a string, got {type(file_type).__name__}')

        self.file_path = file_path   

        # ---- DETECTING FILE TYPES------

        if file_type is None:

            self.file_type = file_path.split('.')[-1].lower()
        else:
            self.file_type = file_type.lower()

        if self.file_type.lower() != self.file_path.split('.')[-1]:
            raise _FileTypeMismatchError(

                expected_type= self.file_path.split('.')[-1].lower(),
                received_type= self.file_type.lower(),
                file_path = self.file_path
                )

        logger.info(f'Data Loader initialized with {self.file_type} file.')

    def load_tabular(
            self,
            load_csv_as_string:bool = False,
            array_type: str = 'auto',
            conversion_threshold: int|None = None,
            **kwargs:dict) -> pd.DataFrame:
        """
        Use this function for loading your tabular data as a pandas DataFrame.

        Parameters
        ------------

        load_csv_as_string: bool, optional 
        
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

            Extra arguments you want to pass into polars file readers.

        Returns
        ---------
        pd.DataFrame

            A pandas DataFrame
        
        Usage Recommendation
        ---------------------

            - Use this function to load datasets quickly without memorizing multiple read functions.
            - Polars -> pandas conversion ensures efficient memory usage and stability, even on low-RAM systems.

        Considerations
        ---------------

            - Adjust array_type and conversion_threshold for very large datasets to optimize performance and memory usage.

        Example
        --------
        >>> # Load a CSV file (default parameters)
            df1 = DataLoader('example.csv').load_tabular()

        >>> # Load a CSV file with string datatype
            df2 = DataLoader('example.csv').load_tabular(load_csv_as_string=True)

        >>> # Load an Excel file
            df3 = DataLoader('example.xlsx').load_tabular()             

        >>> # Load a Parquet file using PyArrow backend
            df4 = DataLoader('example.parquet').load_tabular(array_type='pyarrow')

        >>> # Load a large CSV file with custom conversion threshold
            df5 = DataLoader('large_dataset.csv').load_tabular(conversion_threshold=2000000)

        >>> # Load a JSON file from a subdirectory with auto array backend
            df6 = DataLoader('some/path/to/data.json').load_tabular()
        """    
        if not isinstance(array_type, str):
            raise TypeError(f'array type must be a string, got {type(array_type).__name__}')
        
        if not isinstance(conversion_threshold,(int, type(None))):
            raise TypeError(f'conversion threshold must be an integer, got {type(conversion_threshold).__name__} =')

        if not isinstance(load_csv_as_string, bool):
            raise TypeError(f'load_as_string must be a boolean, got {type(load_csv_as_string).__name__}')

        # If conversion threshold is None, it defaults to 100k rows for converting to pyarrow datatype

        if conversion_threshold is None:
            conversion_threshold = 100_000 

        # ----- LOADING POLARS DATAFRAMES DEPENDING ON FILE TYPE ------

        if self.file_type == 'csv':

            if load_csv_as_string:
                logger.info('Loading csv with string datatype.')
                polars_df = pl.read_csv(self.file_path, infer_schema_length=0, **kwargs)

            else:
                try:
                    # load the file with schema inference
                    polars_df = pl.read_csv(self.file_path, **kwargs)

                    # if polars throw Compute Error
                except pl.exceptions.ComputeError as error:
                    
                    if 'CSV parsing' in str(error):

                        logger.info("Schema inference issue. Loading CSV without schema inference.")
                        polars_df = pl.read_csv(self.file_path, infer_schema_length=None, **kwargs)

                    else:
                        raise

        elif self.file_type == 'parquet':
            polars_df = pl.read_parquet(self.file_path, **kwargs)

        elif self.file_type == 'json':
            polars_df = pl.read_json(self.file_path, **kwargs)

        elif self.file_type in ['xlsx', 'xls']:
            # trying to import fastexcel for reading excel files
            try:
                import fastexcel

            except:
                raise ImportError(
                    "Excel file support requires 'fastexcel'. " 
                    "You can install 'fastexcel' with: pip install datalabx_pre_release[excel]"
                    )

            polars_df = pl.read_excel(self.file_path, **kwargs)

        else:
            raise ValueError(f'Unsupported file type: {self.file_type}')

        df_size = polars_df.height 

        # ------ RETURNING ARRAY TYPE DEPENDING ON USER'S CHOICE
        if array_type == 'auto':
            if df_size >= conversion_threshold:
                return polars_df.to_pandas(use_pyarrow_extension_array=True)
            else:
                return polars_df.to_pandas()

        elif array_type == 'numpy':
            return polars_df.to_pandas()

        elif array_type == 'pyarrow':
            return polars_df.to_pandas(use_pyarrow_extension_array=True)

        else:
            raise ValueError(f'Unsupported array type: {array_type}')

