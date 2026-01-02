import pandas as pd

from .BaseCleaner import DataCleaner
from ..data_diagnosis import DirtyDataDiagnosis

class NumericalCleaner(DataCleaner):

    def __init__(self, df: pd.DataFrame, columns: list =None):
        # Initializing the base data cleaner
        super().__init__(df, columns)

        self.df = df 

        if columns is None: 
            # if passed column is in columns of the DataFrame
            self.columns = self.df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns]
        
        print(f'NumericalCleaner initialized with columns: {self.columns}')

    def round_off(self, decimals:int, inplace:bool=False)-> pd.DataFrame:
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

    def remove_spaces_in_numbers(self)->pd.DataFrame:
        '''
        Removes leading or trailing spaces in numerical data for each column of DataFrame

        Parameters:
        -----------
            self : pd.DataFrame
                A pandas DataFrame

        Returns:
        --------
            pd.DataFrame
                A pandas DataFrame with removed trailing or leading spaces.
        
        Usage Recommendation:
        ---------------------
            1. Use this function when you want to remove leading or trailing spaces in numbers.

        Example:
        --------
            DirtyDataDiagnosis(df).detect_clean_numerical_data()
        '''

        leading_spaces_pattern = r'^\s+[+-]?\d+(\.\d+)?$'
        trailing_spaces_pattern = r'^[+-]?\d+(\.\d+)?\s+$'
        leading_and_trailing_spaces_pattern = r'^\s+[+-]?\d+(\.\d+)?\s+$'

        spaces_in_numerical_data = {}

        for column in self.df[self.columns]:
            # getting rows of data with leading spaces
            detected_leading_spaces = self.df[column].astype(str).str.match(leading_spaces_pattern, na=False)
            # getting rows of data with trailing spaces
            detected_trailing_spaces = self.df[column].astype(str).str.match(trailing_spaces_pattern, na=False)
            # getting rows of data with leading and trailing spaces
            detected_leading_and_trailing_spaces = self.df[column].astype(str).str.match(leading_and_trailing_spaces_pattern, na=False)

            mask = detected_trailing_spaces | detected_leading_spaces | detected_leading_and_trailing_spaces

            # getting rows of the data with leading and trailing spaces and removing the spaces
            self.df.loc[mask, column] = self.df.loc[mask, column].astype(str).str.strip()
            
        return self.df




