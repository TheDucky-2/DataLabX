# STEP 1 - Diagnosis of Missing Data

Missingness Diagnosis in DataLab refers to the diagnosis(check-up) of missing values in the data.

This is the very first step of missingness handling in DataLab, also referred to as "Understanding Missingness"

**Missingness Diagnosis** diagnoses missing data in a data type-aware way.

Because Numerical, Categorical, and Datetime data represent missing values differently, missingness is detected at the column level rather than globally for the whole dataframe.

This keeps detection accurate, extensible, and easy to reason about - even when user defines their own placeholders.

                        Raw data
                           ↓
                    Detect Column Types
                           ↓
            Detect Missingness within each Data Type
                           ↓
    Numerical | Categorical | Datetime Missingness Results

### **DataLab Usage**:

You can initialize Missingness Diagnosis by importing ``MissingnessDiagnosis`` class from datalab directly.

       from datalab import MissingnessDiagnosis

## Detecting Missing Types

Before checking how many missing values exist in the data, DataLab first checks what kinds of missing data exists in the dataset.

DataLab detects missing data separately within Numerical, Categorical, and Datetime columns.

For each data type, DataLab detects both built-in missing values **(NaN/NaT/None)** and user-defined missing placeholders.

It then combines the detected missingness by:

- Numerical columns

- Categorical columns

- Datetime columns

The detected missingness is returned in a type-aware structure of pandas-missing types and placeholder-missing types.

### Numerical Missingness Diagnosis

Numerical columns usually have missing data represented by values like *NaN*, *np.nan* or *pd.NA*. 

These values are considered by Pandas to be truly missing values.

Sometimes missing numbers are also intentionally represented by placeholders, like -999, 0, or 9999, or -1 etc.

However, Pandas treats these as normal numbers.

In DataLab, you can add your own placeholders, so they’re included in the missingness diagnosis alongside the built-in missing values.

### **DataLab Usage**:

You can see what values are missing in the Numerical columns of your DataFrame by using ``detect_numerical_missing_types()`` method from ``MissingnessDiagnosis`` class.

This method returns a dictionary of numerical columns and the types of missing values present in a Numerical DataFrame.

       MissingnessDiagnosis(df).detect_numerical_missing_types()

Output: 

       {'age': {'pandas_missing': [nan], 'placeholder_missing': []},
        'income': {'pandas_missing': [nan], 'placeholder_missing': []},
        'account_balance': {'pandas_missing': [nan], 'placeholder_missing': []}}

Notice! This function returns two categories of numerical missing data types: 

1. **Pandas Missing Types (NAN)** -> Pandas converts anything that is not a number to NAN (Not a Number).

2. **Placeholder Missing Types**-> These are the types your domain considers as missing data in a numerical dataset (Example: -1 or 0 as age where info is missing for a person).

#### **NOTE:**

You can also pass a list of extra placeholders you would like to check if these types are present in your data and in which column, by using **extra_placeholders** as the parameter.

Example:

       MissingnessDiagnosis(df).detect_numerical_missing_types(extra_placeholders = [-999, -1])

Output:

       {'age': {'pandas_missing': [nan], 'placeholder_missing': [-999.0, -1.0]},
        'income': {'pandas_missing': [nan], 'placeholder_missing': []},
        'account_balance': {'pandas_missing': [nan], 'placeholder_missing': []}}

As we can see that these placeholders were present in the 'age' column of the Numerical DataFrame.

### Categorical Missingness Diagnosis

Categorical or text columns columns usually have missing data represented by values like *NaN*, *None* or *pd.NA*. 

These values are considered by Pandas to be truly missing values for categorical types.

Sometimes missing categories or text are also intentionally represented by placeholders, like 'MISSING', 'UNKNOWN', '-', '?' etc.

However, Pandas treats these as normal data.

In DataLab, you can add your own categorical placeholders, so they’re included in the missingness diagnosis alongside the built-in missing values.

### **DataLab Usage**:

You can see what values are missing in the Categorical columns of your DataFrame by using ``detect_categorical_missing_types()`` method from ``MissingnessDiagnosis`` class.

