import pandas as pd
import polars as pl
from polars import selectors as cs

from .BaseCleaner import DataCleaner
from ..utils.Logger import datalab_logger
from ..utils.BackendConverter import BackendConverter

logger = datalab_logger(name= __name__.split('.')[-1])

class TextCleaner(DataCleaner):
    
    def __init__(self, df:pd.DataFrame, columns:list=None):
        
        if not isinstance(df, (pd.DataFrame, pd.Series)):
            raise TypeError(f'df must be a pandas DataFrame or pandas Series, got {type(df).__name__}')

        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be a list of strings or type None, got {type(columns).__name__}')
            
        # creating a copy of the original dataframe
        self.df = df.select_dtypes(include = ['object', 'string', 'category']) 
        
        # if user passes a list of columns
        if columns is None: 
            # columns would default to all of the columns of the dataframe
            self.columns = df.columns.to_list()
        else:
            # columns would be the list of columns passed
            self.columns = [column for column in columns if column in self.df.columns]

        logger.info('Text Cleaner initialized...')

    def to_lowercase(self: pd.DataFrame) -> pd.DataFrame:
        '''
        Converts text to uppercase in one or multiple columns of the DataFrame.

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame

        Usage Recommendation:
        ---------------------
            Use this function when you have mixed values and want to convert strings to lowercase

        Consideration:
        --------------
            1. Uses polars with_columns to apply regex to all string columns
            2. However, it still takes and returns a pandas DataFrame

        Example:
        --------
        >>>    TextCleaner(df, columns=['user_status']).to_lowercase()
        '''
        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        polars_df = polars_df.with_columns(
            cs.string()
            .str.to_lowercase())
        
        self.df = BackendConverter(polars_df).polars_to_pandas()

        logger.info('Converted to lowercase!')

        return self.df

    def to_uppercase(self: pd.DataFrame) -> pd.DataFrame:
        '''
        Converts text to lowercase in one or multiple columns of the DataFrame.

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame

        Usage Recommendation:
        ---------------------
            Use this function when you have mixed values and want to convert strings to uppercase

        Consideration:
        --------------
            1. Uses polars with_columns to apply regex to all string columns
            2. However, it still takes and returns a pandas DataFrame

        Example:
        --------
        >>>    TextCleaner(df, columns=['user_status']).to_uppercase()
        '''
        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        polars_df = polars_df.with_columns(
            cs.string().str.to_uppercase()
        )

        self.df = BackendConverter(polars_df).polars_to_pandas()

        logger.info('Converted to uppercase!')

        return self.df

    def replace_multiple_spaces(self) -> pd.DataFrame:
        '''
        Replaces multiple spaces within characters or words with a single space (" ") for each column of the DataFrame.

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame of columns replaced text.

        Usage Recommendation:
        ---------------------
            Use this function when you want to replace multiple spaces within text with a single space.

        Consideration:
        --------------
            1. Uses polars with_columns to apply regex to all string columns
            2. However, it still takes and returns a pandas DataFrame

        Example:
        --------
        >>>    TextCleaner(df, columns=['gender']).replace_multiple_spaces()
        '''
        multiple_spaces_pattern = r'\s+'

        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        polars_df = polars_df.with_columns(cs.string().str.replace_all(multiple_spaces_pattern, " "))

        self.df = BackendConverter(polars_df).polars_to_pandas()

        logger.info('Replaced multiple spaces!')

        return self.df

    def replace_splitters(self, splitters:list[str]=None, replacement:str=None):
        '''
        Replaces different kinds of splitters present in data, with a single splitter in each column of the DataFrame.

        Parameters:
        -----------
            self

            Optional:

            splitters : list or type None (default is ',')
                A list of splitters you have data separated by

            replacement: str or type None (default is ',')
                A single splitter you want to use for converting splitters to one single type of splitter

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame

        Usage Recommendation:
        ----------------------
            Use this function when you want to normalize multiple splitters with one kind of splitter

        Consideration:
        ---------------
            Uses polars's with_columns to apply regex to all string columns

        Example:
        --------
        >>>    TextCleaner(df, columns=['user_status]).replace_splitters(splitters = [',', '/', '-'], replacement = ',')

        '''
        from ..utils.BackendConverter import BackendConverter
        
        if splitters is None:
            splitters = [',']
        
        if replacement is None:
            replacement = ','

        if not all(isinstance(splitter, str) for splitter in splitters):
            raise TypeError(f"splitters must be a list of strings like ',', '/' etc., got {type(splitter)}")

        if not isinstance(replacement, str):
            raise TypeError(f"replacement must be a strings like ',' etc., got {type(replacement)}")

        splitters = f'[{"".join(splitters)}]'

        polars_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        for column in self.columns:
            pattern_mask = polars_df[column].str.contains(splitters)

            cleaned = polars_df[column].str.replace_all(splitters, replacement)

            polars_df = polars_df.with_columns(
                pl.when(pattern_mask)
                .then(cleaned)
                .otherwise(pl.col(column))
            )

        self.df = BackendConverter(polars_df).polars_to_pandas()

        logger.info('Replaced splitters!')

        return self.df