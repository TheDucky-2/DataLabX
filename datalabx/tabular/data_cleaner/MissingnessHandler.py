"""Handles Missing Data in Numerical and Categorical columns of a DataFrame."""

import pandas as pd
import numpy as np
from ..utils.Logger import datalabx_logger

logger = datalabx_logger(__name__.split('.')[-1])

class MissingnessHandler():
    """
    Initializing Missingness Handler.

    Parameters
    -----------
    df : pd.DataFrame
        A pandas DataFrame containing missing data.

    columns : list, optional
        List of columns you wish to convert, by default None.
    """
    def __init__(self, df, columns: list|None =None, extra_placeholders: list|None = None):

        self.df = df
        
        if columns is None:
            self.columns = self.df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns]

        if extra_placeholders is None:
            self.extra_placeholders = []
            logger.info('Considering only pandas built-in missing values as no extra placeholders received from the user')

        else:
            self.extra_placeholders = extra_placeholders
            logger.info((f'Extra Placeholders received for missing data: {self.extra_placeholders}'))

    def replace_missing(self, replacement: str|float|int|None = None) -> pd.DataFrame:

        """Replace missing values like 'ERROR','MISSING', 'UNKNOWN' etc. with any value of choice.

        Parameters
        ----------
 
        replacement: str, float, int or None, optional
            Value you wish to replace missing values with


        Returns
        -------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        --------------------
            Use this function when you want to replace missing values (NA) across multiple columns, that are not just np.nan. 
            Missing values could include values like ['ERROR', 'UNKNOWN', 'MISSING', 'NA', 'Null', None]

        Considerations
        --------------
            This function is intended to replace missing values with 1 single value. 
            If you wish to apply methods like mean, median or mode or other imputation methods, use ``fill_with_mean()``, ``fill_with_median()`` etc.


        Example:
        >>>    MissingnessHandler(df).replace_missing(replacement = np.nan) 

        >>>    MissingnessHandler(df).replace_missing(replacement = 'MISSING') 
        """
        if replacement is None:
            logger.info('No replacement value received, hence, no changes made.')
            return self.df
            
        if replacement == "":
            logger.info("Missing values will be replaced with empty strings.")

        if not isinstance(replacement, (pd.Series, str, type(None), float, int)):
            raise TypeError(f'replace_with must be a string, None, float or int, got {type(replacement).__name__}')

        pandas_missing = self.df.isna()
        placeholder_missing = self.df.isin(self.extra_placeholders)

        total_missing = pandas_missing | placeholder_missing

        logger.info(f"Replaced missing data with {replacement}")

        return self.df.mask(total_missing, replacement)

    def drop_missing_columns(self, how:str='any')-> pd.DataFrame:
        
        """
        Drops columns that have missing data in a DataFrame

        Parameters
        ----------
        how : str, optional
            How you would like to drop missing rows.

            Available Options:

            - 'any' : Drop rows with missing data in any column
            - 'all': Drop rows with missing data in all columns

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            1. Use this function when a high number of missing values exist in a particular column
            2. Use this function when the column is irrelevant for your analysis or modeling 
            3. DO NOT USE this function to drop columns that are important but may have a high number of missing values, E.g: [Salary, Income Tax].
        
        Considerations
        ---------------
            Be careful while dropping columns since we do not want to lose data that is important in one row even if irrelevant in another.

        Example
        --------
        >>> MissingnessHandler(df, columns=['credit_score']).drop_missing_columns()

        """
        if not isinstance(how, str):
            raise TypeError(f'how must be a string, got {type(how).__name__}')

        # checking for built-in missing values
        pandas_missing = self.df[self.columns].isna()

        # checking for placeholder mising values
        placeholder_missing = self.df[self.columns].isin(self.extra_placeholders)

        # if either pandas or placeholder values exist
        total_missing =  pandas_missing | placeholder_missing

        if how == 'any':
            # ensuring to filter only values that are true.
            columns_to_drop = total_missing.any(axis=0)[total_missing.any(axis=0)].index.tolist()

        elif how == 'all':
            columns_to_drop = total_missing.any(axis=0)[total_missing.any(axis=0)].index.tolist()

        else:
            raise ValueError(f"how must be 'any' or 'all', got {how}")
            
        if columns_to_drop:
            logger.info(f'Dropping columns: {columns_to_drop}')
            return self.df.drop(columns = columns_to_drop)

        else:
            return self.df

    def drop_missing_rows(self, how: str='any')-> pd.DataFrame:
        """
        Drops rows that have missing data(including custom placeholders) in a DataFrame 

        Parameters
        -----------
        how : str, optional
            How you would like to drop missing rows.

            Available Options:

            - 'any' : Drop rows with missing data in any column
            - 'all': Drop rows with missing data in all columns

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            1. Use this function when a low number of missing values exist in rows of a particular column.
            3. DO NOT USE this function to drop rows that are important but may have a high number of missing values, E.g: [Salary, Income Tax].
        
        Considerations
        ---------------
            Be careful while dropping rows since we do not want to lose data that is important in a particular column even if irrelevant in another.

        Example
        --------
        >>> MissingnessHandler(df, columns=['credit_score']).drop_missing_rows()
        """

        if not isinstance(how, str):
            raise TypeError(f'how must be a string, got {type(how).__name__}')

        # checking for built-in missing values
        pandas_missing = self.df[self.columns].isna()

        # checking for placeholder mising values
        placeholder_missing = self.df[self.columns].isin(self.extra_placeholders)

        # if either pandas or placeholder values exist
        total_missing =  pandas_missing | placeholder_missing

        if how == 'any':
            rows_with_missing_data = total_missing.any(axis=1)

            # if any row does not have missing data in any column
            if not rows_with_missing_data.any():
                logger.info('No rows with missing data in any column.')
                return self.df

        elif how == 'all':
            rows_with_missing_data = total_missing.all(axis=1)

            # if any row does not have missing data in all columns
            if not rows_with_missing_data.any():
                logger.info('No rows with missing data in all columns.')
                return self.df

        else:
            raise ValueError(f"how must be 'any' or 'all', got {how}")

        return self.df.loc[~rows_with_missing_data]

    def fill_with_mean(self)-> pd.DataFrame:
        """
        Replaces missing values with mean (average) value of that particular column, in one or multiple columns of a DataFrame.

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ----------------------
            1. Use this function if distribution of the numerical column is roughly normal (bell-curve) and missingness is low (5 - 10 %).
            2. DO NOT USE this function if your data is highly skewed or has strong outliers.

        Considerations
        ---------------
            Since mean is sensitive to outliers, use ``fill_with_median()`` method if your data is skewed.

        Example
        --------
        >>> df['credit_score'] = [734.97, 734.78, np.nan, 712.21, 686.13]

        >>> MissingnessHandler(df, columns=['credit_score']).fill_with_mean()

        >>> df['credit_score'] = [734.97, 734.78, 717.02, 712.21, 686.13]
        """

        pandas_missing = self.df.isna()
        placeholder_missing = self.df.isin(self.extra_placeholders)

        total_missing = pandas_missing | placeholder_missing

        logger.info("Filled missing data with mean value.")

        return self.df.mask(total_missing, self.df.mean(), axis=1)

    def fill_with_median(self)-> pd.DataFrame:
        """
        Replaces missing values with median (middle) value of that particular column, in one or multiple columns of a DataFrame.

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            1. Use this function if distribution of the numerical column is skewed.
            2. Use this function if your data has strong outliers.
            3. Use this function for continous numbers.

        Considerations
        ---------------
            If your data has normal distribution or does not have outliers, use ``fill_with_mean()`` instead.

        Example
        -------

        >>> df['savings'] = [14173.3,37970.2,24008.95,np.nan,17063.67,57161.76,np.nan,5927.63,28954.98,5553.7]

        >>> MissingnessHandler(df, columns=['savings']).fill_with_median()

        >>> df['savings'] = [14173.3, 37970.2, 24008.95, 20536.30, 17063.67, 57161.76, 20536.30, 5927.63, 28954.98, 5553.7]
        """
        
        pandas_missing = self.df.isna()
        placeholder_missing = self.df.isin(self.extra_placeholders)

        total_missing = pandas_missing | placeholder_missing

        logger.info("Filled missing data with median value.")

        return self.df.mask(total_missing, self.df.median(), axis=1)

                
