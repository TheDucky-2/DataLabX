"""Diagnoses the Numerical Data in your DataFrame"""

from ..utils.Logger import datalab_logger

from pathlib import Path
import pandas as pd

logger = datalab_logger(name = __name__.split('.')[-1])

class NumericalDiagnosis:
    """
    Initializing the Numerical Diagnosis.

    Parameters
    -----------

    df: pd.DataFrame
        A pandas dataframe you wish to diagnose.

    columns: list, optional
        A list of columns you wish to apply numerical diagnosis on, by default None.
    """

    def __init__(self, df: pd.DataFrame, columns:list = None):


        if not isinstance(df, pd.DataFrame):
            raise TypeError(f'df must be a pandas DataFrame, got {type(df).__name__}')

        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be a list of column names, got {type(columns).__name__}')

        self.df = df.select_dtypes(include='number')

        if columns is None:
            self.columns = self.df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns]

        logger.info('Numerical Diagnosis initialized.')
            
    def check_sparsity(self, value: int|float = 0) -> dict[str, float]:
        """
        Checks the ratio of occurrence of a specific number (usually 0).

        Parameters
        -----------
        value: int or float, optional
            An integer or a decimal number, by default 0.

        Returns
        --------
        dict[str, float]
            A dictionary of column names and percentage of occurrence of a particular number.
            
        Usage Recommendation
        --------------------
            1. Use this function only for Exploratory Data Analysis.  
            2. Mostly used to check how many values are 0 in a certain column. However, you can also use integers like 3 or floats like 5.888.
            3. This function is intended to help you get an overview of which column may and may not contribute meaningfully to the analysis or ML.

        Considerations
        --------------
            Pass numeric values after converting datatypes to int or float, instead of using strings.
            
        Example
        --------
        >>> NumericalCleaner(df).check_sparsity()
        >>> NumericalCleaner(df).check_sparsity(5)
        """
        sparsity_dict = {
            col: round(float((((self.df[col] == 0).sum())/len(self.df[col]))* 100), 2)
            for col in self.df[self.columns]}

        # Shows occurence of each value in percentage
        logger.info(f'Occurrence of {value} in each column of the dataframe (in %)')
        
        return sparsity_dict

    def detect_outliers(self, method: str ='IQR')-> dict[str, pd.Series]:
        """
        Detects outliers in one or multiple Numerical columns of the DataFrame.

        Parameters
        -----------
        method : str (default is 'IQR')
            Method using which you wish to detect outliers.

            Supports:
            
            - IQR
            - z-score

        Returns
        -------
        dict[str, pd.Series]
            A pandas Series of columns with outliers.
            
        Usage Recommendation
        --------------------
            1. Use this function when you want to check if there are any outliers in your data.
            2. Use this function only for Numerical data (numbers).

        Example
        -------- 
        >>> NumericalDiagnosis(df).detect_outliers()
        """
        from ..computations.Outliers import Outliers

        outliers_dict  = {}

        for col in self.df[self.columns]:
            
            if method == 'IQR':
                
                outliers_dict[col] = Outliers(self.df).iqr_outliers()[col].dropna()

            elif method == 'z_score':

                outliers_dict[col] = Outliers(self.df).zscore_outliers()[col].dropna()

        outliers_dict = {col: series for col, series in outliers_dict.items() if not series.empty}
            
        return outliers_dict

    def check_skewness(self)-> dict[str, float]:
        """
        Checks the skewness in each column of the DataFrame.

        Returns
        --------
        dict[str, float]

            A dictionary of all columns of the DataFrame with skewness values.
            
        Usage Recommendation
        ---------------------
            1. Use this function when you want to check how unevenly data is distributed around the mean (skewness).
            2. Use only for numerical columns.

        Example
        ------- 
        >>> Diagnosis(df).check_skewness()
        """
        from ..computations.Distribution import Distribution

        skewness = Distribution(self.df[self.columns]).skewness()

        skewness_dict = {col: (round(float(skewness[col].iloc[0]), 4) if pd.notna(skewness[col].iloc[0]) else None) for col in self.df[self.columns]}

        return skewness_dict

    def check_kurtosis(self, kurtosis_type='raw')-> dict[str, float]:
        """
        Checks the kurtosis value in each column of the DataFrame.

        Parameters
        ----------
        kurtosis_type : str, optional
            The type of kurtosis you would like to compute, default is 'raw'.

            Types supported:
            
            - 'raw'
            - 'excess'

        Returns
        --------
        dict[str, float]
            A dictionary of all columns of the DataFrame with skewness values.
            
        Usage Recommendation
        ---------------------
            1. Use this function when you want to check how unevenly data is distributed around the mean (skewness).
            2. Use only for numerical columns.

        Example
        ------- 
        >>> Diagnosis(df).check_skewness()
        """ 
        
        if not isinstance(kurtosis_type, str):
            raise TypeError(f'kurtosis type must be a string, got {type(kurtosis_type).__name__}')

        if kurtosis_type not in ['raw', 'excess']:
            raise ValueError("Available kurtosis types: 'raw' or 'excess'.")

        from ..computations import Distribution

        raw_kurtosis = Distribution(self.df[self.columns]).raw_kurtosis()
        excess_kurtosis = Distribution(self.df[self.columns]).excess_kurtosis()

        if kurtosis_type == 'raw':
            kurtosis_dict = {col: ((round(float(raw_kurtosis[col].iloc[0]), 4)) if pd.notna(raw_kurtosis[col].iloc[0]) else None) for col in self.df[self.columns]}

        if kurtosis_type == 'excess':
            kurtosis_dict = {col: ((round(float(excess_kurtosis[col].iloc[0]), 4)) if pd.notna(excess_kurtosis[col].iloc[0]) else None) for col in self.df[self.columns]}

        return kurtosis_dict

    def check_variance(self)-> dict[str, float]:
        """
        Checks if the variance of a column is 0.

        Returns
        --------
        dict[str, float]

            A dictionary of all columns of the DataFrame with their variance
            
        Usage Recommendation
        ---------------------
            1. Use this function when you want to check if all the values in a column are exactly the same.
            2. Use only for numerical columns.

        Example
        ------- 
        >>> Diagnosis(df).check_variance()
        """
        from ..computations.Statistics import Statistics
        
        variance_dict = {}

        for col in self.df[self.columns]:

            variance = Statistics(self.df).variance()[col]

            if (variance == 0):
                variance_dict[col] = variance
            else:
                variance_dict[col] = round(float(variance), 3)

        return variance_dict

    def check_distribution(self, skewness_threshold:int|float=1, kurtosis_threshold: int|float=2)-> dict[str, str]:
        """
        Classifies whether the distribution of data is normal or non-normal, based on skewness and kurtosis values.

        Parameters
        ----------
        skewness_threshold : int or float, optional
            Threshold of skewnes values above which distribution would be considered Non-Normal, default is |1|.

        kurtosis_threshold : int or float, optional
            Threshold of kurtosis values above which distribution would be considered Non-Normal, default is |2|.

        Returns
        --------
        dict[str, str]
            A dictionary of all columns with their classification as Normal or Non-Normal Distribution.
            
        Usage Recommendation
        ---------------------
            1. Use this function when you want to check which columns follow a Normal-Distribution and which ones follow a Non-Normal Distribution.
            2. Use this function explicitly for EDA (Exploratory Data Analysis).
            2. Use only for numerical columns.

        Example
        ------- 
        >>> NumericalDiagnosis(df).check_distribution()
        """ 

        import numpy as np

        if not isinstance(skewness_threshold, (int, float)):
            raise TypeError(f'skewness threshold must be an int or float, got {type(skewness_threshold).__name__}')

        if not isinstance(kurtosis_threshold, (int, float)):
            raise TypeError(f'skewness threshold must be an int or float, got {type(skewness_threshold).__name__}')

        from ..computations.Distribution import Distribution

        distribution_dict = {}
        
        skewness = Distribution(self.df[self.columns]).skewness().abs()
        kurtosis = Distribution(self.df[self.columns]).excess_kurtosis().abs()

        distribution_mask = ((skewness > skewness_threshold) & (kurtosis > kurtosis_threshold)).fillna(False)

        distribution_dict = pd.Series(np.where(distribution_mask.iloc[0], "Non-Normal Distribution", 'Normal Distribution'), index = skewness.columns).to_dict()

        return distribution_dict

