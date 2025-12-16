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

Before checking what missing values exist in the data, DataLab first checks what kinds of missing data exists in the dataset.

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






