
'''
Normalization:
--------------

Normalizing your data means rescaling numerical values to a defined, smaller range — 
typically [0, 1] or sometimes [-1, 1].

This ensures that all features contribute equally to model training and prevents features with large numeric ranges from dominating.
Like a feature with range between [1, 100] would not be dominated in model training by a feature with range between [-infinity, infinity]

Normalization is applied separately to each feature (numerical column) of the dataframe.

Example:

    data = [10, 20, 30, 60, 100]

    Suppose we want to normalize all values between 0 and 1. 

    One simple approach is to divide each value by the maximum value (100 in this case):

        [10, 20, 30, 60, 100] / 100 = [0.1, 0.2, 0.3, 0.6, 1.0]

    Now the data has been normalized within range [0, 1].

Note:
    - This simple dividing-by-maximum method works when the data is strictly positive.
      It does not work for data with neagtive values.

    - A more general approach is Min-Max normalization, using the formula:

        For each feature X,

        X' = (each value of X - minimum value of X) / (maximum value of X - mimumum value of X)

        or simply, 

        X' = (X - min) / (max - min)

      Min-Max normalization can handle data with arbitrary minimum and maximum values.
'''
