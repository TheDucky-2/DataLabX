"""Diagnoses the Categorical columns in your DataFrame."""

import pandas as pd
from ..utils.Logger import datalab_logger
# importing parent class
from .Diagnosis import Diagnosis

logger = datalab_logger(name = __name__.split('.')[-1])

class CategoricalDiagnosis():
    """
    Initializing Categorical Diagnosis.

    Parameters
    -----------
    df: pd.DataFrame
        A pandas DataFrame.

    columns : list, optional
        A list of column names you want to apply diagnosis on, by default None.
    """

    def __init__(self, df: pd.DataFrame, columns: list|type(None) = None):

        if not isinstance(df, pd.DataFrame):
            raise TypeError(f'df must be a pandas DataFrame, got {type(df).__name__}')

        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be a list of column names, got {type(columns).__name__}')

        self.df = df.select_dtypes(include=['object', 'string', 'category'])

        if columns is None:
            self.columns = self.df.columns.to_list()
        else:
            self.columns = [column for column in columns if column in self.df.columns]

        logger.info(f'Categorical Diagnosis initialized.')

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
        method : str 
            Whether frequency should be a count or a percentage.

            Available methods:

            - 'count': Counts the number of unique values in each category (default).
            - 'percent': Calculates the percentage of values in each category.
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
    
