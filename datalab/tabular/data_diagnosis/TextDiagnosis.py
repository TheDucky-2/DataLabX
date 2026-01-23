"""Diagnoses the Text columns in your tabular dataset"""

from ..utils.BackendConverter import BackendConverter
from ..utils.Logger import datalab_logger

import pandas as pd
import polars as pl
import polars.selectors as cs

logger = datalab_logger(name = __name__.split('.')[-1])

class TextDiagnosis:

    def __init__(self, df: pd.DataFrame, columns:list = None):
        from pathlib import Path
        """
        Initializing Text Diagnosis.

        Parameters:
        -----------
        df: pd.DataFrame
            A pandas dataframe you wish to diagnose.

        columns: list, optional
            A list of columns you wish to diagnose text in, by default None.
        
        """
        self.df = df.select_dtypes(include = ['string', 'object', 'category'])

        if columns is not None:
            self.columns = [column for column in columns if column in self.df.columns]
        else:
            self.columns = self.df.columns

        logger.info(f'Text Diagnosis Initialized.')
    
    def detect_empty_string(self) -> dict[str, pd.DataFrame]:
        """
        Filters rows with empty strings for each column of Text DataFrame (string, object or category type columns).

        Returns
        --------
        dict[str, pd.DataFrame]
            A dictionary of columns names with rows of DataFrame containing empty strings as text

        Usage Recommendation
        ---------------------
            Use this function when you want to diagnose rows with empty strings during text diagnosis.

        Considerations
        ---------------
            This function uses polars's filter method to filter out rows where value is an empty string ("").

        Example:
        --------
        >>> TextDiagnosis(df).detect_empty_string()
        
        """
        empty_strings_dict = {}

        # generating index as a column
        self.df = self.df.reset_index()

        # converting pandas -> polars with the index column, to preserve rows
        polars_df = BackendConverter(self.df).pandas_to_polars()

        columns_to_diagnose = [column for column in polars_df.columns if column!='index']
        
        for column in columns_to_diagnose:
            # ensuring that length of string should be equal to 0
            series_mask = (polars_df[column].str.len_chars() == 0)
            
            result_df = BackendConverter(polars_df.filter(series_mask)).polars_to_pandas()

            result_df.set_index('index', inplace=True)

            empty_strings_dict[column] = result_df

        return empty_strings_dict

    def detect_splitters(self, splitters:list = None)-> dict[str, pd.DataFrame]:
        """
        Filters rows with splitters for one or multiple columns of Text DataFrame.

        Parameters
        ----------
        splitters: list
            A list of splitters that may be present in your text, default is ','

        Returns
        --------
        dict[str, pd.DataFrame]
            A dictionary of columns names with rows of DataFrame containing splitters in text

        Usage Recommendation
        ---------------------
            Use this function when you want to diagnose rows of text where values are split.

        Considerations
        ---------------
            This function uses polars's filter method to filter out rows where values have a splitter.

        Example:
        --------
        >>> TextDiagnosis(df).detect_splitters()
        
        """

        if not isinstance(splitters, (list, type(None))):
            raise TypeError(f'splitters must be a list of strings, got {type(splitters).__name__}')

        if splitters is None:
            splitters = [","]
        
        splitters_dict = {}

        self.df = self.df.reset_index()

        polars_df = BackendConverter(self.df).pandas_to_polars()

        columns_to_diagnose = [column for column in polars_df.columns if column!='index']

        # joining splitters to convert them into a regex pattern for detecting splitters
        joined_splitters=f'[{"".join(splitters)}]+'

        # filtering rowx where text contains splitters passed in by the user
        for column in columns_to_diagnose:
            series_mask = (polars_df[column].str.contains(joined_splitters))
            
            result_df = BackendConverter(polars_df.filter(series_mask)).polars_to_pandas()
            # setting 'index' as index of pandas DataFrame
            result_df.set_index('index', inplace=True)

            splitters_dict[column] = result_df

        return splitters_dict


