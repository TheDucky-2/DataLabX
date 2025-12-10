import pandas as pd
from .BaseCleaner import DataCleaner

class DatetimeCleaner(DataCleaner):

    def __init__(self, df:pd.DataFrame, columns:list=None):
        super().__init__(df, columns)

        self.df = self.df.select_dtypes(include=['datetime'])
        self.columns = [column for column in self.columns if column in self.df.columns]

        print(f'Datetime Cleaner initialized with columns: {self.columns}')

