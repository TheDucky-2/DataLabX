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

**DirtyDataDiagnosis** in datalabx refers to the check-up of dirt or issues present in numbers, text or date-time data.

It helps us detect:

- Issues with Numerical data (like units, commas, text, symbols, scientific notations present in numbers).
- Issues with Text data (like numbers, symbols, spaces present in text).
- Issues with Datetime data (like symbols, incorrect dates)

### **datalabx Usage:**

We can explore dirty data by importing ``DirtyDataDiagnosis`` class from datalabx.
```python
from datalabx import DirtyDataDiagnosis

diagnosis = DirtyDataDiagnosis(df)
```

## Before We Explore Dirty Data

Before running any Dirty Data Diagnosis in datalabx, we will learn about a few considerations:

### Index

``datalabx temporarily modifies your DataFrame by adding an index to track original row positions.``

This allows all diagnostics to reference the correct rows reliably.

This change is done **in-place** but is safe and will not interfere with your other columns or your data.

We will collect user feedback to ensure this approach fits real workflows over time.

**Example:** 
```python
df.head(5)
```
**Output:**

| Index | Age | Salary | Expenses | Height_cm | Weight_kg | Temperature_C | Purchase_Amount | Score | Rating | Debt |
|-------|-----|--------|----------|-----------|-----------|----------------|----------------|-------|--------|------|
| 1 | 20.673408544550288 | 134460.66741276794 | 9533.158420128186 | 1,53e+02 | 12193 | 2.05e+01 | 2.40e+03 | one | 3,33e+00 | $58,276.81 |
| 2 | 33.56 | missing | 4104.95 | 204 | 96.50051410846052 | -1,14e+01 | 2877.0871437672777 | four | unknown | 94033.3425007563 |
| 7 | 4748 | 122355,46 | None | 206.76284108092278 | unknown | 3061 | -3813.6973731160588 | 10$ | None | None |
| 8 | 19.668785230642992 | 113743 | None | 209cm | 7,41e+01 | -047 | None | approx 1000 | 1.76 | 7009614 |
| 11 | 5405 | 84,570kg | 3565 | 191,78 | 90 | three | 4.01e+03 | -46.50775056319312 | None | 7675,58 |

---

### Large Datasets

datalabx automatically uses Arrow-backed pandas types for large datasets **(anything > 100000 rows, adjustable)**.

This ensures:

- Faster processing and Polars **<->** Pandas conversion.

- Lower memory usage

- Stable performance even on millions of rows

These considerations help ensure your system does not slow down or crash while exploring real-world messy data.

**Example:**

```python
df.dtypes
```
**Output:**
```python
Age                large_string[pyarrow]
Salary             large_string[pyarrow]
Expenses           large_string[pyarrow]
Height_cm          large_string[pyarrow]
Weight_kg          large_string[pyarrow]
Temperature_C      large_string[pyarrow]
Purchase_Amount    large_string[pyarrow]
Score              large_string[pyarrow]
Rating             large_string[pyarrow]
Debt               large_string[pyarrow]
dtype: object
```

## Performance Note

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
