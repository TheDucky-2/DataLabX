import pandas as pd
import missingno as msno
import matplotlib.axes

from .BaseCleaner import DataCleaner

class NumericalCleaner(DataCleaner):

    def __init__(self, df: pd.DataFrame, columns: list =None):
        # Initializing the base data cleaner
        super().__init__(df, columns)

        self.df = df 

        numerical_columns = self.df.select_dtypes(include='number').columns.tolist() 
        # if passed column is in columns of the DataFrame
        self.columns = [column for column in numerical_columns if column in self.df.columns]
        
        print(f'NumericalCleaner initialized with columns: {self.columns}')

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
        '''

        if inplace:
            self.df[self.columns]= self.df[self.columns].apply(lambda column: column.round(decimals))
            return None
        else:
            self.df[self.columns]= self.df[self.columns].apply(lambda column: column.round(decimals))
            return self.df.copy()
