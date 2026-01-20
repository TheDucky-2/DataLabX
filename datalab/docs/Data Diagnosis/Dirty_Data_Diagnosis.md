# **Dirty Data Diagnosis**

Imagine opening your fridge and noticing a few problems such as:

- Expired food

- Containers with no labels

- The same item is stored in multiple sections

- Ice spread all over the freezer

- Some ingredients are spilled or mixed with each other.

**Dirty data diagnosis** means the same thing for our data.

It means carefully checking our data to find problems like:

- Numbers written as words or mixed with symbols and text, instead of just numbers.

- Empty data or replaced with words like 'missing' or 'unknown' or symbols like '?'.

- Numbers including units like 'cm' or '$' when they should not.

- Numbers written in scientific notation

> Dirty Data Diagnosis is required because we can’t clean or fix data unless we know exactly what’s wrong with it.

Once, we identify the problems that exist in our data, it would be easier to know what and how to clean it.

##  Dirty Data Diagnosis Overview

**DirtyDataDiagnosis** in DataLab refers to the check-up of dirt or issues present in numbers, text or date-time data.

It helps us detect:

- Issues with Numerical data (like units, commas, text, symbols, scientific notations present in numbers).
- Issues with Text data (like numbers, symbols, spaces present in text).
- Issues with Datetime data (like symbols, incorrect dates)

### **DataLab Usage:**

We can explore dirty data by importing ``DirtyDataDiagnosis`` class from DataLab.

    from datalab import DirtyDataDiagnosis

    diagnosis = DirtyDataDiagnosis(df)

## Considerations before we explore dirty data

Before running any dirty data diagnosis in DataLab, we will learn about a few considerations:

### Index

``DataLab temporarily modifies your DataFrame by adding an index to track original row positions.``

This allows all diagnostics to reference the correct rows reliably.

This change is done **in-place** but is safe and will not interfere with your other columns or your data.

We will collect user feedback to ensure this approach fits real workflows over time.

### Large Datasets

DataLab automatically uses Arrow-backed pandas types for large datasets **(anything > 100000 rows, adjustable)**.

This ensures:

- Faster processing and Polars <-> Pandas conversion.

- Lower memory usage

- Stable performance even on millions of rows

These considerations help ensure your system does not slow down or crash while exploring real-world messy data.

## Performance Considerations

``DirtyDataDiagnosis`` has been tested on datasets with over 5 million rows and performs reliably using Arrow-backed pandas conversion.

However:

- Actual performance will be dependent on your system hardware (RAM, CPU).

- Large datasets may take longer to process or require more memory.

- By default, datasets over 100,000 rows automatically use Arrow-backed pandas types for stability and speed.

## What's Next?

We will now explore how we can diagnose:

- Dirty Numerical Data(numbers)

- Dirty Categorical Data (text)

- Dirty Datetime Data (Date & Time)

