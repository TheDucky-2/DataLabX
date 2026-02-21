# **Part 2 - Column Type Detection & Conversion (Continued)....**

In the previous part of this documentation, we explored:

- That a dataset can have different types of columns (Numerical, Categorical and Datetime).

- How we can detect the types of columns in a DataFrame.

- How we can convert incorrectly identified columns into correct ones.

However, we are not done yet, as there is something very important that we will be discussing in this part.

## What is This Very Important Thing?

Let us explore what is this very important thing with an example Dataset:

**Sample Messy Dataset**

| user_id | age  | gender | account_created_at     | last_seen_at | account_closed_at        | country_code | city       | email                 | phone         | plan_tier | billing_amount | currency | event_time           | event_type | session_length_sec | feedback_score | notes          |
|--------:|-----:|:------:|------------------------|--------------|--------------------------|--------------|------------|-----------------------|---------------|-----------|----------------|----------|---------------------|------------|--------------------|----------------|----------------|
| 1 | 21 | M | 2015-07-25 00:00:00 | 2017-07-04 | NaN | US | City_616 | NaN | NaN | basic | 46.68 | NaN | 2024-05-19 21:02:00 | click | 363.110570 | 2.0 | NaN |
| 2 | 65 | M | 2018-11-10 00:00:00 | 2021-03-03 | NaN | UK | City_1220 | user2@example.com | 1.475936e+10 | free | -1.00 | USD | 2018-08-07 11:24:00 | login | 0.000000 | 3.0 | NaN |
| 3 | 57 | NaN | 2018-01-17 00:00:00 | 2018-08-25 | NaN | US | City_5924 | NaN | NaN | basic | 61.31 | INR | 2024-12-09 23:47:00 | purchase | 127.375824 | 2.0 | NaN |
| 4 | 44 | F | 2018-06-20 00:00:00 | 2019-05-05 | NaN | DE | City_5472 | user4@example.com | 1.243738e+10 | pro | 74.66 | USD | 2021-06-27 18:42:00 | login | -1.000000 | 3.0 | NaN |
| 5 | 43 | F | 2019-03-10 00:00:00 | 2022-12-28 | NaN | CA | City_5347 | NaN | NaN | basic | 0.00 | NaN | 2018-10-14 13:53:00 | logout | 289.892775 | -1.0 | NaN |
| 6 | 70 | M | 2018-07-08 00:00:00 | 2022-07-05 | NaN | IN | City_4353 | user6@example.com | 1.764699e+10 | basic | 34.32 | EUR | 2020-08-16 08:33:00 | click | 648.635141 | NaN | NaN |
| 7 | 21 | M | 2018-06-17 00:00:00 | 2022-02-13 | NaN | DE | City_5712 | none | NaN | pro | 6.41 | USD | NaN | logout | 280.832785 | 3.0 | NaN |
| 8 | 60 | M | 2021-07-06 00:00:00 | 2024-06-26 | 2024-07-11 00:00:00 | NaN | City_6525 | user8@example.com | 1.454826e+10 | free | 56.48 | INR | 2020-08-23 00:24:00 | login | 370.928378 | 2.0 | NaN |
| 9 | 28 | F | 2022-08-18 00:00:00 | 2025-05-30 | NaN | NaN | City_3517 | NaN | NaN | pro | 58.55 | USD | 2021-09-05 00:05:00 | click | 371.456613 | 3.0 | Bad UX |
| 10 | 22 | M | 2023-07-27 00:00:00 | 2024-06-18 | NaN | NaN | City_6956 | NaN | NaN | basic | 28.81 | USD | 2019-09-04 18:20:00 | ERROR | 209.346019 | 3.0 | NaN |
| 11 | 49 | M | 2020-05-22 00:00:00 | 2022-07-16 | 2022-09-11 00:00:00 | US | City_5191 | user11@example.com | 1.443582e+10 | free | 46.28 | USD | 2018-07-24 19:31:00 | ERROR | 266.222484 | 5.0 | NaN |
| 12 | 78 | F | UNKNOWN_DATE | NaN | NaN | US | City_2247 | none | 1.838258e+10 | free | 58.85 | USD | NaN | ERROR | 0.000000 | 3.0 | NaN |
| 13 | 63 | F | 2015-05-23 00:00:00 | 2015-07-30 | 2016-01-21 00:00:00 | US | City_1927 | user13@example.com | 1.668452e+10 | NaN | 68.51 | INR | 2018-12-13 03:59:00 | purchase | 298.436304 | 3.0 | . |
| 14 | 64 | F | 2023-06-19 00:00:00 | 2026-02-07 | NaN | IN | City_4418 | user14@example.com | 1.302826e+10 | NaN | 61.98 | USD | 2024-04-21 07:33:00 | logout | 294.113950 | 3.0 | NaN |
| 15 | 61 | M | 2021-03-30 00:00:00 | 2024-09-05 | 2024-12-24 00:00:00 | NaN | City_5977 | NaN | NaN | free | 41.99 | NaN | 2018-12-01 00:41:00 | click | 518.860086 | 4.0 | NaN |
| 16 | 66 | M | 2021-05-25 00:00:00 | 2024-11-14 | CLOSED_UNKNOWN | US | City_336 | user16@example.com | 1.414761e+10 | pro | 53.19 | NaN | 2020-12-20 11:26:00 | login | 235.391323 | NaN | NaN |
| 17 | 48 | F | 2019-09-24 00:00:00 | 2020-10-16 | NaN | US | City_7230 | NaN | NaN | NaN | 54.40 | INR | 2023-01-31 03:48:00 | ERROR | 628.769202 | 4.0 | Great service |
| 18 | 24 | F | 2022-06-15 00:00:00 | 2023-12-31 | NaN | CA | City_6936 | NaN | NaN | pro | 46.10 | INR | 2020-08-12 16:21:00 | logout | 298.485780 | NaN | NaN |
| 19 | 69 | F | 2015-07-30 00:00:00 | 2016-04-05 | NaN | NaN | City_5044 | user19@example.com | 1.402160e+10 | NaN | 35.21 | USD | 2023-08-16 20:13:00 | logout | 420.852723 | 4.0 | NaN |
| 20 | -999 | F | 2019-04-01 00:00:00 | 2019-09-19 | NaN | NaN | City_6451 | user20@example.com | 1.651897e+10 | basic | 92.38 | INR | 2018-01-22 08:17:00 | ERROR | 329.236584 | 4.0 | NaN |


