from ..utils.Logger import datalab_logger

import pandas as pd

logger = datalab_logger(name = __name__.split('.')[-1])

class DirtyDataDiagnosis:

    def __init__(self, df: pd.DataFrame, columns: list = None):
        '''
        Initialising the Dirty Data Diagnosis
        '''

        self.df = df
     
        if columns is not None:
            self.columns = [column for column in columns if column in self.df.columns]
        else:
            self.columns = self.df.columns
    
        logger.info(f'Dirty Data Diagnosis initialized with columns: {self.columns.tolist()}')
        
        
    def detect_clean_numerical_data(self):

        logger.info('Detecting clean numerical data....')

        # creating an empty dictionary
        clean_numbers = {}

        for column in self.df[self.columns]:

            clean_numbers[column] = self.df[self.df[column].astype(str).str.match(r'^[+-]?\d+(\.\d+)?$')]

        return clean_numbers
        


