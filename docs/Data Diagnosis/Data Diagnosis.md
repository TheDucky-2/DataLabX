# **Data Diagnosis**
-----------------
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

Data Diagnosis is required because if your data is 'sick', anything you build using it (like visualizations, analysis, or predictions) will be unreliable.

## What Can I Diagnose?
------------------------

DataLab allows you to diagnose your data by dividing Diagnosis into 5 different categories:

| Category            | Class Name             | What it Diagnoses                                                                 |
|---------------------|------------------------|------------------------------------------------------------------------------------|
| Overall DataFrame   | Diagnosis              | Preview, Shape, Summary, Duplicates, Types (Data, Column), Cardinality, Memory Usage |
| Missing Values      | MissingnessDiagnosis   | Missing counts, missing structure                                                   |
| Numeric Columns     | NumericalDiagnosis     | Stats, distributions, outliers                                                     |
| Categorical Columns | CategoricalDiagnosis   | Unique values, frequencies                                                          |
| Datetime Columns    | DatetimeDiagnosis      | Time patterns, completeness                                                         |

This section focuses specifically on the **Diagnosis** class.

## Diagnosis Overview:
-----------------------

Diagnosis in DataLab refers to the diagnosis(check-up) of overall DataFrame.

Diagnosis helps you to see:

- Preview of Data
- Summary of your Data
- Memory Usage
- Column Types (whether a column is Numerical, Categorical or Datetime)
- Number of Duplicates
- What Duplicate values exist
- Unique values 
- Cardinality (How many unique values are present in a column of your DataFrame).

### **DataLab Usage**:

You can import Diagnosis class directly from DataLab:

    from DataLab import Diagnosis

    diagnosis = Diagnosis(df)

## 1. Data Preview:
-------------------

Data preview shows the first N rows of your DataFrame.

### Why is this useful?

It helps you verify:

- If your data is loaded correctly

- Column Names and Types

- Obvious issues (strange values, wrong data types, missing values, formatting issues, dirty text data)

### **DataLab Usage**:

You can look at N number of rows of your data by using the ``data_preview()`` method from the Diagnosis class of DataLab.

This method by default shows first 10 rows of your DataFrame.

However, you can pass in a parameter *'number_of_rows'* in the method too. 

Example:

    diagnosis.data_preview()   -> Shows first 10 rows by default.
    
    diagnosis.data_preview(5) -> Shows first 5 rows.


## 2. Data Summary:
-------------------

Summary of data in DataLab refers to:

1. Shape of Data (number of rows and columns)
2. Column Names
3. Data Types (whether int, float, str, bool, datetime or category)
4. Index (like house no. of each row of your DataFrame)

### **DataLab Usage:**

You can check the summary of your data by using the ``data_summary()`` method from the Diagnosis class of DataLab.

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
------------------------- 

DataLab can automatically detect:

- Numerical columns
- Categorical columns
- Datetime columns

This helps you identify incorrect types (User ID 12345 detected as Numerical column (numbers)).

### **DataLab Usage:**

You can detect column types by using the ``detect_column_types()`` method from the Diagnosis class of DataLab.

    diagnosis.detect_column_types()

This function returns a dictionary of column names and their detected column type.

    {'Numerical':   ['age', 'income','expenses','savings','credit_score, 'num_of_dependents','years_at_job','risk_score'],
     'Datetime':    [],
     'Categorical': ['loan_amount']}

## Memory Usage:
----------------

Memory Usage refers to how much RAM the DataFrame uses.

### **DataLab Usage:**

You can check the memory usage by using the ``memory_usage()`` method from the Diagnosis class of DataLab.

Example:

    Diagnosis(df).show_memory_usage()

This function does not return anything, but shows memory usage in MB.

## Cardinality:
---------------

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
-------------------
If a column has a few different values -> low cardinality

Example: 

    Gender: 'Male', 'Female', 'Other'

***IMPORTANT:***

If a column has low cardinality, it is easier for a Machine Learning model to learn from it, since there are only a few values to learn from.

### High Cardinality
--------------------

If a column has many different values -> high cardinality

Example: 

    Every person has a different 'User ID'.
    Every transaction has a different 'Transaction ID'.

***IMPORTANT:***

If a column has high cardinality, the Machine Learning model may get confused or learn incorrect patterns, since each value is different.

### **DataLab Usage:**

You can check the cardinality by using the ``show_cardinality()`` method from the Diagnosis class of DataLab.

Example:

    Diagnosis(df).show_cardinality()

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
















































