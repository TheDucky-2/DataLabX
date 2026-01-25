"""Detects the values that are outliers, in a Numerical DataFrame."""

import pandas as pd
from .Computation import Computation

class Outliers(Computation):
    
    def __init__(self, df:pd.DataFrame, columns:list=None):

        """Initializing Outliers Computation.
        
        Parameters
        -----------
        df: pd.DataFrame
            A pandas dataframe you wish to diagnose.

        columns: list, optional
            A list of columns you wish to detect outliers in, default is None.
        """
        import pandas as pd
        import numpy as np

        super().__init__(df, columns)

        self.df = df

        if columns is None:
            self.columns = self.df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns]

    def zscore_outliers(self, zscore_threshold: int|float = 3)-> pd.DataFrame:
        """
        Computes outliers in a column using the Z-score method.

        Parameters
        ----------
        zscore_threshold : int or float, optional
            z-score value above which a value is flagged as an outlier, default is 3.

        Returns
        -------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        --------------------
            Use when data is roughly normal and you want to flag values far from the overall mean(average).
        
        Considerations
        --------------
            1. This method keeps rows with values that are not outliers and they automatically convert to NaN.
            2. However, those rows remain preserved since this method is just meant purely for computation.
            3. Typically, values with |Z-score| > 3 are considered outliers.

        Example
        -------
        >>> Outliers(df).zscore_outliers()
        >>> Outliers(df).zscore_outliers(zscore_threshold=3)
        """

        if not isinstance(zscore_threshold, (int,float)):
            raise TypeError(f'threshold must be an integer, got {type(zscore_threshold).__name__}')

        zscore = (self.df - self.df.mean())/self.df.std()

        # In practice, anything over a z_score of over +3 or less than -3 is considered an outlier.
        zscore_outliers = self.df[(zscore.abs()) > zscore_threshold]

        return zscore_outliers

    def iqr_outliers(self)-> pd.DataFrame:
        """
        Computes outliers in a column using the IQR (Inter-Quartile Range) method.

        Returns
        -------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        --------------------
            Use for skewed data or unknown distributions to detect values outside the typical range.

        Considerations
        --------------
            1. This method keeps rows with values that are not outliers and they automatically convert to NaN.
            2. However, those rows remain preserved since this method is just meant purely for computation.
            3. Outliers are those below (q1 - 1.5 x IQR) or above (q3 + 1.5 x IQR).

        Example
        -------
        >>> Outliers(df).iqr_outliers()
        """
        # calculating 25th and 75th percentiles

        q1 = self.df.quantile(0.25)               # 1st quartile
        q3 = self.df.quantile(0.75)               # 3rd quartile

        # calculating IQR.
        IQR = q3 - q1

        # setting lower and upper boundaries.
        lower_boundary = q1 - (1.5 * IQR)
        upper_boundary = q3 + (1.5 * IQR)

        # outliers are values that are lower than lower boundary or higher than higher boundary.
        iqr_outliers = self.df[(self.df < lower_boundary) | (self.df > upper_boundary)]

        return iqr_outliers

    def quantile_outliers(self, lower_quantile: int|float|None = None , upper_quantile: int|float|None = None) -> pd.DataFrame:
        """
        Computes outliers in a column using the user-defined quantiles.

        Parameters
        ----------
        lower_quantile: int or float, optional
            percentile below which a value is flagged as an outlier, default is 0.01.

        upper_quantile: int or float, optional
            percentile above which a value is flagged as an outlier, default is 0.99.

        Returns
        -------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        --------------------
            Use when you have domain knowledge or want custom thresholds for outliers.

        Considerations
        --------------
            1. This method keeps rows with values that are not outliers and they automatically convert to NaN.
            2. However, those rows remain preserved since this method is just meant purely for computation.
            3. Values below the 10th percentile or above the 99th percentile.

        Example
        -------
        >>> Outliers(df).quantile_outliers()

        >>> Outliers(df).quantile_outliers(0.02, 0.98)
        """
        if not isinstance(lower_quantile, (int, float, type(None))):
            raise TypeError(f'lower quantile must be an int or float, got {type(lower_quantile).__name__}')

        if not isinstance(upper_quantile, (int, float, type(None))):
            raise TypeError(f'upper quantile must be an int or float, got {type(upper_quantile).__name__}')

        if lower_quantile is None:
            lower_quantile = 0.01  # 1st percentile
        if upper_quantile is None:
            upper_quantile = 0.99  # 99th percentile

        # lower boundary would be any quantile passed in by the user.
        lower_boundary = self.df.quantile(q=lower_quantile)
        
        # upper boundary would be any quantile passed in by the user.
        upper_boundary = self.df.quantile(q=upper_quantile)

        # outliers are values that are lower than lower boundary or higher than higher boundary.
        quantile_outliers = self.df[(self.df < lower_boundary) | (self.df > upper_boundary)]

        return quantile_outliers







