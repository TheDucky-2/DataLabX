"""Diagnoses missing data in tabular datasets."""

from ..computations import Statistics
from ..utils.Logger import datalabx_logger

from pathlib import Path
import pandas as pd
import numpy as np

logger = datalabx_logger(name = __name__.split('.')[-1])

class MissingnessDiagnosis:
    """
    Initialize the Missingness Diagnosis.

    Parameters
    -----------
    df: pd.DataFrame
        A pandas dataframe you wish to diagnose.

    columns: list, optional
        A list of columns you wish to apply numerical cleaning on, by default None

    extra_placeholders: list, optional
        A list of extra placeholders considered as missing values depending on the domain, by default None
    """

    def __init__(self, df: pd.DataFrame, columns:list = None, extra_placeholders:list|type(None)=None):
        import pandas as pd
        import numpy as np

        # making sure that the passed df is a pandas DataFrame
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f'df must be a pandas DataFrame, got {type(df).__name__}')
        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be a list of column names, got {type(columns).__name__}')
        if not isinstance(extra_placeholders, (list, type(None))):
            raise TypeError(f'extra_placeholders must be a list of strings, got {type(extra_placeholders).__name__}')

        self.df = df

        if columns is None:
            self.columns = df.columns.to_list()
        else:
            self.columns = [column for column in columns if column in self.df.columns]

        # keeping extra placeholders to be an empty list if None, otherwise creating a mask of placeholders would not be able to find something to iterate over.
        if extra_placeholders is None:
            self.extra_placeholders = []

        else:
            self.extra_placeholders = extra_placeholders
            logger.info(f'Received {self.extra_placeholders} as placeholders for missing data!')

        logger.info(f'Missingness Diagnosis initialized.')

    def detect_missing_types(self)-> dict[str, dict[str, list]]:
        """Detects the types of missing values in each column of the DataFrame.

        Returns
        --------
        dict
            A dictionary of columns and the types of missing values in a Numerical DataFrame.

        Usage Recommendation
        ---------------------
            1. Use this function when you want to detect what kind of missing data exists in your data.
        """
        # keeping a dictionary of missing values
        missing_values = {}

        # creating a mask of pandas considering missing values
        pandas_mask = self.df.isna()

        # creating a mask for extra placeholders user wants to detect in their missing data
        placeholders_mask = self.df.isin(self.extra_placeholders)

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
    
    def show_missing_rows_in_categorical_columns(self)-> dict[str, pd.DataFrame]:
        """Shows the rows where data is missing in Categorical columns of the DataFrame.

        Returns
        --------
        dict
            A dictionary of Categorical columns with rows containing missing values (pandas or placeholder).

        Usage Recommendation
        ---------------------
            Use this function to see missing values in categorical columns before deciding how to clean or handle them.
        """
        # selecting only the categorical or text data 
        missing_categorical_data = {}

        if self.columns is None:
            categorical_columns = self.df.select_dtypes(include = ["object", "string", "category"]).columns
        else:
            categorical_columns = self.columns

        for column in categorical_columns:
        
            # creating a true false mask of pandas missing types if missing returns true otherwise false
            pandas_mask = self.df[column].isna()

            # creating a true false mask of placeholder missing types if missing returns true otherwise false
            placeholders_mask = self.df[column].isin(self.extra_placeholders)

            # if pandas or placeholder missing values exist, show either of the data
            missing_mask = pandas_mask | placeholders_mask

            # Only including a column in the output if it actually has missing values.
            if missing_mask.any():
                missing_categorical_data[column] = self.df.loc[missing_mask]
        
        return missing_categorical_data

    def show_missing_rows_in_numerical_columns(self)-> dict[str, pd.DataFrame]:
        """Shows the rows where data is missing in Numerical columns of the DataFrame.

        Returns
        --------
        dict
            A dictionary of Numerical columns with rows containing missing values (pandas or placeholder).

        Usage Recommendation
        ---------------------
            Use this function to see missing values in numerical columns before deciding how to clean or handle them.
        """
        missing_numerical_data = {}
        
        if self.columns is None:
            # selecting only the numerical data 
            numerical_columns = self.df.select_dtypes(include = ['number']).columns
        else:
            numerical_columns = self.columns

        for column in numerical_columns:

            # creating a true false mask of pandas missing types if missing returns true otherwise false
            pandas_mask = self.df[column].isna()

            # creating a true false mask of placeholder missing types if missing returns true otherwise false
            placeholders_mask = self.df[column].isin(self.extra_placeholders)

            # if pandas or placeholder missing values exist, show both data (using OR)
            missing_mask = pandas_mask | placeholders_mask

            # Only including a column in the output if it actually has missing values.
            if missing_mask.any():
                missing_numerical_data[column] = self.df.loc[missing_mask]

        return missing_numerical_data

    def show_missing_rows_in_datetime_columns(self)-> dict[str, pd.DataFrame]:
        """Shows the rows where data is missing in Date or Time columns of the DataFrame.

        Returns
        --------
        dict
            A dictionary of DateTime columns with rows containing missing values (pandas or placeholder).

        Usage Recommendation
        ---------------------
            Use this function to see missing values in date or time columns before deciding how to clean or handle them.
        """
        missing_datetime_data = {}
        
        if self.columns is None:
            datetime_columns = self.df.select_dtypes(include = ['datetime']).columns
        else:
            datetime_columns = self.columns

        for column in datetime_columns:

            # creating a true false mask of pandas missing types if missing returns true otherwise false
            pandas_mask = self.df[column].isna()

            # creating a true false mask of placeholder missing types if missing returns true otherwise false
            placeholders_mask = self.df[column].isin(self.extra_placeholders)

            # if pandas or placeholder missing values exist, show both data (using OR)
            missing_mask = pandas_mask | placeholders_mask

            # Only including a column in the output if it actually has missing values.
            if missing_mask.any():
                missing_datetime_data[column] = self.df.loc[missing_mask]
                
        return missing_datetime_data

    def missing_data_summary(self, method='count')-> dict[str, int]:
        """Shows the number of rows with missing values present in each column, irrespective of column type (Categorical, Numerical or Datetime)

        Parameters
        -----------
        method : str (default is 'count')

            How you would like to show the total of missing values.

                - 'count'    : Shows a count of rows with missing values per column
                - 'percent': Shows the percentage of rows with missing values per column

        Returns
        --------
        dict
            A dictionary of counts or percentages of missing values per column

        Usage Recommendation
        ---------------------
            Use this function when you want to see a count or percentage of missing values before deciding whether to drop or fill missing values.
        """
        # a mask of pandas missing values to get pandas missing types
        pandas_mask = self.df.isna()
        
        # a mask of placeholder missing types 
        placeholders_mask = self.df.isin(self.extra_placeholders)

        # an empty to dictionary of missing_data_summary
        missing_data_summary = {}
        
        # to ensure pandas or placeholder types are both picked
        mask = pandas_mask | placeholders_mask

        for col in self.df[self.columns]:

            # if missing values are present in any column 
            if mask[col].any():

                # to ensure user can get a count of rows where values are missing
                if method == 'count':

                    missing_data_summary[col] = len(self.df.loc[mask[col]])

                # if user wants to see percentage
                elif method == 'percent':

                    missing_data_summary[col] = (len(self.df.loc[mask[col]])/ len(self.df)) * 100

                # only sum and percent are acceptable types
                else:
                    raise ValueError(f"method must be 'count' or 'percent', got {method}")

        # rounding off values to 2 decimal places
        missing_data_summary = {col: round(value, 2) for col, value in missing_data_summary.items()}

        return missing_data_summary
        
    def rows_with_all_columns_missing(self)-> pd.DataFrame:
        """Detects and shows all the rows where all the columns are missing values together in a DataFrame.

        Returns
        --------
        pd.DataFrame
            A pandas dataframe of all rows where data is missing together in all the columns.

        Usage Recommendation
        ---------------------
            Use this function when you want to see data where all columns have values missing.
        """
        # creating a mask of pandas missing values
        pandas_mask = self.df.isna()

        # creating a mask of placeholder missing values
        placeholder_mask = self.df.isin(self.extra_placeholders)

        # accepting both values
        missing_mask = pandas_mask | placeholder_mask

        # this is the main part where we check rows where all columns are missing values 
        missing_data = missing_mask.all(axis=1)

        # getting only the data of rows where all columns are missing values
        all_columns_missing_data = self.df.loc[missing_data]

        return all_columns_missing_data

    def rows_with_specific_columns_missing(self, extra_placeholders=None)-> pd.DataFrame:
        """Detects and shows all the rows where only specific columns are missing valeues together in a DataFrame.

        Returns
        -------
        pd.DataFrame
            A pandas dataframe of all rows where data is missing together in only the columns decided by user.

        Usage Recommendation
        ---------------------
            Use this function when you want to see data where only your decided columns have values missing.
        """    
        # creating a mask of pandas missing values
        pandas_mask = self.df[self.columns].isna()
        
        # creating a mask of placeholder missing values
        placeholder_mask = self.df[self.columns].isin(self.extra_placeholders)

        # accepting both values
        missing_mask = pandas_mask | placeholder_mask

        # this is the main part where we check rows where only specific columns are missing values
        missing_data = missing_mask.all(axis=1)

        # getting only the data of rows where specific columns are missing values
        missing_data_in_specific_columns = self.df[self.columns].loc[missing_data]

        return missing_data_in_specific_columns