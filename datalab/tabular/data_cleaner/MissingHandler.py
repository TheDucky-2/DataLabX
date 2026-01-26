"""Handles Missing Data in Numerical and Categorical columns of a DataFrame."""

import pandas as pd
import numpy as np

class MissingHandler():
    """
    Initializing Missing Handler.

    Parameters
    -----------
    df : pd.DataFrame
        A pandas DataFrame containing missing data.

    columns : list, optional
        List of columns you wish to convert, by default None.
    """
    def __init__(self, df, columns: list=None, extra_placeholders: list = None):

        self.df = df
        
        if columns is None:
            self.columns = self.df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns]

        if extra_placeholders is None:
            self.extra_placeholders = []
    
    def replace_missing(self, to_replace: list[str| float| type(np.nan)], replace_with: str|float|int, **kwargs: dict) -> pd.DataFrame:

        """Replace missing values like 'ERROR','MISSING', 'UNKNOWN' etc. with any value of choice.

        Parameters
        ----------

        to_replace  :list[str, float]
            List of values you wish to replace. Example: ['NA', 'ERROR', 'MISSING', np.nan]

        replace_with: str, float or int
            Value you wish to replace with

        kwargs: dict, optional
            A dictionary of extra keyword arguments you wish to pass in pandas ``df.replace()`` method, like regex=True

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
        >>>    MissingHandler(df).replace_missing(to_replace=['UNKNOWN', 'MISSING', None], replace_with = np.nan) 

        >>>    MissingHandler(df).replace_missing(to_replace=['UNKNOWN', 'MISSING', np.nan], replace_with = 'MISSING') 
        """
        if not isinstance(to_replace, (list, (float, int, str))):
            raise TypeError(f'to_replace must be a list of strings or np.nan, got {type(to_replace).__name__}')

        if not isinstance(replace_with, (pd.Series, str, type(None), float, int)):
            raise TypeError(f'replace_with must be a string, None, float or int, got {type(replace_with).__name__}')

        self.df[self.columns] = self.df[self.columns].replace(to_replace, replace_with, **kwargs)

        return self.df

    def drop_missing_columns(self, **kwargs)-> pd.DataFrame:
        """
        Drops columns that have missing data in a DataFrame

        Parameters
        ----------

        kwargs: dict, optional
            A dictionary of extra keyword arguments you wish to pass in pandas ``df.drop_na()`` method

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
        >>> MissingHandler(df, columns=['credit_score']).drop_missing_columns()

        """
        return self.df[self.columns].dropna(axis=1, **kwargs)

    def drop_missing_rows(self, **kwargs)-> pd.DataFrame:
        """
        Drops rows that have missing data in a DataFrame

        Parameters
        -----------
        kwargs: dict, optional
            A dictionary of extra keyword arguments you wish to pass in pandas ``df.drop_na()`` method

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
        >>> MissingHandler(df, columns=['credit_score']).drop_missing_rows()
        """
        return self.df[self.columns].dropna(**kwargs)

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

        >>> MissingHandler(df, columns=['credit_score']).fill_with_mean()

        >>> df['credit_score'] = [734.97, 734.78, 717.02, 712.21, 686.13]
        """
        return self.df[self.columns].fillna(self.df[self.columns].mean())

    def fill_with_median(self):
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

        >>> MissingHandler(df, columns=['savings']).fill_with_median()

        >>> df['savings'] = [14173.3, 37970.2, 24008.95, 20536.30, 17063.67, 57161.76, 20536.30, 5927.63, 28954.98, 5553.7]
        """
        return self.df[self.columns].fillna(self.df[self.columns].median())

        
