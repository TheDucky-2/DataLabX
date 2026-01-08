from ..utils import BackendConverter

import pandas as pd
import polars as pl

import polars.selectors as cs

class TextDiagnosis():

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
        self.df = df.select_dtypes(include = ['string', 'object', 'category'])

        if columns is not None:
            self.columns = [column for column in columns if column in self.df.columns]
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
        # converting pandas -> polars
        polars_df = BackendConverter(self.df).pandas_to_polars()

        # setting an extra column called 'Index' to preserve row id.
        polars_df = polars_df.with_row_index('Index')
        
        # checking for empty string in any column  while also excluding 'Index' column
        empty_string_df = polars_df.filter(pl.any_horizontal(cs.exclude('Index').str.len_chars() == 0))

        # converting back to Pandas
        empty_string_df = BackendConverter(empty_string_df).polars_to_pandas()

        # setting 'Index' column as the index to preserve row id
        empty_string_df.index = empty_string_df['Index']

        # removing the extra 'Index' column
        empty_string_df.drop(columns='Index', inplace=True)
        
        return empty_string_df

    def detect_splitters(self, splitters = [","]):

        polars_df = BackendConverter(self.df).pandas_to_polars()

        polars_df = polars_df.with_row_index('Index')

        # joining splitters to convert them into a regex pattern for detecting splitters
        joined_splitters=f'[{"".join(splitters)}]+'

        # filtering rowx where text contains splitters passed in by the user
        splitters_df = polars_df.filter(
        pl.any_horizontal(
        [pl.col(column).str.contains(joined_splitters) for column in self.columns]))

        df = BackendConverter(splitters_df).polars_to_pandas()

        df.index = df['Index']

        df.drop(columns='Index', inplace=True)
        
        return df



