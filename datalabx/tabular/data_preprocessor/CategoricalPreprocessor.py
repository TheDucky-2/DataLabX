"""Preprocesses Categorical Data in a DataFrame"""

import pandas as pd
from .DataPreprocessor import DataPreprocessor
from ..utils.Logger import datalabx_logger

logger = datalabx_logger(name = __name__.split('.')[-1])

class CategoricalPreprocessor(DataPreprocessor):
    """
    Initializing the Categorical Preprocessor.

    Parameters
    -----------
    df: pd.DataFrame
        A pandas Dataframe you wish to diagnose.

    columns: list, optional
        A list of columns you wish to preprocess, by default None.
    """

    def __init__(self, df:pd.DataFrame, columns: list|type(None) = None):

        super().__init__(df, columns)

        self.df = df.select_dtypes(include= ['object', 'string', 'category'])

        if columns is None:
            self.columns = df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns]

        logger.info('Categorical Preprocessor initialized.')

    def one_hot_encoding(self)-> pd.DataFrame:
        """
        Applies One-Hot Encoding (1 for category that exist, 0 for category that does not exist).

        Returns:
        -------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            1. Use this function when your categorical data does not have an order.

                E.g. Gender: [''Male', 'Female', 'Other'] does not have an order
                E.g. Categories: ['Clothing', 'Sports', 'Cosmetics', 'Electronics'] do not have an order

            2. Use this function when your column does not have more than 100 unique categories.
                That is because this function creates a separate column for each category.

        Considerations
        ---------------
            This function converts values to binary integer datatype (0 or 1)

        Example
        --------
        >>>  CategoricalPreprocessor(df, ['gender', 'city']).one_hot_encoding()
        """

        return pd.get_dummies(self.df[self.columns], dtype=int)

    def label_encoding(self)-> pd.DataFrame:
        """
        Applies Label Encoding (converts each category to a unique integer).

        Returns
        -------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            Use this function when your categorical data **DOES NOT HAVE AN ORDER**.

            E.g. Gender: ['Male', 'Female', 'Other'] does not have an order
            E.g. Categories: ['Clothing', 'Sports', 'Cosmetics', 'Electronics'] do not have an order

        Considerations
        ---------------
            1. This method is NOT recommended for linear models if the numbers might be treated as ordinal.
            2. Always keep track of the mapping to decode back if needed.

        Example
        --------
        >>> CategoricalPreprocessor(df, ['gender', 'city']).label_encoding()
        """
        from sklearn.preprocessing import LabelEncoder

        label_encoder = LabelEncoder()

        encodings= {}

        for col in self.df[self.columns]:

            encodings[col] = label_encoder.fit_transform(self.df[col])

        return pd.DataFrame(encodings)

    def ordinal_encoding(self, order_map: dict|None=None)-> pd.DataFrame:
        """
        Applies Ordinal Encoding (converts each category to a unique integer with an order).

        Parameters
        -----------
        order_map : dict or type None

            A dictionary specifying the desired order for each categorical column.

            Example: 

            order_map = {
            'size': ['Small', 'Medium', 'Large'],
            'rating': ['Poor', 'Average', 'Good', 'Excellent']
            }

        Returns:
        -------
        pd.DataFrame
            A pandas DataFrame

        Usage Recommendation
        ---------------------
            1. Use this function when your categorical data **has a natural order**.

                E.g. Sizes: ['Small', 'Medium', 'Large']
                E.g. Ratings: ['Poor', 'Average', 'Good', 'Excellent']

            2. DO NOT USE this function for Columns that do not have an order.
            3. You must define the **order of categories** when using this function to preserve meaning by using order map.

        Considerations
        ---------------
            1. The numeric values **imply order**, so models or analysis treats them as ranked.
            2. Columns without meaningful order should not use this encoding.
            3. Keep track of the mapping if you need to revert back to original labels.

        Example
        --------
        >>> CategoricalPreprocessor(df, ['size']).ordinal_encoding(order_map={'size':['Small','Medium','Large']})
        """

        if order_map is None:
            logger.info('No order mapping received, hence, no changes made.')
            return self.df

        from sklearn.preprocessing import OrdinalEncoder

        encoder = OrdinalEncoder()

        df = pd.DataFrame(encoder.fit_transform(self.df[self.columns], order_map=order_map))

        df.columns = self.columns

        return df
