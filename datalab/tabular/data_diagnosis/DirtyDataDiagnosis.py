"""Diagnoses Dirty Data in a pandas DataFrame"""

from ..utils.Logger import datalab_logger
import pandas as pd
import polars as pl

logger = datalab_logger(name = __name__.split('.')[-1])

class DirtyDataDiagnosis:
    """
    Initialize the DirtyDataDiagnosis class.

    Parameters
    -----------
    df: pd.DataFrame
        A pandas dataframe you wish to diagnose.

    columns: list, optional
        A list of columns you wish to diagnose, by default None.

    array_type: str, optional
        The backend you wish to work with in pandas: 'numpy' or 'pyarrow', by default 'auto'.

    conversion_threshold: int, optional
        The number of rows upon which backend automatically switches to 'pyarrow' in pandas, by default 100000.
    """

    def __init__(self, df: pd.DataFrame, columns: list = None, array_type='auto', conversion_threshold: int= None):
     
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f'df must be a pandas DataFrame, got {type(df).__name__}')

        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be list of strings or type None, got {type(columns).__name__}')

        if not isinstance(array_type, str):
            raise TypeError(f'array type must be a string, got {type(array_type).__name__}')

        if not isinstance(conversion_threshold, (int, type(None))):
            raise TypeError(f'conversion threshold must be an integer or type None, got {type(conversion_threshold).__name__}')

        self.df = df
     
        if columns is None:
            self.columns = self.df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns]

        self.array_type= array_type
        self.conversion_threshold = conversion_threshold

        logger.info(f'Dirty Data Diagnosis initialized with {self.array_type} backend.')

    def diagnose_numbers(self, show_available_methods: bool=False)-> dict[str, dict[str, pd.DataFrame]]:
        """Detects patterns and common formatting issues in numbers in each column of the DataFrame.

        The following diagnostics are computed per column:

        - is_valid:                Values containing only valid integers or decimals (e.g: 1000, -10.048)
        - is_text:                 Values containing alphabetic characters and spaces ('unknown', 'error', 'missing', what)
        - is_dirty:                Values that are not strictly numeric (e.g: approx 1000, $100,00CD#44)
        - is_missing:              Values that are null or missing values (pandas missing types- NA or NaN)
        - is_scientific_notation:  Numbers expressed in scientific notation (e.g: 1.06E+1)
        - has_commas:              Numbers that contain commas (e.g: 10,000 or 1,000,000)
        - has_decimals:            Numbers that contain decimal points (e.g: -1.62, 1000.44)
        - has_units:               Numbers that are suffixed with alphabetical units (e.g: '10kg', '100cm')
        - has_symbols:             Numbers containing non-alphanumeric or special symbols (e.g: '?', '/' , '.')
        - has_currency:            Numbers containing currency symbols (prefix or suffix) (e.g. $10 or 10$)
        - has_spaces:              Numbers that contain leading or trailing spaces (e.g: '  missing', '1.066 ', '1.34    ')
        - has_multiple_decimals:     Numbers that contain double decimals (e.g: 1.34.567, 1.4444.0000)
        - has_multiple_commas:     Numbers that contain more than one commas (e.g: '9,628,62' or '1234,56')

        Parameters
        -----------
        show_available_methods : bool (default is False)
            Shows diagnostic options that are available in diagnose_numbers() method.

        Returns
        --------
        dict[str, dict[str, pd.DataFrame]]
            A nested dictionary of diagnostic results per column.

        Usage Recommendation
        ---------------------
            1. Use this function when you want to see what kind of issues exist in columns that contain numbers in your DataFrame

        Considerations
        ---------------
            1. This method adds a default **index** column by resetting the DataFrame's index.
            2. This is necessary to preserve original row IDs during conversion to Polars and back.
            3. The index column DOES NOT AFFECT your transformations and are automatically restored in all returned DataFrames
            4. This method also uses Polars regex under the hood for pattern matching
            5. This method is intended for diagnostic purposes, not data mutation.

        Example
        --------
        >>>     diagnostics = DirtyDataDiagnosis(df).diagnose_numbers()

        >>>     diagnostics['price']['has_currency'].head()
        """
        from ..utils.BackendConverter import BackendConverter
        
        # resetting index to ensure index is turned into a new column 'index' in pandas dataframe
        self.df = self.df.reset_index()   

        # passing dataframe including the new column 'index'
        polars_df = BackendConverter(self.df).pandas_to_polars()

        numeric_diagnosis = {}

        # patterns is a dictionary of available methods and regex patterns to detect them 
        PATTERNS = {
            'is_valid': r'^[+-]?\d+(\.\d+)?$',
            'is_dirty': r'^[+-]?\d+(\.\d+)?$',  # keeping the same as 'is_valid' since everything that is not valid will be dirty
            'is_text': r'^[A-Za-z ]+$',
            'is_symbol': r'^[^A-Za-z0-9]$',
            'is_missing': None,
            'is_scientific_notation': r'^[+-]?\d+(?:[.,]\d+)?[eE][+-]?\d*$',
            'has_units': r'^[+-]?\d+(?:[,.]\d+)?\s*[A-Za-z]+$',
            'has_symbols': r"[^\d\s\p{Sc}\p{L},.+-]\d+|\d+[^\d\s\p{Sc}\p{L},.+-]",
            'has_commas': r'^\d*,\d*$',
            'has_currency': r'^[\p{Sc}]\s*\d[\d,]*(\.\d+)?$|^\d[\d,]*(\.\d+)?\s*[\p{Sc}]$',
            'has_multiple_decimals': r'^[+-]?\d*(?:\.\d+){2,}$',
            'has_multiple_commas': r'^[+-]?\d*(?:,\d+){2,}$',
            'has_spaces': r'^\s+[+-]?\d+(?:\.\d+)?$|^[+-]?\d+(?:\.\d+)?\s+$|^\s+[+-]?\d+(?:\.\d+)?\s+$',
            'has_decimals': r'^[+-]?\d*\.\d+$',
            'has_text': r'(?i)(?:[A-Za-z]+.*\d+|\d+.*[A-Za-z])'
            }

        # excluding index column so that it is not involved in diagnosis 
        columns_to_diagnose = [column for column in polars_df.columns if column != 'index']

        for col in columns_to_diagnose:
            
            numeric_diagnosis[col] = {}
            series = polars_df[col]

            for method, pattern in PATTERNS.items():
                
                if method == 'is_missing':
                    pattern_mask = series.is_null()

                elif method == 'is_dirty':

                    pattern_mask = ~series.str.contains(PATTERNS['is_valid'])

                elif method == 'has_text':
                    # ensuring that only text that is not units or scientific notation is detected
                    pattern_mask = (series.str.contains(PATTERNS['has_text'])
                     & ~series.str.contains(PATTERNS['has_units'])
                     & ~series.str.contains(PATTERNS['is_scientific_notation']))

                else:
                    pattern_mask = series.str.contains(pattern)
                
                # filtering pattern masks out of the polars dataframe 
                result_df = BackendConverter(polars_df.filter(pattern_mask)).polars_to_pandas(array_type = self.array_type, conversion_threshold = self.conversion_threshold)

                # setting default index to be 'index'
                result_df.set_index('index', inplace=True)

                numeric_diagnosis[col][method] = result_df
                
        if show_available_methods:
            logger.info(f'Available diagnostic methods: {list(numeric_diagnosis[col].keys())}')

        return numeric_diagnosis

    def diagnose_text(self, show_available_methods=False)-> dict[str, dict[str, pd.DataFrame]]:
        """Detects patterns and common formatting issues in text in each column of the DataFrame.

        The following diagnostics are computed per column:
        
        - is_symbol:    Values containing only symbols.
        - is_valid:     Values containing alphabetic characters and spaces
        - is_dirty:     Values that are not strictly text
        - is_empty:     Values that are empty strings
        - has_symbols:  Values containing non-alphanumeric or special symbols
        - is_missing:      Values that are null or missing values.
        - has_numbers:  Values that contain numbers in text.
        - has_spaces:   Values that contain leading or trailing spaces 

        Parameters
        -----------
        show_available_methods : bool (default is False)
            Shows diagnostic options that are available in diagnose_numbers() method.

        Returns
        --------
        dict[str, dict[str, pd.DataFrame]]
            A nested dictionary of diagnostic results per column.

        Usage Recommendation
        ---------------------
            1. Use this function when you want to see what kind of issues exist in columns that contain text in your DataFrame

        Considerations
        ---------------
            1. This method adds a default **index** column by resetting the DataFrame's index.
            2. This is necessary to preserve original row IDs during conversion to Polars and back.
            3. The index column DOES NOT AFFECT your transformations and are automatically restored in all returned DataFrames
            4. This method also uses Polars regex under the hood for pattern matching
            5. This method is intended for diagnostic purposes, not data mutation.

        Example
        --------
        >>>     diagnostics = DirtyDataDiagnosis(df).diagnose_text()

        >>>     diagnostics['user_id']['is_dirty'].head()
        """
        from ..utils.BackendConverter import BackendConverter

        self.df = self.df.reset_index()
        
        polars_df = BackendConverter(self.df).pandas_to_polars()

        columns_to_diagnose = [column for column in polars_df.columns if column!= 'index']

        text_diagnosis = {}

        PATTERNS = {
                'is_dirty': r'^[^A-Za-z ]+$',
                'is_symbol': r'^[^\p{L}]+$',
                'is_empty': r'^$',
                'has_symbols': r'\p{L}.*[^\p{L}]|[^\p{L}].*\p{L}',
                'is_valid': r'^[A-Za-z ]+$',
                'is_missing': None,
                'has_spaces': r'^\s|\s$',
                'has_numbers': r'\p{N}'
            }

        for col in columns_to_diagnose:

            text_diagnosis[col] = {}

            series = polars_df[col]

            for method, pattern in PATTERNS.items():
                
                if method == 'is_null': 
                    pattern_mask = series.is_null()

                elif method == 'is_dirty':
                    pattern_mask = series.str.contains(PATTERNS['is_dirty'])

                else:
                    pattern_mask = series.str.contains(pattern)

                # ensuring by default, pyarrow is used for datasets over 100000 rows
                
                result_df = BackendConverter(polars_df.filter(pattern_mask)).polars_to_pandas(array_type = self.array_type, conversion_threshold = self.conversion_threshold)

                result_df.set_index('index', inplace=True)

                text_diagnosis[col][method] = result_df

        if show_available_methods:
            logger.info(f'Available diagnostic methods: {list(text_diagnosis[col].keys())}')

        return text_diagnosis

    def diagnose_datetime(self, show_available_methods=False)-> dict[str, dict[str, pd.DataFrame]]:
        """Detects patterns and formatting issues in date-time in one or multiple columns of the DataFrame.

        The following diagnostics are computed per column:
        
            'is_valid_date': Datetime values that are correct dates. (like 01-01-2024 or 2024-01-01) 
            'is_valid_time': Datetime values that are correct time. (like 13:21:07 or 00:00)
            'is_valid_datetime': Datetime values that are both correct date and time (like 2025-09-29 23:54:02)
            'is_text': Datetime values that contain just text (like 'yesterday' or 'tomorrow')
            'is_number': Datetime values that are just plain numbers (like 01012024)
            'is_missing': Pandas built-in missing values
            'is_dirty': Values that are not correct date/time or dae
        }

        Parameters
        -----------
        show_available_methods : bool (default is False)
            Shows diagnostic options that are available in diagnose_numbers() method.
            
        Returns
        --------
        dict[str, dict[str, pd.DataFrame]]
            A nested dictionary of diagnostic results per column.

        Usage Recommendation
        --------------------
            1. Use this function when you want to see what kind of issues exist in columns that contain datetime data in your DataFrame

        Considerations
        ---------------
            1. This method adds a default **index** column by resetting the DataFrame's index.
            2. This is necessary to preserve original row IDs during conversion to Polars and back.
            3. The index column DOES NOT AFFECT your transformations and are automatically restored in all returned DataFrames
            4. This method also uses Polars regex under the hood for pattern matching
            5. This method is intended for diagnostic purposes, not data mutation.

        Example
        --------
        >>>     diagnostics = DirtyDataDiagnosis(df).diagnose_datetime()

        >>>     diagnostics['signup_date']['is_dirty'].head()
        """
        from ..utils.BackendConverter import BackendConverter
        
        self.df = self.df.reset_index()

        pol_df = BackendConverter(self.df).pandas_to_polars()
        datetime_diagnosis = {}

        PATTERNS = {
            'is_valid_date': r'^(?:\d{2,4}[\/-]\d{1,2}[\/-]\d{1,2}|\d{1,2}[\/-]\d{1,2}[\/-]\d{2,4})$',
            'is_valid_time': r'^\d{1,2}:\d{2}(?::\d{2})?$',
            'is_valid_datetime':r'^(?:\d{2,4}[\/-]\d{1,2}[\/-]\d{1,2}[ T]\d{1,2}:\d{2}(?::\d{2})?|\d{1,2}[\/-]\d{1,2}[\/-]\d{2,4}[ T]\d{1,2}:\d{2}(?::\d{2})?)$',
            'is_text': r'^[a-zA-Z ]+$',
            'is_number':  r'^\d{6}$|^\d{8}$|^\d{12}$|^\d{14}$',
            'is_missing':None,
            'is_dirty': None
            }

        cols_to_diagnose = [column for column in pol_df.columns if column!='index']

        for col in cols_to_diagnose:
            datetime_diagnosis[col] = {}

            for method, pattern in PATTERNS.items():

                series = pol_df[col]

                if method == 'is_missing':
                    pattern_mask = series.is_null()
                if method == 'is_dirty':
                    pattern_mask = (
                        ~series.str.contains(PATTERNS['is_valid_date'])
                        & ~series.str.contains(PATTERNS['is_valid_time'])
                        & ~series.str.contains(PATTERNS['is_valid_datetime'])
                    )
                else:
                    pattern_mask = series.str.contains(pattern)
                    
                # ensuring by default, pyarrow is used for datasets over 100000 rows
                result_df =BackendConverter(pol_df.filter(pattern_mask)).polars_to_pandas(array_type = self.array_type, conversion_threshold = self.conversion_threshold)

                result_df.set_index('index', inplace=True)

                datetime_diagnosis[col][method] = result_df

        if show_available_methods:
            logger.info(f'Available diagnostic methods: {list(datetime_diagnosis[col].keys())}')
        
        return datetime_diagnosis
