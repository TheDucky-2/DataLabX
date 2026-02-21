# **Data Diagnosis**

Imagine you’re about to cook a meal. 

Before you even start, you check the ingredients to make sure:

- Nothing is missing
- Nothing is spoiled
- Everything is in the right place
- You know what each ingredient is 

**Data diagnosis** means the same thing for your data.

It means checking your data to see:

- The summary of your data
- If there are any duplicates
- If there are missing values in your data
- Some numbers look wrong
- The data is in the wrong format
- Whether data is numbers, text, or date-time
- If anything looks unusual or suspicious

> Data Diagnosis is required because if your data is 'sick', anything you build using it (like visualizations, analysis, or predictions) will be unreliable.

## What Can I Diagnose?

datalabx allows you to diagnose your data by dividing Diagnosis into 5 different categories:

| Category            | Class Name             | What it Diagnoses                                                                 |
|---------------------|------------------------|------------------------------------------------------------------------------------|
| Overall DataFrame   | Diagnosis              | Preview, Shape, Summary, Duplicates, Types (Data, Column), Cardinality, Memory Usage |
| Missing Values      | MissingnessDiagnosis   | Missing counts, missing structure                                                   |
| Numeric Columns     | NumericalDiagnosis     | Stats, distributions, outliers                                                     |
| Categorical Columns | CategoricalDiagnosis   | Unique values, frequencies                                                          |
| Datetime Columns    | DatetimeDiagnosis      | Time patterns, completeness                                                         | 
| Dirty Data          | DirtyDataDiagnosis     | Inconsistencies or formatting issues with the Numerical, Text or Datetime Data      |

This section focuses specifically on the **Diagnosis** class.

## Diagnosis Overview:

Diagnosis in datalabx refers to the diagnosis(check-up) of overall DataFrame.

Diagnosis helps you to see:

- Preview of Data
- Summary of your Data
- Memory Usage
- Column Types (whether a column is Numerical, Categorical or Datetime)
- Number of Duplicates
- What Duplicate values exist
- Unique values 
- Cardinality (How many unique values are present in a column of your DataFrame).
- Separation of Column Types

### **datalabx Usage**:

You can import Diagnosis class directly from datalabx:

    from datalabx import Diagnosis

    diagnosis = Diagnosis(df)

## 1. Data Preview:

Data preview shows the first N rows of your DataFrame.

### Why is this useful?

It helps you verify:

- If your data is loaded correctly

- Column Names and Types

- Obvious issues (strange values, wrong data types, missing values, formatting issues, dirty text data)

### **datalabx Usage**:

You can look at N number of rows of your data by using the ``data_preview()`` method from the Diagnosis class of datalabx.

This method by default shows first 10 rows of your DataFrame.

However, you can pass in a parameter *'number_of_rows'* in the method too. 

Example:

    diagnosis.data_preview()   -> Shows first 10 rows by default.
    
    diagnosis.data_preview(5) -> Shows first 5 rows.


## 2. Data Summary:

Summary of data in datalabx refers to:

1. Shape of Data (number of rows and columns)
2. Column Names
3. Data Types (whether int, float, str, bool, datetime or category)
4. Index (like house no. of each row of your DataFrame)

### **datalabx Usage:**

You can check the summary of your data by using the ``data_summary()`` method from the Diagnosis class of datalabx.

Example:

    summary = diagnosis.data_summary() 

This function returns a dictionary. 

>   summary['shape'] 

    (1000000, 9)
    
>   summary['columns'] 

    ['age','income','expenses','savings','loan_amount','credit_score','num_of_dependents','years_at_job','risk_score']

>   summary['index']

    RangeIndex(start=0, stop=1000000, step=1)

>   summary['dtypes']

    age                  float64
    income               float64
    expenses             float64
    savings              float64
    loan_amount           object
    credit_score         float64
    num_of_dependents    float64
    years_at_job         float64
    risk_score           float64
    dtype: object


## 3. Detecting Column Types

datalabx can automatically detect:

- Numerical columns
- Categorical columns
- Datetime columns

This helps you identify incorrect types (User ID 12345 detected as Numerical column (numbers)).

### **datalabx Usage:**

You can detect column types by using the ``detect_column_types()`` method from the Diagnosis class of datalabx.

    diagnosis.detect_column_types()

