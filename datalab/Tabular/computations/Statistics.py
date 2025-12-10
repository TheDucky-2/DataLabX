from .Computation import Computation

import pandas as pd
import numpy as np


class Statistics(Computation):
    
    def __init__(self, df:pd.DataFrame, columns:list=None):
        import pandas as pd
        import numpy as np

        '''
        Initializing the Statistics Computation

        Parameters:
        -----------
        df: pd.DataFrame
            A pandas dataframe you wish to diagnose

        columns: list
            A list of columns you wish to apply numerical cleaning on
        '''

        super().__init__(df, columns)

        self.df = df.copy()
        self.columns = [column for column in self.columns if column in self.df.columns]
    
    def max(self):

        return self.df.max()

    def min(self):
    
        return self.df.min()

    def Range(self):

        Range= Statistics(self.df).max() - Statistics(self.df).min()

        return Range

    def mean(self) -> pd.Series:
        '''
        Computes the mean (Average) for each column of the DataFrame passed.

        Return:
            pd.Series
            A pandas Series of mean values for each column
    
        Usage Recommendation:
            Use this function when you want to find the average value of each column

        Considerations:
            This function keeps null values and np.nan, but converts them to <NA> (Int64Dtype)

        >>> Example: 
                Statistics(df).mean()
                ->
                age                     48.998814
                income               76426.897317
                expenses             47351.295358
                savings              24495.968469
                loan_amount          11340.452913
                credit_score           699.995727
                num_of_dependents        2.500065
                years_at_job            20.013299
                risk_score               0.128864
                dtype: Float64

        '''
        return self.df[self.columns].mean()
    
    def median(self):

        return self.df[self.columns].median()

    def standard_deviation(self):

        return self.df[self.columns].std()

    def quantiles(self, q:float, groupby:str = None, **kwargs)->pd.DataFrame:
        
        if groupby:
            grouped_df = self.df.groupby(groupby)
            return grouped_df.quantile(q=q, **kwargs)

        else:
            return self.df.quantile(q=q, **kwargs)

            
    def IQR(self):
        '''
        Computes the mean (Average) for each column of the DataFrame passed.

        Return:
            pd.Series
            A pandas Series of mean values for each column
    
        Usage Recommendation:
            Use this function when you want to find the average value of each column

        Considerations:
            This function keeps null values and np.nan, but converts them to <NA> (Int64Dtype)

        >>> Example: 
                Statistics(df).mean()
                ->
                age                     48.998814
                income               76426.897317
                expenses             47351.295358
                savings              24495.968469
                loan_amount          11340.452913
                credit_score           699.995727
                num_of_dependents        2.500065
                years_at_job            20.013299
                risk_score               0.128864
                dtype: Float64

        '''
        Q1 = Statistics(self.df).quantiles(0.25)
        Q3 = Statistics(self.df).quantiles(0.75)

        IQR = Q3 - Q1 

        return IQR

    def variance(self, method='sample'):
            
        if method == 'sample':

            sample_variance_dict={}

            n = len(self.df) # n is size of population

            for column in self.df[self.columns]:
                
                sample_variance_dict[column] = ((self.df[column] - self.df[column].mean()) ** 2).sum()/(n-1) # (n-1) for Sample

            return sample_variance_dict

        elif method == 'population':

            population_variance_dict={}

            n = len(self.df) # n is size of population

            for column in self.df[self.columns]:
                
                population_variance_dict[column] = ((self.df[column] - self.df[column].mean()) ** 2).sum()/(n) # (n) for Population

            return population_variance_dict

    def MAD(self) -> int|float:
    
        # Since MAD is Median Absolute Deviation, we calculate MAD as 'median of(x - median of x)'
        MAD_dict = {}

        for column in self.df[self.columns]:
            
            MAD_dict[column] = np.median(self.df[column] - np.median(self.df[column]))

        return MAD_dict

    def scaled_MAD(self):
        import numpy as np

        MAD_values = np.array(list(Statistics(self.df).MAD().values()))
        
        scaled_MAD = 1.4826 * MAD_values
        
        return scaled_MAD

    def z_score(self) -> pd.DataFrame:
        '''
        Computes the z-score statistic in each column of the DataFrame.

        Formula :
            z_score = (data - data.mean())/ data.standard_deviation()

        Return:
            pd.Series
            A pandas DataFrame of z-scores

        Considerations:
            This function 

        >>> Example: 
                Statistics(df).z_score()
                ->
                age	       income	  expenses	 savings    loan_amount  credit_score num_of_dependents	years_at_job  risk_score
            0	0.407928	0.014422	0.215059	0.310909	0.922220	0.575553	1.588035	0.17694	    0.072122
            1	1.165394	0.134350	0.393634	0.228567	0.436231	0.825689	0.27316	    1.781166	0.039981
            2	0.174738	0.290930	0.512151	0.030971	0.301431	0.070949	0.347238	0.624103	0.889512
            3	0.000062	0.275514	0.565031	0.261314	0.697162	1.582880	1.513957	1.425147	0.176865
            4	0.640994	0.980286	1.844369	0.984926	2.311555	0.029477	1.588035	1.781166	0.983226

        '''
        import numpy as np
        
        z_scores = {}

        for column in self.df[self.columns]:

            mean = self.df[column].mean()

            std_dev = self.df[column].std()
            
            z_scores[column] = np.abs((self.df[column] - self.df[column].mean())/self.df[column].std())
            
        # creating a dataframe from the dictionary of z_scores
        z_scores = pd.DataFrame(z_scores)
            
        return z_scores

    