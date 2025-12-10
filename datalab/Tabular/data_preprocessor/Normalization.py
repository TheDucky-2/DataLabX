import pandas as pd
import numpy as np
from .DataPreprocessor import DataPreprocessor

'''
Normalization:
--------------

Normalizing your data means rescaling numerical values to a defined, smaller range — 
typically [0, 1] or sometimes [-1, 1].

This ensures that all features contribute equally to model training and prevents features with large numeric ranges from dominating.
Like a feature with range between [1, 100] would not be dominated in model training by a feature with range between [-infinity, infinity]

Normalization is applied separately to each feature (numerical column) of the dataframe.

Example:

    data = [10, 20, 30, 60, 100]

    Suppose we want to normalize all values between 0 and 1. 

    One simple approach is to divide each value by the maximum value (100 in this case):

        [10, 20, 30, 60, 100] / 100 = [0.1, 0.2, 0.3, 0.6, 1.0]

    Now the data has been normalized within range [0, 1].

Note:
    - This simple dividing-by-maximum method works when the data is strictly positive.
      It does not work for data with neagtive values.

    - A more general approach is Min-Max normalization, using the formula:

        For each feature X,

        X' = (each value of X - minimum value of X) / (maximum value of X - mimumum value of X)

        or simply, 

        X' = (X - min) / (max - min)

      Min-Max normalization can handle data with arbitrary minimum and maximum values.
'''

