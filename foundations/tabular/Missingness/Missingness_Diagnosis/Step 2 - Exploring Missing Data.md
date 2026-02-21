# STEP 2: Exploring Missing Data

### **(Missingness Diagnosis continued)**....

In **Step 1**, we learned what values are identified as missing in our data.

## What is this step about?

This step is simply about ``finding missing information in your data``.

Now that datalabx knows what **missing** means for your dataset, we can move ahead and explore:

- How much data is missing

- Which columns are affected the most

- What missing data really looks like in rows of DataFrame

No data is changed at this step. We are only observing and understanding.

## Why did we not directly look at the Missing data?

Because before **Step 1**, we didn’t even know what really counts as missing.

Some missing values are:

- Automatically detected by Pandas (like NaN or NaT)

- Hidden inside placeholder values (like -999, 'UNKNOWN', 'MISSING' 'EMPTY')

If we skipped detection and looked at rows directly, we might miss important missing values or misunderstand the data.

That’s why detection comes first, and exploration comes next.

## What does datalabx explore in this step?

Using the missing value definitions from **Step 1**, datalabx explores missing data in three simple ways:

- How much data is missing

- Where missing data exists

- Missingness by column type (Numerical, Categorical, Datetime)

### Missing Data Summary

The first thing datalabx shows is a summary of missing data.

This summary answers simple but important questions like:

- How many rows are missing in each column?

- What percentage of each column is missing?

### **datalabx Usage:**

We can check missing data summary by using ``missing_data_summary()`` method from ``MissignessDiagnosis`` class.

It returns a dictionary of columns and number of rows with missing data in those columns.

Example:

    MissingnessDiagnosis(df).missing_data_summary()

Output:

    {'age': 24970,
    'income': 49984,
    'account_balance': 49833,
    'gender': 24728,
    'country': 24962,
    'device_type': 25117,
    'email': 150070,
    'notes': 166658,
    'phone_number': 249491,
    'is_active': 50121,
    'signup_date': 4932,
    'last_login': 24342,
    'event_timestamp': 4985}

This returns the count of missing rows per column.

However, we can check the percentage of missing rows per column like this:

Example:

    MissingnessDiagnosis(df).missing_data_summary('percent')

Output:

    {'age': 4.99,
    'income': 10.0,
    'account_balance': 9.97,
    'gender': 4.95,
    'country': 4.99,
    'device_type': 5.02,
    'email': 30.01,
    'notes': 33.33,
    'phone_number': 49.9,
    'is_active': 10.02,
    'signup_date': 0.99,
    'last_login': 4.87,
    'event_timestamp': 1.0}

We can see in this output that we now have percentage of missing data in each column.

> However, till this point, we have only been looking at Pandas **built-in missing** values.

We can now include our placeholders and see the count or percentage of missing data in each column, like this:

Example:

    MissingnessDiagnosis(df).missing_data_summary('percent', extra_placeholders = [-999, -1, '-999'])

**Notice the difference between integer -999 and text '-999'.**

Output:

    {'age': 10.0,             # this almost doubled
    'income': 10.0,
    'account_balance': 9.97,
    'gender': 4.95,
    'country': 4.99,
    'device_type': 5.02,
    'email': 30.01,
    'notes': 33.33,
    'phone_number': 74.94,    # missingness increased here by 25%!
    'is_active': 10.02,
    'signup_date': 0.99,
    'last_login': 4.87,
    'event_timestamp': 1.0}

**Great!** We now know how to check summary of missing data.

### Viewing rows with missing data

After seeing the summary, datalabx lets us look at the actual rows where data is missing.

This is done separately for:

- Numerical columns

- Categorical columns

- Datetime columns

This helps us see:

- Whether missing values appear together

- Whether they follow a pattern

- Whether missingness looks random or has a structure

#### Missing data in Numerical columns:

We can explore rows of missing data in numerical columns of a DataFrame by using ``show_missing_rows_in_numerical_columns()`` method from MissingnessDiagnosis class.

This function returns a dictionary of columns and rows of DataFrame containing missing values in those columns. 

