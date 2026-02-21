"""Computes Correlation between two columns of a DataFrame."""

import pandas as pd

from .Computation import Computation
from ..utils.Logger import datalabx_logger

logger = datalabx_logger(name = __name__.split('.')[-1])

class Correlation(Computation):
    """
    Initializing the Correlation Computation .

    Parameters
    -----------
    df: pd.DataFrame
        A pandas dataframe you wish to diagnose.

    columns: list, optional
        A list of columns you wish to check correlation for, by default None.
    """

    def __init__(self, df:pd.DataFrame, columns:list=None):

        super().__init__(df, columns)

        self.df = df
        
        if columns is None:
            self.columns = self.df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns]

        logger.info(f'Correlation initialized.')

    def covariance(self)-> pd.DataFrame:
        """
        Computes the covariance matrix of a pandas DataFrame.

        Covariance shows how two columns (variables) change together:

        - Positive -> both increase together
        - Negative -> one increases while the other decreases
        - Zero -> mostly independent

        Returns
        -------
        pd.DataFrame
            A pandas DataFrame

        Example
        -------
        >>> Correlation(df).covariance()
        """
        return self.df.cov()
        
    def correlation(self, method:str = 'pearson')-> pd.DataFrame:
        """
        Computes the correlation matrix of a pandas DataFrame.

        Pearson correlation measures how strongly two variables are linearly related:

        - +1 -> perfectly positively correlated
        - -1 -> perfectly negatively correlated
        - 0  -> no linear correlation

        Parameters
        -----------
            method: str, optional
                Method using which you would like to calculate correlation, default is 'pearson'.

                Available methods:

                - 'pearson': measures how much two columns go up or down together in a straight-line.
                - 'spearman': measures how much two columns move together based on their ranking order.
                - 'kendall': measures how often two columns move in the same direction when comparing all pairs.

        Returns
        -------
        pd.DataFrame
            A pandas DataFrame

        Example
        -------
        >>> Correlation(df).correlation()
        >>> Correlation(df).correlation('spearman')
        >>> Correlation(df).correlation('kendall')
        """

        if not isinstance(method, str):
            raise TypeError(f'method must be a string, got {type(method).__name__}')

        if method not in ['pearson', 'spearman', 'kendall']:
            raise ValueError(f"Available methods are: 'pearson', 'spearman', 'kendall'")

        logger.info(f'Computing correlation using {method} method.')

        return self.df.corr(method = method)
