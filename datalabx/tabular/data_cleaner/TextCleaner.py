"""Clean text or Categorical columns in a tabular dataset"""

import pandas as pd
import polars as pl
from polars import selectors as cs

from .BaseCleaner import DataCleaner

from ..utils.Logger import datalabx_logger
from ..utils.BackendConverter import BackendConverter

logger = datalabx_logger(name= __name__.split('.')[-1])

class TextCleaner(DataCleaner):
    """
    Initializing Text Cleaner.

    Parameters
    -----------
    df: pd.DataFrame
        A pandas DataFrame
    
    columns: list, optional
        List of columns you wish to apply cleaning on, by default None.
    """
    
    def __init__(self, df:pd.DataFrame, columns:list=None):
        
        if not isinstance(df, (pd.DataFrame, pd.Series)):
            raise TypeError(f'df must be a pandas DataFrame or pandas Series, got {type(df).__name__}')

        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be a list of strings or type None, got {type(columns).__name__}')
            
        # ensuring only text based datatypes are selected
        self.df = df.select_dtypes(include = ['object', 'string', 'category']) 
        
        if columns is None: 
            self.columns = self.df.columns.to_list()
        else:
            self.columns = [column for column in columns if column in self.df.columns]

        logger.info('Text Cleaner initialized.')

    def to_lowercase(self) -> pd.DataFrame:
        """
        Converts text to uppercase in one or multiple columns of the DataFrame.

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            Use this function when you have mixed values and want to convert strings to lowercase

        Consideration
        --------------
            1. Uses polars with_columns to apply regex to all string columns
            2. However, it still takes and returns a pandas DataFrame

        Example
        --------
        >>>    TextCleaner(df, columns=['user_status']).to_lowercase()
        """
        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        polars_df = polars_df.with_columns(
            cs.string()
            .str.to_lowercase())
        
        self.df = BackendConverter(polars_df).polars_to_pandas()

        logger.info('Converted to lowercase!')

        return self.df

    def to_uppercase(self) -> pd.DataFrame:
        """
        Converts text to lowercase in one or multiple columns of the DataFrame.

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            Use this function when you have mixed values and want to convert strings to uppercase

        Consideration
        --------------
            1. Uses polars with_columns to apply regex to all string columns
            2. However, it still takes and returns a pandas DataFrame

        Example:
        --------
        >>>    TextCleaner(df, columns=['user_status']).to_uppercase()
        """
        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        polars_df = polars_df.with_columns(
            cs.string().str.to_uppercase()
        )

        self.df = BackendConverter(polars_df).polars_to_pandas()

        logger.info('Converted to uppercase!')

        return self.df

    def remove_multiple_spaces(self) -> pd.DataFrame:
        """
        Removes multiple spaces within characters or words for one or multiple columns of the DataFrame.

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            Use this function when you want to remove multiple spaces within text values.

        Considerations
        --------------
            1. Uses polars with_columns to apply regex to all string columns
            2. However, it still takes and returns a pandas DataFrame

        Example
        --------
        >>>    TextCleaner(df, columns=['gender']).remove_multiple_spaces()
        """
        multiple_spaces_pattern = r'\s+'

        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        polars_df = polars_df.with_columns(cs.string().str.replace_all(multiple_spaces_pattern, ""))

        self.df = BackendConverter(polars_df).polars_to_pandas()

        logger.info('Removed multiple spaces!')

        return self.df

    def replace_splitters(self, splitters_and_replacements: dict[str, str]=None)-> pd.DataFrame:
        """
        Replaces different kinds of splitters present in data with the desired value, in one or multiple columns of the DataFrame.

        E.g: 'active/member' -> 'active-member', 'masters/ male' -> 'masters, male'.

        Parameters
        -----------
        splitters_and_replacements: dict 
            A dictionary of splitters and their replacements

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            Use this function when you want to normalize multiple splitters with one kind of splitter

        Considerations
        ---------------
            1. Uses polars with_columns to apply regex to all string columns
            2. However, it still takes and returns a pandas DataFrame

        Example
        --------
        >>>    TextCleaner(df, columns=['user_status]).replace_splitters({',': ''})
        """
        from ..utils.BackendConverter import BackendConverter
        import re
        
        if splitters_and_replacements is None:
            splitters_and_replacements={'':''}

        if not isinstance(splitters_and_replacements, dict):
            raise TypeError(f'splitters and replacements must be a dict, got {type(splitters_and_replacements).__name__}')

        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        for column in polars_df.columns:
            
            for splitter, replacement in splitters_and_replacements.items():
                
                # using re.escape to make values as literal
                polars_df=polars_df.with_columns(
                    pl.when(pl.col(column).str.contains(re.escape(splitter)))
                    .then(pl.col(column).str.replace_all(re.escape(splitter), replacement))
                    .otherwise(pl.col(column))
                )
                
        self.df = BackendConverter(polars_df).polars_to_pandas()

        return self.df

    def replace_symbols(self, symbols_and_replacements: dict[str, str]=None)-> pd.DataFrame:
        """
        Replaces different kinds of symbols present in data, with the desired value in one or multiple columns of the DataFrame.

        Example: 'Germ@any' -> 'Germany', 'Empl0y3d' -> 'Employed' or '<<active>>' -> 'active'

        Parameters
        -----------
        symbols_and_replacements: dict 
            A dictionary of symbols and their replacements, by default None

        Returns
        --------
            pd.DataFrame
                A pandas DataFrame

        Usage Recommendation
        ----------------------
            1. Use this function when you want to replace symbols with text or other symbols

        Consideration
        ---------------
            1. Uses polars with_columns to apply regex to all string columns
            2. However, it still takes and returns a pandas DataFrame

        Example
        --------
        >>>    TextCleaner(df, columns=['user_status]).replace_symbols({'@':'a', '0':'o'})
        """
        import re

        # if symbols and replacements are not passed, they default to empty strings 
        if symbols_and_replacements is None:
            symbols_and_replacements = {"":""} 

        if not isinstance(symbols_and_replacements, dict):
            raise TypeError(f'symbols and replacements must be a dict, got {type(symbols_and_replacements).__name__}')

        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        for col in polars_df.columns:

            for symbol, replacement in symbols_and_replacements.items():
                
                polars_df = polars_df.with_columns(
                    # using re.escape to ensure symbols passed are used as literal characters
                    pl.when(pl.col(col).str.contains(re.escape(symbol)))
                    .then(pl.col(col).str.replace_all(re.escape(symbol), replacement))
                    .otherwise(pl.col(col))
                )
    
        self.df = BackendConverter(polars_df).polars_to_pandas()

        return self.df
