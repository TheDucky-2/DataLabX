from ..data_loader import load_tabular
from ..computations import Statistics

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
        self.columns = [column for column in columns if column in self.df.columns]


    def detect_numerical_missing_types(self, extra_placeholders: list | None = None)-> dict[str, dict[str, list]]:
        '''
        Detects the types of missing values in Numerical (numbers) columns of the DataFrame.

        Parameters:
        -----------

            self: pd.DataFrame
                A pandas DataFrame of Numerical columns

            Optional:

                extra_placeholders: list or type None (default is None)
                    A list of extra placeholders you wish to pass as missing values depending on your domain
            
        Returns:
        --------
            dict
                A dictionary of numerical columns and the types of missing values in a Numerical DataFrame.
            
        Usage Recommendation:
        ---------------------
                Use this function when you want to detect what kind of missing data exists in your numbers.

        Considerations:
        ---------------

            1. This function returns two categories of numerical missing data types: 

                a. Pandas Missing Types (NAN) -> Pandas converts anything that is not a number to NAN (Not a Number).
                b. Domain Dependent Missing Types-> These are the types your domain considers as missing data (Example: -1, 0 (in age where info is missing for a person))

        Example: 
        --------
                    MissingnessDiagnosis(df).detect_numerical_missing_types()

                Output:
                
                    {'age': {'pandas_missing': [nan], 'placeholder_missing': [-999.0, -1.0]},
                    'income': {'pandas_missing': [nan], 'placeholder_missing': []},
                    'account_balance': {'pandas_missing': [nan], 'placeholder_missing': []}}
                
                
        '''
        self.df = self.df.select_dtypes(include = ['number']) # ensuring that we only work on numerical dataframe

        # keeping a dictionary of missing values
        missing_values = {}

        # keeping extra placeholders to be an empty list if None, otherwise creating a mask of placeholders would not be able to find something to iterate over.
        if extra_placeholders is None:
            extra_placeholders = []

        # creating a mask of pandas considering missing values
        pandas_mask = self.df.isna()

        # creating a mask for extra placeholders user wants to detect in their missing data
        placeholders_mask = self.df.isin(extra_placeholders)

        for column in self.df[self.columns]:

            # converting to object type, otherwise .unique() returned a lot of unnecessary categorical information
            pandas_missing = self.df.loc[pandas_mask[column], column].astype('object').unique().tolist()

            # getting those values that are missing
            place_holder_missing = self.df.loc[placeholders_mask[column], column].astype('object').unique().tolist()
            
            # if either of the values exist, show the results
            if pandas_missing or place_holder_missing:
                missing_values[column] = {
                    'pandas_missing': pandas_missing,
                    'placeholder_missing': place_holder_missing
                }

        return missing_values

    def detect_categorical_missing_types(self, extra_placeholders: list|None = None):

        '''
        Detects the types of missing values in Categorical (text or categories) columns of the DataFrame.

        Parameters:
        -----------

            self: pd.DataFrame
                A pandas DataFrame of Categorical columns

            Optional:

                extra_placeholders: list or type None (default is None)

                    A list of extra placeholders you wish to pass as missing values depending on your domain
            
        Returns:
        --------
            dict
                A dictionary of categorical columns and the types of missing values in a Categorical DataFrame.
            
        Usage Recommendation:
        ---------------------
                Use this function when you want to detect what kind of missing data exists in your text.

        Considerations:
        ---------------

            1. This function returns two categories of numerical missing data types: 

                a. Pandas Missing Types (NAN) -> Pandas converts anything that is not a number to NAN (Not a Number).
                b. Domain Dependent Missing Types-> These are the types your domain considers as missing data (Example: -1, 0 (in age where info is missing for a person))

        Example: 
        --------
                    MissingnessDiagnosis(df).detect_categorical_missing_types()

                Output:
            
                    {'gender': {'pandas_missing': [nan], 'placeholder_missing': []},
                    'country': {'pandas_missing': [nan], 'placeholder_missing': []},
                    'device_type': {'pandas_missing': [nan], 'placeholder_missing': []},
                    'email': {'pandas_missing': [nan], 'placeholder_missing': []},
                    'notes': {'pandas_missing': [nan], 'placeholder_missing': ['?', "['list']"]},
                    'phone_number': {'pandas_missing': [nan], 'placeholder_missing': ['-999']},
                    'is_active': {'pandas_missing': [nan], 'placeholder_missing': []}}
                
        '''
        categorical_missing_types = {}

        self.df = self.df.select_dtypes(include = ['object', 'string', 'category'])

        if extra_placeholders is None:
            extra_placeholders = []

        pandas_mask = self.df.isna()
        placeholders_mask = self.df.isin(extra_placeholders)

        for column in self.df[self.columns]:
            pandas_missing = self.df.loc[pandas_mask[column], column].astype('object').unique().tolist()
            placeholders_missing = self.df.loc[placeholders_mask[column], column].astype('object').unique().tolist()

            if pandas_missing or placeholders_missing:
                categorical_missing_types[f'{column}'] = {
                    'pandas_missing': pandas_missing,
                    'placeholder_missing': placeholders_missing
                }
                
        return categorical_missing_types
        
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