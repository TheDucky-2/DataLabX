# STEP 3: Exploring Missing Data - Row Level Checks
### **(Missingness Diagnosis continued)....**

In the previous steps, we used DataLab to learn:

**Step 1:** What really counts as missing in our dataset (built-in or placeholders).

**Step 2:** How much data is missing in each column and which rows contain missing values.

## What is this step about?

This step is simply about ``finding empty rows in your data``.

Now that we know **what counts as missing data**, and **how much data is missing**, we now move to **row-level checks**. 

Here, we look at entire rows that are affected by missing data.

This is very useful when you want to quickly identify:

- Rows that are completely empty

- Rows that are missing specific important columns

No data is modified even at this step - we are only observing.

## Why Row-Level Checks when in Step 1 we checked Column by Column?

That is because sometimes knowing only the column-level counts is not enough.

We may also want to see:

- Are there any rows where data is completely missing (all columns are empty)

- Are there any rows which are missing critical columns that can affect analysis or modeling

This step helps in:

- Detecting incomplete data

- Making decisions about removing rows or filling rows

- Investigating patterns of missing data across multiple columns

## Types of Row-Level Checks

DataLab supports two main types of row-level checks:

1. Rows with all columns having missing data
2. Rows with only specific columns having missing data

Let us now move to exploring these checks:

## **DataLab Usage**

Let us use an example dataset of all missing values to understand that.

**Sample Dataset:**

| customer_id | age       | income | account_balance | gender | country | device_type | email | notes | phone_number | is_active | signup_date | last_login | event_timestamp |
|-------------|-----------|--------|----------------|--------|---------|-------------|-------|-------|--------------|-----------|-------------|------------|----------------|
| missing_data   | NaN       | NaN    | NaN            | NaN    | NaN     | NaN         | NaN   | NaN   | NaN          | NaN       | NaN         | NaN        | NaN            |
| missing_data   | NaN       | NaN    | NaN            | NaN    | NaN     | NaN         | NaN   | NaN   | NaN          | NaN       | NaN         | NaN        | NaN            |
| missing_data   | NaN       | NaN    | NaN            | NaN    | NaN     | NaN         | NaN   | NaN   | NaN          | NaN       | NaN         | NaN        | NaN            |
| missing_data   | NaN       | NaN    | NaN            | NaN    | NaN     | NaN         | NaN   | NaN   | NaN          | NaN       | NaN         | NaN        | NaN            |
| missing_data   | NaN       | NaN    | NaN            | NaN    | NaN     | NaN         | NaN   | NaN   | NaN          | NaN       | NaN         | NaN        | NaN            |

We can see:

- Column *'customer_id'* has placeholder '**missing_data**'.
- Rest of the columns have '**NaN**' as missing values.
- All the rows of this dataset have missing values in all columns.

### Rows with all columns missing

This check shows all the rows in a dataset where all columns are missing data.

We can check all these rows by using ``rows_with_all_columns_missing()`` method from **MissingnessDiagnosis** class.

Example:

    MissingnessDiagnosis(df).rows_with_all_columns_missing()

Output:

| customer_id | age | income | account_balance | gender | country | device_type | email | notes | phone_number | is_active | signup_date | last_login | event_timestamp |
|-------------|-----|--------|----------------|--------|---------|-------------|-------|-------|--------------|-----------|-------------|------------|----------------|

We can see:

- We got an empty DataFrame
- No rows have all columns missing

But, Why is that? Why did **nothing get detected?**

That is because the column *'customer_id'* has placeholder value as missing value.

It is seen having useful data by pandas, which is why we can pass in the placeholder like this:

    MissingnessDiagnosis(df).rows_with_all_columns_missing(extra_placeholders = ['missing_data'])

Output:

| customer_id   | age | income | account_balance | gender | country | device_type | email | notes | phone_number | is_active | signup_date | last_login | event_timestamp |
|---------------|-----|--------|----------------|--------|---------|-------------|-------|-------|--------------|-----------|-------------|------------|----------------|
| missing_data  | NaN | NaN    | NaN            | NaN    | NaN     | NaN         | NaN   | NaN   | NaN          | NaN       | NaN         | NaN        | NaN            |
| missing_data  | NaN | NaN    | NaN            | NaN    | NaN     | NaN         | NaN   | NaN   | NaN          | NaN       | NaN         | NaN        | NaN            |
| missing_data  | NaN | NaN    | NaN            | NaN    | NaN     | NaN         | NaN   | NaN   | NaN          | NaN       | NaN         | NaN        | NaN            |
| missing_data  | NaN | NaN    | NaN            | NaN    | NaN     | NaN         | NaN   | NaN   | NaN          | NaN       | NaN         | NaN        | NaN            |
| missing_data  | NaN | NaN    | NaN            | NaN    | NaN     | NaN         | NaN   | NaN   | NaN          | NaN       | NaN         | NaN        | NaN            |

We can see:

- All rows of the dataset have been detected where all columns are missing values.
- Placeholder 'missing_data' is now being detected as missing value.

**That's Great!**

We are now able to detect all rows where all columns are missing data.

But what if I want to see all rows where only a specific column of my choice is missing values?

Let us now move onto:

### Rows with specific columns missing

This check allows us to specify important columns and see rows where one or more of those columns are missing.

We can check all rows where a specific column is missing values by using ``rows_with_specific_columns_missing()`` method from **MissingnessDiagnosis** class.

Example:

    # passing a list of columns we would like to explore missing rows in

    MissingnessDiagnosis(df, ['age', 'income']).rows_with_specific_columns_missing([])

Output:

| age | income |
|-----|--------|
| NaN | NaN    |
| NaN | NaN    |
| NaN | NaN    |
| NaN | NaN    |
| NaN | NaN    |

We can see:

- All rows missing values for the columns we mentioned.
.
- All the missing values are pandas built-in types (NaN).

But, what if I want to also explore missing values in *'customer_id'* column?

Example:

    MissingnessDiagnosis(df, ['age', 'income', 'customer_id']).rows_with_specific_columns_missing()

Output:

| age | income | customer_id |
|-----|--------|-------------|

We can see:

- Nothing got detected.
- Output shows an empty DataFrame of the columns we have passed.

That is because the column **'customer_id'** has placeholder value **'missing_data'** instead of **NaN**, like other columns.

This is the best time to pass in the placeholder value like this:

    MissingnessDiagnosis(df, ['age', 'income', 'customer_id']).rows_with_specific_columns_missing(extra_placeholders=['missing_data'])

Output:

| age | income | customer_id   |
|-----|--------|---------------|
| NaN | NaN    | missing_data  |
| NaN | NaN    | missing_data  |
| NaN | NaN    | missing_data  |
| NaN | NaN    | missing_data  |
| NaN | NaN    | missing_data  |

We can see:

- All rows with missing values have been detected in the specific columns we passed.
- Both pandas and placeholder values have been detected.

## Why this step?

By the end of this step, we will know:

- Which rows are completely missing and may be good candidates for removal

- Which rows are missing specific critical columns

- How missingness is identified and distributed at the row level, not just by column

This step naturally prepares us for the next stage: visualizing simple images of missing data.

It helps in identifying patterns of missing data and spotting complex relationships between missing data in different columns.
