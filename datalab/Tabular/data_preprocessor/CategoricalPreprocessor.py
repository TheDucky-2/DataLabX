import pandas as pd
from .DataPreprocessor import DataPreprocessor

class CategoricalPreprocessor(DataPreprocessor):

    def __init__(self, df:pd.DataFrame, columns: list|type(None) = None):

        super().__init__(df, columns)

        self.df = df.select_dtypes(include= ['object', 'string', 'category'])

        if columns is not None:
            self.columns = [column for column in df.columns if column in self.df.columns]
        else:
            self.columns = df.columns

    def one_hot_encoding(self, columns_to_encode=None):
        '''
        Applies One-Hot Encoding to each column of the DataFrame (1 for category that exist, 0 for category that does not exist)

        Parameters:

            Optional:

                columns_to_encode: str or type(None) (default is None)

        Returns:
        -------
            df : pd.DataFrame
                A pandas DataFrame of rows with empty strings.
        
        Usage Recommendation:
        ---------------------
            1. Use this function when your categorical data does not have an order. 

                E.g. Gender: [''Male', 'Female', 'Other'] does not have an order
                E.g. Categories: ['Clothing', 'Sports', 'Cosmetics', 'Electronics'] do not have an order

            2. Use this function when your column does not have more than 100 unique categories.
            That is because this function creates a separate column for each category.

        Considerations:
        ---------------
            This function converts values to binary integer datatype (0 or 1)

        Example:
        --------
            CategoricalPreprocessor(df).one_hot_encoding(columns_to_encode=['gender', 'city'])
        
        '''

        if columns_to_encode:

            columns_to_encode = columns_to_encode
        
        else:
            columns_to_encode = self.columns

        return pd.get_dummies(self.df, columns = columns_to_encode, dtype=int)
