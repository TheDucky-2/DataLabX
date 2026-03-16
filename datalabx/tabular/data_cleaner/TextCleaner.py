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

        super().__init__(df,columns)
        
        if not isinstance(df, (pd.DataFrame, pd.Series)):
            raise TypeError(f'df must be a pandas DataFrame or pandas Series, got {type(df).__name__}')

        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be a list of strings or type None, got {type(columns).__name__}')
            
        # ensuring only text based datatypes are selected
        self.df = df
        
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
        multiple_spaces_pattern = r'\s{2,}'

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
            logger.info('No splitters and replacements received, hence, no changes made.')
            return self.df

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
            logger.info('No symbols and replacements received, hence, no changes made.')
            return self.df
            

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

    def remove_square_brackets_and_content(self,include_columns: bool =False)-> pd.DataFrame:
        """
        Removes square brackets and content inside, in one or multiple columns of the DataFrame.

        E.g: "United Nations(2024)[7]", "China[n 1]", IMF(2026)[1], etc.

        Parameters
        -----------
        include_columns: bool, optional
            Whether you would like same changes to be applied to columns as well, default is False.

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame
        
        Usage Recommendation
        ---------------------
            Use this method to remove square brackets and content inside them during cleaning.
        
        Considerations
        ---------------
            1. This method keeps the converted number as string instead of a numerical datatype like int or float.
            2. Use this method on numerical data.
            3. This method keeps a track of values that cannot be cleaned.

        Example
        --------
                # Removing from rows except column names row
        >>>    NumericalCleaner(df).remove_square_brackets_and_content()

                # Removing from rows including column names row
        >>>    NumericalCleaner(df).remove_square_brackets_and_content(include_columns=True)
        """
        import re

        if not isinstance(include_columns, bool):
            raise TypeError(f'include_columns must be a bool, got {type(include_columns).__name__}')
            
        # regex pattern for removing square brackets and everything inside except ']'
        PATTERN = r'\[[^\]]*\]'

        pol_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        for col in pol_df.columns:
            # maintaining before, mask, cleaned and after for tracking dirty values after cleaning
            before = pol_df.get_column(col)
            mask = before.str.contains(PATTERN)

            pol_df = pol_df.with_columns(
                pl.col(col).str.replace_all(PATTERN, "").str.strip_chars()
            )
            after = pol_df.get_column(col)

            self.track_not_cleaned(
                col=col,
                method ="remove_square_brackets_and_content",
                before = before,
                mask = mask, 
                after = after)

        # renaming column names if columns have to be included
        if include_columns:
            pol_df = pol_df.rename(
                {col: re.sub(PATTERN, "", col).strip() for col in pol_df.columns}
            )
            logger.info('Removed square brackets and content in column names of the DataFrame.')
        
        if self.inplace:
            self.df[self.columns] = BackendConverter(pol_df).polars_to_pandas()
            logger.info(f"Removed square brackets and content in rows of the DataFrame, in place.")
            return None
        
        else:
            df = BackendConverter(pol_df).polars_to_pandas()
            logger.info(f"Removed square brackets and content in rows of the DataFrame.")
            return df

    def remove_parentheses_and_content(self, include_columns:bool = False):
        import re

        if not isinstance(include_columns, bool):
            raise TypeError(f'include_columns must be a bool, got {type(include_columns).__name__}')
            
        # regex pattern for removing parantheses and everything inside except ')'
        PATTERN = r'\s*\([^\)].*\)\s*'

        pol_df = BackendConverter(self.df[self.columns]).pandas_to_polars()

        for col in pol_df.columns:

            before = pol_df.get_column(col)
            mask = before.str.contains(PATTERN)

            pol_df = pol_df.with_columns(
                pl.col(col).str.replace_all(PATTERN, "").str.strip_chars()
            )
            after = pol_df.get_column(col)

            self.track_not_cleaned(
                col = col,
                method = 'remove_parentheses_and_content',
                before = before,
                mask = mask,
                after = after
            )
        # renaming column names if columns have to be included
        if include_columns:
            pol_df = pol_df.rename({col: re.sub(PATTERN, "", col).strip()
                for col in pol_df.columns})
            logger.info('Removed parantheses and content in column names of the DataFrame.')

        if self.inplace:
            self.df[self.columns] = BackendConverter(pol_df).polars_to_pandas()
            logger.info(f"Removed parantheses and content in rows of the DataFrame, in place.")
            return None

        else:
            df = BackendConverter(pol_df).polars_to_pandas()
            logger.info(f"Removed parantheses and content in rows of the DataFrame.")
            return df
    