Let us begin by detecting column types in this dataset.

    from datalabx import Diagnosis

    Diagnosis(df).detect_column_types()

Output:

    {
        'Numerical': ['user_id','phone','billing_amount','session_length_sec', 'feedback_score'],

        'Datetime': [],

        'Categorical': ['age','gender','account_created_at','last_seen_at','account_closed_at','country_code',
        
                        'city','email','plan_tier','currency','event_time','event_type','notes']
    }

We can see:

- Most of the columns have been identified as **Categorical** type.

- None of the columns have been identified as **Datetime** type. 

Let us look at the datatypes to understand why is that?

    Diagnosis(df).data_summary()['dtypes']

Output:

    user_id                 int64              # Incorrectly Identified
    age                    object              # Incorrectly Identified
    gender                 object      
    account_created_at     object              # Incorrectly Identified
    last_seen_at           object              # Incorrectly Identified
    account_closed_at      object              # Incorrectly Identified
    country_code           object
    city                   object
    email                  object
    phone                 float64              # Incorrectly Identified
    plan_tier              object              
    billing_amount        float64            
    currency               object
    event_time             object              # Incorrectly Identified
    event_type             object
    session_length_sec    float64
    feedback_score        float64
    notes                  object
    dtype: object

We can see:

- Column *'user_id'* has **object** datatype as it is a number, however, we read earlier that ``user-id is a unique identification``, and hence, a **category**.
- Column *'age'* is a number we can do calculations on, however, it has **object** datatype here.
- Columns *'account_created_at'*, *'last_seen_at'*, and *'account_closed_at'* are dates and timestamps, however, they have **object** datatype here.
- Column *'phone'* is a number however it is also a unique id like user-id, and is a category, however, it has **float64** as datatype, which is for numbers.
- Column *'event_time'* is also a date-time column, however, it has **object** datatype here.

But, what is new about all this? Didn't we do the same thing in the previous part?

Yes, we certainly did, however, let us take a closer look at Columns *'account_created_at'* and *'account_closed_at'*.

What's common about these both is that they have some data in them, that is not dates.

We can see:

- They have good dates and time data (like **2020-05-22 00:00:00**).

- They have some values that are NaN (these represent missing data)

