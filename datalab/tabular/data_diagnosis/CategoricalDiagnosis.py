"""Diagnoses the Categorical columns in your DataFrame"""

import pandas as pd
from ..utils.BackendConverter import BackendConverter
# importing parent class
from .Diagnosis import Diagnosis

class CategoricalDiagnosis(Diagnosis):

    def __init__(self, df: pd.DataFrame, columns: list|type(None) = None):
        """
        Parameters
        -----------

        df: pd.DataFrame
            A pandas DataFrame

        columns : list or type(None)
            A list column names. 
            Use column names when you want to apply diagnosis only on the desired columns
        """
        super().__init__(df, columns)

        self.df = df.select_dtypes(include=['object', 'string', 'category'])

        if columns is not None:
            self.columns = [column for column in df.columns if column in self.df.columns]
        else:
            self.columns = df.columns.tolist()
        
    def count_unique_categories(self):
        """Shows count of unique categories in one or multiple columns of DataFrame.
        
        Returns
        --------
        dict
            A dictionary of count of unique categories in each column
        """
        
        unique_categories = {}

        for column in self.df[self.columns]:
            unique_categories[column]=len(self.df[column].unique())

        return unique_categories

    def show_frequency(self, method='count'):
        """Shows frequency ('count' or 'percent') of categories in one or multiple columns of DataFrame.

        Parameters
        -----------

        method : str (default is 'count')

            Available methods:

            - 'count': Counts the number of unique values in each category (default)
            - 'percent': Calculates the percentage of values in each category
        """
        # using a dictionary for storing frequency of category values
        frequency_count = {}

        # getting the percentage
        # renaming as frequency count and rounding off to 2 places 
        for column in self.df[self.columns]:
            
            if method == 'count':
                frequency_count[column]=self.df[column].value_counts().rename(f'Frequency Count')

            elif method == 'percent':
                frequency_count[column]=self.df[column].value_counts(normalize=True).rename(f'Frequency Percentage').round(2)

            else:
                raise ValueError("Unknown method. Valid methods: 'sum' (default) or 'percent'")
        # returning the dictionary of frequency percentage
        
        return frequency_count
    
