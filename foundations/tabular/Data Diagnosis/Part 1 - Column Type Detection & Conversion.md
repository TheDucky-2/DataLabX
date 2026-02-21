# **Part 1 - Column Type Detection & Conversion**

**Column Type Detection and Conversion** refers to detecting what type of columns we are working with, in our dataset and converting incorrectly identified columns into correct ones.

## Why is it Important?

This is important because incorrectly identified columns lead to:

- Incorrect results when numbers are identified as text, and we try to do math on them.
- Inaccurate analysis, visualization and even cleaning operations will fail.
- Date operations fail if dates are not correctly identified as they are usually written in a specific format.
- Conversion of values into missing data

## **datalabx Usage:**

**Example:**

Let's say we have this **Sample Messy Dataset:**

|   | age                | income             | expenses            | debt               | score               | savings_ratio       | gender | region | membership_type | subscription_status | signup_date | last_active |
|---|------------------|------------------|-------------------|-----------------|------------------|------------------|--------|--------|----------------|------------------|-------------|-------------|
| 0 | 45.960569836134795 | tpUwb             | 21337.20758558362 | 2077881.1645985672 | 49.015507649186574 | 0.43115855636906564 | M      | East   | vip            | inactive          | 2019-10-23 | 2019-11-05 |
| 1 | 38.340828385945784 | 17182.44345210847 | 3621.2092817197617 | 3752.959576902923 | 60.75904929703295 | 0.7892494573421452  | M      | East   | basic          | active            | 2019-10-14 | 2021-04-11 |
| 2 | NXlMl             | 23497.04853541588 | 16516.059770785752 | NaN               | NaN               | 0.29710066581800887 | M      | East   | basic          | active            | 2015-05-07 | 2017-02-09 |
| 3 | 58.2763582768963  | 10510.744673253303 | 8219.049415817683 | 9614.040727545927 | 70.71124084031835 | 0.2180335769422026  | F      | West   | basic          | active            | 2013-10-06 | 2015-03-22 |
| 4 | 37.19015950331997 | 18865.239961809577 | NaN               | 11116.85061890834 | 34.32423437519151 | NaN                | M      | West   | basic          | active            | INVALID     | INVALID     |

<br>

We can see that first 6 columns are numbers, next 4 are texts (categories) and the remaining 2 are dates.

However, let us detect what is the type of each column in the default dataset:

## Column Type Detection

We can detect what type of columns we have in our DataFrame using ``detect_column_types()`` method from Diagnosis class.

This function returns a dictionary of columns and their column type.

Example:

    Diagnosis(df).detect_column_types()

This function returns a dictionary of columns and their column type.

    {'Numerical': [],
    'Datetime': [],
    'Categorical': ['age',
    'income',
    'expenses',
    'debt',
    'score',
    'savings_ratio',
    'gender',
    'region',
    'membership_type',
    'subscription_status',
    'signup_date',
    'last_active']}

We can see that all columns have been identified as **Categorical** type columns.

However, when we compare this to the preview of our DataFrame, we can see that some of them are **Numerical**, some are **Categorical** and a few **Datetime** type columns.

Following are the correct types of columns in the DataFrame:

    Numerical: ['age', 'income', 'expenses', 'debt', 'score', 'savings_ratio']

    Categorical: ['gender', 'region', 'membership_type', 'subscription_status']

    Datetime: ['signup_date', 'last_active']

## Column Type Conversion

We can convert the incorrectly identified column types to correct ones, by importing the ``ColumnConverter`` class from datalabx.

    from datalabx import ColumnConverter

#### **IMPORTANT:**

All classes in datalabx, whether they are the Column Converters, Backend Converters, Data Visualizers, Cleaners, Preprocessors, or Diagnosis etc..

All of them accept specific columns you wish to work with, otherwise, they apply operations to all columns of the DataFrame.

And for this dataset, we definitely may not be doing that, otherwise everything that is not a number, will be converted into NAN (Not a Number).

That is why we will be directly mentioning the list of columns we wish to convert to these specific column types - **Numerical**, **Categorical** or **Datetime**.

### Numerical Type Conversion:

To convert incorrectly identified columns into numerical columns, we will be using ``to_numerical()`` method, from ``ColumnConverter`` class of datalabx.

