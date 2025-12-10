from .Diagnosis import Diagnosis
from ..utils import BackendConverter

from pathlib import Path

import pandas as pd
import polars as pl

class TextDiagnosis(Diagnosis):

    def __init__(self, df: pd.DataFrame, columns:list = None):
        from pathlib import Path
        '''
        Initializing the Diagnosis

        Parameters:
        -----------
        df: pd.DataFrame
            A pandas dataframe you wish to diagnose

        columns: list
            A list of columns you wish to apply numerical cleaning on

        Considerations:
            This class uses polars under the hood for text processing, since pandas was extremely slow.
            
            However, it accepts pandas DataFrame as input and returns a pandas DataFrame as output.
        '''
        super().__init__(df, columns)

        self.df = df.select_dtypes(include = ['string', 'object', 'category'])

        if columns is not None:
            self.columns = [column for column in columns if column in df.columns]
        else:
            self.columns = self.df.columns
    
    def detect_empty_string(self) -> pd.DataFrame:
        '''
        Filters rows with empty strings for each column of Text DataFrame (string, object or category type columns).
        
        Return:
            df : pd.DataFrame
            A pandas DataFrame of rows with empty strings.
        
        Usage Recommendation:
            Use this function when you want to diagnose rows with empty strings during text diagnosis.

        Considerations:
            This function uses polars's filter method to filter out rows where value is an empty string ("").

        Example: 
            TextDiagnosis(df).detect_empty_string()
		    ->
			    Returns all rows with empty_strings
        
        '''
        polars_df = BackendConverter(self.df).pandas_to_polars()

        empty_string_df = polars_df.filter(pl.any_horizontal([(pl.col(column) == "") for column in polars_df.columns]))

        empty_string_df = BackendConverter(empty_string_df).polars_to_pandas()
        
        return empty_string_df

    def detect_whitespaces(self) -> pd.DataFrame:
        '''
        Filters rows with whitespaces for each column of Text DataFrame (string, object or category type columns).
        
        Return:
            df : pd.DataFrame
            A pandas DataFrame of rows with whitespaces or simply spaces, for values.
        
        Usage Recommendation:
            Use this function when you want to diagnose rows with whitespaces during text diagnosis.

        Considerations:
            This function uses polars's filter method to filter out rows where value is a whitespace (" ").

        Example: 
            TextDiagnosis(df).detect_whitespaces()
            ->
                Returns all rows with white spaces
        
        '''
        polars_df = BackendConverter(self.df).pandas_to_polars()

        whitespace_df = polars_df.filter(pl.any_horizontal([(pl.col(column) == " ") for column in polars_df.columns]))

        whitespace_df = BackendConverter(whitespace_df).polars_to_pandas()
            
        return whitespace_df

    def detect_multiple_spaces(self) -> pd.DataFrame:

        '''
        Detects multiple spaces within characters or words in each column of the Text DataFrame.

        Returns:
            pd.DataFrame
            A pandas DataFrame of rows with text having multiple spaces.

        Usage Recommendation:
        ---------------------
            1. Use this function when you want to detect multiple spaces inside text.
            2. Use this for diagnosing text before replacing multiple spaces with TextCleaner(df).replace_multiple_spaces_with_single()

        Considerations:
        --------------
            Checks two consecutive spaces under the hood.

        Example:
            TextDiagnosis(df).detect_multiple_spaces()
        '''
        polars_df = BackendConverter(self.df).pandas_to_polars()

        multiple_spaces_df = polars_df.filter(pl.any_horizontal([pl.col(c).str.contains(r'\s{2,}') for c in polars_df.columns]))
        
        multiple_spaces_df = BackendConverter(multiple_spaces_df).polars_to_pandas()
        
        return multiple_spaces_df

    def detect_dots_within_text(df)-> pd.DataFrame:
        '''
        Detects dots within words or strings for one or multiple columns of the DataFrame.

        Returns:
            pd.DataFrame
            A pandas DataFrame of rows with one or more dots within text.

        Usage Recommendation:
            Use this function when you want to detect if there are dots within text.

        Consideration:
            Use this function for exploring data before replacing dots with TextCleaner(df).replace_dots_within_text()

        Example:
            TextDiagnosis(df).detect_dots_within_text()

        '''
        polars_df = BackendConverter(df).pandas_to_polars()
        
        text_with_dots_df = polars_df.filter(pl.any_horizontal(pl.col(pl.Utf8).str.contains(r'\.')))

        text_with_dots = BackendConverter(text_with_dots_df).polars_to_pandas()

        return text_with_dots