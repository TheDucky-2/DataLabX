"""Base cleaner class that is the parent of all other Cleaner classes"""

import pandas as pd
import polars as pl

class DataCleaner:
    """
    Initializing Base Cleaner
            
    Parameters
    -----------
    df: pd.DataFrame
        A pandas dataframe you wish to clean.

    columns: list, optional
        A list of columns you wish to apply cleaning on, default is None.
    """
    
    def __init__(self, df:pd.DataFrame, columns:list=None, inplace: bool=False):

        if not isinstance(df, (pd.DataFrame, pd.Series)):
            raise TypeError(f'df must be a pandas DataFrame or pandas Series, got {type(df).__name__}')

        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be a list of strings or type None, got {type(columns).__name__}')
        
        if not isinstance(inplace, bool):
            raise TypeError(f'inplace must be True or False, got {type(inplace).__name__}')
            
        # creating a copy of the original dataframe
        self.df = df.copy()  
        
        # if user passes a list of columns
        if columns is None: 
            # columns would default to all of the columns of the dataframe
            self.columns = df.columns.to_list()
        else:
            # columns would be the list of columns passed
            self.columns = columns

        self.not_cleaned = {}
        self.inplace = inplace
        
    def validate_columns(self):
        """This function just makes sure that the columns passed by the user actually exist in the dataframe.""" 
        # if the column passed by the user is not in dataframe
        missing_columns = [column for column in self.columns if column not in self.df.columns] 

        if missing_columns:
            raise TypeError(f'Columns not found in dataframe: {missing_columns}')
    
    def track_not_cleaned(self, *, method:str, col:str, before: pd.Series|pl.Series, mask:pd.Series|pl.Series, after:pd.Series|pl.Series)-> set:
        """
        This is an internal function used for tracking values that remain dirty even after cleaning.
        """

        if not isinstance(method, str):
            raise TypeError(f"'method' must be a str, got {type(method)}")

        if not isinstance(col, str):
            raise TypeError(f"'col' must be a str, got {type(col)}")
        
        def series_to_pandas(series):
            if isinstance(series, pd.Series):
                return series
            if isinstance(series, pl.Series):
                return series.to_pandas()
            else:
                raise TypeError(f'Expected pandas or polars Series, got {type(series)}')
        
        before = series_to_pandas(before)
        mask = series_to_pandas(mask)
        after = series_to_pandas(after)
        
        # if conversion failed, 
        cleaning_failed = mask & (before == after)

        if cleaning_failed.any():
            self.not_cleaned.setdefault(col, {})
            self.not_cleaned[col].setdefault(method, set())

            # making sure values that originally failed cleaning will be added
            self.not_cleaned[col][method].update(before[cleaning_failed].tolist())






