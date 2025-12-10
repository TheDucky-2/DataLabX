# One-Hot Encoding:
-------------------
One-Hot encoding is a way to turn categorical values (like colors, gender, cities, Ratings, etc.) into numbers so machine-learning models can understand them.

### **IMPORTANT NOTE**:

One-Hot encoding does not work with categories that have an order. 

Examples of Order: 

``Ratings: Low < Medium < High``

``Education: High School < Bachelors < Masters < PhD``

Examples of No Order:

Cities: ['Sydney', 'Berlin', 'New York', 'London', 'Tokyo', 'New Delhi'] 

Colors:  ['Red', 'Blue', 'Green', 'Black', 'White', 'Grey'] does not have an order.

### How does it work?

Let's say we have a category called colors.

colors = ['Red', 'Blue', 'Green', 'Black', 'White', 'Grey']

Now, computers and ML models can’t work directly with words like these. They work with numbers.
So, one-hot encoding creates a new column for each category and tags it as:

1 → if the category exists in that row

0 → if it does not exist in that row

It’s basically like asking:

'Is this row Red?'  -> yes (1) or no (0)
'Is this row Blue?' -> yes (1) or no (0)

One-hot encoding converts the category that exists into 1, and the category that does not exist into 0.

Notice that it creates one column per category!

    Color	Red	    Green	Blue  Black  Grey  White 
    Red	    1	    0	    0       0     0      0 
    Blue	0	    0	    1       0     0      0 
    Green	0	    1	    0       0     0      0
    Black   0       0       0       1     0      0
    White   0       0       0       0     0      1
    Grey    0       0       0       0     1      0

### When to Use One-Hot Encoding:

1. When there is no order (no category is greater than another)
2. When the number of categories is small to moderate. (Ideally < 100)
3. When you are using ML models that expect numerical, non-ordered inputs. E.g: Linear Regression, Naive Bayes, SVM, Tree models.

### When to Avoid One-Hot Encoding:

1. When there is an order (a category is greater than another)
2. When the number of unique categories is high. (> 500 unique values) 
3. When you are using models that already handle categorical data. E.g: LightGBM, H2O, CatBoost etc.
4. When you need low-dimensional data (not many columns) that is dense (does not have a lot of zeroes).

### DataLab Usage:

You can apply one-hot encoding to your nominal categorical data by using one_hot_encoding() method from CategoricalPreprocessor module.

**Example:**

    from DataLab import CategoricalPreprocessor

    categorical_preprocessor = CategoricalPreprocessor(df)

    categorical_preprocessor.one_hot_encoding(columns = ['Gender', 'City', 'Country'])

This applies one-hot encoding to the gender, city and country columns of the DataFrame







