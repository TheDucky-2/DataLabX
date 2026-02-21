![datalabx logo](assets/datalabx_logo.png)

# API Return Types Reference

This file lists all public modules and methods in **datalabx** and their expected return types.

This helps users know what to expect when calling functions and methods.

---

## 📂 datalabx.tabular.data_loader

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|---------|
| DataLoader | `pandas.DataFrame` | Returns a pandas dataframe from CSV, Excel, JSON, or Parquet | ``from datalabx import DataLoader``

---

## 📂 datalabx.tabular.computations

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|---------|
| Correlation | `pandas.DataFrame` | Column correlations | ``from datalabx import Correlation``
| Distribution | `pandas.DataFrame` | Value distributions per column | ``from datalabx import Distribution``
| Outliers | `pandas.DataFrame` | Detected outliers | ``from datalabx import Outliers``
| Statistics | `pandas.Series` | Column-level statistics | ``from datalabx import Statistics``

---

## 📂 datalabx.tabular.data_cleaner

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|---------|
| ColumnConverter | `pandas.DataFrame` | Converts column types (numeric, categorical, datetime) | ``from datalabx import ColumnConverter``
| MissingHandler | `pandas.DataFrame` | Handles missing values using guided strategies | ``from datalabx import MissingHandler``
| NumericalCleaner | `pandas.DataFrame` | Cleans numeric columns (spaces, units, currency, etc.) | ``from datalabx import NumericalCleaner``
| TextCleaner | `pandas.DataFrame` | Cleans text columns (punctuation, placeholders, normalization) | ``from datalabx import TextCleaner``

---

## 📂 datalabx.tabular.data_preprocessor

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|----------|
| CategoricalPreprocessor | `pandas.DataFrame` | Encodes categorical columns (ordinal, one-hot, etc.) | ``from datalabx import CategoricalPreprocessor`` 
| Normalization | `pandas.DataFrame` | Normalizes numeric columns | ``from datalabx import Normalization``
| Standardization | `pandas.DataFrame` | Standardizes numeric columns | ``from datalabx import Standardization``

---

## 📂 datalabx.tabular.data_visualization

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|----------|
| CategoricalVisualizer | `tuple[Figure, Axes]` | Returns Matplotlib figure and axes for further customization | ``from datalabx import CategoricalVisualizer``
| MissingnessVisualizer | `tuple[Figure, Axes]` | Returns Matplotlib figure and axes for missing data visualization | ``from datalabx import MissingnessVisualizer``
| NumericalVisualizer | `tuple[Figure, Axes]` | Returns Matplotlib figure and axes (histogram, boxplot, KDE, etc.) | ``from datalabx import NumericalVisualizer``

---

## 📂 datalabx.tabular.utils

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|----------|
| BackendConverter | ``pandas.DataFrame`` or ``polars.DataFrame`` | Converts pandas <-> polars | ``from datalabx import BackendConverter``

---

## 📂 datalabx.tabular.data_diagnosis

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|---------|
| DirtyDataDiagnosis | `dict[str, dict[str, pandas.DataFrame]]` | Column-level diagnostics for messy data | ``from datalabx import DirtyDataDiagnosis``
| TextDiagnosis | `dict[str, pandas.DataFrame]` | Text column diagnostics (lengths, patterns, invalid values) | ``from datalabx import TextDiagnosis``
| CategoricalDiagnosis.count_unique_categories | `dict[str, float]` | Number of unique values per column | ``from datalabx import CategoricalDiagnosis``
| CategoricalDiagnosis.show_frequency | `dict[str, pandas.Series]` | Frequency counts per category |
| NumericalDiagnosis.check_distribution | `dict[str, str]` | Distribution type per numeric column | ``from datalabx import NumericalDiagnosis``
| NumericalDiagnosis.check_sparsity | `dict[str, float]` | Occurrence of a specific value per column |
| NumericalDiagnosis.check_skewness | `dict[str, float]` | Skewness per numeric column |
| NumericalDiagnosis.check_kurtosis | `dict[str, float]` | Kurtosis per numeric column |
| NumericalDiagnosis.check_variance | `dict[str, float]` | Variance per numeric column |
| NumericalDiagnosis.detect_outliers | `dict[str, pandas.Series]` | Rows of detected outliers per column |
| MissingnessDiagnosis.detect_missing_types | `dict[str, dict[str, list]]` | Shows missing types per column (pandas missing, placeholders, etc.) | ``from datalabx import MissingnessDiagnosis``
| MissingnessDiagnosis.missing_data_summary | `dict[str, float]` | Fraction of missing data per column |
| MissingnessDiagnosis.rows_with_all_columns_missing | `pandas.DataFrame` | Rows where all columns are missing |
| MissingnessDiagnosis.rows_with_specific_columns_missing | `pandas.DataFrame` | Rows where specific columns are missing |
| MissingnessDiagnosis.show_missing_rows_in_categorical_columns | `dict[str, pandas.DataFrame]` | Missing rows by categorical column |
| MissingnessDiagnosis.show_missing_rows_in_datetime_columns | `dict[str, pandas.DataFrame]` | Missing rows by datetime column |
| MissingnessDiagnosis.show_missing_rows_in_numerical_columns | `dict[str, pandas.DataFrame]` | Missing rows by numeric column |