class Normalization(DataPreprocessor):

    def __init__(self, df: pd.DataFrame, columns: list = None):
        super().__init__(df, columns)
        '''
        Initializing Normalization

        Parameters:
        -----------
        df: pd.DataFrame
            A pandas dataframe you wish to normalize

        columns: list
            A list of numerical columns you want to apply normalization on
        '''
        self.df = self.df.select_dtypes(include='number')
        
        if columns is None:
            self.columns = self.df.columns
        else:
            self.columns = [column for column in columns if column in self.df.columns]

    def MaxNormalization(self) -> pd.DataFrame:
        '''
        Normalizes your data by dividing each value with the maximum value of that column for each column of the DataFrame

        Formula:
                    X
            X' =  -----
                   max

        Return:
            pd.DataFrame
            A pandas DataFrame of normalized values 
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you do not have negative values in your data.
            2. Use this function when your models are sensitive to feature scaling. 
               Examples: KNN, Neural Networks, k-means, DBSCAN, or Gradient based (Adam, SGD)

            3. DO NOT USE this function if your maximum value is an outlier. It will distort scaling.

        Considerations:
            1. This function scales your data by squeezing it between 0 and 1 without changing the shape of your data.
            2. It does not mean that the mean of your data will be 0, or 1 standard deviation away from the mean.
            3. For making your data zero-centered (mean = 0, std=1), use Standardization()

        Example: 
            Normalization(df).MaxNormalization()
        '''
        normalized_data = {}

        for column in self.df[self.columns]:
            
            data = np.array(self.df[column]) 

            maximum_absolute_value = np.abs(data.max())

            normalized_data[column] = (data/maximum_absolute_value)
            
            normalized_df = pd.DataFrame(normalized_data) 

        return normalized_df
        
    def MinMaxNormalization(self) -> pd.DataFrame:
        '''
        Normalizes your data to a range [0, 1] based on the minimum and maximum values of each column of the DataFrame.

        Formula:
                  (X - min)
            X' =  ---------  
                 (max - min)

        Return:
            pd.DataFrame
            A pandas DataFrame of normalized values 
        
        Usage Recommendation:
        ---------------------
            1. Use this function when your models are sensitive to feature scaling. 
               Examples: KNN, Neural Networks, k-means, DBSCAN, or Gradient based (Adam, SGD)

            2. DO NOT USE this function if your maximum value is an outlier. It will distort scaling.

        Considerations:
            1. This function scales your data by squeezing it between 0 and 1 without changing the shape of your data.
            2. It does not mean that the mean of your data will be 0, or 1 standard deviation away from the mean.
            3. For making your data zero-centered (mean = 0, std=1), use Standardization()

        Example: 
            Normalization(df).MinMaxNormalization()
            
        '''

        minmax_normalized_data ={}

        for column in self.df[self.columns]:
            
            data = np.array(self.df[column])

            minmax_normalized_data[column] = (data - data.min()) / (data.max() - data.min())

        minmax_normalized_df = pd.DataFrame(minmax_normalized_data)
            
        return minmax_normalized_df

    def FeatureRangeNormalization(self, range:tuple = (0, 1)) -> pd.DataFrame:
        '''
        Normalizes your data to a specified range based on the minimum and maximum values of each column of the DataFrame.

        Formula:
                   (X - min)
            X' =  ----------- 
                  (max - min)

        Parameters:

            range: tuple
            A tuple of minimum and maximum value you wish to scale your data between

        Return:
            pd.DataFrame
            A pandas DataFrame of normalized values 
        
        Usage Recommendation:
        ---------------------
            1. Use this function when your models are sensitive to feature scaling. 
               Examples: KNN, Neural Networks, k-means, DBSCAN, or Gradient based (Adam, SGD)

            2. DO NOT USE this function if your maximum value is an outlier. It will distort scaling.

        Considerations:
            1. This function scales your data by squeezing it between 0 and 1 without changing the shape of your data.
            2. It does not mean that the mean of your data will be 0, or 1 standard deviation away from the mean.
            3. For making your data zero-centered (mean = 0, std=1), use Standardization()

        Example: 
            Normalization(df).FeatureRangeNormalization()
        '''
        minmax_normalized_data = Normalization(self.df).MinMaxNormalization()

        r_min, r_max = range

        featurerange_normalized_df = minmax_normalized_data * (r_max - r_min) + r_min

        return featurerange_normalized_df

    def MeanNormalization(self) -> pd.DataFrame:
        '''
        Normalizes your data by subtracting the mean and dividing by the range (max-min) of each feature (column) of the dataframe
        
        Formula:

                  (X - mean)
            X' =  ----------
                  (max - min)

        Return:
            pd.DataFrame
            A pandas DataFrame of normalized values 
        
        Usage Recommendation:
        ---------------------
            1. Use this function when your models are sensitive to feature scaling. 
               Examples: KNN, Neural Networks, k-means, DBSCAN, or Gradient based (Adam, SGD)

            2. DO NOT USE this function if your maximum value is an outlier. It will distort scaling.

        Considerations:
            1. This function scales your data within a limited range, usually [-1, 1]
            2. It also centers your data around 0 (the mean). 
            3. If you want unit variance, use z_score standardization

        Example: 
            Normalization(df).MeanNormalization()

        '''
        normalized_data ={}

        for column in self.df[self.columns]:
            
            data = np.array(self.df[column])

            data_mean = data.mean()

            normalized_data[column] = (data - data_mean) / (data.max() - data.min())

        return pd.DataFrame(normalized_data)

    def L1Normalization(self) -> pd.DataFrame:
        '''
        Normalizes your data by dividing each value with the sum of absolute values for each column of the DataFrame.

        Formula:
                      X
            X' =  --------- 
                    ∑| X |

        Return:
            pd.DataFrame
            A pandas DataFrame of L1 normalized values 
        
        Usage Recommendation:
        ---------------------
            1. Use this function when ratio (proportions) of values matter more than than the size (magnitude) of value.
            2. Use this function if your data is sparse (have a lot of zeroes)

            3. DO NOT USE this function if your data is negative since L1 Normalization uses absolute values.

        Considerations:
            1. This function scales your data to proportions that sum up to a value of 1
            2. It does not affect the shape of your data. 

        Example: 
            Normalization(df).L1Normalization()

        '''
        l1_norm = {}

        for column in self.df[self.columns]:
            data = np.array(self.df[column])

            l1_norm[column] = data / np.abs(data.sum())

        l1_df = pd.DataFrame(l1_norm)

        return l1_df

    def L2Normalization(self) -> pd.DataFrame:
        '''
        Normalizes your data by dividing each value with the square root of the sum of squared values for each column of the DataFrame.

        Formula:
                             X
            X' =     ------------------
                    square root of (∑ (X^2))

        Return:
            pd.DataFrame
            A pandas DataFrame of L2 normalized values 
        
        Usage Recommendation:
        ---------------------
            1. Use this function when direction (pattern) or shape of data matter more than how big the numbers are.
            2. Use this function if your data is sparse (have a lot of zeroes)

            3. DO NOT USE if magnitude (size) of your data matters more than the direction of data.
            4. DO NOT USE if you want to keep a lot of zeroes in your data since this function spreads values around.
            5. DO NOT USE if your features have a lot of outliers.

        Considerations:
            1. This function does not affect the shape or direction of your data. 

        Example: 
            Normalization(df).L2Normalization()

        '''
        l2_norm = {}

        for column in self.df[self.columns]:
            data = np.array(self.df[column])

            l2_norm[column] = data / (np.sqrt(((data)**2).sum()))

        l2_df = pd.DataFrame(l2_norm)

        return l2_df

    def LMaxNormalization(self) -> pd.DataFrame:
        '''
        Normalizes your data by dividing each value with the maximum absolute value for each column of the DataFrame

        Formula:
                        X
            X' =    ----------
                    max(| X |)

        Return:
            pd.DataFrame
            A pandas DataFrame of LMax normalized values 
        
        Usage Recommendation:
        ---------------------
            1. Use this function when direction (pattern) or shape of data matter more than how big the numbers are.
            2. Use this function if your data is sparse (have a lot of zeroes)

            3. DO NOT USE if magnitude (size) of your data matters more than the direction of data.
            4. DO NOT USE if you want to keep a lot of zeroes in your data since this function spreads values around.
            5. DO NOT USE if your features have a lot of outliers.

        Considerations:
            1. This function does not affect the shape or direction of your data. 

        Example: 
            Normalization(df).LMaxNormalization()

        '''
        
        l_max_normalization = {}

        for column in self.df[self.columns]:
            data = np.array(self.df[column])

            l_max_normalization[column] = data / (np.abs(data).max())

        l_max_df = pd.DataFrame(l_max_normalization)

        return l_max_df
        