from ..utils.Logger import datalab_logger
import pandas as pd

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
        
    def detect_clean_numerical_data(self):
        '''
        Shows rows of numerical data that includes just +ve or -ve numbers including decimals in each column of the DataFrame.

        Parameters:
        -----------
            self : pd.DataFrame
                A pandas DataFrame

        Returns:
        --------
            dict
                A python dictionary of column names and rows of clean numerical data
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to see what rows in your data contains only numbers to separate rows 

        Example:
        --------
            DirtyDataDiagnosis(df).detect_clean_numerical_data()
        '''

        # creating an empty dictionary
        clean_numbers = {}

        for column in self.df[self.columns]:
            
            # using the regex pattern to only detect numbers or numbers with decimals
            clean_numbers[column] = self.df[self.df[column].astype(str).str.match(r'^[+-]?\d+(\.\d+)?$')]

        logger.info(f'Done!')

        return clean_numbers
        
    def detect_dirty_numerical_data(self, pattern=None):
        '''
        Shows rows of numerical data that do not include +ve or -ve numbers including decimals in each column of the DataFrame.

        Parameters:
        -----------
            self : pd.DataFrame
                A pandas DataFrame

        Returns:
        --------
            dict
                A python dictionary of column names and rows of dirty numerical data
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to see rows with non-numbers or numbers that include text or symbols to separate dirty data for cleaning 

        Example:
        --------
            DirtyDataDiagnosis(df).detect_dirty_numerical_data()
        '''
        if pattern is None:
            pattern = r'^[+-]?\d+(\.\d+)?$'
        else:
            pattern = pattern

        dirty_numerical_data = {}

        for col in self.df[self.columns]:
            # detecting the rows that are not clean numbers
            dirty_numerical_data[col] = self.df[~self.df[col].astype(str).str.match(pattern)]

        logger.info(f'Done!')

        return dirty_numerical_data

    def detect_spaces_in_numerical_data(self):
        '''
        Shows rows of numerical data that contain leading or trailing spaces or both, for each column of DataFrame

        Parameters:
        -----------
            self : pd.DataFrame
                A pandas DataFrame

        Returns:
        --------
            dict
                A python dictionary of column names and rows of data that contain numbers with leading or trailing spaces
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to see what rows in your data contains only numbers with leading or trailing spaces.

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

            spaces_in_numerical_data[column] = self.df[mask]

        logger.info(f'Done!')
        
        return spaces_in_numerical_data

    def detect_commas_in_numbers(self):
        '''
        Shows rows of numerical data that contain commas in each column of the DataFrame

        Parameters:
        -----------
            self : pd.DataFrame
                A pandas DataFrame

        Returns:
        --------
            dict
                A python dictionary of column names and rows of numbers that contain commas
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to see what numbers contain commas.

        Example:
        --------
            DirtyDataDiagnosis(df).detect_commas_in_numbers()
            '''
        commas_dict = {}

        pattern = r'\d[\d.,]*,\d'

        for col in self.df[self.columns]:
            # using regex pattern for detecting commas 
            commas_dict[col] = self.df[self.df[col].astype(str).str.match(pattern, na=False)]

        return commas_dict
                    
    def detect_currency_symbols_in_numbers(self):
        '''
        Shows rows of numerical data that contain currency symbols in beginning or end, in each column of the DataFrame

        Parameters:
        -----------
            self : pd.DataFrame
                A pandas DataFrame

        Returns:
        --------
            dict
                A python dictionary of column names and rows of numbers that contain symbols in start or end
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to see what numbers contain currency symbols

        Example:
        --------
            DirtyDataDiagnosis(df).detect_currency_symbols_in_numbers()
        '''
        currency_symbols=  {}

        # detecting currency symbols in end or beginning
        detecting_currency_in_start_or_end = r'^[\$\£\€\¥\₹]\s*\d[\d,]*(\.\d+)?$|^\d[\d,]*(\.\d+)?\s*[\$\£\€\¥\₹]$'

        for col in self.df[self.columns]:

            currency_symbols[col] = self.df[self.df[col].astype(str).str.match(detecting_currency_in_start_or_end)]

        return currency_symbols

    def detect_scientific_notation_in_numbers(self):

        '''
        Shows rows of numerical data that have numbers in scientific notation in each column of the DataFrame

        Parameters:
        -----------
            self : pd.DataFrame
                A pandas DataFrame

        Returns:
        --------
            dict
                A python dictionary of column names and rows of numbers that are scientific notation
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to see what numbers contain scientific notation

        Example:
        --------
            DirtyDataDiagnosis(df).detect_scientific_notation_in_numbers()
        ''' 
        # detecting scientific notation in both decimals or commas
        pattern = r'^[+-]?\d+(?:[.,]\d+)[eE][+-]?\d+'

        detected_scientific_notation = {}
        
        for col in self.df[self.columns]:  

            detected_scientific_notation[col] = self.df[self.df[col].astype(str).str.match(pattern, na=False)]

        return detected_scientific_notation

    def detect_units_in_numbers(self):
        '''
        Detects if there are any units or text at the end of numbers (E.g 2cm or 2 kg) in each column of the DataFrame.

        Parameters:
        -----------
            self : pd.DataFrame
                A pandas DataFrame

        Returns:
        --------
            dict
                A python dictionary of column names and rows of numbers containing units
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to see what positive or negative numbers contain units. (cm, kg, etc.)

        Example:
        --------
            DirtyDataDiagnosis(df).detect_units_in_numbers()
        '''
        # ensuring that text can appear with/without spaces after numbers
        detect_units_pattern = r'[+-]?\d{1,3}(?:[,.]\d{2,3})?\s*[A-Za-z]+$'

        units_in_numbers_dict = {}

        for col in self.df[self.columns]:
            
            # converting to pandas String datatype rather than python str, to convert null values to <NA> and disclude them from matching
            units_in_numbers_dict[col] = self.df[self.df[col].astype('string').str.match(detect_units_pattern, na=False)]

        return units_in_numbers_dict

