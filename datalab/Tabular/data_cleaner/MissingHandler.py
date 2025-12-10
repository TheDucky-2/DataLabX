from .BaseCleaner import DataCleaner
import pandas as pd
import numpy as np
import matplotlib
import missingno as msno

class MissingHandler(DataCleaner):

    def __init__(self, df, columns=None):
        super().__init__(df, columns)

        self.df = df.copy()
        
        if columns is None:
            self.columns = self.df.columns.to_list()
        else:
            self.columns = columns
    
    def missing_data_guide(self)-> dict:
        
        '''
        Just a guide function for assistance in handling missing data of your DataFrame

            Parameters:
                df : pd.DataFrame
                    A pandas DataFrame

            Returns:
                dict
                1. viz_guide         : It is intended to help user with reading and interpreting the missing data visualizations
                2. missingness_guide : It is a guide that recommends what actions to take when dealing with different percentages of missing data

            Usage Recommendations:
                1. Use this function along with visualize_missing() function

            Considerations:
                1. This function uses missingno library under the hood. Just make sure you have it installed or use 'pip install missingno'
                2. For assistance with handling missing values, use visualize_missing() along with this function for better decision making.
                3. If you get an issue while viewing the full output in your Jupyter notebook, choose the option of viewing as 'scrollable element'

            EXTRAS:
                This section includes a section of code you can use to visualize the viz_guide dictionary in a nice looking format.

                    for key, doc in viz_guide.items():
                        print(f'📊 {key.upper()} VISUALIZATION')
                        print('-' * (len(key) + 18))
                        print(doc.strip())
                        print('\n' + "="*60 + '\n')

        '''

        viz_guide = {

        'bar': 
            '''
            Shows count of non-missing values per column

            1. Short bars mean many missing values
            2. Complete bars mean less missing values
            ''',

        'matrix': 
            '''
            Shows missingness in rows

            1. Many vertical white lines mean many null values in a column. E.g: Many values missing in the 'Last_Name' column of the DataFrame
            2. Horizontally stacked lines mean rows with multiple null values. E.g: Missing values in columns 'age', 'income', 'education' for customer 'Alice'
            ''',

        'heatmap':
            '''
            Shows a heatmap of how missing values in your columns are related.

            1. Each square shows how often two columns are missing data at the same time.
                - Light or white colors mean the missing values happen independently.
                - Bright or darker colors mean the columns are often missing together.

            2. If your heatmap looks mostly white:
                → Missing values across columns are random. You can handle each column separately.

            3. If you see colored blocks or groups (clusters):
                → Some columns lose data together. Try cleaning or filling them as a group.
            ''',

        'dendrogram':
            '''
            Shows how columns group together based on similar missing value patterns.

            1. Columns that are close together in the tree tend to have missing values in the same rows. Columns far apart have different missing patterns.

            2. If you see columns joined closely:
                → They often lose data together. Consider cleaning or filling them as a group.

            3. If most columns are separate:
                → Their missing values are unrelated. You can handle each column independently.
            '''
            }

        missingness_guide = {  # numbers denote percentage of missing values

        'Under 5' : ['Missingness is Low', 'Filling with mean/median/mode'],
        '5 - 20': ['Keep these columns since they are manageable', 'Fill (Impute) them carefully'],
        '20 - 40': ['Missingness is Medium', 'Drop columns if not important'],
        '40 - 50': ['High missingness', 'Drop columns unless very very important'],
        'Over 50': ['Very sparse', 'Always drop these columns']

            }
        print(f'\nmissing data guide returns a tuple of dictionaries missingness_viz_guide and missingness_handling_guide')
        return viz_guide, missingness_guide

    def replace_missing(self, to_replace: list[str| float| type(np.nan)], replace_with: str|float|int, **kwargs: dict) -> pd.DataFrame:
        '''
        Replace missing values of categorical columns like 'ERROR', 'MISSING', 'UNKNOWN' etc. with any value of choice

        Parameters:
            df          : a pandas DataFrame
            columns     : a python list of columns you wish to replace values of. It can also be a list of a single column
            to_replace  : a python list of strings/np.nan you wish to replace. Example: ['NA', 'ERROR', 'MISSING', np.nan]
            replace_with: a python string or np.nan you wish to replace with
            kwargs**    : a python dictionary of extra keyword arguments, like regex=True

        Returns:
            a pandas DataFrame of columns with replaced values.

        Usage Recommendation:
            Use this function when you want to replace missing values (NA) across multiple columns, that are not just np.nan. 
            Missing values could include values like ['ERROR', 'UNKNOWN', 'MISSING', 'NA', 'Null', None]

        Considerations:
            This function is intended to replace missing values with 1 single value. 
            If you wish to apply methods like mean, median or mode or other imputation methods, use fill_with_mean, fill_with_median etc.


        Example:
        >>>    replace_na(df, ['Items'], ['ERROR', 'UNKNOWN', 'MISSING', 'NA', 'Null', None], np.nan) --> turns everything into np.nan
        >>>    replace_na(df, ['Items', 'Payment Method', 'Location'], ['ERROR', 'UNKNOWN', 'MISSING', 'NA', 'Null', None], 'Missing') -> turns everything into string 'NA'
            
        '''
        self.to_replace = to_replace
        self.replace_with = replace_with

        if not isinstance(self.to_replace, (list)):
            raise TypeError(f'to_replace must be a list of strings or np.nan, got {type(self.to_replace).__name__}')

        if not isinstance(self.replace_with, (pd.Series, str, type(None), float, int)):
            raise TypeError(f'replace_with must be a string, None, float or int, got {type(self.replace_with).__name__}')

        self.df[self.columns] = self.df[self.columns].replace(self.to_replace, self.replace_with, **kwargs)

        return self.df

    def drop_missing_columns(self, **kwargs):
        '''

        Usage Recommendation:
            1. Use this function when a high number of missing values are present in a particular column
            2. Use this function when the column is irrelevant for your analysis or modeling 
            3. DO NOT USE this function to drop columns that are important but may have a high number of missing values. E.g: [Salary, Income Tax]

        Considerations:
           
        
        '''
        return self.df[self.columns].dropna(axis=1, **kwargs)

    def drop_missing_rows(self, **kwargs):
        
        '''
        Usage Recommendation:
            1. Use this function when number of rows missing data is low (less than 5 - 10%).
            2. Use this function when losing a tiny bit of data won't hurt your analysis or modeling (you have a lot of data!).
            3. Use this function when missingness of data is random (values in one column dont increase or decrease with values in another)
            4. DO NOT USE this function when missingness is correlated

        Considerations:
            Be careful while dropping rows since we do not want to lose data that matters in one column even if irrelevant in another. 
            
        
        '''
        return self.df[self.columns].dropna(**kwargs)

    def fill_with_mean(self):
        '''
        Replace missing values with mean values for numerical column of a DataFrame

        Returns:
            a pandas Series or a pandas DataFrame of numerical columns replaced with mean value of the column.

        Usage Recommendation:
            1. Use this function if distribution of the numerical column is roughly normal (bell-curve) and missingness is low (5 - 10 %).
            2. DO NOT USE this function if your data is heavily skewed or has strong outliers.

        Considerations:
            Mean is sensitive to outliers, so if your data is skewed, use fill_with_median or other methods

        Example:

            df['credit_score'] = [734.97, 734.78, np.nan, 712.21, 686.13]

            MissingHandler(df, ['credit_score']).fill_with_mean()

        ->  df['credit_score'] = [734.97, 734.78, 717.02, 712.21, 686.13]

        '''
        return self.df[self.columns].fillna(self.df[self.columns].mean())

    def fill_with_median(self):
        '''
        Replace missing values with median (middle) values for numerical column of a DataFrame

        Returns:
            a pandas Series or a pandas DataFrame of numerical columns replaced with median value of the column.

        Usage Recommendation:
            1. Use this function if distribution of the numerical column is skewed.
            2. Use this function if your data has strong outliers.
            3. Use this function for continous numerical variables.

        Considerations:
            If your data has normal distribution or does not have outliers, use fill_with_mean instead

        Example:

            df['savings'] = [14173.3,37970.2,24008.95,np.nan,17063.67,57161.76,np.nan,5927.63,28954.98,5553.7]

            MissingHandler(df, ['savings']).fill_with_median()

        ->  df['savings'] = [14173.3, 37970.2, 24008.95, 20536.30, 17063.67, 57161.76, 20536.30, 5927.63, 28954.98, 5553.7]

        '''
        return self.df[self.columns].fillna(self.df[self.columns].median())

        
        