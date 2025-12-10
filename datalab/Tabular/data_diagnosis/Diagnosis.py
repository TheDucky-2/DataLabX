from ..data_loader import load_tabular
from ..computations import Statistics
from ..computations import Distribution

from pathlib import Path

import pandas as pd
import numpy as np

class Diagnosis:

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

    def data_preview(self, number_of_rows=10):
        '''
        Shows a preview of your DataFrame

        Parameters:
        ----------

        self: pd.DataFrame
            A pandas DataFrame

            Optional:

                number_of_rows : int (default is 10)
                    N numbers of rows you would like to see 

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame of N number of rows. 
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want a preview of your data during diagnosis 

        Considerations:
        ---------------
            1. This function uses df.head() under the hood.

        Example:
        --------
                Diagnosis(df).data_preview(5)
                
        '''
        return self.df.head(number_of_rows)

    def data_summary(self):

        summary = {

            'shape'        : self.df.shape,
            'columns'      : self.columns,
            'dtypes'       : self.df.dtypes,
            'index'        : self.df.index
        }

        return summary

    def show_memory_usage(self, usage_by='total'):

        if usage_by == 'total':

            total_usage = self.df.memory_usage(deep=True).sum()/(1024**2)
            print(f'Total Memory Usage: {self.df.memory_usage(deep=True).sum()/(1024**2):.2f} MB')
            return total_usage
        
        elif usage_by == 'separate':

            separate_usage = self.df.memory_usage(deep=True)/(1024**2)
            print('Data Usage in MB:\n')
            return separate_usage

    def detect_column_types(self) -> dict [str, list[str]]:

        '''
        Detect the column types (Categorical, Numerical, Datetime) for each column of a DataFrame
            
        Returns:
        --------
        Return a dictionary with list of column types.
            
            dict    
                Numerical  : List of Numerical type columns
                Datetime   : List of Datetime type columns
                Categorical: List of Categorical or object type columns

        Usage Recommendation:
        ---------------------
            1. Use this function to check whether a column is categorized as 'Categorical or text', 'Numerical', or Datetime.
            2. Use 'dl.ColumnConverter' to change column types if column type is not detected correctly.

        '''

        self.column_types = {'Numerical': [], 'Datetime' :[], 'Categorical':[]}

        for col in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[col]):
                self.column_types['Numerical'].append(col)

            elif pd.api.types.is_datetime64_any_dtype(self.df[col]):
                self.column_types['Datetime'].append(col)

            elif pd.api.types.is_object_dtype(self.df[col]) or pd.api.types.is_categorical_dtype(self.df[col]):
                self.column_types['Categorical'].append(col)

        return self.column_types 

    def show_unique_values(self) -> dict[list[str]]:
        '''
        Return a dictionary of unique values in each column. 
            {'column_name': df[column].unique()}
        
        Returns:
            dict
            A dictionary of key, value pairs of column and unique values present in that column

        Usage Recommendation:
            Use this function when you want to see what unique values are present in the column.

        Example: 
            show_unique_values()['Item'] -> {'Item': ['Coffee', 'Cake', 'Cookie', 'Salad', 'Smoothie', 'UNKNOWN','Sandwich', nan, 'ERROR', 'Juice', 'Tea']}
        
        '''
        self.unique_values = {}

        for col in self.df.columns:
            self.unique_values[f'{col}'] = col
            self.unique_values[col] = self.df[col].unique()

        return self.unique_values  

    def show_cardinality(self)-> dict:
        '''
        Shows how many different values exist in each column of the DataFrame.

        Parameters:
        -----------
            self : pd.DataFrame
                A pandas DataFrame

        Returns:
        --------
            dict
                A python dictionary of column names and cardinality values
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to see how many unique values exist before using encoding your Categorical data.

        Example:
        --------
            Diagnosis(df).show_cardinality()
        '''
        # using a dictionary to store values for each column
        cardinality={}

        for column in self.df[self.columns]:
            # checking how many unique values exist
            cardinality[column] = len(self.df[column].unique())

        return cardinality

    def show_duplicates(self, in_columns=None) -> pd.Series:

        return self.df[self.df[self.columns].duplicated(subset=in_columns)]

    def count_duplicates(self, in_columns=None ):

        return self.df[self.columns].duplicated(subset=in_columns).sum()
    
    def get_numerical_columns(self):
        '''
        Separates Numerical (numbers) columns from rest of the DataFrame.

        Parameters:
        -----------
            self: pd.DataFrame

        Return:
        -------
            pd.DataFrame
                A pandas DataFrame of Numerical columns.
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to work specifically on Numerical data, not overall DataFrame (including Categorical, Datetime).
            2. Use this function if you wish to follow DataLab guided workflow for diagnosis, cleaning and preprocessing of Numerical data.

        Example: 
        
        >>>> Diagnosis(df).get_numerical_columns()
        '''

        return self.df.select_dtypes(include='number')

    def get_categorical_columns(self):
        '''
        Separates Categorical (text or category) columns from rest of the DataFrame.

        Parameters:
        -----------
            self: pd.DataFrame

        Return:
        -------
            pd.DataFrame
                A pandas DataFrame of Categorical columns.
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to work specifically on Categorical data, not overall DataFrame (including Numerical, Datetime).
            2. Use this function if you wish to follow DataLab guided workflow for diagnosis, cleaning and preprocessing of Categorical data.

        Example: 
        
        >>>> Diagnosis(df).get_categorical_columns()
    
        '''
        return self.df.select_dtypes(include=['object', 'string', 'category'])

    def get_datetime_columns(self):

        '''
        Separates Datetime (dates or timestamps) columns from rest of the DataFrame.

        Parameters:
        -----------
            self: pd.DataFrame

        Return:
        -------
            pd.DataFrame
                A pandas DataFrame of Datetime columns.
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to work specifically on Date and Time columns, not overall DataFrame (including Numerical, Datetime).
            2. Use this function if you wish to follow DataLab guided workflow for diagnosis, cleaning and preprocessing of Datetime data.

        Example: 
        
        >>>> Diagnosis(df).get_datetime_columns()
    
        '''

        return self.df.select_dtypes(include = ['datetime'])