Example:

    numerical_missing_data = MissingnessDiagnosis(df).show_missing_rows_in_numerical_columns()

    numerical_missing_data

Output:

        {
        "age": "<<-- rows of DataFrame where age is missing -->>",
        "income": "<<-- rows where income is missing -->>",
        "account_balance": "<<-- rows where balance is missing -->>",
        "gender": "<<-- rows with unknown or missing gender -->>",
        "country": "<<-- rows with missing country -->>",
        "device_type": "<<-- rows with missing device type -->>",
        "email": "<<-- rows with missing email -->>",
        "notes": "<<-- rows with missing or malformed notes -->>",
        "phone_number": "<<-- rows with missing phone numbers -->>",
        "is_active": "<<-- rows with missing activity flag -->>",
        "signup_date": "<<-- rows with missing signup date -->>",
        "last_login": "<<-- rows with missing last login -->>",
        "event_timestamp": "<<-- rows with missing event timestamp -->>"
        }

We can then check these rows by selecting the column we wish to explore data in.

Example:

    numerical_missing_data['age']

Output:

| customer_id | age | income | account_balance | gender | country | device_type | email            | notes     | phone_number | is_active | signup_date | last_login           | event_timestamp       |
|------------:|----:|:------:|----------------:|--------|---------|-------------|------------------|-----------|----------------|-----------|-------------|----------------------|-----------------------|
| 28          | NaN | NaN    | 3526.37         | Female | US      | desktop     | NaN              | NaN       | NaN            | NaN       | 2019-12-14  | 2020-12-27 13:00:00  | 2020-12-10 09:49:00   |
| 52          | NaN | NaN    | 536.27          | Female | FR      | desktop     | user@example.com | NaN       | 123-456-7890  | True      | 2020-11-08  | 2024-11-02 09:00:00  | NaT                   |
| 69          | NaN | NaN    | -827.47         | Male   | UK      | mobile      | user@example.com | OK        | NaN            | False     | 2019-03-06  | 2022-03-06 01:00:00  | 2019-07-26 15:45:00   |

#### Missing data in Numerical columns - With Placeholders:

By default, numerical missing rows include only values like NaN.

If our dataset uses numeric placeholders such as -999 or -1, we can include them like this:

    missing_data = MissingnessDiagnosis(df).show_missing_rows_in_numerical_columns(extra_placeholders = [-999, -1])
    missing_data['age']

Output:

| customer_id | age   | income | account_balance | gender | country | device_type | email            | notes                         | phone_number | is_active | signup_date | last_login           | event_timestamp       |
|------------:|------:|:------:|----------------:|--------|---------|-------------|------------------|-------------------------------|--------------|-----------|-------------|----------------------|-----------------------|
| 5           | -999.0| NaN    | 1499.295644     | Female | UK      | desktop     | user@example.com | OK                            | NaN          | False     | 2022-03-23  | NaT                  | 2024-12-18 11:47:00   |
| 18          | -1.0  | NaN    | 1667.969528     | Female | FR      | NaN         | user@example.com | {'free_text': 'call later'}   | NaN          | True      | 2016-11-14  | 2023-01-02 05:00:00  | 2022-06-13 08:06:00   |
| 28          | NaN   | NaN    | 3526.370925     | Female | US      | desktop     | NaN              | NaN                           | NaN          | NaN       | 2019-12-14  | 2020-12-27 13:00:00  | 2020-12-10 09:49:00   |

We can see:

- Rows where age is NaN

- Rows where age is -999 or -1

- All shown together in one place

This helps us see how missing numerical data is actually stored in our dataset.

#### Missing data in Categorical columns:

We can explore rows of missing data in categorical columns of a DataFrame by using ``show_missing_rows_in_categorical_columns()`` method from MissingnessDiagnosis class.

This function returns a dictionary of columns and rows of DataFrame containing missing values in those columns. 

Example:

    missing_data = MissingnessDiagnosis(df).show_missing_rows_in_categorical_columns()

    missing_data

