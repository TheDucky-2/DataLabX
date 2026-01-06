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


    def diagnose_numbers(self)-> pd.DataFrame:
        '''
        Detects patterns and common formatting issues in numbers in each column of the DataFrame.

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame

        Usage Recommendation:
        ---------------------
            1. Use this function when you want to see what kind of issues exist in columns that contain numbers in your DataFrame

        Considerations:
        ---------------
            1. All pattern matching is performed using Polars regex.
            2. Each diagnostic is converted back to pandas before being returned.
            3. This method is intended for diagnostic purposes, not data mutation.

        Example:
        --------
        >>>     diagnostics = DirtyDataDiagnosis(df).diagnose_numbers()

        >>>     diagnostics["price"]["has_currency"].head()
        
        '''
        from ..utils.BackendConverter import BackendConverter
        
        # converting pandas DataFrame -> polars DataFrame
        polars_df = BackendConverter(self.df).pandas_to_polars()

        # creating an empty dictionary
        numeric_diagnosis = {}
        
        for col in polars_df.columns:
            
            numeric_diagnosis[col] = {
                'only_numbers' : None,
                'is_dirty' : None,
                'has_commas': None,
                'has_decimals': None,
                'has_units': None,
                'has_symbols': None,
                'has_scientific_notation': None,
                'only_text': None
            }
            
            # checking patterns using polars string expressions and converting to pandas DataFrame
            numeric_diagnosis[col]['only_numbers']= BackendConverter(polars_df.filter(pl.col(col).str.contains(r'^[+-]?\d+(\.\d+)?$'))).polars_to_pandas()
            numeric_diagnosis[col]['only_text'] = BackendConverter(polars_df.filter(pl.col(col).str.contains(r'[A-Za-z ]+'))).polars_to_pandas()
            numeric_diagnosis[col]['is_dirty']= BackendConverter(polars_df.filter(~pl.col(col).str.contains(r'^[+-]?\d+(\.\d+)?$'))).polars_to_pandas()
            numeric_diagnosis[col]['has_units']= BackendConverter(polars_df.filter(pl.col(col).str.contains(r'^[+-]?\d+(?:[,.]\d+)?\s*[A-Za-z]+$'))).polars_to_pandas()
            numeric_diagnosis[col]['has_symbols']= BackendConverter(polars_df.filter(pl.col(col).str.contains(r'[^A-Za-z0-9\s,.+$€£¥₹₩₺₫₦₱₪฿₲₴₡-]'))).polars_to_pandas()
            numeric_diagnosis[col]['has_commas']= BackendConverter(polars_df.filter(pl.col(col).str.contains(r'\d[\d.,]*,\d'))).polars_to_pandas()
            numeric_diagnosis[col]['has_currency']= BackendConverter(polars_df.filter(pl.col(col).str.contains(r'^[$€£¥₹₩₺₫₦₱₪฿₲₴₡]\s*\d[\d,]*(\.\d+)?$|^\d[\d,]*(\.\d+)?\s*[$€£¥₹₩₺₫₦₱₪฿₲₴₡]$'))).polars_to_pandas()
            numeric_diagnosis[col]['has_scientific_notation']= BackendConverter(polars_df.filter(pl.col(col).str.contains(r'^[+-]?\d+(?:[.,]\d+)[eE][+-]?\d+'))).polars_to_pandas()
        
        return numeric_diagnosis