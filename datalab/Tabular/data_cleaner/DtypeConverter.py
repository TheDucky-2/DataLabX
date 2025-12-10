import pandas as pd

class DtypeConverter:
    
    def __init__(self, df:pd.DataFrame | pd.Series, columns:list=None):
        '''
        Initializing the ColumnConverter
        
        Parameters:
        -----------
        df       : pd.DataFrame 
            A pandas DataFrame 

        columns  : list or type(None)
            List of columns to convert into numerical columns. E.g: ['Quantity', 'Price', 'Number of Orders']
        
        '''
        if not isinstance(df, (pd.DataFrame, pd.Series)):
            raise TypeError(f'df must be a pandas DataFrame or a pandas Series, got {type(df).__name__}')

        if not isinstance(columns, (list, type(None))):
            raise TypeError(f'columns must be a list of strings or type None, got {type(columns).__name__}')
            
        # creating a copy of the original dataframe
        self.df = df.copy()  
        
        # if user passes a list of columns
        if columns is None: 
            # columns would default to all of the columns of the dataframe
            self.columns = df.columns.to_list()
        else:
            # columns would be the list of columns passed
            self.columns = columns
        
        print(f'DtypeConverter initialized with columns: {self.columns}')

    def float64_to_Int64(self, inplace: bool=False) -> pd.DataFrame:
        '''
        Convert datatypes of one or more columns from 'float' to 'Int64' safely (using nullable integers)

        Parameters:
            df:       pd.DataFrame, a pandas DataFrame
            columns : list of column names
            inplace  : bool (default, False)
                If True, modifies the original DataFrame in place.
                If False, returns a new DataFrame with only the converted columns.

        Return:
            pd.DataFrame
            A pandas DataFrame of only the columns with values converted from float to Int64 (nullable, which means it can include null values)

        Usage Recommendation:
            Use this function when you want to convert float (decimals) into int (integer), including null values & np.nan.

        Considerations:
            This function keeps null values and np.nan, but converts them to <NA> (Int64Dtype)

        >>> Example: 
                    Input   :   df['age'] = [56.0, 64.0, 75.0, 23.0, NaN]
                    Function:   df = float_to_Int64(df, ['age'], inplace=True) 
                    Output  :   Entire Original DataFrame, with values converted in column 'age' as [56, 64, 75, 23, <NA>]

            Example: 
                    Input   :   df['age']               = [56.0, 64.0, 75.0, 23.0, NaN]
                                df['num_of_dependents'] = [0.0, 1.0, NaN, 5.0, 2.0]

                    Function:   df = float_to_Int64(df, ['age', 'num_of_dependents'], inplace=True) 

                    Output  :   DataFrame of columns 'age' and 'num_of_dependents'.
                                df['age']                 = [56, 64, 75, 23, <NA>]
                                df['num_of_dependents']   = [0, 1, <NA>, 5, 2]

        '''
        
        missing_columns = [column for column in self.columns if column not in self.df.columns]
        if missing_columns:
            raise ValueError(f'The following columns are not in the dataframe: {missing_columns}')

        if inplace:
            self.df[self.columns] = self.df[self.columns].apply(lambda col: col.astype('Int64'))
            return None
        else:
            df_copy = self.df.copy()
            df_copy[self.columns] = df_copy[self.columns].apply(lambda col: col.astype('Int64'))
            return df_copy

    def to_string(df: pd.DataFrame, columns: list, inplace:bool=False):
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
        
        >>> to_string(df, ['ID', 'Nationality', 'Club', 'Bank Account No.'], inplace=True]) 
        #   returns full original dataframe with converted columns

        >>> to_string(df, ['ID', 'Nationality', 'Club', 'Bank Account No.']]) 
        #   returns only the dataframe of converted columns
        '''

        if not isinstance(inplace, bool):
            raise TypeError(f'inplace must be a boolean: True or False, got {type(inplace).__name__}')

        # converting columns into string type
        df[columns] = df[columns].apply(lambda column: column.astype('string'))

        if inplace:
            return df
        else:
            return df[columns]

    def float64_to_int64(self):

        return self.df[self.columns].apply(lambda x: x.astype('int64'))