This returns a pandas DataFrame with the selected columns converted to numeric. Non-numeric values are left as it is.
    
    # passing a list of numerical columns that were incorrectly identified

    df = ColumnConverter(df, columns=['age', 'income', 'expenses', 'debt', 'score', 'savings_ratio']).to_numerical()

We can now verify that by checking column types:

    Diagnosis(df).detect_column_types()

Output:

    {'Numerical': ['age', 'income', 'expenses', 'debt', 'score', 'savings_ratio'],
    'Datetime': [],
    'Categorical': ['gender',
    'region',
    'membership_type',
    'subscription_status',
    'signup_date',
    'last_active']}

**Great!**

We have been able to successfully perform numerical type conversion.

### Categorical Type Conversion:

To convert incorrectly identified columns into categorical columns, we will be using ``to_categorical()`` method, from ``ColumnConverter`` class of datalabx.

This returns a pandas DataFrame with the selected columns converted to categorical. Non-categorical values are left as it is.

Even though the categorical columns in the **Sample Messy Dataset** are already correctly identified, we will be using another tiny example to understand it.

**Sample Categorical Dataset**

| customer_id | zip_code | store_id | product_code | order_date | status_code |
| ----------: | -------: | -------: | -----------: | ---------- | ----------: |
|           1 |    02139 |      101 |         1001 | 2023-01-05 |           1 |
|           2 |    94107 |      102 |         1002 | 2023-01-06 |           2 |
|           3 |    02139 |      101 |         1003 | 2023-01-06 |           1 |
|           4 |    30301 |      103 |         1001 | 2023-01-07 |           3 |
|           5 |    94107 |      102 |         1002 | 2023-01-07 |           2 |

We can see that this dataset is all about numbers, but, would it be reasonable to do maths on these numbers?

Like, can we even add or subtract these numbers? The simple answer is... No.

Because we know that anything that is used to identify someone, like **employee id**, is just a unique number given to identify the employee in the company's systems.

You cannot really subtract my employee id from yours or add mine to yours, they are just unique identifications for you and I.

And that unique identification is what is a **Category**.

In our Dataset, all the columns are Categories, as they are unique identifications (like zip code of your city).

Let us detect what are the types of these columns in the sample dataset:

    Diagnosis(df).detect_column_types()

Output:
    
    {'Numerical': ['customer_id',
    'zip_code',
    'store_id',
    'product_code',
    'status_code'],
    'Datetime': [],
    'Categorical': ['order_date']}

We can see all of these categorical columns have been incorrectly identified as numerical, just because they are numbers.

Let us convert them to categorical columns by using the ``to_categorical()`` method:

    # passing a list of categorical columns that were incorrectly identified

    df = ColumnConverter(df, columns=['customer_id','zip_code','store_id','product_code','status_code']).to_categorical()

Let us now verify that the columns we passed in, have been converted to Categorical type.

    Diagnosis(df).detect_column_types()

Output:

    {'Numerical': [],
    'Datetime': [],
    'Categorical': ['customer_id',
    'zip_code',
    'store_id',
    'product_code',
    'order_date',
    'status_code']}

**Great!**

We have also been able to successfully perform categorical type conversion.

However, we can see that the column 'order_date' is not a category, but a datetime type column.

Let us move onto how we can do that...

### Datetime Type Conversion:

To convert incorrectly identified columns into date-time columns, we will be using ``to_datetime()`` method, from ``ColumnConverter`` class of datalabx.

This returns a pandas DataFrame with the selected columns converted to date-time. Non-datetime values are left as it is.
    
    # passing a list of datetime columns that were incorrectly identified

    df = ColumnConverter(df, columns=['order_date']).to_datetime()

We can now verify that column has been converted into date-time type by checking column types:

    Diagnosis(df).detect_column_types()

Output:

    {'Numerical': [],
    'Datetime': ['order_date'],
    'Categorical': ['customer_id',
    'zip_code',
    'store_id',
    'product_code',
    'status_code']}

**Great!**

We have been able to successfully perform datetime type conversion.

However, there is something very important that we will explore in **Part 2 - Column Type Detection & Conversion** docs.

## Summary:

- Numbers dont always mean we are dealing with Numerical data

- IDs are categories

- Dates must be separated

- Always verify after column type conversion
