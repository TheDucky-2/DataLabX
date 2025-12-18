# STEP 1: Finding Missing Data (Missingness Diagnosis)

We are now at the first step of understanding our missing data.

## What is this step about?

This step is simply about ``finding missing types in your data``.

Before fixing or filling missing values, DataLab first checks what data is missing and how it is represented.

Think of this as a **health check-up** of your dataset.

## Why does DataLab check column by column?

DataLab looks for missing values column by column because not all data is the same:

- Numbers (like age or income)
- Text / categories (like gender or country)
- Dates and times (like signup date or last login)

Each type shows missing values differently. 

Because of this, DataLab checks **each column based on its type**, instead of checking the whole table at once.

This makes the results more accurate and easier to understand.

## How DataLab finds missing values

DataLab looks for missing values in three simple steps:

1. Look at the raw data
2. Identify the type of each column (number, text, or date)
3. Find missing values inside each column type

The results are grouped into:

- Numerical missing values
- Categorical missing values
- Datetime missing values

## Two kinds of missing values

DataLab finds **two kinds of missing data** in every column:

### 1. Built‑in missing values (automatic)

These are the values Pandas automatically understands as missing:

- Numbers **->** ``NaN``
- Text **->** ``NaN``, ``None``
- Dates **->** ``NaT``

### 2. Placeholder missing values (user‑defined)

These are values that ``look real but actually mean 'missing'`` in your data, depending on your domain.

Examples:

- Numbers **->** `-1`, `0`, `9999`
- Text **->**  `"UNKNOWN"`, `"?"`, `"MISSING"`
- Dates **->** `"00-00-0000"`

Pandas does NOT treat these as missing by default - so DataLab lets you tell it what to look for.

## **DataLab Usage:**

You can begin diagnosing your missing data by importing the ``MissingnessDiagnosis`` class from DataLab:

       from datalab import MissingnessDiagnosis


## Numerical Missing Data (Numbers)

Numerical columns usually contain missing values like `NaN`.

Sometimes missing numbers are replaced by special values like `-1`, `0`, or `-999`.

You can check what types of missing values are present in Numerical columns by using ``detect_numerical_missing_types()`` method from **MissingnessDiagnosis** class:

       # pass a list of numerical columns or pass a dataframe of only numeric columns

       MissingnessDiagnosis(df, ['age', 'income', 'account_balance']).detect_numerical_missing_types()

Output: 

       {'age': 
              {
               'pandas_missing': [nan], 
               'placeholder_missing': []
              },
       'income':
              {
               'pandas_missing': [nan],
               'placeholder_missing': []
              },
       'account_balance': 
              {
               'pandas_missing': [nan],
               'placeholder_missing': []
              }
       }

We can see that only pandas missing types have been detected as we have not passed anything else that is to be considered missing data.

We can add our own placeholders by passing **extra_placeholders** like this:

Example:

       MissingnessDiagnosis(df).detect_numerical_missing_types(extra_placeholders=[-1, -999])

Output:

       {
       'age': 
                     {
                     'pandas_missing': [nan], 
                     'placeholder_missing': [-999.0, -1.0]
                     },

       'income':
                     {
                     'pandas_missing': [nan],
                     'placeholder_missing': []
                     },

       'account_balance': 
                     {
                     'pandas_missing': [nan],
                     'placeholder_missing': []
                     }
       }

We can see:

- Which numerical columns have missing values
- Whether they are real missing values or placeholders

## Categorical Missing Data (text/category)

Text based columns often contain missing values like `NaN`, 'NULL' or `None`.

Sometimes missing text is written as values like:

- `"UNKNOWN"`
- `"?"`
- ``-``
- `"MISSING"`

You can check missing values in Categorical columns by using ``detect_categorical_missing_types()`` method from **MissingnessDiagnosis** class:

Example:

       # pass a list of categorical columns or pass a dataframe of only categorical or text columns

       MissingnessDiagnosis(df, ['email','notes','phone_number','is_active']).detect_categorical_missing_types()

Output: 

       {
       "email": {
              "pandas_missing": [nan],
              "placeholder_missing": []
       },
       "notes": {
              "pandas_missing": [nan],
              "placeholder_missing": []
       },
       "phone_number": {
              "pandas_missing": [nan],
              "placeholder_missing": []
       },
       "is_active": {
              "pandas_missing": [nan],
              "placeholder_missing": []
       }
       }

We can add a list of our own placeholders if needed, like this:

       MissingnessDiagnosis(df, ['email','notes','phone_number','is_active']).detect_categorical_missing_types(extra_placeholders=['?', 'UNKNOWN', '-999'])

Output:

       {
       "email": {
              "pandas_missing": [nan],
              "placeholder_missing": []
       },
       "notes": {
              "pandas_missing": [nan],
              "placeholder_missing": ['?']
       },
       "phone_number": {
              "pandas_missing": [nan],
              "placeholder_missing": ['-999']
       },
       "is_active": {
              "pandas_missing": [nan],
              "placeholder_missing": []
       }
       }

We can see:

- Placeholder values got detected in the columns they exist. 
- What kind of missing values exist where.

## Date and Time Data

Date and time columns usually use `NaT (Not a Number)` to represent missing values.

Sometimes missing dates are kept as fake dates like:

- `"00-00-0000"`
- `"01-01-1000"`

You can check missing values in Date-time columns by using ``detect_datetime_missing_types()`` method from **MissingnessDiagnosis** class:

Example:

       
       MissingnessDiagnosis(df, ['signup_date', 'last_login', 'event_timestamp']).detect_datetime_missing_types()
       
Output:

       {
       'signup_date': {
              'pandas_missing': [NaT],
              'placeholder_missing': []
       },
       'last_login': {
              'pandas_missing': [NaT],
              'placeholder_missing' : []
       },
       'event_timestamp': {
              'pandas_missing': [NaT],
              'placeholder_missing': []
       }}

We can add custom date placeholders if our data uses them:

Example:

       MissingnessDiagnosis(df, ['signup_date', 'last_login']).detect_datetime_missing_types(extra_placeholders=["00-00-0000"])

Output:

       {
       'signup_date': {
              'pandas_missing': [NaT],
              'placeholder_missing': []
       },
       'last_login': {
              'pandas_missing': [NaT],
              'placeholder_missing' : []
       }}

We can see:

- Only Pandas missing types got detected.
- The placeholder is not detected because it does not exist in any column.
- We can pass in any kind of placeholder.

## Why this step?

Because by the end of this step, we will know:

- Which columns have missing data
- What types of missing data they contain
- Whether missing values are real or hidden as placeholders

This makes the next step, exploring the missing data **much safer and easier**.