Output:

        {
        "age": "<<-- rows of DataFrame where age is missing -->>",
        "income": "<<-- rows where income is missing -->>",
        "account_balance": "<<-- rows where balance is missing -->>",
        "gender": "<<-- rows with unknown or missing gender -->>",
        "country": "<<-- rows with missing country -->>",
        "device_type": "<<-- rows with missing device type -->>",
        "email": "<<-- rows with missing email -->>",
        "notes": "<<-- rows with missing or malformed notes -->>",
        "phone_number": "<<-- rows with missing phone numbers -->>",
        "is_active": "<<-- rows with missing activity flag -->>",
        "signup_date": "<<-- rows with missing signup date -->>",
        "last_login": "<<-- rows with missing last login -->>",
        "event_timestamp": "<<-- rows with missing event timestamp -->>"
        }

We can then check these rows by selecting the column we wish to see missing data in.

Example:

    missing_data['notes']

Output:

| customer_id | age | income        | account_balance | gender | country | device_type | email            | notes                         | phone_number   | is_active | signup_date | last_login           | event_timestamp       |
|------------:|----:|---------------:|----------------:|--------|---------|-------------|------------------|-------------------------------|----------------|-----------|-------------|----------------------|-----------------------|
| 7           | 70.0| 56150.668311  | 3378.154020     | Male   | US      | desktop     | user@example.com | {'free_text': 'call later'}   | NaN            | True      | 2020-01-29  | 2020-04-22 16:00:00  | NaT                   |
| 10          | 46.0| 41775.538675  | 1033.822987     | NaN    | NaN     | mobile      | user@example.com | ['list']                      | NaN            | True      | 2020-10-10  | 2022-11-14 03:00:00  | 2022-01-02 15:53:00   |
| 13          | 61.0| 43382.412472  | 1211.586960     | Female | US      | NaN         | user@example.com | NaN                           | 123-456-7890  | True      | 2015-12-10  | 2022-10-31 23:00:00  | 2020-04-24 11:51:00   |
| 14          | 75.0| 58088.643143  | 2803.877054     | Male   | DE      | desktop     | NaN              | {'free_text': 'call later'}   | 123-456-7890  | NaN       | 2022-08-20  | 2023-11-01 13:00:00  | 2020-09-20 02:07:00   |

#### Missing data in Categorical columns - With Placeholders:

Categorical data often hides missingness in values like:

- 'UNKNOWN'

- 'MISSING'

- '?'

- Free-text structures or lists

We can include these placeholders when exploring missing rows:

    missing_data = MissingnessDiagnosis(df).show_missing_rows_in_categorical_columns(extra_placeholders = ["{'free_text': 'call later'}", "['list']"])

    missing_data['notes']

Output:

| customer_id | age | income        | account_balance | gender | country | device_type | email            | notes                         | phone_number   | is_active | signup_date | last_login           | event_timestamp       |
|------------:|----:|---------------:|----------------:|--------|---------|-------------|------------------|-------------------------------|----------------|-----------|-------------|----------------------|-----------------------|
| 7           | 70.0| 56150.668311  | 3378.154020     | Male   | US      | desktop     | user@example.com | {'free_text': 'call later'}   | NaN            | True      | 2020-01-29  | 2020-04-22 16:00:00  | NaT                   |
| 10          | 46.0| 41775.538675  | 1033.822987     | NaN    | NaN     | mobile      | user@example.com | ['list']                      | NaN            | True      | 2020-10-10  | 2022-11-14 03:00:00  | 2022-01-02 15:53:00   |
| 13          | 61.0| 43382.412472  | 1211.586960     | Female | US      | NaN         | user@example.com | NaN                           | 123-456-7890  | True      | 2015-12-10  | 2022-10-31 23:00:00  | 2020-04-24 11:51:00   |
| 14          | 75.0| 58088.643143  | 2803.877054     | Male   | DE      | desktop     | NaN              | {'free_text': 'call later'}   | 123-456-7890  | NaN       | 2022-08-20  | 2023-11-01 13:00:00  | 2020-09-20 02:07:00   |

We can see:

- Rows where notes is NaN

- Rows where notes contains placeholder values ("{'free_text': 'call later'}", "['list']" etc.)

- Missing text data grouped together

This is especially useful for text fields where missingness is not obvious at first.

