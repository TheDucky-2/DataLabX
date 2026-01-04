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
        
        logger.info(f'Done!')

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

        logger.info(f'Done!')

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

        logger.info(f'Done!')

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

        logger.info(f'Done!')

        return units_in_numbers_dict

    def detect_only_letters(self):
        '''
        Detects rows that contain only alphabets with or with spaces in each column of the DataFrame.

        Parameters:
        -----------
            self : pd.DataFrame
                A pandas DataFrame

        Returns:
        --------
            dict
                A python dictionary of column names and rows of numbers containing only letters and spaces
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to see what rows contain only letters and spaces.

        Example:
        --------
            DirtyDataDiagnosis(df).detect_only_letters()
        '''
        # detect text pattern
        text_pattern = r'[A-Za-z ]+'

        text_only_dict = {}

        for col in df.columns:
            # using fullmatch to ensure only rows containing only letters is detected
            text_only_dict[col]=self.df[self.df[col].astype('string').str.fullmatch(text_pattern, na=False)]
        
        logger.info(f'Done!')

        return text_only_dict
    
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
        

