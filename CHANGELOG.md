![DataLab logo](assets/DataLab_logo.png)

# DataLab Change-Log

All versions listed below `0.1.0` are **pre-releases published to TestPyPI only**.

The first stable public release on PyPI will be **0.1.0**.

---

## v0.1.0b5 - Feb 01, 2026

**Status:** Beta (pre-release - TestPyPI only)

DataLab **v0.1.0b5** is a **stabilization and correctness release** that fixes issues introduced in v0.1.0b4, with a strong focus on **API reliability, type-safety, testing, and documentation clarity**.

**⚠️ Pre-release note:** This release primarily fixes bugs and documentation inconsistencies; no major new features are introduced.

### 🚀 Major Changes

- Stabilized APIs and behaviors affected in v0.1.0b4.

- Introduced a dedicated **DataLab API Return Types Reference (DataLab_API_RETURN_TYPES.md)** documenting expected return types for all public APIs.

### ✨ Added

- Centralized API return type reference covering all public modules and methods.

- Expanded output-type tests to enforce documented return type guarantees.

- Completed **type hint coverage** across remaining preprocessing, diagnosis, and visualization modules.

- Utilities package fully integrated into the project structure.

### 💡 Improved

- README refined for accuracy and clarity.

- Documentation formatting and structure polished for better readability.

- CI workflows adjusted to ensure consistent testing and documentation builds.

### 🐛 Fixed

- Fixed bugs in:

  - ``Distribution.skewness()``, ``Distribution.raw_kurtosis()`` and ``Distribution.excess_kurtosis()``.

  - ``NumericalDiagnosis.check_kurtosis()`` and ``NumericalDiagnosis.check_skewness()``

- Corrected mismatches between documented and actual API return types.

- Fixed test failures and edge cases introduced in **v0.1.0b4.**

- Resolved documentation build issues related to **assets, logo paths, and pdoc rendering.**

### 💡 Key Notes for Users

- **Recommended upgrade:** v0.1.0b5 supersedes v0.1.0b4.

- **API clarity:** Users can now rely on a single, authoritative return-type reference.

- **Stability:** Improved testing and bug fixes increase confidence in API behavior.

- **Pre-release reminder:** APIs are nearing stability ahead of ``v0.1.0.``

## v0.1.0b4 - Jan 27, 2026

**Status:** Beta (pre-release - TestPyPI only)

DataLab **v0.1.0b4** is a pre-release version with improvements in **documentation**, **CI/CD**, **badges**, and **preprocessing workflows**, focusing on **better usability**, **consistency**, and **API clarity**.

⚠️ **Pre-release note:** APIs may change as the library evolves, especially around backend handling.

### 🚀 Major Changes

#### 1. **CSV Data Loading**:

**``load_tabular()``** method now loads all columns of a **CSV** file as **"string"** type by default to improve handling of dirty or mixed-type datasets.

- For full API reference, see [DataLab API Docs](https://theducky-2.github.io/DataLab/)

#### 2. **CI/CD Workflows**:

Triggers, environment setup, and documentation generation with pdoc.

#### 3. **README**:

README updated with **Python version**, **license**, **TestPyPI**, **status**, and **API documentation badges**.

#### 4. **Python-version Requirement**:

Python version requirement updated to **>=3.12**.

#### 5. **Preprocessing**

Core preprocessing modules refactored for **API consistency** and **readability**.

### ✨ New Features & Improvements

- Logging throughout key modules to track workflow steps and operations.

- New methods for categorical preprocessing and distribution analysis:

  - ``label_encoding()``

  - ``ordinal_encoding()``

  - ``skewness()``

- ``NumericalCleaner`` now supports **array type** and **conversion thresholds** functionality.

- Refactored code for **consistency**, **readability**, and **API stability**.

- Enhanced preprocessing methods with **better validation** and **error handling**.

- Reformatted documentation for better clarity and **GitHub Pages** integration.

- Backend flexibility planning extended to other Polars-based classes.

- Docstrings refactored from ``__init__.py`` to ``class-level`` across multiple packages for **cleaner documentation** and better **API reference generation**.

### 🐛 Fixed

- Various bugs in ``Normalization``, ``Distribution``, and ``preprocessing`` modules.

- Docstring formatting and API documentation visibility issues.

- Code consistency issues and output type mismatches across modules.

- Removed ``DtypeConverter`` class and its methods.

- Removed base classes like ``DataPreprocessor`` and ``DataVisualizer`` from ``__init__.py`` of their respective packages.

---

## v0.1.0b2 - Jan 22, 2026
**Status:** Beta (pre-release - TestPyPI only)

DataLab **v0.1.0b2** is a pre-release version with improvements in **performance, dirty data diagnosis, visualizations, and usability**.

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

v0.1.0a4 focused on **missing data visualization, initial diagnosis workflows, and documentation improvements**.  

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