#### Missing data in Datetime columns:

We can explore rows of missing data in date-time columns of a DataFrame by using ``show_missing_rows_in_datetime_columns()`` method from MissingnessDiagnosis class.

This function returns a dictionary of columns and rows of DataFrame containing missing values in those columns. 

Example:

    datetime_missing_data = MissingnessDiagnosis(df).show_missing_rows_in_datetime_columns()

    datetime_missing_data

Output:

        {
        "age": "<<-- rows of DataFrame where age is missing -->>",
        "income": "<<-- rows where income is missing -->>",
        "account_balance": "<<-- rows where balance is missing -->>",
        "gender": "<<-- rows with unknown or missing gender -->>",
        "country": "<<-- rows with missing country -->>",
        "device_type": "<<-- rows with missing device type -->>",
        "email": "<<-- rows with missing email -->>",
        "notes": "<<-- rows with missing or malformed notes -->>",
        "phone_number": "<<-- rows with missing phone numbers -->>",
        "is_active": "<<-- rows with missing activity flag -->>",
        "signup_date": "<<-- rows with missing signup date -->>",
        "last_login": "<<-- rows with missing last login -->>",
        "event_timestamp": "<<-- rows with missing event timestamp -->>"
        }

We can then check these rows by selecting the column we wish to explore data in.

Example:

    datetime_missing_data['last_login']

Output:

| customer_id | age   | income        | account_balance | gender | country | device_type | email            | notes                         | phone_number   | is_active | signup_date | last_login | event_timestamp       |
|------------:|------:|---------------:|----------------:|--------|---------|-------------|------------------|-------------------------------|----------------|-----------|-------------|------------|-----------------------|
| 5           | -999.0| NaN            | 1499.295644     | Female | UK      | desktop     | user@example.com | OK                            | NaN            | False     | 2022-03-23  | NaT        | 2024-12-18 11:47:00   |
| 92          | 65.0  | 25530.131462  | 2891.337813     | Female | US      | tablet      | user@example.com | OK                            | 123-456-7890  | True      | 2016-11-09  | NaT        | 2022-05-09 09:58:00   |
| 133         | 56.0  | 34950.921308  | NaN             | NaN    | UK      | tablet      | NaN              | OK                            | NaN            | False     | 2020-01-17  | NaT        | 2019-10-29 19:45:00   |

#### Missing data in Datetime columns - With Placeholders:

Sometimes, missing dates are stored as fake or invalid dates like "00-00-0000".

We can include such placeholders like this:

    placeholder_missing_dates = MissingnessDiagnosis(df).show_missing_rows_in_datetime_columns(extra_placeholders = ['00-00-0000'])
    placeholder_missing_dates['last_login']

Output: 

| customer_id | age   | income        | account_balance | gender | country | device_type | email            | notes | phone_number   | is_active | signup_date | last_login | event_timestamp       |
|------------:|------:|---------------:|----------------:|--------|---------|-------------|------------------|-------|----------------|-----------|-------------|------------|-----------------------|
| 5           | -999.0| NaN            | 1499.295644     | Female | UK      | desktop     | user@example.com | OK    | NaN            | False     | 2022-03-23  | NaT        | 2024-12-18 11:47:00   |
| 92          | 65.0  | 25530.131462  | 2891.337813     | Female | US      | tablet      | user@example.com | OK    | 123-456-7890  | True      | 2016-11-09  | NaT        | 2022-05-09 09:58:00   |
| 133         | 56.0  | 34950.921308  | NaN             | NaN    | UK      | tablet      | NaN              | OK    | NaN            | False     | 2020-01-17  | NaT        | 2019-10-29 19:45:00   |

We can see:

- Rows where *last_login* is NaT.

- Rows where placeholder dates exist (if present)

If no rows appear, it confirms the placeholder is not used.

## Why this step?

By the end of **Step 2**, we know:

- How much data is missing

- Which columns are most affected

- What missing values look like in real rows

- Whether missingness is random or has a pattern

Only after seeing this clearly does it make sense to look at the rows of data where everything is missing.

This leads naturally into the next step of the workflow.







