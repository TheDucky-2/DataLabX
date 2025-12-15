from ..data_loader import load_tabular
from ..computations import Statistics
from ..utils import ProjectHelpers

from pathlib import Path
import pandas as pd
import numpy as np

class MissingnessDiagnosis:

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

        # making sure that the passed df is a pandas DataFrame
        if isinstance(df, pd.DataFrame):
            df = df.copy()     # using a copy to avoid modifying original df

        elif isinstance(df, (str, Path)):
            df = load_tabular(df)     # reading if a file  

        else:
            raise TypeError(f'df must be a pandas DataFrame or a file path, got {type(df).__name__}')

        if columns is None:
            columns = df.columns.to_list()
        # ensuring that the columns passed are in a list
        elif not isinstance(columns, list):
            raise TypeError(f'columns must be a list of column names, got {type(self.columns).__name__}')

        self.df = df
        self.columns = [column for column in columns if column in df.columns]


    def show_missing_types(self, extra_placeholders: list=None)-> dict[str, list[object]]:

        '''
        Show missing types (NA or null values) present in each column, irrespective of column type (Categorical, Numerical or Datetime)

        Parameters:
        -----------
        extra_placeholders  : list 
            A list of extra placeholders you wish to pass as NA or null values
        
        Return:
            dict
            missing_per_column    : a dictionary of key, value pairs of column names and null values that match the placeholders
        
        Recommendation:
            Use this function when you want to see what missing values are present in each column type: Categorical, Numerical or Datetime

        Example: 
        
        >>>>> show_missing_types(df) -> {'Location': ['UNKNOWN', nan, 'ERROR'], 'Quantity': [np.float64(nan)], 'Transaction ID': []}
        
        >>>>> show_missing_types(categorical) -> {'Transaction ID': [], 'Item': ['UNKNOWN', nan, 'ERROR'],'Payment Method': ['UNKNOWN', 'ERROR', nan],'Location': ['UNKNOWN', nan, 'ERROR']}

        >>>>> show_missing_types(numerical) -> {'Quantity': [np.float64(nan)], 'Price Per Unit': [np.float64(nan)], 'Total Spent': [np.float64(nan)]}

        >>>>> show_missing_types(datetime) -> {'Transaction Date': []}

        '''
        # creating a copy of original df
        
        self.extra_placeholders = extra_placeholders

        # if a dataframe is not passed
        if not isinstance(self.df, pd.DataFrame):
            raise TypeError(f'df must be a pandas dataframe, got {type(self.df).__name__}')

        # if a list of extra_placeholders is passed
        if extra_placeholders is not None:
            
            # if extra_placeholders is not a list
            if not isinstance(self.extra_placeholders, list):
                raise TypeError(f'extra_placeholders must either be a list of placeholders or None, got {type(self.extra_placeholders).__name__}')

            # for every element passed in extra_placeholders, it should be among (str, float, int, type(None)
            if not all(isinstance(placeholder, (str, float, int, type(None))) for placeholder in self.extra_placeholders):
                raise TypeError(f'All elements passed in extra_placeholders must be str, int, float or None type, got: {type(extra_placeholders).__name__}')


        # a list of default common placeholders used in categorical columns
        DEFAULT_PLACEHOLDERS= ['NA', np.nan, 'NAN', 'na', 'NaN', 'nan', 'ERROR', 'MISSING', 'Error', 'Missing', 'Not Available', None, 'not available', 'UNKNOWN', 'Unknown']
        
        # an empty dictionary to store key, value pairs of column names as keys, and list of missing values as values
        missing_per_column = {}   

        # just creating a copy of placeholders to avoid changing original placeholders
        placeholders = DEFAULT_PLACEHOLDERS.copy()  
        
        # if user passes a list of placeholders
        if self.extra_placeholders is not None:                          
            placeholders.extend(self.extra_placeholders)       # add more place_holders to the list

        for column in self.df[self.columns]:                            
            # creating a boolean mask values in columns that match values in the placeholders
            bool_mask = self.df[column].isin(placeholders)              

            # getting unique values of missing values that matched to placeholders in each column 
            found_missing_values = self.df.loc[bool_mask, column].unique() 
            
            missing_per_column[f'{column}'] = list(found_missing_values)       

        return missing_per_column

    def  show_missing_stats(self, how: str = 'percent') -> pd.Series:

        '''
        Shows total missing values (NA or null values) present in each column, irrespective of column type (Categorical, Numerical or Datetime)

        Parameters:
        -----------
        how : str (default is 'percent')

            How you would like to show the total of missing values.
                - 'sum'    : Shows the sum of missing values per column
                - 'percent': Shows the percentage of missing values per column
        
        Return:
        -------
        pd.Series
            A pandas Series of total missing values per column
        
        Usage Recommendation:
        ---------------------
            Use this function when you want to see the sum or percentage of missing values before deciding whether to drop or fill missing values
        
        '''
        self.how = how

        if self.how == 'sum':
            print(f'\nSum of missing data in each column')
            return self.df.isnull().sum()

        elif self.how == 'percent':
            print(f'\nPercentage of missing data in each column')
            return (self.df.isnull().sum()/len(self.df))*100

        elif self.how not in ['sum', 'percent']:
            raise ValueError(f"how must either be 'sum' or 'percent', got {self.how}")

    def any_missing_rows(self) -> pd.DataFrame:
        '''
        Detects and shows all the rows where any row is missing data in a DataFrame

        Parameters:
        -----------
            self: pd.DataFrame
        
        Return:
        -------
            pd.DataFrame
            A pandas DataFrame of all rows where any column is missing value.

        '''

        return self.df[self.df.isna().any(axis=1)]

    def all_rows_missing(self) -> pd.DataFrame:

        '''
        Detects and shows all the rows that are missing data together in a DataFrame

        Parameters:
        -----------
            self: pd.DataFrame
        
        Return:
        -------
            pd.DataFrame
            A pandas dataframe of all rows where data is missing together. 

        Example:
        --------

            
        '''
        return self.df[self.df.isna().all(axis=1)]
        

    def rows_missing_specific_columns(self) -> dict :

        '''
        Detects and shows all rows where values are missing in a specific column of the DataFrame
        '''
        rows_with_columns_missing_values = {col: self.df[self.df[col].isna()] for col in self.df.columns}

        return rows_with_columns_missing_values

    def any_missing_index(self):
        '''
        Provides the index of rows where any value may be missing in a column of the DataFrame.
        
        '''
        missing_index = self.df[self.df.isna().any(axis=1)].index.to_list()
        
        return missing_index

    def column_missing_index(self) -> dict :
    
        rows_missing_specific_columns = MissingnessDiagnosis(self.df).rows_missing_specific_columns()

        missing_index = {}

        for column, missing_rows in rows_missing_specific_columns.items():

            missing_index[column] = missing_rows.index.to_list()

        return missing_index