- Column *'account_created_at'* has a value that says **'UNKNOWN_DATE'**.

- Column *'account_closed_at'* has a value that reads **CLOSED_UNKNOWN**.

<br>

We can clearly see that we have valid dates, NaN that represent missing data, and some text that also represents missing data.

We can read more about both kinds of missing data (NaN and text based missing values like UNKNOWN etc.) in **Missingness** docs.

However, what do you think may happen when we try to convert these incorrectly identified date-time columns with text data into correct date-time columns?

*Well, that's easy! We can just convert them into Datetime columns as usual, can't we?*

Well, it may seem very logical to have them converted into Datetime Columns, however, this is a common limitation in many data tools. 

### **Limitation:**

``A column will only become a date/time column when all its values are actual dates or timestamps.``

``If any value is text or mixed in, the column is treated as text so nothing is accidentally changed or lost.``

As we have text as missing data in columns *'account_created_at'* and *'account_closed_at'*, even after the datetime conversion, they still remain of **object** datatype.

**This is done in order to preserve and maintain data-integrity**.

Let us see what happens when we try to convert them:

Example:

    df = ColumnConverter(df, ['account_created_at', 'last_seen_at', 'account_closed_at', 'event_time']).to_datetime()

Output:

| user_id | age  | gender | account_created_at     | last_seen_at | account_closed_at        | country_code | city       | email                 | phone         | plan_tier | billing_amount | currency | event_time           | event_type | session_length_sec | feedback_score | notes          |
|--------:|-----:|:------:|------------------------|--------------|--------------------------|--------------|------------|-----------------------|---------------|-----------|----------------|----------|---------------------|------------|--------------------|----------------|----------------|
| 1 | 21 | M | 2015-07-25 00:00:00 | 2017-07-04 | NaN | US | City_616 | NaN | NaN | basic | 46.68 | NaN | 2024-05-19 21:02:00 | click | 363.110570 | 2.0 | NaN |
| 2 | 65 | M | 2018-11-10 00:00:00 | 2021-03-03 | NaN | UK | City_1220 | user2@example.com | 1.475936e+10 | free | -1.00 | USD | 2018-08-07 11:24:00 | login | 0.000000 | 3.0 | NaN |
| 3 | 57 | NaN | 2018-01-17 00:00:00 | 2018-08-25 | NaN | US | City_5924 | NaN | NaN | basic | 61.31 | INR | 2024-12-09 23:47:00 | purchase | 127.375824 | 2.0 | NaN |
| 4 | 44 | F | 2018-06-20 00:00:00 | 2019-05-05 | NaN | DE | City_5472 | user4@example.com | 1.243738e+10 | pro | 74.66 | USD | 2021-06-27 18:42:00 | login | -1.000000 | 3.0 | NaN |
| 5 | 43 | F | 2019-03-10 00:00:00 | 2022-12-28 | NaN | CA | City_5347 | NaN | NaN | basic | 0.00 | NaN | 2018-10-14 13:53:00 | logout | 289.892775 | -1.0 | NaN |
| 6 | 70 | M | 2018-07-08 00:00:00 | 2022-07-05 | NaN | IN | City_4353 | user6@example.com | 1.764699e+10 | basic | 34.32 | EUR | 2020-08-16 08:33:00 | click | 648.635141 | NaN | NaN |
| 7 | 21 | M | 2018-06-17 00:00:00 | 2022-02-13 | NaN | DE | City_5712 | none | NaN | pro | 6.41 | USD | NaN | logout | 280.832785 | 3.0 | NaN |
| 8 | 60 | M | 2021-07-06 00:00:00 | 2024-06-26 | 2024-07-11 00:00:00 | NaN | City_6525 | user8@example.com | 1.454826e+10 | free | 56.48 | INR | 2020-08-23 00:24:00 | login | 370.928378 | 2.0 | NaN |
| 9 | 28 | F | 2022-08-18 00:00:00 | 2025-05-30 | NaN | NaN | City_3517 | NaN | NaN | pro | 58.55 | USD | 2021-09-05 00:05:00 | click | 371.456613 | 3.0 | Bad UX |
| 10 | 22 | M | 2023-07-27 00:00:00 | 2024-06-18 | NaN | NaN | City_6956 | NaN | NaN | basic | 28.81 | USD | 2019-09-04 18:20:00 | ERROR | 209.346019 | 3.0 | NaN |
| 11 | 49 | M | 2020-05-22 00:00:00 | 2022-07-16 | 2022-09-11 00:00:00 | US | City_5191 | user11@example.com | 1.443582e+10 | free | 46.28 | USD | 2018-07-24 19:31:00 | ERROR | 266.222484 | 5.0 | NaN |
| 12 | 78 | F | UNKNOWN_DATE | NaT | NaN | US | City_2247 | none | 1.838258e+10 | free | 58.85 | USD | NaN | ERROR | 0.000000 | 3.0 | NaN |
| 13 | 63 | F | 2015-05-23 00:00:00 | 2015-07-30 | 2016-01-21 00:00:00 | US | City_1927 | user13@example.com | 1.668452e+10 | NaN | 68.51 | INR | 2018-12-13 03:59:00 | purchase | 298.436304 | 3.0 | . |
| 14 | 64 | F | 2023-06-19 00:00:00 | 2026-02-07 | NaN | IN | City_4418 | user14@example.com | 1.302826e+10 | NaN | 61.98 | USD | 2024-04-21 07:33:00 | logout | 294.113950 | 3.0 | NaN |
| 15 | 61 | M | 2021-03-30 00:00:00 | 2024-09-05 | 2024-12-24 00:00:00 | NaN | City_5977 | NaN | NaN | free | 41.99 | NaN | 2018-12-01 00:41:00 | click | 518.860086 | 4.0 | NaN |
| 16 | 66 | M | 2021-05-25 00:00:00 | 2024-11-14 | CLOSED_UNKNOWN | US | City_336 | user16@example.com | 1.414761e+10 | pro | 53.19 | NaN | 2020-12-20 11:26:00 | login | 235.391323 | NaN | NaN |
| 17 | 48 | F | 2019-09-24 00:00:00 | 2020-10-16 | NaN | US | City_7230 | NaN | NaN | NaN | 54.40 | INR | 2023-01-31 03:48:00 | ERROR | 628.769202 | 4.0 | Great service |
| 18 | 24 | F | 2022-06-15 00:00:00 | 2023-12-31 | NaN | CA | City_6936 | NaN | NaN | pro | 46.10 | INR | 2020-08-12 16:21:00 | logout | 298.485780 | NaN | NaN |
| 19 | 69 | F | 2015-07-30 00:00:00 | 2016-04-05 | NaN | NaN | City_5044 | user19@example.com | 1.402160e+10 | NaN | 35.21 | USD | 2023-08-16 20:13:00 | logout | 420.852723 | 4.0 | NaN |
| 20 | -999 | F | 2019-04-01 00:00:00 | 2019-09-19 | NaN | NaN | City_6451 | user20@example.com | 1.651897e+10 | basic | 92.38 | INR | 2018-01-22 08:17:00 | ERROR | 329.236584 | 4.0 | NaN |

