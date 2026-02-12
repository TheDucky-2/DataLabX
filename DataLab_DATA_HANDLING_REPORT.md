![DataLab logo](/assets/DataLab_logo.png)

# Data Handling Report

This document explains how **DataLab handles data** in different modules and functions specifying whether a step **mutates data or only changes representation**. 

---

## Why this document exists

Real-world data is **messy**, **inconsistent**, and often **ambiguous**. 

Even small mistakes in handling can lead to **incorrect conclusions**, **broken workflows**, or **silent data corruption**.

This document exists to make DataLab’s data handling **explicit and transparent**. It is intended to serve several purposes:

#### For Users:

- Understand how DataLab treats data at each step.

- Distinguish between representation changes **(format, type, placeholders)** and meaningful data changes **(cleaning, preprocessing)**.

- Know why certain transformations are applied, how missing values are handled, and what visualizations actually do.

#### For Contributors:

- Identify which modules or functions can change data and which are purely observational.

- Ensure that new features, bug fixes, or refactors **do not accidentally alter data meaning.**

- Aligns with DataLab’s philosophy of **safety, transparency, and diagnosis-first workflows.**

#### For Audit and Reproducibility:

- Single reference for **data mutation rules** across the library.

- Ensures analyses are reproducible and predictable, even with dirty datasets.

- Clarifies which operations are safe to run without altering data meaning.

In short, this document is about **trust and clarity**.

> It is for making sure anyone interacting with DataLab - whether a user, a contributor or a reviewer, knows what happens to the data at each step, and can reason about it with confidence.

---

## 📈 TABULAR DATA

DataLab currently focuses on **tabular data**, so this report covers modules for tabular workflows. 

As DataLab evolves, additional modules and data types will be included.

### 1. Data Loading

**Sub-Package:** ``data_loader``

| Module Name | Action           | Data Mutation?                                                      | Notes                                                 |
|-------------| ---------------- | --------------------------------------------------------------------- | ----------------------------------------------------- |
|``data_loader``| Load all columns of the dataset and converts them to ``string`` datatype|    ``❌`` **Only representation changes**     | Avoids silent coercion; preserves dirty/mixed data    |
|             | Pandas missing types (`NA`, `np.nan`, `None`, `Null`, `NAT`) --> `None`   | ``❌`` **Only representation changes**  | Ensures that meaning of missing data is preserved.

> Loading is observational; it standardizes representation but does not alter what the data represents.

### 2. Data Diagnosis

**Sub-package** -> ``data_diagnosis``

| Module Name          | Action                                                                                           | Data Mutation? | Notes                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------ | -------------- | -------------------------------------------------------- |
| ``Diagnosis``            | Provides previews, summaries and column insights (duplicates, types, cardinality, memory usage, unique values)               | ``❌`` **No mutation**  | Returns computed summaries in dicts or DataFrames        |
| ``DirtyDataDiagnosis``   | Diagnose inconsistencies and dirty data                                                       | ``❌`` **No mutation**  | Inspects and reports dirty values without changing data  |
| ``TextDiagnosis``        | Text column diagnostics (lengths, patterns, invalid values)                                      | ``❌`` **No mutation**  | Reports issues in text columns for understanding         |
| ``NumericalDiagnosis``   | Distribution type, sparsity, skewness, kurtosis, variance, outlier detection | ``❌`` **No mutation**  | Observational, returns results in dicts/Series           |
| ``CategoricalDiagnosis`` | Unique category counts, frequency per category                                                   | ``❌`` **No mutation**  | Reports frequency statistics without modifying data      |
| ``MissingnessDiagnosis`` | Rows/columns containing missing data, missing data types (**pandas + domain dependant**), missing data summaries                       | ``❌`` **No mutation**  | Observes missing values; does not fill or alter anything |

> Diagnosis modules are strictly observational; no changes to underlying data occur.

### 3. Data Cleaning

**Sub-Package:** ``data_cleaner``

| Module Name | Action           | Data Mutation?                                                      | 
|-------------| ---------------- | --------------------------------------------------------------------- | 
| ``ColumnConverter`` | Converts column to numeric, categorical, datetime as requested |  ``✅`` **Yes, explicit mutation**      | 
|  ``MissingHandler``           | Fills or imputes missing values according to strategy   | ``✅`` **Yes, explicit mutation**   | 
| ``NumericalCleaner`` | Removes currency symbols, units, text etc. |    ``✅`` **Yes, explicit mutation**    | 
|  ``TextCleaner``           | Normalizes text, removes placeholders/punctuation   | ``✅`` **Yes, explicit mutation**  

> Cleaning mutates data, but all changes are intentional, documented, and reversible where possible.

### 4. Data Preprocessing

**Sub-Package:** ``data_preprocessor``

| Module Name | Action           | Data Mutation?               |
|-------------| ---------------- | --------------------------------------------------------------------- | 
| ``CategoricalPreprocessor`` | Converts to ordinal encoding, one-hot encoding, etc. |  ``✅`` **Yes, explicit mutation**      |
|  ``Normalization``           | Scales/normalizes columns   | ``✅`` **Yes, explicit mutation**   | 
| ``Standardization`` | Standardizes numeric columns |    ``✅`` **Yes, explicit mutation**    |

> Preprocessing mutates data for downstream analysis but is auditable and intentional.

### 5. Data Visualization

**Sub-Package:** ``data_visualization``

| Module Name | Action           | Data Mutation?               |
|-------------| ---------------- | --------------------------------------------------------------------- | 
| ``CategoricalVisualizer`` | Plots frequency of categories |  ``❌`` No mutation; side-effect     |
|  ``NumericalVisualizer``           | Plots distributions (histogram, kde, box plot, qq plot)   | ``❌`` No mutation; side-effect   | 
| ``MissingnessVisualizer`` | Converts user-provided, domain-specific missing value placeholders --> `np.nan` **strictly for visualization purposes** |   ``✅`` ⚠️ Representation-level mutation only with **meaning preserved** and behavior explicitly documented     |

> Visualizations are observational; they do not alter data.

### 6. Utilities

**Sub-Package**: ``utils``

Module Name | Action                           | Action                        | Data Mutation?                                              |
|-----------| -------------------------------- | --------------------------------------- | ----------------------------------------------------------- |
``BackendConverter`` | Converts between Pandas DataFrame **<-->** Polars DataFrame | Returns new DataFrame of requested type | ``✅`` Only representation changes; **underlying meaning preserved** |

---

## Key Notes for Users & Contributors

1. **Observation vs. Mutation:**

    - Observation --> only inspecting, reporting, visualizing
    - Mutation --> changing the actual values or structure

2. **Representation changes** are allowed in loading and backend conversion, but **meaning is never silently changed.**

3. **Explicit cleaning or preprocessing** is the only time meaning changes intentionally.

4. All modules **follow** DataLab’s diagnosis-first philosophy: understand data before changing it.