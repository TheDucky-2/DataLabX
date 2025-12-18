# **Missingness (Missing Data)**

Imagine someone gives you some random data and says - ``Use this data to make an important decision``.

You open the file.

There are hundreds to thousands of rows and several columns.

Everything looks fine at first glance. You see numbers, words, dates - it really feels complete.

You build charts, do analysis, create models and share your results.

Later, someone says - ``Did you notice that half of the income data was missing?``

You didn’t. 

The missing values were hidden inside the data.

And because of that, your results turned out to be misleading.

This is a very common situation in the field of data, and this is why missing data deserves its own section.

## But, What does Missing Data mean in DataLab?

In DataLab, missingness does not only mean absence of values.

Missingness means:

- Values that are truly absent, like nothing is there. Just empty space.

- Values like NaN (Not a Number), which is a placeholder value for missing numbers.

- Values like NaT (Not a Time) which is placeholder value for missing dates or time.

- Values explicitly decided by the user to be missing, like UNKNOWN, MISSING or ERROR etc.

- Values that look valid but actually mean **we don’t know** in the domain context.

Because missingness is often context-dependent, there is no single universal definition that works for every dataset.

That’s why DataLab treats missingness as something to be understood and handled separately, not guessed or auto-detected.

## ⚠️ **Important Note:** Missingness Can Be Meaningful

In real-world data scenarios, a missing value does not always mean ``hey, this data has no value!``.

Sometimes, why a value is missing is itself an important thing to look out for.

For example:

    income	credit score
    45000	   720
     NaN	   680
     NaN	   510


In this case, missing income values may indicate:

- Unreported income
- Informal or irregular employment
- Limitations in data collection

Automatically removing or filling these values may hide important patterns.

That’s why DataLab follows a simple principle:

> **Always understand what missingness represents before deciding how to handle it.**

## How DataLab Handles Missingness

DataLab does not treat all missing values as the same.

Instead, it looks at missing values step by step, based on the type of data:

- Numbers, text, and dates are checked separately.

- Missing values that already exist (like NaN or NaT) and values chosen by the user (like MISSING or UNKNOWN) are detected together.

- Missing values are handled by column type, not all at once for the whole dataset.

- The user can decide what are missing values and what to do with them. For example - they can look at them, keep them, change them, or remove them.

This makes missing data easier to understand, more flexible to work with, and closer to how real data actually behaves.

## What Comes Next? Handling Missing Data

Missing data is not something you fix in one step.

It should be handled step by step.

In DataLab, missing data is handled in three simple stages:

**1.** **Understand**

Before fixing anything, DataLab helps you look at your data:

- First, it shows which values are missing

- Then, it lets you see the data itself, including empty cells or words like NAN, UNKNOWN, ERROR etc.

- Finally, it shows simple counts, like how many values are missing

Nothing is changed here.

This step is just about looking and learning about your data, not fixing.

**2. See**

Next, DataLab shows missing data using simple pictures (like **missingno** charts):

- You can see where data is missing in each row and column

- You can spot blocks or groups where values are missing together

- You may notice patterns that hint why data is missing

These pictures make missing data easy to notice, even if you’re new to data.

They help you see problems that numbers alone might miss.

**3. Decide**

After you understand and see the missing data, you can choose what to do:

- Use different options for numbers, text, and dates

- You are in control - nothing happens automatically

- Any changes are clear and easy to understand

## Why This Way?

Going step by step - ``Understand -> See -> Decide How to Handle -> Helps Avoid Mistakes.``

It makes sure missing data is handled carefully and on purpose, just like in real data work.