This method returns a dictionary of categorical columns and the types of missing values present in a Categorical DataFrame.

       MissingnessDiagnosis(df).detect_categorical_missing_types()

Output: 

       {'gender': {'pandas_missing': [nan], 'placeholder_missing': []},
        'country': {'pandas_missing': [nan], 'placeholder_missing': []},
        'device_type': {'pandas_missing': [nan], 'placeholder_missing': []},
        'email': {'pandas_missing': [nan], 'placeholder_missing': []},
        'notes': {'pandas_missing': [nan], 'placeholder_missing': []},
        'phone_number': {'pandas_missing': [nan], 'placeholder_missing': []},
        'is_active': {'pandas_missing': [nan], 'placeholder_missing': []}}

This function also returns two categories of categorical missing data types: 

1. **Pandas Missing Types (NAN)** -> Pandas converts anything that is not a number to NAN (Not a Number).

2. **Placeholder Missing Types**-> These are the types your domain considers as missing data in a categorical dataset (Example: Missing phone numbers represented by '0000000000')

#### **NOTE:**

You can also pass a list of extra placeholders you would like to check if these missing types are present in your data and in which column, by using **extra_placeholders** as the parameter.

Example:

       MissingnessDiagnosis(cat_df).detect_categorical_missing_types(extra_placeholders = ['-999', '?'])

Output:

       {'gender': {'pandas_missing': [nan], 'placeholder_missing': []},
        'country': {'pandas_missing': [nan], 'placeholder_missing': []},
        'device_type': {'pandas_missing': [nan], 'placeholder_missing': []},
        'email': {'pandas_missing': [nan], 'placeholder_missing': []},
        'notes': {'pandas_missing': [nan], 'placeholder_missing': ['?']},
        'phone_number': {'pandas_missing': [nan], 'placeholder_missing': ['-999']},
        'is_active': {'pandas_missing': [nan], 'placeholder_missing': []}}

As we can see that placeholders "?" and "-999" were present in the 'Notes' and 'Phone Number' columns of the Categorical DataFrame respectively.

### Date-time Missingness Diagnosis

Dates or time based data columns usually have missing data represented by values like *NaT* (Not a Time).

These values are considered by Pandas to be truly missing values for date-time types.

Sometimes missing dates or timestamps are also intentionally represented by placeholders, like '00-00-0000' or '??-??-????' or '01-01-1000'.

However, Pandas treats these as normal dates.

In DataLab, you can add your own datetime placeholders, so they’re included in the missingness diagnosis alongside the built-in missing values.

### **DataLab Usage**:

You can see what values are missing in the date-time columns of your DataFrame by using ``detect_datetime_missing_types()`` method from ``MissingnessDiagnosis`` class.

This method returns a dictionary of date-time columns and the types of missing values present in a Date-Time DataFrame.

       MissingnessDiagnosis(datetime_df).detect_datetime_missing_types()

Output: 

       {'signup_date': {'pandas_missing': [NaT], 'placeholder_missing': []},
       'last_login': {'pandas_missing': [NaT], 'placeholder_missing': []},
       'event_timestamp': {'pandas_missing': [NaT], 'placeholder_missing': []}}

This function also returns two categories of categorical missing data types: 

1. **Pandas Missing Types (NAN)** -> Pandas converts anything that is not a date or time to NAT (Not a Time).

2. **Placeholder Missing Types**-> These are the types your domain considers as missing data in a date-time dataset. (Example: Missing phone numbers represented by '0000000000')

#### **NOTE:**

You can also pass a list of extra placeholders you would like to check if these missing types are present in your data and in which column, by using **extra_placeholders** as the parameter.

Example:

       MissingnessDiagnosis(datetime_df).detect_datetime_missing_types(extra_placeholders = ['00-00-0000'])

Output:

       {'signup_date': {'pandas_missing': [NaT], 'placeholder_missing': []},
       'last_login': {'pandas_missing': [NaT], 'placeholder_missing': []},
       'event_timestamp': {'pandas_missing': [NaT], 'placeholder_missing': []}}

As we can see that placeholder '00-00-0000' is not present in any columns of the Date-time DataFrame.