This function returns a dictionary of column names and their detected column type.

    {'Numerical':   ['age', 'income','expenses','savings','credit_score, 'num_of_dependents','years_at_job','risk_score'],
     'Datetime':    [],
     'Categorical': ['loan_amount']}

## Memory Usage:

Memory Usage refers to how much RAM the DataFrame uses.

### **datalabx Usage:**

You can check the memory usage by using the ``memory_usage()`` method from the Diagnosis class of datalabx.

Example:

    diagnosis.show_memory_usage()

This function does not return anything, but shows memory usage in MB.

## Cardinality:

In data, cardinality means how many different kinds of values are in a column.

Imagine you have a list of your favorite colors in one column:

Example:

**Colors**

Red

Blue

Red

Green

Yellow

Even though there are 5 rows, there are only 4 different colors.

So the cardinality is 4.

***IMPORTANT:***

Even though cardinality is usually used in Categorical data, however, it can be used for all categories of data.

### Low Cardinality

If a column has a few different values -> low cardinality

Example: 

    Gender: 'Male', 'Female', 'Other'

***IMPORTANT:***

If a column has low cardinality, it is easier for a Machine Learning model to learn from it, since there are only a few values to learn from.

### High Cardinality

If a column has many different values -> high cardinality

Example: 

    Every person has a different 'User ID'.
    Every transaction has a different 'Transaction ID'.

***IMPORTANT:***

If a column has high cardinality, the Machine Learning model may get confused or learn incorrect patterns, since each value is different.

### **datalabx Usage:**

You can check the cardinality by using the ``show_cardinality()`` method from the Diagnosis class of datalabx.

Example:

    diagnosis.show_cardinality()

This function returns a dictionary of column names and number of unique values in that column.

    {'age': 64,
    'income': 944772,
    'expenses': 935530,
    'savings': 920519,
    'loan_amount': 920609,
    'credit_score': 941267,
    'num_of_dependents': 7,
    'years_at_job': 42,
    'risk_score': 517721}

## Separation of Column Types

Sepration of column types refers to separating specific type of columns - Numerical, Categorical or Datetime from rest of the DataFrame.

This leads to easy exploration and understanding of your data, one type at a time.

You can read more about why it is important in **Column Type Detection & Conversion** docs under **Workflow Docs** section of datalabx.

Let us now explore how we can do that using datalabx:

### **datalabx Usage:**

#### Numerical Column Types (Numbers):

We can separate Numerical columns from rest of the DataFrame by using ``get_numerical_columns()`` from Diagnosis class.

Example:
    
    diagnosis.get_numerical_columns()

This function returns a pandas DataFrame of only numeric columns.

    | age        | income      | expenses       | debt           | score        | savings_ratio |
    |------------|-------------|----------------|----------------|--------------|---------------|
    | 45.960570  | NaN         | 21337.207586   | 2,077,881.000  | 49.015508    | 0.431159      |
    | 38.340828  | 17182.443452| 3621.209282    | 3,752.960      | 60.759049    | 0.789249      |
    | NaN        | 23497.048535| 16516.059771   | NaN            | NaN          | 0.297101      |


#### Categorical Column Types (Categories or Text)

We can separate Categorical columns from rest of the DataFrame by using ``get_categorical_columns()`` from Diagnosis class.

Example:

    diagnosis.get_categorical_columns()

This function returns a pandas DataFrame of only categorical columns.

    | gender | region | membership_type | subscription_status |
    | ------ | ------ | --------------- | ------------------- |
    | M      | East   | vip             | inactive            |
    | M      | East   | basic           | active              |
    | M      | East   | basic           | active              |

#### Datetime Column Types (Dates and Timestamps)

We can separate Datetime columns from rest of the DataFrame by using ``get_datetime_columns()`` from Diagnosis class.

Example:

    diagnosis.get_datetime_columns()

This function returns a pandas DataFrame of only datetime columns.

    | signup_date | last_active |
    | ----------- | ----------- |
    | 2019-10-23  | 2019-11-05  |
    | 2019-10-14  | 2021-04-11  |
    | 2015-05-07  | 2017-02-09  |

## Summary:

- Data diagnosis is a health check up for your dataset -> it helps you understand structure, types, missing values, duplicates, and suspicious patterns before doing any analysis.

- Incorrect data types lead to incorrect results -> numbers, categories, and dates must be identified and handled differently.

- Diagnosis helps you catch problems early -> messy values, high cardinality, memory issues, and wrong formats can silently break your workflows.

- A clean diagnosis leads to reliable insights -> once your data is understood and verified, cleaning, visualization, and analysis become safer and more meaningful.















































