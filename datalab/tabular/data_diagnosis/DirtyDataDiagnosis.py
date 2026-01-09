from ..utils.Logger import datalab_logger
import pandas as pd
import polars as pl

logger = datalab_logger(name = __name__.split('.')[-1])

class DirtyDataDiagnosis:

    def __init__(self, df: pd.DataFrame, columns: list = None):
        '''
        Initializing the Dirty Data Diagnosis
        '''
        self.df = df
     
        if columns is not None:
            self.columns = [column for column in columns if column in self.df.columns]
        else:
            self.columns = self.df.columns
    
        logger.info(f'Dirty Data Diagnosis initialized!')
    
    def count_commas(self)-> dict[str, int]:

        '''
        Counts the number of rows with strings that contain commas in each column of the DataFrame
        
        Returns:
        --------
            dict
                A python dictionary of columns and number of rows with comma
        '''

        comma_count = {}

        for col in self.df[self.columns]:

            #  taking a count of strings that contain a comma ','
            comma_count[col] = int(self.df[col].astype('string').str.count(',').sum())

        return comma_count

    def count_decimals(self)-> dict[str, int]:

        '''
        Counts the number of rows that have decimals, in each column of the DataFrame
        
        Returns:
        --------
            dict
                A python dictionary of columns and number of rows with decimal (.)

        Example:
        -------
            DirtyDataDiagnosis(df).count_decimals()
        '''

        decimal_count = {}

        for col in self.df[self.columns]:
            #  taking a count of strings that contain a decimal
            decimal_count[col] = int(self.df[col].astype('string').str.count(r'\.').sum())

        return decimal_count

    def count_commas_with_decimals(self)-> dict[str, int]:
        '''
        Counts the number of rows that have decimals and commas both in each column of the DataFrame
        
        Returns:
        --------
            dict
                A python dictionary of columns and number of rows with decimal (.) and commas. (E.g: 1,250.40)
            
        Example:
        -------
            DirtyDataDiagnosis(df).count_commas_with_decimals()
            
        '''
        commas_and_decimals_count = {}

        for col in self.df[self.columns]:

            # ensuring that string contains a dot(or decimal)
            has_decimals = self.df[col].astype('string').str.count(r'\.')

            # ensuring that string contains a comma
            has_commas = self.df[col].astype('string').str.count(r',')

            # the string must atleast have 1 dot and 1 comma
            commas_and_decimals_count[col] = int(((has_decimals >=1) & (has_commas>=1)).sum())

        return commas_and_decimals_count

    def diagnose_numbers(self, show_available_methods=False)-> dict[str, dict[str, pd.DataFrame]]:
        '''
            Detects patterns and common formatting issues in numbers in each column of the DataFrame.

            The following diagnostics are computed per column:

            - only_numbers:            Values containing only integers or decimals (e.g: 1000, -10.048)
            - only_text:               Values containing alphabetic characters and spaces ('unknown', 'error', 'missing', what)
            - is_dirty:                Values that are not strictly numeric (e.g: approx 1000, $100,00CD#44)
            - is_null:                 Values that are null or missing values (pandas missing types- NA or NaN)
            - has_commas:              Numeric values containing comma separators (e.g: 10,000 or 1,000,000)
            - has_decimals:            Numeric values containing decimal points (e.g: -1.62, 1000.44)
            - has_units:               Numeric values suffixed with alphabetic units (e.g., "10kg")
            - has_symbols:             Values containing non-alphanumeric or special symbols (e.g: '?', '/' , '.')
            - has_currency:            Values containing currency symbols (prefix or suffix) (e.g. $10 or 10$)
            - has_scientific_notation: Values expressed in scientific notation (e.g: 1.06E+1)
            - has_spaces:              Values that contain leading or trailing spaces (e.g: '  missing', '1.066 ', '1.34    ')
            - has_double_decimals:     Values that contain double decimals (e.g: 1.34.567, 1.4444.0000)

            Parameters:
            -----------
                self

                Optional:
                ---------
                show_available_methods : bool (default is False)
                    Shows diagnostic options that are available in diagnose_numbers() method.

            Returns:
            --------
                pd.DataFrame
                    A pandas DataFrame

            Usage Recommendation:
            ---------------------
                1. Use this function when you want to see what kind of issues exist in columns that contain numbers in your DataFrame

            Considerations:
            ---------------
                1. This method adds a default **index** column by resetting the DataFrame's index.
                2. This is necessary to preserve original row IDs during conversion to Polars and back.
                3. The index column DOES NOT AFFECT your transformations and are automatically restored in all returned DataFrames
                4. This method also uses Polars regex under the hood for pattern matching
                5. This method is intended for diagnostic purposes, not data mutation.

            Example:
            --------
            >>>     diagnostics = DirtyDataDiagnosis(df).diagnose_numbers()

            >>>     diagnostics['price']['has_currency'].head()
            
            '''
        from ..utils.BackendConverter import BackendConverter
        
        # resetting index to ensure index is turned into a new column 'index' in pandas dataframe
        self.df = self.df.reset_index()   

        # passing dataframe including the new column 'index'
        polars_df = BackendConverter(self.df).pandas_to_polars()

        numeric_diagnosis={}

        # patterns is a dictionary of available methods and regex patterns to detect them 
        patterns = {
            'only_numbers': r'^[+-]?\d+(\.\d+)?$',
            'only_text': r'^[A-Za-z ]+$',
            'is_dirty': r'^[+-]?\d+(\.\d+)?$',
            'has_units': r'^[+-]?\d+(?:[,.]\d+)?\s*[A-Za-z]+$',
            'has_symbols': r'[^A-Za-z0-9\s,.+$€£¥₹₩₺₫₦₱₪฿₲₴₡-]',
            'has_commas': r'\d[\d.,]*,\d',
            'has_currency': r'^[$€£¥₹₩₺₫₦₱₪฿₲₴₡]\s*\d[\d,]*(\.\d+)?$|^\d[\d,]*(\.\d+)?\s*[$€£¥₹₩₺₫₦₱₪฿₲₴₡]$',
            'has_scientific_notation': r'^[+-]?\d+(?:[.,]\d+)[eE][+-]?\d+',
            'has_double_decimals': r'^[+-]?\d+(?:\.\d+){2,}$',
            'has_spaces': r'^\s+[+-]?\d+(?:\.\d+)?$|^[+-]?\d+(?:\.\d+)?\s+$|^\s+[+-]?\d+(?:\.\d+)?\s+$',
            'is_null': None,
            'has_decimals': r'^[+-]?\d*\.\d+$'
            }

        # excluding index column so that it is not involved in diagnosis 
        columns_to_diagnose = [column for column in polars_df.columns if column != 'index']

        for col in columns_to_diagnose:
            
            numeric_diagnosis[col] = {}
            series = polars_df[col]

            for method, pattern in patterns.items():
                
                if method == 'is_null':
                    mask = series.is_null()

                elif method == 'is_dirty':

                    mask = ~series.str.contains(patterns['is_dirty'])

                else:
                    mask = series.str.contains(pattern)
                
                # filtering pattern masks out of the polars dataframe 
                result_df = BackendConverter(polars_df.filter(mask)).polars_to_pandas()

                # setting default index to be 'index'
                result_df.set_index('index', inplace=True)

                numeric_diagnosis[col][method] = result_df
                
        if show_available_methods:
            logger.info(f'Available diagnostic methods: {list(numeric_diagnosis[col].keys())}')

        return numeric_diagnosis

    def diagnose_text(self, show_available_methods=False)-> dict[str, dict[str, pd.DataFrame]]:
        '''
        Detects patterns and common formatting issues in text in each column of the DataFrame.

        The following diagnostics are computed per column:
        
        - only_symbols: Values containing only symbols.
        - only_text:    Values containing alphabetic characters and spaces
        - is_dirty:     Values that are not strictly text
        - has_symbols:  Values containing non-alphanumeric or special symbols
        - is_null:      Values that are null or missing values.
        - has_numbers:  Values that contain numbers in text.
        - has_spaces:   Values that contain leading or trailing spaces 

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame

        Usage Recommendation:
        ---------------------
            1. Use this function when you want to see what kind of issues exist in columns that contain text in your DataFrame

        Considerations:
        ---------------
            1. This method uses Polars regex under the hood for pattern matching and is converted back to pandas before being returned.
            2. This method is intended for diagnostic purposes, not data mutation.

        Example:
        --------
        >>>     diagnostics = DirtyDataDiagnosis(df).diagnose_text()

        >>>     diagnostics['user_id']['is_dirty'].head()
        
        '''
        from ..utils.BackendConverter import BackendConverter
        
        pol_df = BackendConverter(self.df).pandas_to_polars()

        text_diagnosis = {}

        for col in pol_df.columns:

            text_diagnosis[col] = {
                'is_dirty':None,
                'only_symbols': None,
                'has_symbols': None,
                'only_text': None,
                'is_null': None,
                'has_spaces': None,
                'has_numbers': None
            }

            text_diagnosis[col]['is_dirty']= BackendConverter(pol_df.filter(pl.col(col).str.contains(r'[^A-Za-z]'))).polars_to_pandas()
            text_diagnosis[col]['only_text'] = BackendConverter(pol_df.filter(pl.col(col).str.contains(r'^[A-Za-z ]+$'))).polars_to_pandas()
            text_diagnosis[col]['only_symbols'] = BackendConverter(pol_df.filter(pl.col(col).str.contains(r'^[^\p{L}]+$'))).polars_to_pandas()
            text_diagnosis[col]['has_symbols'] = BackendConverter(pol_df.filter(pl.col(col).str.contains(r'\p{L}.*[^\p{L}]|[^\p{L}].*\p{L}'))).polars_to_pandas()
            text_diagnosis[col]['has_numbers'] = BackendConverter(pol_df.filter(pl.col(col).str.contains(r'\p{N}'))).polars_to_pandas()
            text_diagnosis[col]['is_null'] = BackendConverter(pol_df.filter(pl.col(col).is_null())).polars_to_pandas()
            text_diagnosis[col]['has_spaces'] = BackendConverter(pol_df.filter(pl.col(col).str.contains(r'^\s|\s$'))).polars_to_pandas()

        if show_available_methods:
            logger.info(f'Available diagnostic methods: {list(text_diagnosis[col].keys())}')

        return text_diagnosis


