"""Standardisation means turning numbers into "above average” or “below average” scores."""

import pandas as pd
from .DataPreprocessor import DataPreprocessor
from ..utils.Logger import datalab_logger

logger = datalab_logger(name = __name__.split('.')[-1])

class Standardization(DataPreprocessor):

    def __init__(self, df: pd.DataFrame, columns: list = None):
        super().__init__(df, columns)
        """
        Initializing Standardization.

        Parameters:
        -----------
        df: pd.DataFrame
            A pandas dataframe you wish to standardize.

        columns: list, optional
            A list of numerical columns you want to apply standardization on, default is None.
        """
        self.df = self.df.select_dtypes(include='number')
        
        if columns is None:
            self.columns = self.df.columns
        else:
            self.columns = [column for column in columns if column in self.df.columns]

        logger.info('Standardization initialized.')

    def z_score_standardization(self) -> pd.DataFrame:
        """Also known as StandardScaler()."""
        import numpy as np

        z_scores = np.abs((self.df - self.df.mean())/self.df.std())

        standardized_data = self.df / z_scores

        logger.info('Standardized data using z-score method.')

        return standardized_data

    def robust_iqr_standardization(self) -> pd.DataFrame:
        """Standardizes data by centering data at the median and scales by IQR(Inter-Quartile Range)."""

        from ..computations import Statistics

        standardized_data = (self.df - self.df.median())/ Statistics(self.df).iqr()

        logger.info('Standardized data using iqr method.')

        return standardized_data

    def robust_mad_standardization(self) -> pd.DataFrame:
        """Standardizes data by centering data at the median and scales by scaled-MAD(Median Absolute Deviation)."""

        from ..computations import Statistics

        robust_standardized_data = (self.df - self.df.median())/Statistics(self.df).scaled_median_absolute_deviation()

        logger.info('Standardized data using median absolute deviation.')

        return robust_standardized_data

    def unit_variance(self) -> pd.DataFrame:
        """Standardizes data by scaling the numbers so they are 1 standard deviation away from each other."""
        from ..computations import Statistics

        standardized_data = self.df / Statistics(self.df).standard_deviation()

        logger.info('Standardized data by spreading data 1 standard deviation away.')

        return standardized_data

    def mean_centering(self)-> pd.DataFrame:
        """Standardizes data by centering data around the mean."""
        mean_centered_data = self.df - self.df.mean()

        logger.info('Standardized data by centering it around the mean.')
        return mean_centered_data


