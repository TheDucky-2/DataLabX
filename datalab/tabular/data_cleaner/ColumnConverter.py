"""Converts columns to Numerical, Categorical or Datetime type"""

import pandas as pd
from ..utils.Logger import datalab_logger

logger = datalab_logger(name = __name__.split('.')[-1])

class ColumnConverter:
    def __init__(self, df:pd.DataFrame, columns: list = None):
        """
        Initializing the ColumnConverter.

        Parameters
        -----------
        df : pd.DataFrame
            A pandas DataFrame.

        columns : list or type(None)
            List of columns you wish to convert, by default None.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f'df must be pandas DataFrame, got {type(df).__name__}')

        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be a list or type None, got {type(columns).__name__}')

        self.df = df

        if columns is None:
            self.columns = self.df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns]

        logger.info(f'ColumnConverter initialized.')

    def to_datetime(self, inplace: bool=False, dayfirst=False, **kwargs) -> pd.DataFrame:
        """
        Convert one or more columns column into datetime columns.

        Parameters
        -----------
        inplace  : bool, optional
            Whether you want to apply changes to dataframe the original dataframe in place, by default False.

        dayfirst : bool, optional
            Whether the order of days is to be set before months in dates, by default False.
        
        kwargs: dict, optional
            A dictionary of keyword arguments you wish to pass in ``pd.to_datetime()`` method.

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame 

            1. Makes changes to the original dataframe in place, but returns None, if inplace=True.
            2. Returns the dataframe of converted datetime columns with rest of the non-datetime columns, if inplace = False.

        Usage Recommendation
        ---------------------
            Use this function to convert columns into datetime columns for working with date and time data later.

        Considerations
        ---------------
            This function keeps non-converted values as they are.

        Example
        --------
        >>> ColumnConverter(df).to_datetime()
        
        >>> ColumnConverter(df).to_datetime(inplace=True) 
        """
        if not isinstance(inplace, bool):
            raise TypeError(f'inplace must be a boolean: True or False, got {type(inplace).__name__}')

        if not isinstance(dayfirst, bool):
            raise TypeError(f'dayfirst must be True or False, got {type(dayfirst).__name__}')

        if not isinstance(kwargs, dict):
            raise TypeError(f'keyword arguments must be a dict, got {type(kwargs).__name__}')

        for column in self.df[self.columns]:
            
            if dayfirst:
                # apply datetime conversion to all columns passed
                converted_to_datetime = pd.to_datetime(self.df[column], dayfirst=True, errors = 'coerce', **kwargs)
            
            else:
                converted_to_datetime = pd.to_datetime(self.df[column], dayfirst=False,errors='coerce', **kwargs)
            
            # values where conversion can be done will stay True
            conversion_successful = converted_to_datetime.notna()

            # we want values where failed conversion resulted into NA, however, those values were not NA in original dataframe
            conversion_failed = converted_to_datetime.isna() & self.df[column].notna()

            # if conversion to datetime does not fail
            if not conversion_failed.any():

                # assign converted values to the whole columns of the DataFrame
                self.df[column] = converted_to_datetime
            else:
                if conversion_successful.any():
                    # if conversion fails, only convert correct datetime values and leave others as they are
                    self.df.loc[converted_to_datetime.notna(), column] = converted_to_datetime[converted_to_datetime.notna()]

        if inplace:
            return None
            
        else:
            return self.df

    def to_categorical(self,inplace: bool=False, **kwargs)-> pd.DataFrame:
        """
        Convert a column to a Categorical column.

        Parameters
        -----------
        inplace  : bool (default is False)
            Making changes to the original dataframe. E.g: True or False.

        kwargs: dict
            A dictionary of keyword arguments you wish to pass in ``pd.Categorical()`` method.

            Optional keyword arguments:

            - categories : list, optional, default None
                If passed, it will keep only the values passed in, and will convert everything else to NAN. E.g: ['Great','Good','Better','OK'].

            - ordered    : bool, optional, default False
                Whether the categories need to have an order or not, E.g: (Great > Good > Better > OK) or (1 < 2 < 3 < 4 < 5).

        Returns
        ------
        pd.DataFrame
            A pandas DataFrame

            1. Return a pandas DataFrame with columns converted as Categorical, if 'categories' and 'ordered' passed as parameters.
            2. Return a pandas DataFrame with updated columns with 'category' dtype, if parameters not passed.

        Usage Recommendation
        ---------------------
            1. Use this function when there aren't many unique values in your string columns. 
            2. DO NOT Use this function for text columns that you would not be converting to integers, E.g: ['Email', 'Name', 'Transaction ID'].

        Considerations
        ---------------
            If in doubt whether a column has to be converted to categorical or not, leave the column as an object or string until required.

        Example
        --------
        >>>  ColumnConverter(df).to_categorical(inplace=True) 

        >>>  ColumnConverter(df).to_categorical(categories= ['Great','Good','Better','OK'], ordered=True)
        """
        if not isinstance(inplace, bool):
            raise TypeError(f'inplace must be True or False, got {type(inplace).__name__}')
            
        if not isinstance(kwargs, dict):
            raise TypeError(f'keyword arguments must be a dict, got {type(kwargs).__name__}')

        categories = kwargs.get('categories', None)
        ordered = kwargs.get('ordered', False)

        for column in self.df[self.columns]:

            if categories is not None:
                self.df[column] = pd.Categorical(self.df[column], categories=categories, ordered = ordered)

            else:
                self.df[column] = self.df[column].astype('category')

        if inplace:
            return None
            
        else:
            return self.df
        
    def to_numerical(self, inplace:bool=False, **kwargs) -> pd.DataFrame:
        """
        Convert one or more columns into numerical columns.

        Parameters
        -----------
        inplace  : bool, optional
            Making changes to the original dataframe, by default False.

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame 
                1. Makes changes to the original dataframe in place, but returns None, if inplace=True
                2. Returns the dataframe of converted numerical columns with rest of the non-numerical columns, if inplace = False.

        Usage Recommendation
        ---------------------
            Use this function to convert columns into numeric values for later calculations.
        
        Considerations
        ---------------
            This function keeps non-convertible values as they are, but columns may remain of 'object' dtype in case numbers are dirty.

        Example
        --------
        
        >>> ColumnConverter(df).to_numerical(inplace=True) 

        >>> ColumnConverter(df).to_numerical()
        """ 
        if not isinstance(inplace, bool):
            raise TypeError(f'inplace must be True or False, got {type(inplace).__name__}')

        if not isinstance(kwargs, dict):
            raise TypeError(f'keyword arguments must be a dict, got {type(kwargs).__name__}')

        original_columns = self.df[self.columns].copy()
            
        # first converting all data to numerical, and non-numerical get converted to NaN
        self.df[self.columns] = self.df[self.columns].apply(pd.to_numeric, errors = 'coerce', **kwargs)

        #  reverting NaN values back to original missing values
        self.df[self.columns] = self.df[self.columns].combine_first(original_columns)

        if inplace:
            return None
        else:
            return self.df

    def to_numerical_forced(self, inplace:bool=False, **kwargs)-> pd.DataFrame:
        """
        Convert one or more columns column into numerical columns forcibly as it turns non-convertible values to NaN.

        Parameters
        -----------
        inplace  : bool, optional
            Making changes to the original dataframe, by default False.

        kwargs: dict, optional
            A dictionary of keyword arguments you wish to pass in ``pd.to_numeric()`` method.

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame 

                1. Makes changes to the original dataframe in place, but returns None, if inplace=True
                2. Returns the dataframe of converted numerical columns with rest of the non-numerical columns, if inplace = False.

        Usage Recommendation
        ---------------------
            1. Use this function to convert columns into numeric datatype for later calculations.
        
        Considerations
        ---------------
            This function converts non-convertible values to NaN, and forces conversion to numeric dtype.

        Example
        --------

        >>> ColumnConverter(df).to_numerical_forced(inplace=True) 

        >>> ColumnConverter(df).to_numerical_forced()

        """ 
        if not isinstance(inplace, bool):
            raise TypeError(f'inplace must be True or False, got {type(inplace).__name__}')
            
        if not isinstance(kwargs, dict):
            raise TypeError(f'keyword arguments must be a dict, got {type(kwargs).__name__}')

        # first converting all data to numerical, and non-numerical get converted to NaN
        self.df[self.columns] = self.df[self.columns].apply(pd.to_numeric, errors = 'coerce', **kwargs)

        if inplace:
            return None
        else:
            return self.df



