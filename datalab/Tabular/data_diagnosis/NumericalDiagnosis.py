from .Diagnosis import Diagnosis
from ..computations import Distribution

from pathlib import Path

import pandas as pd
import numpy as np

class NumericalDiagnosis(Diagnosis):

    def __init__(self, df: pd.DataFrame, columns:list = None):
        import pandas as pd
        import numpy as np

        '''
        Initializing the Diagnosis

        Parameters:
        -----------
        df: pd.DataFrame
            A pandas dataframe you wish to diagnose

        columns: list
            A list of columns you wish to apply numerical cleaning on
        '''
        super().__init__(df, columns)

        self.df = df.select_dtypes(include='number')

        if columns is not None:

            self.columns = [column for column in columns if column in df.columns]

        else:
            self.columns = self.df.columns
            
    def check_sparsity(self, value: int|float) -> pd.Series:
        '''
        Checks the ratio of a specific number (usually 0) present in the selected column of the DataFrame

        Parameters:
            df   :       pd.DataFrame, a pandas DataFrame
            value:       int or float , an integer or a decimal number

        Returns:
            pd.Series
            A pandas Series of the columns passed in, along with the ratio of the value. 
            
        Usage Recommendation:
            1. Use this function only for Exploratory Data Analysis.  
            2. Mostly used to check how many values are 0 in a certain column. However, you can also use integers like 3 or floats like 5.888
            3. This function is intended to help you get an overview of which column may and may not contribute meaningfully to the analysis or ML.

        Considerations:
            Pass numeric values after converting datatypes to int or float, instead of using strings.
            

        >>> Example: 
                    Input : NumericalCleaner(df).check_sparsity(0)
                    Output: age                  0.000000
                            income               0.000000
                            expenses             0.000000
                            savings              0.000000
                            loan_amount          0.000000
                            credit_score         0.000000
                            num_of_dependents    0.147308
                            years_at_job         0.021907
                            risk_score           0.335651           <- 33.5% values in column 'risk_score' are 0 (or 0.00).
                            dtype: float64
        '''

        self.value = value

        # getting the ratio of value present in the column
        sparsity = self.df[self.columns].apply(lambda column: ((column == self.value).sum()/len(column))*100)

        print(f'\nOccurrence of {self.value} in each column of the dataframe (in %)')
        
        return sparsity

    def detect_outliers(self, method='IQR'):
        
        print("\nUses IQR method by default. If you want to detect outliers using z-score, pass the parameter 'z-score'")
        
        self.method = method

        if self.method == 'IQR':

            outliers = {}

            for column in self.df.columns:

                Q1 = self.df[column].quantile(0.25)
                Q3 = self.df[column].quantile(0.75)

                # Inter Quartile Range
                IQR = Q3 - Q1 

                lower_bound = Q1 - (1.5 * IQR)
                upper_bound = Q3 + (1.5 * IQR)

                outliers[column] = self.df[(self.df[column] < lower_bound) | (self.df[column] > upper_bound)]

        elif self.method == 'z-score':

            outliers = {}

            for column in self.df.columns:
                mean = self.df[column].mean()
                std_dev = self.df[column].std()

                z_scores = np.abs((self.df[column] - self.df[column].mean())/self.df[column].std())

                outliers_per_column = self.df[column][z_scores > 3].to_list()
                outliers[column] = outliers_per_column
                
        return outliers

    def check_skewness(self)-> pd.Series:
        '''
        Checks the skewness in each column of the DataFrame

            Returns:
                pd.Series
                A pandas Series of all columns of the DataFrame with skewness values.
                
            Usage Recommendation:
                1. Use this function when you want to check how unevenly data is distributed around the mean (skewness).
                2. Use only for numerical columns
    
            >>> Example: 
                    Diagnosis(df).check_skewness()
        
        '''
        
        return self.df.skew()

    def check_zero_variance(self):
            
        if Statistics(self.df).variance() == 0:
            return f'These columns have zero variance: {column}'
        
        elif Statistics(self.df).variance() != 0:
            return f'No columns have zero variance'
    
    def check_distribution(self, skewness_threshold: int|float=1,kurtosis_threshold: int|float=2)-> pd.Series :
        '''
        Checks whether the distribution of data is Normal or Non-Normal, for each column of DataFrame

        Parameters:
        
            Optional:

                skewness_threshold: int or float (default is 1)
        
                    The absolute value for skewness |skewness| below which the data distribution is considered to be a Normal Distribution.
                    
                kurtosis_threshold: int or float( default is 2)

                    The absolute value for kurtosis |kurtosis| below which the data distribution is considered to be a Normal Distribution.

        Returns:
            pd.Series
            A pandas Series of column names and their classification as 'Normal' vs 'Non-Normal'. 
            
        Usage Recommendation:
            1. Use this function only for Exploratory Data Analysis.  
            2. Use this function before exploring strategies for handling missing data and data preprocessing.
            
        >>> Example: 

                Diagnosis(df).check_distribution()
                
                    age                      Normal Distribution
                    income               Non-Normal Distribution
                    expenses             Non-Normal Distribution
                    savings              Non-Normal Distribution
                    loan_amount          Non-Normal Distribution
                    credit_score             Normal Distribution
                    num_of_dependents        Normal Distribution
                    years_at_job             Normal Distribution
                    risk_score               Normal Distribution
                    dtype: object
        '''
        skewness = NumericalDiagnosis(self.df).check_skewness()
        kurtosis = Distribution(self.df).excess_kurtosis()

        distributions = {}

        for column in self.df[self.columns]:
        
            if np.abs(skewness[column]) < skewness_threshold and np.abs(kurtosis[column]) < kurtosis_threshold:
                distributions[column] = 'Normal Distribution'

            else:
                distributions[column] = 'Non-Normal Distribution'
            
        distributions= pd.Series(distributions)

        return distributions