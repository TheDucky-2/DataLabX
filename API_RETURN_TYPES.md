# DataLab API Return Types Reference

This file lists all public modules and methods in DataLab and their expected return types.  
This helps users know what to expect when calling functions and methods.

---

## 📂 datalab.tabular.data_loader

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|---------|
| loader | `pandas.DataFrame` | Returns loaded dataframe from CSV, Excel, JSON, or Parquet | ``from datalab import load_tabular``

---

## 📂 datalab.tabular.computations

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|---------|
| Correlation | `pandas.DataFrame` | Column correlations | ``from datalab import Correlation``
| Distribution | `pandas.DataFrame` | Value distributions per column | ``from datalab import Distribution``
| Outliers | `pandas.DataFrame` | Detected outliers | ``from datalab import Outliers``
| Statistics | `pandas.Series` | Column-level statistics | ``from datalab import Statistics``

---

## 📂 datalab.tabular.data_cleaner

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|---------|
| ColumnConverter | `pandas.DataFrame` | Converts column types (numeric, categorical, datetime) | ``from datalab import ColumnConverter``
| MissingHandler | `pandas.DataFrame` | Handles missing values using guided strategies | ``from datalab import MissingHandler``
| NumericalCleaner | `pandas.DataFrame` | Cleans numeric columns (spaces, units, currency, etc.) | ``from datalab import NumericalCleaner``
| TextCleaner | `pandas.DataFrame` | Cleans text columns (punctuation, placeholders, normalization) | ``from datalab import TextCleaner``

---

## 📂 datalab.tabular.data_preprocessor

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|----------|
| CategoricalPreprocessor | `pandas.DataFrame` | Encodes categorical columns (ordinal, one-hot, etc.) | ``from datalab import CategoricalPreprocessor`` 
| Normalization | `pandas.DataFrame` | Normalizes numeric columns | ``from datalab import Normalization``
| Standardization | `pandas.DataFrame` | Standardizes numeric columns | ``from datalab import Standardization``

---

## 📂 datalab.tabular.data_visualization

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|----------|
| CategoricalVisualizer | `None` | Visualization only (plots categories) | ``from datalab import CategoricalVisualizer``
| MissingnessVisualizer | `None` | Visualization only (missing data plots) | ``from datalab import MissingnessVisualizer``
| NumericalVisualizer | `None` | Visualization only (numeric plots: histogram, boxplot, KDE) | ``from datalab import NumericalVisualizer``

---

## 📂 datalab.tabular.utils

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|----------|
| BackendConverter | ``pandas.DataFrame`` or ``polars.DataFrame`` | Converts pandas <-> polars | ``from datalab import BackendConverter``

---

## 📂 datalab.tabular.data_diagnosis

| Module / Method | Return Type | Notes | Import |
|-----------------|------------|-------|---------|
| DirtyDataDiagnosis | `dict[str, dict[str, pandas.DataFrame]]` | Column-level diagnostics for messy data | ``from datalab import DirtyDataDiagnosis``
| TextDiagnosis | `dict[str, pandas.DataFrame]` | Text column diagnostics (lengths, patterns, invalid values) | ``from datalab import TextDiagnosis``
| CategoricalDiagnosis.count_unique_categories | `dict[str, float]` | Number of unique values per column | ``from datalab import CategoricalDiagnosis``
| CategoricalDiagnosis.show_frequency | `dict[str, pandas.Series]` | Frequency counts per category |
| NumericalDiagnosis.check_distribution | `dict[str, str]` | Distribution type per numeric column | ``from datalab import NumericalDiagnosis``
| NumericalDiagnosis.check_sparsity | `dict[str, float]` | Fraction of missing values per column |
| NumericalDiagnosis.check_skewness | `dict[str, float]` | Skewness per numeric column |
| NumericalDiagnosis.check_kurtosis | `dict[str, float]` | Kurtosis per numeric column |
| NumericalDiagnosis.check_variance | `dict[str, float]` | Variance per numeric column |
| NumericalDiagnosis.detect_outliers | `dict[str, pandas.Series]` | Indices of detected outliers per column |
| MissingnessDiagnosis.detect_missing_types | `dict[str, dict[str, list]]` | Shows missing types per column (pandas missing, placeholders, etc.) | ``from datalab import MissingnessDiagnosis``
| MissingnessDiagnosis.missing_data_summary | `dict[str, float]` | Fraction of missing data per column |
| MissingnessDiagnosis.rows_with_all_columns_missing | `pandas.DataFrame` | Rows where all columns are missing |
| MissingnessDiagnosis.rows_with_specific_columns_missing | `pandas.DataFrame` | Rows where specific columns are missing |
| MissingnessDiagnosis.show_missing_rows_in_categorical_columns | `dict[str, pandas.DataFrame]` | Missing rows by categorical column |
| MissingnessDiagnosis.show_missing_rows_in_datetime_columns | `dict[str, pandas.DataFrame]` | Missing rows by datetime column |
| MissingnessDiagnosis.show_missing_rows_in_numerical_columns | `dict[str, pandas.DataFrame]` | Missing rows by numeric column |
