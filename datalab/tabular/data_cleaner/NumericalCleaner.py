import pandas as pd
import polars as pl

from .BaseCleaner import DataCleaner # base data cleaner class 
from ..utils.BackendConverter import BackendConverter
from ..utils.Logger import datalab_logger # logger for logging

logger = datalab_logger(name = __name__.split('.')[-1])

class NumericalCleaner(DataCleaner):
    
    def __init__(self, df: pd.DataFrame, columns: list = None, inplace:bool=False):
        # Initializing the base data cleaner
        super().__init__(df, columns, inplace)
        self.df = df 

        if columns is None: 
            # if passed column is in columns of the DataFrame
            self.columns = self.df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns]
        
        self.inplace = inplace

        logger.info(f'NumericalCleaner initialized...')

    def round_off(self, decimals:int=2)-> pd.DataFrame:
        '''
        Round off numbers by N decimals in one or multiple columns of the DataFrame

        E.g: '23.00000000757575'-> '23.00', '3333556.89786'-> '3333556.89'

        Parameters:
        -----------
            self
                A pandas DataFrame
            
            Optional:
            ---------
                decimals : int (default is 2)
                    Number of decimals you want to round off by

                inplace : bool (default is False)
                    If True, modifies the DataFrame in place and returns None.
                    If False, returns a new DataFrame.

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame 

        Usage Recommendation:
        ---------------------
            1. Use this function when you want to round off floats (decimals) to either 2 or 3 decimal places.

        Considerations:
        ----------------
            1. Use this method only on numerical data.

        Example:
        ---------
        >>> cleaner = NumericalCleaner(df, columns= ['salary'])
        >>> cleaner.round_off(3, inplace=True)
        '''
        if not isinstance(decimals, int):
            raise TypeError(f'decimals must be a int, got {type(decimals).__name__}')

        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        for col in polars_df.columns:
            # getting values before conversion
            before = polars_df.select(pl.col(col)).to_series()
            # keeping a simple mask of values as rounding off is applied to all rows of the DataFrame
            mask = pl.Series(values=[True] * polars_df.height, dtype=pl.Boolean)
            # applying conversion
            polars_df=polars_df.with_columns(
                pl.col(col).round(decimals)
                )
            # getting values after conversion
            after = polars_df.select(pl.col(col)).to_series()
            # updating the not_cleaned dictionary to store values 
            self.track_not_cleaned(col=col, method = 'round_off',mask=mask, before=before, after=after)
            
        if self.inplace:
            self.df[self.columns] = BackendConverter(polars_df).polars_to_pandas()
            logger.info(f'Rounded off to {decimals} decimals, inplace.')
            return None
        else:
            df = BackendConverter(polars_df).polars_to_pandas()
            logger.info(f'Rounded off to {decimals} decimals')
            return df
    
    def remove_spaces(self):
        '''
        Removes leading or trailing spaces in numerical data for each column of DataFrame

        Parameters:
        -----------
            self : pd.DataFrame
                A pandas DataFrame

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame with removed trailing or leading spaces.
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to remove leading or trailing spaces in numbers.

        Example:
        --------
            DirtyDataDiagnosis(df).remove_spaces()
        '''
        SPACES_PATTERN = r'^\s+|\s+$'

        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        for col in polars_df.columns:
            # keeping a track of values before conversion
            before = polars_df.select(pl.col(col)).to_series()
            # creating a mask of values with spaces
            mask = polars_df.select(pl.col(col).str.contains(SPACES_PATTERN)).to_series()
            # making changes to the dataframe if spaces are present
            polars_df = polars_df.with_columns(
                pl.when(pl.col(col).str.contains(SPACES_PATTERN))
                .then(pl.col(col).str.replace_all(SPACES_PATTERN, ""))
                .otherwise(pl.col(col))
                )
            # tracking values after conversion
            after = polars_df.select(pl.col(col)).to_series()
            # storing data in the tracker
            self.track_not_cleaned(col = col, method= 'remove_spaces', before = before, mask = mask, after = after)
        
        if self.inplace:
            self.df[self.columns] = BackendConverter(polars_df).polars_to_pandas()
            logger.info(f'Removed leading or trailing spaces in place.')
            return None    
        else:
            df = BackendConverter(polars_df).polars_to_pandas()
            logger.info(f'Removed leading or trailing spaces.')
            return df

    def remove_units(self)-> pd.DataFrame:
        '''
        Detects units (like cm or kg) appearing after numbers and removes them in each column of the DataFrame.

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame

        Usage Recommendation:
        ---------------------
            1. Use this function when you want to clean numbers that contain units or text appearing after numbers.

        Example:
        --------
            NumericalCleaner(df).remove_units()
        '''
        # pattern for detecting rows containing units
        UNITS_PATTERN = r'^[+-]?\d+(?:[,.]\d+)?\s*[A-Za-z]+$'

        # pattern for detecting only text, so we can use this to replace the units
        units = r'\s*[A-Za-z]+$'
        
        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        for col in polars_df.columns:

            before = polars_df.select(pl.col(col)).to_series()
            mask = polars_df.select(pl.col(col).str.contains(UNITS_PATTERN)).to_series()
            polars_df = polars_df.with_columns(
                pl.when(pl.col(col).str.contains(UNITS_PATTERN))
                .then(pl.col(col).str.replace_all(units, ""))
                .otherwise(pl.col(col))
                )
            after = polars_df.select(pl.col(col)).to_series()
        
            self.track_not_cleaned(col = col, method= 'remove_units', before = before, mask = mask, after = after)

        if self.inplace:
            self.df[self.columns] = BackendConverter(polars_df).polars_to_pandas()
            logger.info(f'Removed units in place.')
            return None    
        else:
            df = BackendConverter(polars_df).polars_to_pandas()
            logger.info(f'Removed units.')
            return df

    def remove_currency_symbols(self)-> pd.DataFrame:
        '''
        Removes currency symbols appearing before or after numbers in each column of the DataFrame

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame

        Usage Recommendation:
        ---------------------
            1. Use this function when you want to remove currency symbols like $.
        
        Example:
        ---------
            NumericalCleaner(df).remove_currency_symbols()
        '''
        # ensuring that currency is detected at beginning or end of string
        CURRENCY_SYMBOLS_PATTERN = r'^[$€£¥₹₩₺₫₦₱₪฿₲₴₡]\s*\d[\d,]*(.\d+)?$|^\d[\d,]*(.\d+)?s*[$€£¥₹₩₺₫₦₱₪฿₲₴₡]$'

        CURRENCY_SYMBOLS = r'^[$€£¥₹₩₺₫₦₱₪฿₲₴₡]\s*|\s*[$€£¥₹₩₺₫₦₱₪฿₲₴₡]$'
        
        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        for col in polars_df.columns:
            before = polars_df.select(pl.col(col)).to_series()
            mask = polars_df.select(pl.col(col).str.contains(CURRENCY_SYMBOLS_PATTERN)).to_series()
            
            polars_df = polars_df.with_columns(
                pl.when(pl.col(col).str.contains(CURRENCY_SYMBOLS_PATTERN))
                .then(pl.col(col).str.replace_all(CURRENCY_SYMBOLS_PATTERN, ""))
                .otherwise(pl.col(col))
            )
            
            after = polars_df.select(pl.col(col)).to_series()
        
            self.track_not_cleaned(col = col, method= 'remove_currency_symbols', before = before, mask = mask, after = after)

        if self.inplace:
            self.df[self.columns] = BackendConverter(polars_df).polars_to_pandas()
            logger.info(f'Removed currency symbols in place.')
            return None    
        else:
            df = BackendConverter(polars_df).polars_to_pandas()
            logger.info(f'Removed currency symbols.')
            return df

    def replace_commas_with_decimals(self)-> pd.DataFrame:
        '''
        Replaces commas (,) that are used as decimal replacements, with decimals (.) in each column of the DataFrame

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame

        Usage Recommendation:
        ---------------------
            1. Use this function when you want to replace commas with decimal values during numerical cleaning
        
        Example:
        ---------
            NumericalCleaner(df).replace_commas_with_decimals()
        '''
        commas_pattern = r'^-?\d+(\,\d+)$'

        for col in self.df[self.columns]:
            # creating a mask of matched values
            mask = self.df[col].astype('string').str.match(commas_pattern, na=False)
            # replacing commas with decimals in those values
            self.df.loc[mask, col]= self.df.loc[mask, col].astype(str).str.replace(',', '.')

        return self.df

    def convert_scientific_notation_to_numbers(self)-> pd.DataFrame:
        '''
        Converts scientific notation like (4.67e01 or 4,67e01 or 1.04e+05) to readable numbers like 104000 in each column of the DataFrame

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame
        
        Usage Recommendation:
        ----------------------
            1. Use this method to convert scientific notation into numbers, during numerical cleaning.

        Example:
        --------
            NumericalCleaner(df).convert_scientific_notation_into_numbers()
        '''
        from decimal import Decimal

        SCIENTIFIC_NOTATION_PATTERN = r'^[+-]?\d+(?:[.,]\d+)?[eE][+-]?\d*$'
        
        scientific_notation_dict = {}

        def scientific_notation_to_number(text):
            text = text.strip().replace(',', '.').replace('E', 'e')
            try:
                return format(Decimal(text), 'f')
            except:
                return text

        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()
        
        for col in polars_df.columns:
            before = polars_df.select(pl.col(col)).to_series()
            mask = polars_df.select(pl.col(col).str.contains(SCIENTIFIC_NOTATION_PATTERN)).to_series()
            polars_df = polars_df.with_columns(
                pl.when(pl.col(col).str.contains(SCIENTIFIC_NOTATION_PATTERN))
                .then(pl.col(col).map_elements(scientific_notation_to_number))
                .otherwise(pl.col(col))
            )
            after = polars_df.select(pl.col(col)).to_series()
            self.track_not_cleaned(col=col, method='convert_scientific_notation_to_numbers',mask=mask, before=before, after=after )

        if self.inplace:
            self.df[self.columns] = BackendConverter(polars_df).polars_to_pandas()
            logger.info('Converted scientific notation to readable numbers in place.')
            return None
        else:
            df = BackendConverter(polars_df).polars_to_pandas()
            logger.info('Converted scientific notation to readable numbers.')
            return df

    def convert_text_to_numbers(self, text_to_number:dict[str, str]=None)-> pd.DataFrame:
        '''
        Converts text to numbers in one or multiple columns of the DataFrame

        E.g: 'five' ->  5, 'one' -> 1, 'thirty' -> 30 etc.

        Parameters:
        -----------
            self

            Optional:
            ---------
                text_to_number : dict
                    A dictionary of text and its replacement number.

        Returns:
        ---------
            pd.DataFrame
                A pandas DataFrame
        
        Usage Recommendation:
        ----------------------
            1. Use this method to convert textual numbers 'one', 'two' to numbers like 1, 2, during numerical cleaning.
        
        Considerations:
        ---------------
            1. This method keeps the converted number as string instead of a numerical datatype like int or float.

        Example:
        --------
        >>>    NumericalCleaner(df).convert_text_to_numbers({'five': 5, 'two': 2, 'one': 1})
        '''
        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        if text_to_number is None:
            logger.info('No text-to-number mapping received, hence, no changes made!')
            return self.df

        for col in polars_df.columns:
            for text, number in text_to_number.items():

                before = polars_df.select(pl.col(col)).to_series()
                mask = polars_df.select(pl.col(col).str.contains(text)).to_series()
                polars_df = polars_df.with_columns(
                    pl.when(pl.col(col).str.contains(text))
                    .then(pl.col(col).str.replace_all(text, number))
                    .otherwise(pl.col(col))
                )

                after = polars_df.select(pl.col(col)).to_series()

                self.track_not_cleaned(col=col, method = 'convert_text_to_numbers', before = before, mask = mask, after = after)

        if self.inplace:
            self.df[self.columns] = BackendConverter(polars_df).polars_to_pandas()
            logger.info(f"Converted '{text}' to '{number}' in place.")
            return None

        else:
            df = BackendConverter(polars_df).polars_to_pandas()
            logger.info(f"Converted '{text}' to '{number}'.")
            return df
                