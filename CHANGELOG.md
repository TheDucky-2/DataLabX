![DataLab logo](DataLab_logo_images/DataLab_logo.png)

# DataLab Change-Log

All versions listed below `0.1.0` are **pre-releases published to TestPyPI only**.

The first stable public release on PyPI will be **0.1.0**.

---

## v0.1.0b2 - Jan 22, 2026
**Status:** Beta (pre-release - TestPyPI only)

DataLab **v0.1.b2** is a pre-release version with improvements in **performance, dirty data diagnosis, visualizations, and usability**.

It provides a **Pandas-facing API**, so users always work with familiar Pandas DataFrames, while internally using **Polars** for performance and memory-efficient computations.  

⚠️ **Pre-release note:** APIs may change as the library evolves, especially around backend handling.

### 🚀 Major Changes

#### 1. **Polars-first workflow:**

User files are **loaded as Polars DataFrames** first, then **converted to Pandas** for the user-facing API.  

- Improves performance on low-RAM systems.

- Users can choose **NumPy** (default) or **PyArrow** backends.

#### 2. **Large dataset optimization:**

Datasets **≥ 100,000 rows** are automatically converted to PyArrow types for faster processing and lower memory usage.

#### 3. **BackendConverter updates:**

- Supports both **NumPy** and **PyArrow** during Pandas **<->** Polars conversion.

- Users can manually select backend or leave as auto.

#### 4. **DirtyDataDiagnosis performance & backend options:**

**DirtyDataDiagnosis** is the first class in DataLab that **fully supports backend switching between NumPy and PyArrow.**

- **Performance note:** Regex-based checks on dirty data are inherently slow on any tool.

  - **Backend switching** allows users to **optimize performance** for their dataset size and available memory.

- **Default backend selection:** datasets ≥ 100,000 rows **->** PyArrow; otherwise NumPy; Manual override is possible.

Backend flexibility will be extended to other Polars-based classes in future releases

#### 5. **Dirty data diagnosis now supports:**  

- **Numerical, Categorical, and Datetime columns** using **Polars regex** for faster and structured detection.

---

### ✨ New Features & Improvements

- Added ``DirtyDataDiagnosis`` class for diagnosing dirty data in Numerical, Categorical, and Datetime columns.

- Added Logger to track workflow steps and operations.

- Merged missing datatype detection into ``detect_missing_types()``.

- Added QQ plot in ``NumericalVisualizer`` to check numerical distributions.

- Renamed ``histogram`` -> ``plot_histogram()`` with bar labels for easier visualization.

- Added ``to_numerical_forced()`` in ColumnConverter to force conversions to Numerical datatype.

- Added a tracker in ``Data Cleaner`` classes to log values that remain dirty even after cleaning.

- Refactored ``TextCleaner`` and ``Text Diagnosis`` code: **updated docstrings and workflow guides.**

- Integrated Polars in ``DirtyDataDiagnosis``, ``NumericalCleaner`` and ``TextCleaner`` for faster processing on large datasets.

---

### 📚 Documentation Improvements

- **API reference and conceptual guides** have been **separated** for clarity.  
- Users can now clearly access:  
  - **API guides** for method usage, parameters, and workflows  
  - **Conceptual guides** explaining **why** each step matters in data diagnosis and cleaning  
- Improves **readability and usability** for beginners and advanced users alike.

---

### 🐛 Bug Fixes

- Fixed silent coercion of non-numeric values into NaN in ``ColumnConverter.to_numerical()``.

- Fixed bugs in ``Text Diagnosis`` and ``TextCleaner`` classes.

- Fixed issues in ``ColumnConverter.to_numerical()``.

---

### 💡 Key Notes for Users

- **Performance:** Backend flexibility allows better performance on large datasets without user intervention.

- **Experimental:** DirtyDataDiagnosis backend handling is currently the first class with Polars + Backend switching; this will expand to other heavy operations in future releases.

- **Safety & usability:** Explicit cleaning workflows, logging, and tracking ensure auditability and reproducibility.

- **Pre-release reminder:** APIs may change as the library develops and your feedback is welcome!

---

## **v0.1.0a4 – Dec 26, 2025**  
**Status:** Alpha (pre-release – TestPyPI only)  

v0.1.a4 focused on **missing data visualization, initial diagnosis workflows, and documentation improvements**.  

### 🚀 Major Changes

- **Missingness Visualization workflow completed:**  

  - Bar plots  
  - Matrix plots  
  - Heatmaps  
  - Dendrograms  

- Support for **custom missing value placeholders** across missingness diagnostics and visualizations.  
- **Annotated example images** for all missingness plots to help users build intuition.  
- Beginner-friendly, step-by-step documentation explaining **what each plot shows and why it matters**.  

---

### ✨ New Features & Improvements

- Clear separation of workflows:  
  - Exploring & visualizing missing data  
  - Handling missing data (intentionally deferred) 

- Improved **column type conversion logic** for accurate missingness detection and visualization.  

- Enhanced explanations of **patterns of missing data & relationships** across rows, columns, and groups of columns.  

- Introduced **Step 6: Understanding the Data (Preview)** to bridge missingness analysis with:  
  - Distributions  
  - Skewness  
  - Outliers  
  - Frequency  
  
- Documentation now follows a **connected, story-driven workflow** rather than isolated examples.  

---

### 🐛 Bug Fixes
- Fixed **Column Type Conversion**: non-convertible values remain unchanged to prevent data loss.  
- Fixed issues in **Distribution** module (`computations`) and **NumericalVisualizer** (`data_visualization`).  
- Resolved **versioning metadata issue** on TestPyPI.  

---

### 💡 Key Notes for Users
- **Deferred:** Missing data handling logic is postponed until after data diagnosis and visualization steps.  
- **Pre-release:** APIs and workflows are **subject to change**.  