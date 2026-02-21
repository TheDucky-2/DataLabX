"""Normalization is adjusting numbers so they're on the same scale."""

import pandas as pd
import numpy as np
from .DataPreprocessor import DataPreprocessor

class Normalization(DataPreprocessor):
    """
    Initializing Normalization.

    Parameters
    -----------
    df: pd.DataFrame
        A pandas dataframe you wish to normalize

    columns: list, optional
        A list of numerical columns you want to apply normalization on, default is None.
    """

    def __init__(self, df: pd.DataFrame, columns: list = None):
        super().__init__(df, columns)
      
        self.df = self.df.select_dtypes(include='number')
        
        if columns is None:
            self.columns = self.df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns]

    def max_normalization(self) -> pd.DataFrame:
        """
        Normalizes your data by dividing each value with the maximum value of that column.

        Formula
        --------
                    X
            X' =  -----
                   max

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            1. Use this function when you do not have negative values in your data.
            2. Use this function when your models are sensitive to feature scaling.
               Examples: KNN, Neural Networks, k-means, DBSCAN, or Gradient based (Adam, SGD)

            3. DO NOT USE this function if your maximum value is an outlier. It will distort scaling.

        Considerations
        ---------------
            1. This function scales your data by squeezing it between 0 and 1 without changing the shape of your data.
            2. It does not mean that the mean of your data will be 0, or 1 standard deviation away from the mean.
            3. For making your data zero-centered (mean = 0, std=1), use ``Standardization()``

        Example
        -------
        >>>    Normalization(df).max_normalization()
        """
        normalized_data = {}

        for column in self.df[self.columns]:
            
            data = np.array(self.df[column]) 

            maximum_absolute_value = np.abs(data.max())

            normalized_data[column] = (data/maximum_absolute_value)
            
            normalized_df = pd.DataFrame(normalized_data) 

        return normalized_df
        
    def minmax_normalization(self) -> pd.DataFrame:
        """
        Normalizes your data to a range [0, 1] based on the minimum and maximum values.

        Formula
        -------
                  (X - min)
            X' =  ---------
                 (max - min)

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            1. Use this function when your models are sensitive to feature scaling.
               Examples: KNN, Neural Networks, k-means, DBSCAN, or Gradient based (Adam, SGD)

            2. DO NOT USE this function if your maximum value is an outlier. It will distort scaling.

        Considerations
        ---------------
            1. This function scales your data by squeezing it between 0 and 1 without changing the shape of your data.
            2. It does not mean that the mean of your data will be 0, or 1 standard deviation away from the mean.
            3. For making your data zero-centered (mean = 0, std=1), use Standardization()

        Example
        --------
        >>>    Normalization(df).minmax_normalization()
        """
        minmax_normalized_data ={}

        for column in self.df[self.columns]:
            
            data = np.array(self.df[column])

            minmax_normalized_data[column] = (data - data.min()) / (data.max() - data.min())

        minmax_normalized_df = pd.DataFrame(minmax_normalized_data)
            
        return minmax_normalized_df

    def feature_range_normalization(self, range:tuple = (0, 1)) -> pd.DataFrame:
        """
        Normalizes your data to a specified range based on the minimum and maximum values.

        Formula
        --------
                   (X - min)
            X' =  -----------
                  (max - min)

        Parameters
        -----------
        range: tuple, optional
            A tuple of minimum and maximum value you wish to scale your data between, default is (0,1).

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            1. Use this function when your models are sensitive to feature scaling.
               Examples: KNN, Neural Networks, k-means, DBSCAN, or Gradient based (Adam, SGD)

            2. DO NOT USE this function if your maximum value is an outlier. It will distort scaling.

        Considerations
        ---------------
            1. This function scales your data by squeezing it between 0 and 1 without changing the shape of your data.
            2. It does not mean that the mean of your data will be 0, or 1 standard deviation away from the mean.
            3. For making your data zero-centered (mean = 0, std=1), use Standardization()

        Example
        --------
        >>>    Normalization(df).feature_range_normalization()
        """
        minmax_normalized_data = Normalization(self.df).minmax_normalization()

        r_min, r_max = range

        featurerange_normalized_df = minmax_normalized_data * (r_max - r_min) + r_min

        return featurerange_normalized_df

    def mean_normalization(self) -> pd.DataFrame:
        """
        Normalizes your data by subtracting the mean and dividing by the range (max-min)..

        Formula:

                  (X - mean)
            X' =  ----------
                  (max - min)

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            1. Use this function when your models are sensitive to feature scaling.
               Examples: KNN, Neural Networks, k-means, DBSCAN, or Gradient based (Adam, SGD)

            2. DO NOT USE this function if your maximum value is an outlier. It will distort scaling.

        Considerations
        ---------------
            1. This function scales your data within a limited range, usually [-1, 1]
            2. It also centers your data around 0 (the mean).
            3. If you want unit variance, use z_score standardization

        Example
        -------
        >>>    Normalization(df).mean_normalization()
        """
        normalized_data ={}

        for column in self.df[self.columns]:
            
            data = np.array(self.df[column])

            data_mean = data.mean()

            normalized_data[column] = (data - data_mean) / (data.max() - data.min())

        return pd.DataFrame(normalized_data)

    def l1_normalization(self) -> pd.DataFrame:
        """
        Normalizes your data by dividing each value with the sum of absolute values.

        Formula
        --------
                      X
            X' =  ---------
                    ∑| X |

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            1. Use this function when ratio (proportions) of values matter more than than the size (magnitude) of value.
            2. Use this function if your data is sparse (have a lot of zeroes)

            3. DO NOT USE this function if your data is negative since L1 Normalization uses absolute values.

        Considerations
        ---------------
            1. This function scales your data to proportions that sum up to a value of 1
            2. It does not affect the shape of your data.

        Example
        -------
            Normalization(df).l1_normalization()
        """
        l1_norm = {}

        for column in self.df[self.columns]:
            data = np.array(self.df[column])

            l1_norm[column] = data / np.abs(data.sum())

        l1_df = pd.DataFrame(l1_norm)

        return l1_df

    def l2_normalization(self) -> pd.DataFrame:
        """
        Normalizes your data by dividing each value with the square root of the sum of squared values.

        Formula
        --------
                             X
            X' =     ------------------
                    square root of (∑ (X^2))

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            1. Use this function when direction (pattern) or shape of data matter more than how big the numbers are.
            2. Use this function if your data is sparse (have a lot of zeroes)

            3. DO NOT USE if magnitude (size) of your data matters more than the direction of data.
            4. DO NOT USE if you want to keep a lot of zeroes in your data since this function spreads values around.
            5. DO NOT USE if your features have a lot of outliers.

        Considerations
        ---------------
            1. This function does not affect the shape or direction of your data.

        Example
        --------
            Normalization(df).l2_normalization()
        """
        l2_norm = {}

        for column in self.df[self.columns]:
            data = np.array(self.df[column])

            l2_norm[column] = data / (np.sqrt(((data)**2).sum()))

        l2_df = pd.DataFrame(l2_norm)

        return l2_df

    def lmax_normalization(self) -> pd.DataFrame:
        """
        Normalizes your data by dividing each value with the maximum absolute value.

        Formula
        --------
                        X
            X' =    ----------
                    max(| X |)

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            1. Use this function when direction (pattern) or shape of data matter more than how big the numbers are.
            2. Use this function if your data is sparse (have a lot of zeroes)

            3. DO NOT USE if magnitude (size) of your data matters more than the direction of data.
            4. DO NOT USE if you want to keep a lot of zeroes in your data since this function spreads values around.
            5. DO NOT USE if your features have a lot of outliers.

        Considerations
        ---------------
            1. This function does not affect the shape or direction of your data.

        Example
        --------
        >>>    Normalization(df).lmax_normalization()
        """
        l_max_normalization = {}

        for column in self.df[self.columns]:
            data = np.array(self.df[column])

            l_max_normalization[column] = data / (np.abs(data).max())

        l_max_df = pd.DataFrame(l_max_normalization)

        return l_max_df
