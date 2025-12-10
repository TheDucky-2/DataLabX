import pandas as pd
from .Computation import Computation

class Correlation(Computation):

    def __init__(self, df:pd.DataFrame, columns:list=None):

        '''
        Initializing the Statistics Computation

        Parameters:
        -----------
        df: pd.DataFrame
            A pandas dataframe you wish to diagnose

        columns: list
            A list of columns you wish to apply numerical cleaning on
        '''

        import pandas as pd

        super().__init__(df, columns)

        self.df = df.copy()
        self.columns = [column for column in self.columns if column in self.df.columns]

    def covariance(self):
        
        n = len(self.df)
        centered_df = self.df - self.df.mean()

        covar_matrix = (centered_df.T @ centered_df) / (n-1)

        return covar_matrix
        
    def pearson_corr(self):

        return self.df.corr()
