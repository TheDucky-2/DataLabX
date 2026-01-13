import pandas as pd

from .BaseCleaner import DataCleaner # base data cleaner class 
from ..utils.Logger import datalab_logger # logger for logging

logger = datalab_logger(name = __name__.split('.')[-1])

class NumericalCleaner(DataCleaner):
    
    def __init__(self, df: pd.DataFrame, columns: list = None):
        # Initializing the base data cleaner
        super().__init__(df, columns)
        self.df = df 

        if columns is None: 
            # if passed column is in columns of the DataFrame
            self.columns = self.df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns]
        
        logger.info(f'NumericalCleaner initialized...')

    def round_off(self, decimals:int=2, inplace:bool=False)-> pd.DataFrame:
        '''
        Round off numbers by N decimals in one or multiple columns of the DataFrame

        E.g: '23.00000000757575'-> '23.00', '3333556.89786'-> '3333556.89'

        Parameters:
        -----------
            self
                A pandas DataFrame

            decimals : int (default is 2)
                Number of decimals you want to round off by

            inplace  : bool (default, False)
                If True, modifies the original DataFrame in place.
                If False, returns a new DataFrame with only the converted columns.

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

        >>> NumericalCleaner(df, ['salary']).round_off(3, inplace=True)
        
        >>> NumericalCleaner(df, ['salary']).round_off(3)
        '''
        if inplace:
            self.df[self.columns]= self.df[self.columns].apply(lambda column: column.round(decimals))
            return None
        else:
            self.df[self.columns]= self.df[self.columns].apply(lambda column: column.round(decimals))
            logger.info(f'Rounded off to {decimals} decimals.')
            return self.df.copy()

    def remove_spaces(self)->pd.DataFrame:
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
            DirtyDataDiagnosis(df).detect_clean_numerical_data()
        '''

        leading_spaces_pattern = r'^\s+[+-]?\d+(\.\d+)?$'
        trailing_spaces_pattern = r'^[+-]?\d+(\.\d+)?\s+$'
        leading_and_trailing_spaces_pattern = r'^\s+[+-]?\d+(\.\d+)?\s+$'

        spaces_in_numerical_data = {}

        for column in self.df[self.columns]:
            # getting rows of data with leading spaces
            detected_leading_spaces = self.df[column].astype(str).str.match(leading_spaces_pattern, na=False)
            # getting rows of data with trailing spaces
            detected_trailing_spaces = self.df[column].astype(str).str.match(trailing_spaces_pattern, na=False)
            # getting rows of data with leading and trailing spaces
            detected_leading_and_trailing_spaces = self.df[column].astype(str).str.match(leading_and_trailing_spaces_pattern, na=False)

            mask = detected_trailing_spaces | detected_leading_spaces | detected_leading_and_trailing_spaces

            # getting rows of the data with leading and trailing spaces and removing the spaces
            self.df.loc[mask, column] = self.df.loc[mask, column].astype(str).str.strip()
        
        logger.info('Removed leading and trailing spaces!')
            
        return self.df

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
        detect_units_pattern = r'^[+-]?\d+(?:[,.]\d+)?\s*[A-Za-z]+$'

        # pattern for detecting only text, so we can use this to replace the units
        units = r'\s*[A-Za-z]+$'

        for col in self.df[self.columns]:

            unit_mask = self.df[col].astype('string').str.match(detect_units_pattern, na=False)

            self.df.loc[unit_mask, col] = self.df.loc[unit_mask, col].astype('string').str.replace(units, "", regex=True)

        return self.df

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
        currency_in_start_or_end = r'^[\$\€\£\¥\₹\₩\₺\₫\₦\₱\₪\฿\₲\₴\₡]\s*\d[\d,]*(\.\d+)?$|^\d[\d,]*(\.\d+)?\s*[\$\€\£\¥\₹\₩\₺\₫\₦\₱\₪\฿\₲\₴\₡]$'


        for col in self.df[self.columns]:
            mask = self.df[col].astype(str).str.match(currency_in_start_or_end, na=False)
            
            # removing currency symbols
            self.df.loc[mask, col] = self.df.loc[mask, col].astype(str).str.replace(r'[\$\€\£\¥\₹\₩\₺\₫\₦\₱\₪\฿\₲\₴\₡]', '', regex=True)

        return self.df

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

        pattern = r'^[+-]?\d+(?:[.,]\d+)?[eE][+-]?\d*$'
        
        scientific_notation_dict = {}

        def scientific_notation_to_number(text):
            text = text.strip().replace(',', '.').replace('E', 'e')
            try:
                return format(Decimal(text), 'f')
            except:
                return text

        for col in self.df[self.columns]:
            before = self.df[col].copy()
            mask = self.df[col].astype(str).str.match(pattern)
            self.df.loc[mask, col] = self.df.loc[mask, col].apply(scientific_notation_to_number)
            after = self.df[col]
            self.track_not_cleaned(col=col, method='convert_scientific_notation_to_numbers',mask=mask, before=before, after=after )
    
        return self.df

    def convert_text_to_numbers(self, text_and_number: dict[str,str]=None)-> pd.DataFrame:
        '''
        Converts text to numbers in one or multiple columns of the DataFrame

        E.g: 'five' ->  5, 'one' -> 1, 'thirty' -> 30 etc.

        Parameters:
        -----------
            self

            Optional:
            ---------
                text_and_number : dict
                    A dictionary of text and its number replacement.

        Returns:
        ---------
            pd.DataFrame
                A pandas DataFrame
        
        Usage Recommendation:
        ----------------------
            1. Use this method to convert textual numbers like 'one', 'two' to numbers like 1, 2, during numerical cleaning.
        
        Considerations:
        ---------------
            1. This method keeps the converted number into a string datatype, instead of a numerical datatype like int or float.

        Example:
        --------
        >>>    NumericalCleaner(df).convert_text_to_numbers({'five': 5, 'two': 2, 'one': 1})
        '''
        
        if text_and_number is None:
            logger.info('No text-to-number mapping received, hence, no changes made!')
            return self.df
            
        if not isinstance(text_and_number, dict):
            raise TypeError(f'Expected a dictionary of text and its numerical replacement, got {type(text_and_number)}')

        for text, number in text_and_number.items():

            for column in self.df[self.columns]:

                self.df[column] = self.df[column].astype('string').str.replace(text, str(number))

            logger.info(f"Converted '{text}' to '{number}'.")

        return self.df

    

