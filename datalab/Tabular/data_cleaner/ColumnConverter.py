import pandas as pd

class ColumnConverter:
    def __init__(self, df:pd.DataFrame, columns: list = None, **kwargs):
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

        self.df = df.copy()
        self.kwargs = kwargs

        if columns is None:
            self.columns = df.columns.to_list()
        else:
            self.columns = columns

        print(f'ColumnConverter initialized with columns: {self.columns}')

    def to_numerical(self, errors: str='coerce', inplace:bool=False) -> pd.DataFrame:
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
            This function converts non-convertible values into np.nan (Not a Number) by default.

        Examples:
        
        >>> to_numerical(df, ['Quantity', 'Price Per Unit', 'Total Spent'], inplace=True]) 
        #   returns full original dataframe with converted columns

        >>> to_numerical(df, ['Quantity', 'Price Per Unit', 'Total Spent'])
        #   returns dataframe of numeric columns ['Quantity', 'Price Per Unit', 'Total Spent']
        ''' 

        if not isinstance(inplace, bool):
            raise TypeError(f'inplace must be True or False, got {type(inplace).__name__}')

        if not isinstance(errors, str):
            raise TypeError(f'errors must be a string, got {type(errors).__name__}')

        self.errors = errors
        self.inplace = inplace

        if self.inplace:
            self.df[self.columns] = self.df[self.columns].apply(pd.to_numeric, errors=self.errors, **self.kwargs)
            return None

        else:
            df_copy = self.df.copy()
            df_copy[self.columns] = df_copy[self.columns].apply(pd.to_numeric, errors=self.errors, **self.kwargs)
            
            return df_copy

    def to_datetime(self, inplace: bool=False) -> pd.DataFrame:
        '''
        Convert one or more columns column into datetime columns.

        Parameters:
            df       : A pandas DataFrame or a file path (pd.DataFrame or 'example.csv')
            columns  : list of columns to convert into datetime columns
            inplace  : True or False, default False
        
        Returns:
            a pandas DataFrame 
            1. return the original dataframe with converted datetime columns, if inplace=True
            2. return only the dataframe of converted datetime columns, if inplace=False

        Usage Recommendation:
            Use this function to convert columns into datetime columns for extracting date and time later

        Considerations:
            This function converts non-convertible values into np.nan (Not a Number)

        Examples:
        
        >>>> to_numerical(df, ['Quantity', 'Price Per Unit', 'Total Spent'], inplace=True]) 
        #   returns full original dataframe with converted columns

        >>>> to_numerical(df, ['Quantity', 'Price Per Unit', 'Total Spent'])
        #   returns dataframe of numeric columns ['Quantity', 'Price Per Unit', 'Total Spent'] 

        '''

        if not isinstance(inplace, bool):
            raise TypeError(f'inplace must be a boolean: True or False, got {type(inplace).__name__}')

        self.inplace=inplace

        if self.inplace:
            self.df[self.columns] = self.df[self.columns].apply(pd.to_datetime, errors='coerce', **self.kwargs)
            return df

        else:
            df_copy = self.df.copy()
            df_copy[self.columns] = df_copy[self.columns].apply(pd.to_datetime, errors='coerce', **self.kwargs)
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
            

    def to_string(self, inplace:bool=False):
        '''
        Convert one or more columns column into string type columns.

        Parameters:
            df       : pd.DataFrame or str
                A pandas DataFrame or a file path. E.g: (pd.DataFrame or 'example.csv')

            columns  : list 
                List of columns to convert into string type. E.g: ['Player ID', 'Club', 'Nationality', 'Bank Account No.']

            inplace  : bool (default, False)
                If True, modifies the original DataFrame in place.
                If False, returns a new DataFrame with only the converted columns.
            
        Returns:
            a pandas DataFrame 
            1. If inplace=True, returns the original DataFrame with the converted string columns.
            2. If inplace=False, returns a DataFrame of only the converted columns.

        Usage Recommendation:
            1. Use this function to convert any column into text-based column for text cleaning later.
            2. Use this function when there are many unique values in each column. 
            3. Don't use this for columns that contain categories. E.g: ['Good', 'Great', 'Poor'] or ['High', 'Low', 'Medium']. 
            For those columns, use `to_categorical` instead.

        Considerations:
            This function converts mostly everything into string type. 
            If anything fails, it gets converted to <NA> (pandas null string).
        
        Examples:
        
        >>> dl.ColumnConverter(df, ['Transaction ID']).to_string(inplace=True) 
        #   returns modified original dataframe with converted columns

        >>> dl.ColumnConverter(df, ['Transaction ID']).to_string() 
        #   returns a copy of the dataframe with converted columns
        '''

        if not isinstance(inplace, bool):
            raise TypeError(f'inplace must be a boolean: True or False, got {type(inplace).__name__}')

        self.inplace=inplace

        # converting columns into string type
        self.df[columns] = df[columns].apply(lambda column: column.astype('string'))

        if inplace:
            self.df[self.columns] = self.df[self.columns].apply(lambda column: column.astype('string'))
            return None
        else:
            df_copy = self.df.copy()
            return df_copy

