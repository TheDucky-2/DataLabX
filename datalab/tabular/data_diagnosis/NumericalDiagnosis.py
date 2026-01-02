from .Diagnosis import Diagnosis
from ..computations import Distribution

from pathlib import Path

import pandas as pd

def convert_numpy_scalars_to_python(number)-> dict[str, dict]:
    import numpy as np

    if isinstance(number, np.integer):
        return int(number)
    
    elif isinstance(number, np.floating):
        return float(number)
    
    else:
        return number

class NumericalDiagnosis(Diagnosis):

    def __init__(self, df: pd.DataFrame, columns:list = None):

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
            
    def check_sparsity(self, value: int|float = 0) -> pd.Series:
        '''
        Checks the ratio of a specific number (usually 0) present in the selected column of the DataFrame

        Parameters:
        -----------
            df: pd.DataFrame
                A pandas DataFrame

            value: int or float
                An integer or a decimal number

        Returns:
            pd.Series
                A pandas Series of the columns passed in, along with the ratio that value appears in the Dataframe. 
            
        Usage Recommendation:
            1. Use this function only for Exploratory Data Analysis.  
            2. Mostly used to check how many values are 0 in a certain column. However, you can also use integers like 3 or floats like 5.888
            3. This function is intended to help you get an overview of which column may and may not contribute meaningfully to the analysis or ML.

        Considerations:
            Pass numeric values after converting datatypes to int or float, instead of using strings.
            
        >>> Example: 
                    Input : NumericalCleaner(df).check_sparsity()
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

        # getting the ratio of value present in the column
        sparsity = self.df[self.columns].apply(lambda column: ((column == value).sum()/len(column))*100)

        # Shows occurence of each value in percent
        print(f'\nOccurrence of {value} in each column of the dataframe (in %)')
        
        return sparsity

    def detect_outliers(self, method: str ='IQR')-> dict[str, pd.Series]:

        '''
        Detects outliers in each Numerical column of the DataFrame

        Parameters:
        -----------
            self

            Optional:

                method : str (default is 'IQR')

                    Method using which you wish to detecting outliers. Supports:
                    
                    - IQR
                    - z-score
        Returns:
            pd.Series
            A pandas Series of columns with outliers
            
        Usage Recommendation:
            1. Use this function when you want to check if there are any outliers in your data.
            2. Use this function only for Numerical data (numbers).

        >>> Example: 
                NumericalDiagnosis(df).detect_outliers()
            
        '''
        outliers_dict  = {}

        for col in self.df[self.columns]:
            
            if method == 'IQR':
                
                # the 1st quartile 
                q1 = self.df[col].quantile(0.25)

                # the 3rd quartile
                q3 = self.df[col].quantile(0.75)

                # the remaining 50% of data in the middle
                IQR = q3 - q1

                # we are subtracting 1.5 times of 50% of data from the 25% quantile, which means values would be very high in negative
                lower_bound = q1 - (1.5 * IQR)

                # we are add 1.5 times of 50% of data to the 75% quantile, which means values would be very high in positive
                upper_bound = q3 + (1.5 * IQR)

                # getting outliers that are numbers which are either lower than lower boundary or higher than higher boundary
                outliers_dict[col] = self.df[((self.df[col]) < lower_bound) | ((self.df[col]) > upper_bound)][col]

            elif method == 'z-score':
                mean = self.df[col].mean()
                std = self.df[col].std()

                z_score = np.abs((self.df[col] - mean)/std)
                
                # getting outliers which have a z-score of more than 3 
                outliers = (self.df[col][z_score>3])

                outliers_dict[col] = outliers

        # getting only the columns where outliers actually exist
        outliers_dict = {col: df for col, df in outliers_dict.items() if not df.empty}
        print("\nUses IQR method by default. If you want to detect outliers using z-score, use method = 'z-score'")
            
        return outliers_dict
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
        
                    The absolute value for skewness(|skewness|) below which the data distribution is considered to be a Normal Distribution.
                    
                kurtosis_threshold: int or float( default is 2)

                    The absolute value for kurtosis(|kurtosis|) below which the data distribution is considered to be a Normal Distribution.

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
        import numpy as np
        
        # getting Skewness from numerical diagnosis class and kurtosis calculation from Distribution class
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

    def show_minmax(self):
        '''
        Show minimum and maximum values prexentt in each Numerical column of the DataFrame

        Parameters:
        -----------
            self

        Returns:
        --------
            A dictionary of column names and min-max values present in that column

        Example:
        --------

        >>> NumericalDiagnosis(df).show_min_max()
        '''
        range_dict = {}
    
        for column in self.df[self.columns]:
            min = self.df[column].min()
            max = self.df[column].max()
            
            # applying the method to convert numpy scalars into python numbers.
            range_dict[column] = {
                'min': convert_numpy_scalars_to_python(min),
                'max': convert_numpy_scalars_to_python(max)
            }

        return range_dict

   