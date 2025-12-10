import pandas as pd
from .DataPreprocessor import DataPreprocessor
from ..computations import Outliers

class Standardization(DataPreprocessor):

    def __init__(self, df: pd.DataFrame, columns: list = None):
        super().__init__(df, columns)
        '''
        Initializing Standardization

        Parameters:
        -----------
        df: pd.DataFrame
            A pandas dataframe you wish to standardize

        columns: list
            A list of numerical columns you want to apply standardization on
        '''
        self.df = self.df.select_dtypes(include='number')
        
        if columns is None:
            self.columns = self.df.columns
        else:
            self.columns = [column for column in columns if column in self.df.columns]

    def Z_scoreStandardization(self) -> pd.DataFrame:

        '''
        Also known as StandardScaler()
        '''

        z_scores = Outliers(self.df).z_score()

        standardized_data = self.df / z_scores

        return standardized_data

    def RobustStandardization(self) -> pd.DataFrame:

        from ..computations import Statistics

        standardized_data = self.df - self.df.median()/ Statistics(self.df).IQR()

        return standardized_data


    def UnitVariance(self) -> pd.DataFrame:

        from ..computations import Statistics

        standardized_data = self.df / Statistics(df).std_dev()

        return standardized_data

    def MeanCentering(self):

        mean_centered_data = self.df - self.df.mean()

        return mean_centered_data


