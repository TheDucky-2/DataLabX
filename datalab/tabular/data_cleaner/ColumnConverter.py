import pandas as pd

class ColumnConverter:
    def __init__(self, df:pd.DataFrame, columns: list = None):
        ''' 
        Initializing the ColumnConverter
        
        Parameters:
        -----------
        df       : pd.DataFrame 
            A pandas DataFrame 

        columns  : list or type(None)
            List of columns to convert into numerical columns. E.g: ['Quantity', 'Price', 'Number of Orders']

        **kwargs : dict
            A dict of extra keyword arguments you may want to pass
        '''

        if not isinstance(df, pd.DataFrame):
            raise TypeError(f'df must be pandas DataFrame, got {type(df).__name__}')

        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be a list or type None, got {type(columns).__name__}')

        self.df = df

        if columns is None:
            self.columns = df.columns.tolist()
        else:
            self.columns = columns

        print(f'ColumnConverter initialized with columns: {self.columns}')

    
    def to_datetime(self, inplace: bool=False, dayfirst=False) -> pd.DataFrame:
        '''
        Convert one or more columns column into datetime columns.

        Parameters:
        -----------
            self: pd.DataFrame
                A pandas DataFrame

            Optional:

            inplace  : bool (default is False)
                Whether you want to apply changes to dataframe. 

            dayfirst : bool (default is False)
                Whether you would like day to appear first or months to appear first, in dates.
        
        Returns:
        --------
            A pandas DataFrame 

            1. return the original dataframe with converted datetime columns, if inplace=True
            2. return only the dataframe of converted datetime columns with rest of the DataFrame unchanged, if default.-

        Usage Recommendation:
        ---------------------
            Use this function to convert columns into datetime columns for extracting date and time later

        Considerations:
        ---------------
            This function converts keeps the values that cannot be converted as they are.

        Examples:
        
        >>>> to_numerical(df, ['Quantity', 'Price Per Unit', 'Total Spent'], inplace=True]) 
        #   returns full original dataframe with converted columns

        >>>> to_numerical(df, ['Quantity', 'Price Per Unit', 'Total Spent'])
        #   returns dataframe of numeric columns ['Quantity', 'Price Per Unit', 'Total Spent'] 

        '''

        if not isinstance(inplace, bool):
            raise TypeError(f'inplace must be a boolean: True or False, got {type(inplace).__name__}')
        # we will be creating a function to convert each value to datetime if valid, else we will leave it as it is.

        if not isinstance(dayfirst, bool):
            raise TypeError(f'dayfirst must be True or False, got {type(dayfirst).__name__}')

        df_copy = self.df.copy()

        for column in df_copy[self.columns]:
            
            if dayfirst:
                # apply datetime conversion to all columns passed
                converted_to_datetime = pd.to_datetime(df_copy[column], dayfirst=True, errors = 'coerce')
            
            else:
                converted_to_datetime = pd.to_datetime(df_copy[column], dayfirst=False,errors='coerce')
                
            conversion_successful = converted_to_datetime.notna()
            # now check scenarios where conversion to datetime failed but is not invalid value in the DataFrame
            conversion_failed = converted_to_datetime.isna() & df_copy[column].notna()

            # if conversion to datetime does not fail
            if not conversion_failed.any():

                # assign converted values to the whole columns of the DataFrame
                df_copy[column] = converted_to_datetime
            else:
                if conversion_successful.any():
                    # if conversion fails, only convert correct datetime values and leave others as they are
                    df_copy.loc[converted_to_datetime.notna(), column] = converted_to_datetime[converted_to_datetime.notna()]

        if inplace:
            return None
            
        else:
            return df_copy

    def to_categorical(self,inplace: bool=False)-> pd.DataFrame:
        '''
        Convert a column to a Categorical column

        Parameters:
            df      : pd.DataFrame | str | Path 
            A pandas DataFrame or a file Path. E.g: (pd.DataFrame or 'example.csv')

            columns : list[str]
            A list of one or more column names.Example: ['Item', 'Payment Method', 'Location']

            inplace  : bool (default is False)
            Making changes to the original dataframe. E.g: True or False

            **kwargs: dict
            Optional keyword arguments:
            - categories : list
                If passed, it will keep only the category names passed in, and will convert everything else to NAN. E.g: ['Great','Good','Better','OK']
            - ordered    : bool , default False
                Whether the categories need to have an order or not. E.g: (Great > Good > Better > OK) or (1 < 2 < 3 < 4 < 5)

        Return:
            pd.DataFrame
            1. Return a pandas DataFrame with columns converted as Categoricals, if 'categories' and 'ordered' passed as parameters.
            2. Return a pandas DataFrame with updated columns with dtype 'category', if parameters not passed.

        Usage Recommendation:
            1. Use this function when there aren't many unique values in your string columns. 
            2. Do not use this function for columns that do not require you to convert text to integers for encoding later. ['Email', 'Name', 'Transaction ID']

        Considerations: 
            If in doubt whether a column has to be converted to categorical or not, leave the column as an object or string until required.

        Examples:
        >>>     to_categorical(df, ['Item', 'Payment Method', 'Ratings'], inplace=True) 
        #       returns full original dataframe with converted columns

        >>>     to_categorical(df, ['Ratings'], categories= ['Great','Good','Better','OK'], ordered=True)
        #       returns the pandas Series with converted column having only the values passed as categories, and everything else converted to NAN
        '''

        if not isinstance(inplace, bool):
            raise TypeError(f'inplace must be True or False, got {type(inplace).__name__}')

        self.inplace = inplace

        categories = self.kwargs.get('categories', None)
        ordered = self.kwargs.get('ordered', False)

        # created a copy of the data that we will be working on, to assign to self.df if inplace = True later
        df_copy = self.df if inplace else self.df.copy()

        for column in self.columns:
            if categories is not None:
                df_copy[column] = pd.Categorical(df_copy[column], categories=categories, ordered = ordered)

            else:
                df_copy[column] = df_copy[column].astype('category')

        if self.inplace:
            self.df = df_copy
            return None
            
        else:
            return df_copy
        
    def to_numerical(self, inplace:bool=False) -> pd.DataFrame:
        '''
        Convert one or more columns column into numerical columns.

        Parameters:
        -----------
        inplace  : bool
            Making changes to the original dataframe. E.g: True or False

        Returns:
        --------
        pd.DataFrame
            A pandas DataFrame 
                1. return the original dataframe with converted numerical columns, if inplace=True
                2. return only the dataframe of converted numerical columns, if inplace=False

        Usage Recommendation:
        ---------------------
            Use this function to convert columns into numeric values for later calculations.
        
        Considerations:
        ---------------
            This function converts non-convertible values to NaN and then restores those values back from NaN to original.

        Examples:
        
        >>> to_numerical(df, ['Quantity', 'Price Per Unit', 'Total Spent'], inplace=True]) 
        #   returns full original dataframe with converted columns

        >>> to_numerical(df, ['Quantity', 'Price Per Unit', 'Total Spent'])
        #   returns dataframe of numeric columns ['Quantity', 'Price Per Unit', 'Total Spent']
        ''' 

        if not isinstance(inplace, bool):
            raise TypeError(f'inplace must be True or False, got {type(inplace).__name__}')

        if inplace:
            original_columns = self.df[self.columns].copy()
            # first converting all data to numerical, and non-numerical get converted to NaN
            self.df[self.columns] = self.df[self.columns].apply(pd.to_numeric, errors = 'coerce')

            #  reverting NaN values back to original missing values
            self.df[self.columns] = self.df[self.columns].combine_first(original_columns)
            return None

        else:
            df_copy = self.df.copy()
            # first converting all data to numerical, and non-numerical get converted to NaN
            df_copy[self.columns] = self.df[self.columns].apply(pd.to_numeric, errors='coerce')

            #  reverting NaN values back to original missing values
            df_copy[self.columns] = df_copy[self.columns].combine_first(self.df[self.columns])
            return df_copy

