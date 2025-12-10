import pandas as pd
import missingno as msno
import matplotlib.axes

from .BaseCleaner import DataCleaner

class NumericalCleaner(DataCleaner):

    def __init__(self, df: pd.DataFrame, columns: list =None):
        # Initializing the base data cleaner
        super().__init__(df, columns)

        # only the numeric datatype
        self.df = self.df.select_dtypes(include='number')
        # if passed column is in columns of the DataFrame
        self.columns = [column for column in self.columns if column in self.df.columns]
        
        print(f'NumericalCleaner initialized with columns: {self.columns}')

    def float_to_Int64(self, inplace: bool=False) -> pd.DataFrame:
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
        if not isinstance(self.df, pd.DataFrame):
            raise TypeError(f'df must be a pandas dataframe, got {type(self.df).__name__}')

        if not isinstance(self.columns, list):
            raise TypeError(f'columns must be a list of column names, got {type(self.columns).__name__}')
        
        missing_columns = [column for column in self.columns if column not in self.df.columns]
        if missing_columns:
            raise ValueError(f'The following columns are not in the dataframe: {missing_columns}')

        self.df[self.columns] = self.df[self.columns].apply(lambda col: col.astype('Int64'))

        if inplace:
            return None
        else:
            return self.df[self.columns].copy()

    def round_off(self, decimals:int, inplace:bool=False):
        '''
        Round off numbers by 

        Parameters:
            df       : pd.DataFrame, a pandas DataFrame
            decimals : int 
            inplace  : bool (default, False)
                If True, modifies the original DataFrame in place.
                If False, returns a new DataFrame with only the converted columns.

        Return:
            pd.DataFrame
            A pandas DataFrame of only the columns with float values rounded off (upto usually 2 or 3 decimal places).

        Usage Recommendation:
            Use this function when you want to round off floats (decimals) to either 2 or 3 decimal places.
            (If you wish to remove the decimals completely, convert to int type and use float_to_Int64 (if your column includes null types))

        Considerations:
            Pass numeric values after converting datatypes to float, instead of strings.

        >>> Example: 
                    Input   :   df['salary'] = ["73892.871297", "55599.652884", "17417.103660", "18809.367362655572", "72700.914047"]
                    Usage   :   NumericalCleaner(df, ['salary']).round_off(3, inplace=True)
                    Output  :   Entire Original DataFrame, with values converted in column 'salary' as ["73892.871", "55599.652", "17417.103", "18809.367", "72700.914"]

            Example: 
                
                    Input   :   df['salary'] = ["73892.871297", "55599.652884", "17417.103660", "18809.367362655572", "72700.914047"]
                    Usage   :   NumericalCleaner(df, ['salary']).round_off(3)
                    Output  :   Pandas series, with values converted in column 'salary' as ["73892.871", "55599.652", "17417.103", "18809.367", "72700.914"]

        >>> Example: 
                    Input   :   df['salary'] = ["73892.871297", "55599.652884", "17417.103660", "18809.367362655572", "72700.914047"]
                    Usage   :   NumericalCleaner(df, ['salary']).round_off(2, inplace=True)
                    Output  :   Entire Original DataFrame, with values converted in column 'salary' as ["73892.87", "55599.65", "17417.10", "18809.36", "72700.91"]

            Example: 
                
                    Input   :   df['salary'] = ["73892.871297", "55599.652884", "17417.103660", "18809.367362655572", "72700.914047"]
                    Usage   :   NumericalCleaner(df, ['salary']).round_off(2)
                    Output  :   Pandas series, with values converted in column 'salary' as ["73892.87", "55599.65", "17417.10", "18809.36", "72700.91"]
        '''
        
        self.decimals = decimals

        self.df[self.columns]= self.df[self.columns].apply(lambda column: column.round(self.decimals))
        
        if inplace:
            return None
        else:
            return self.df[self.columns].copy()
