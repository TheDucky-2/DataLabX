import pandas as pd
from .Computation import Computation


class Outliers(Computation):
    
    def __init__(self, df:pd.DataFrame, columns:list=None):
        import pandas as pd
        import numpy as np

        '''
        Initializing the Outliers Computation

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

    def IQR_boundaries(self):

        from .Statistics import Statistics

        Quarter1 = Statistics(self.df).quantiles(0.25)
        median = Statistics(self.df).quantiles(0.50)
        Quarter3 = Statistics(self.df).quantiles(0.75)

        IQR = Quarter3 - Quarter1 

        lower_boundary = Quarter1 - (1.5 * IQR)
        upper_boundary = Quarter3 + (1.5 * IQR)

        return lower_boundary, upper_boundary








            