Let us now attempting detecting column types:

    Diagnosis(df).detect_column_types()

Output:


    {'Numerical': ['user_id',
    'phone',
    'billing_amount',
    'session_length_sec',
    'feedback_score'],

    'Datetime': ['last_seen_at'],               <- Only 'last_seen_at' got added as Datetime.

    'Categorical': ['age',
    'gender',
    'account_created_at',
    'account_closed_at',
    'country_code',
    'city',
    'email',
    'plan_tier',
    'currency',
    'event_time',
    'event_type',
    'notes']}

Let us also verify the datatypes:

    Diagnosis(df).data_summary()['dtypes']

Output:

    user_id                        int64
    age                           object
    gender                        object
    account_created_at            object
    last_seen_at          datetime64[ns]
    account_closed_at             object
    country_code                  object
    city                          object
    email                         object
    phone                        float64
    plan_tier                     object
    billing_amount               float64
    currency                      object
    event_time                    object
    event_type                    object
    session_length_sec           float64
    feedback_score               float64
    notes                         object
    dtype: object
        
We can see:

- Only column *'last_seen_at'* got converted to **Datetime** because it did not have text as replacement for missing data.

- Columns *['account_created_at', 'account_closed_at', 'event_time']* still have **object** datatype and are not converted to **Datetime**.

## Does that mean I cannot convert to Datetime?

No. 

It just means that if you have text as replacement for missing data in **Datetime** columns, then, it is okay to leave them as text or **object** datatype for now.

We will come back to them later after we learn how to handle missing data in our dataset.
