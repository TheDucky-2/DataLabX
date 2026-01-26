"""Computes descriptive statistics for one or more Numerical columns of the DataFrame"""

from .Computation import Computation

import pandas as pd
import numpy as np

class Statistics(Computation):
    """
    Initializing the Statistics Computation.

    Parameters
    -----------
    df: pd.DataFrame
        A pandas dataframe

    columns: list, optional
        A list of columns you wish to compute statistics of, default is None.
    """
    
    def __init__(self, df:pd.DataFrame, columns:list=None):
        import pandas as pd
        import numpy as np

        super().__init__(df, columns)

        self.df = df.select_dtypes(include = 'number')

        if columns is None:
            self.columns = self.df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns]
    
    def max(self)-> pd.Series:
        """Computes maximum value per column.
        
        Returns
        --------
        pd.Series
            A pandas Series

        Example
        --------
        >>>  Statistics(df).max()
        """
        return self.df.max()

    def min(self)-> pd.Series:
        """Computes minimum value per column.

        Returns
        --------
        pd.Series
            A pandas Series

        Example
        --------
        >>>  Statistics(df).min()
        """
        return self.df.min()

    def range(self)-> pd.Series:
        """
        Computes range of a column.

        Returns
        --------
        pd.Series
            A pandas Series

        Example
        --------
        >>>  Statistics(df).range()
        """
        range = Statistics(self.df).max() - Statistics(self.df).min()

        return range

    def mean(self) -> pd.Series:
        """
        Computes the mean (Average).

        Returns
        --------
        pd.Series
            A pandas Series

        Example
        --------
        >>>  Statistics(df).mean()   
        """
        return self.df[self.columns].mean()
    
    def median(self)-> pd.Series:
        """
        Computes the median (middle value).

        Returns
        --------
        pd.Series
            A pandas Series

        Example
        --------
        >>>  Statistics(df).median()   
        """
        return self.df[self.columns].median()

    def standard_deviation(self)-> pd.Series:
        """
        Computes the standard deviation.

        Returns
        --------
        pd.Series
            A pandas Series

        Example
        --------
        >>>  Statistics(df).standard_deviation()  
        """
        return self.df[self.columns].std()

    def quantiles(self, quantile:int|float, **kwargs)-> pd.Series:
        """
        Computes the quantiles.

        Returns
        --------
        pd.Series
            A pandas Series

        Example
        --------
        >>>  Statistics(df).quantiles(0.75)  
        """
        if not isinstance(quantile, (float, int)):
            raise TypeError(f'quantile must be float or int, got {type(quantile).__name__}')

        return self.df.quantile(q=quantile, **kwargs)
            
    def iqr(self)-> pd.Series:
        """
        Computes the IQR (Inter-Quartile Range).

        Returns
        --------
        pd.Series
            A pandas Series

        Example
        --------
        >>> Statistics(df).iqr()
        """
        Q1 = Statistics(self.df).quantiles(0.25)
        Q3 = Statistics(self.df).quantiles(0.75)

        IQR = Q3 - Q1 

        return IQR

    def variance(self, method:str ='sample')-> pd.Series:

        """Computes variance.
        
        Returns
        -------
        pd.Series 
            A pandas Series

        Example
        --------
        >>> Statistics(df).variance('sample')

        >>> Statistics(df).variance('population')
        """
        if not isinstance(method, str):
            raise TypeError(f'method must be a string, got {type(method).__name__}')
        
        if method not in ['sample', 'population']:
            raise ValueError(f"method must either be 'sample' or 'population', got {method}")

        n = len(self.df)
                
        if method == 'sample':

            return ((self.df - self.df.mean())**2).sum()/(n-1)

        elif method == 'population':

            return ((self.df - self.df.mean())**2).sum()/(n)

    def median_absolute_deviation(self) -> pd.Series :
        """
        Computes the MAD (Median Absolute Deviation).

        Returns
        --------
        pd.Series
            A pandas Series

        Example
        --------
        >>> Statistics(df).median_absolute_deviation()
        """
        median = self.df.median()

        # subtracting median value from the values
        return (self.df.sub(median)).abs().median() 

    def scaled_median_absolute_deviation(self)-> pd.Series:
        """
        Computes the scaled MAD (Median Absolute Deviation), which is ~1.4826 * median_absolute_deviation().

        Returns
        --------
        pd.Series
            A pandas Series

        Example
        --------
        >>> Statistics(df).scaled_median_absolute_deviation()
        """
        return 1.4826 * Statistics(self.df).median_absolute_deviation()