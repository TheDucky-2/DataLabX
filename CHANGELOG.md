![DataLabX logo](assets/datalabx_logo.png)

# Change-Log

All versions listed below `0.1.b10` are **pre-releases published to TestPyPI only**.

The first stable public release on PyPI will be **0.1.0**.

---

## 🔁 Versions

### DataLabX

##### PyPI Versions

- [v0.1.0b13](#v010b13---apr-24-2026)
- [v0.1.0b12](#v010b12---mar-30-2026)
- [v0.1.0b11](#v010b11---mar-16-2026)
- [v0.1.0b10](#v010b10---feb-22-2026)

### DataLab (TestPyPI Only)

##### TestPyPI Versions

- [v0.1.0b9](#v010b9---feb-17-2026)
- [v0.1.0b8](#v010b8---feb-17-2026)
- [v0.1.0b7](#v010b7---feb-08-2026)
- [v0.1.0b6](#v010b6---feb-01-2026)
- [v0.1.0b4](#v010b4---jan-27-2026)
- [v0.1.0b2](#v010b2---jan-22-2026)
- [v0.1.0a4](#v010a4-–-dec-26-2025)

---

## v0.1.0b13 - Apr 24, 2026

**Status:** Beta (PyPI)

DataLabX **v0.1.0b13** improves data loading robustness, error handling, and diagnosis performance, with better support for **real-world file inconsistencies** and **malformed data**.

### ⚠️ Important Updates

- Added JSON5 support as a fallback parser for handling **loosely formatted JSON** files.
- Introduced a custom **EmptyFileError** for clearer handling of empty or invalid file inputs.
- Improved DataLoader reliability for real-world file ingestion scenarios.

### 🚀 Major Changes

#### 1. Robust JSON Handling

- Added json5 as a dependency to handle **non-strict JSON formats** commonly found in real-world data.
- Implemented **JSON5 fallback parsing** when standard JSON parsing fails.
- Improved compatibility with loosely structured API and scraped data.

#### 2. DataLoader Improvements

- Enhanced file input handling across formats.
- Improved error handling for **invalid or empty files**.
- Added support for **detecting** and **handling empty file** inputs gracefully.

#### Custom Error Handling

- Introduced **EmptyFileError** for clearer debugging and control.
- Refactored error structure for better **consistency and readability**.

#### Diagnosis Performance Optimization

- Refactored **Dirty Data Diagnosis** to use cached pattern masks, improving performance.
- Reduced **redundant computations** during repeated checks on large datasets.

#### Testing Improvements

- Added **test_file_input** to improve reliability of file ingestion workflows.

### 🐛 Bug Fixes

- Fixed issues in DataLoader when handling empty or malformed files.
- Improved stability of JSON parsing in edge cases.

### 💡 Key Notes

- This release strengthens **real-world data ingestion**, especially for messy JSON and scraped data.
- Performance improvements in diagnosis make DataLabX more efficient on **repeated operations**.
- Continues the focus on **robustness, correctness**, and **practical usability**.
- Upcoming releases will introduce **DuckDB integration** for improved performance, scalable data processing, and advanced querying capabilities.

## v0.1.0b12 - Mar 30, 2026

**Status**: Beta (PyPI)

DataLabX **v0.1.0b12** focuses on **support for txt files**, **refining missingness detection**, **improving data loading flexibility**, and fixing **critical warnings and stability issues**, based on **real-world usage**.

### ⚠️ Important Updates

- Addition of support for **.txt** files. Users can now load .txt files using ``DataLoader``.

- ``MissingnessDiagnosis().detect_missing_types()`` now returns **total missing types**, simplifying interpretation and removing separation between pandas and placeholder-based missing values.
- Introduced **DEFAULT_PLACEHOLDERS** for common real-world missing value representations, combined with user-defined placeholders.
- Excel support improved via optional dependency **fastexcel**.

### 🚀 Major Changes

#### 1. Missingness Detection Improvements

- Added **DEFAULT_PLACEHOLDERS** (e.g., "NA", "N/A", "-", etc.) for commonly used missingness placeholders for more realistic missing data detection.

- ``detect_missing_types()`` redesigned to return a unified missingness view instead of split categories.

```python
from datalabx import MissingnessDiagnosis

result = MissingnessDiagnosis(df).detect_missing_types()

print(result)

>>> {'total_deaths': [''],
 'total_recovered': ['N/A', ''],
 'active_cases': ['N/A'],
 'total_tests': [''],
 'population': [''],
 'total_cases_per_1m_pop': [''],
 'deaths_per_1m_pop': [''],
 'tests_per_1m_pop': ['']}
```

- Supports user-provided placeholders, making detection flexible for messy datasets.


#### 2. Data Loading Enhancements

- DataLoader now supports **.txt** files.

```python
from datalabx import DataLoader

df = DataLoader('sample_txt_file.txt').load_tabular()
```
- Improved Excel loading with optional dependency support **(fastexcel)** which can be installed with:

```bash
pip install datalabx[excel]
```

- Fixed issues causing failures during data loading.

#### API & Internal Improvements

- Updated API return types for ``detect_missing_types()`` for consistency. (see [DataLab API Return Types Reference](DataLabX_API_RETURN_TYPES.md))
- Dependency updates for **scipy** and **pyarrow** for better compatibility with **Python 3.10+.**

#### Developer Experience
Improved feature request template with clearer examples for contributors and users. (see [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md))


### 🐛 Bug Fixes

- Fixed **SettingCopyWarning** in ``ColumnConverter().to_numerical_forced()``.
- Ensures safer transformations without unintended side effects.
- Fixed data loading bugs affecting certain file types.

### 💡 Key Notes

- This release continues strengthening **real-world missingness handling**, a core part of DataLabX.
- Focus is on **correctness, consistency, and usability**, not new high-level features.
- Prepares the foundation for upcoming **DuckDB integration and performance enhancements.**

---

## v0.1.0b11 - March 16, 2026

**Status**: Beta (fully installable on PyPI)

DataLabX **v0.1.0b11** is the **first version extensively developed and validated on real-world messy datasets**, acquired via **web scraping, REST APIs**, and **raw HTML/Excel sources**.
This release **emphasizes practical usability, robust diagnostics, and advanced cleaning workflows** for real-world tabular data.

### ⚠️ Important Updates

- DataLabX is now fully installable on PyPI: 

##### Installation

DataLabX can now be installed with this command:

```bash
pip install datalabx
```
Instead of:

```bash
pip install datalabx_pre_release
```

- Text cleaning now returns the **full DataFrame** for consistent downstream workflows.
- Added new cleaning methods for removing **bracketed/parenthesized content**.
- Added ``validate_missingness()`` for explicit missing data validation.
- DataLoader updated with **robust error handling** and case-insensitive file type support.

### 🚀 Major Changes

#### 1. Real-World Data Focus

- This is the first DataLabX release tested and improved using messy real-world datasets.

- Data was collected via web scraping **(Requests, BeautifulSoup, Playwright)** and **REST APIs**, capturing messy, unstructured tabular data and diverse missingness patterns.

- All improvements to **cleaning, missingness validation, and DataLoader** behavior were informed by these real-world examples.

#### 2. Advanced Cleaning Utilities

- ``remove_square_brackets_and_content()``: Removes square brackets and content inside "[content]" from columns.
    - Example:
        DataLabX [Pre-Release] -> DataLabX 

- ``remove_parantheses_and_content()``: Removes (content) from columns.
    - Example:
        DataLabX (Pre-Release) -> DataLabX 

- Fixed **remove_multiple_spaces()** to prevent unintended space removal.

#### 3. Missingness Validation

- ``validate_missingness()`` allows checking existence of missing values across columns with custom placeholders.

- Added full docstrings for better documentation and usability.

#### 4. Data Loading Improvements

- Improved error handling for **invalid file types** and **array_type** parameter in DataLoader.

- Case-insensitive file type comparison for CSV and Excel files.

#### 5. API & Usability Refinements

- ``TextCleaner`` now returns the **full DataFrame** post-cleaning.

- ``data_preview()`` now shows both **head** and **tail** of datasets.

- ``show_memory_usage() ``renamed to ``memory_usage()`` with improved error handling.

#### 6. Documentation Updates

- Guides updated to reflect new DataLoader API, cleaning methods, and real-world workflow examples.

- Diagnosis modules updated in API Return Types Reference for consistency.

### 🐛 Bug Fixes

- Fixed multiple spaces removal issue in ``TextCleaner``.

- Fixed case sensitivity in file type comparison for ``DataLoader``.

- Corrected ``data_preview()`` behavior to show both head and tail.

### 💡 Key Notes for Users

- **First real-world validated release:** All cleaning and missingness methods tested with messy scraped and API-collected datasets.

- **New capabilities:** Users can clean bracketed/parenthesized content, validate missingness explicitly, and preview datasets comprehensively.

- **Breaking Changes:** Minimal; mostly bug fixes and new features.

- **Next Steps:** Future releases will add analysis modules, advanced visualization, and workflow automation for messy datasets.

---

## v0.1.0b10 - Feb 22, 2026

### DataLabX & First PyPI Release

**Status:** Beta
**Distribution:** PyPI (First Official Distribution)

>This is the first publicly installable version via PyPI.

This release marks the renaming of **DataLab** to **DataLabX** and introduces a **permanent architectural overhaul** that defines the long-term structure of the project.

It introduces:

  - A **fully class-based framework**
  - A **redesigned data loading engine**
  - **Standardized API naming**
  - **Logging expansion**
  - **Improved error handling**.

### 🔁 Project Rename

Renamed **DataLab** --> **DataLabX**.

- Establishes the long-term identity of the framework.

- All future development continues under the DataLabX name

### ⬇️ Installation

DataLabX can now be installed directly from PyPI:

```bash
pip install datalabx_pre_release
```

### 🚀 Major Changes

#### 1. Full Class-Based Framework

- Transitioned entire framework to **class-based design** (except utils).

- Standardized naming conventions across modules.

- Improved internal consistency and maintainability.

#### 2. DataLoader Redesign

- Renamed ``data_loader`` module **-->** ``DataLoader``.

- Converted from **single-function module** to **structured class**.

- DataLoader accepts:
    - **file path**
    - optional **file type** ``(automatically detected)``
    - optional **array type**
    - optional **conversion threshold** ``(NumPy <--> Pyarrow)``.

###### Example:

```python
from datalabx import DataLoader

df = DataLoader('example.csv').load_tabular()
df = DataLoader('example.excel', array_type = 'numpy', conversion_threshold = 500000).load_tabular()
```

#### ⚙️ Polars-Based Internal Engine

- All files - CSV, Excel, JSON and Parquet, are now internally loaded using **Polars**.

- DataFrames are converted to Pandas for the **user-facing API**.

- Ensures performance internally while preserving Pandas compatibility.

### 💡 Improved

- Improved **error handling** for CSV and Excel loading.

- More informative exceptions for:

    - Invalid file paths

    - Unsupported file types

    - Loading failures

- General internal refactoring for **stability** and **readability**.

- Codebase cleaned up during loader refactor.
 
### 🔄 Renamed

- Project renamed from ``DataLab`` --> ``DataLabX``

- ``load_as_string`` parameter in ``DataLoader`` class renamed to ``load_csv_as_string``

###### Example:

```python
DataLoader('example.csv').load_tabular(load_csv_as_string = True)
```

### 🐛 Fixed

- Fixed bugs in ``show_duplicates()`` method of ``Diagnosis`` class.


### ⚠️ Breaking Changes

- ``load_tabular()`` function removed. 

**❌ This no longer works** 

```python
from datalab import load_tabular

df = load_tabular('example.csv')
```

**✅ Use ``DataLoader`` class instead.**

```python
from datalabx import DataLoader

df = DataLoader('example.csv').load_tabular()
```

### 📦 Distribution Milestone

- First PyPI release.

- First release under the **DataLabX** name.

- Intended for installation validation and early feedback.

This release establishes the architectural foundation for a future stable v0.1.0.

---

##  v0.1.0b9 - Feb 17, 2026

**Status:** Beta (pre-release - TestPyPI only)

DataLab **v0.1.0b9** introduces **optional string-only data loading** and a **refined missing data handler API**, providing more flexibility and consistency for users.

#### ⚠️ Important Updates

- CSV files are **no longer forced to load all columns as strings**; loading as strings is now **completely optional**.

- ``MissingHandler`` class renamed to ``MissingnessHandler`` for consistency with other Missingness modules.

### 🚀 Major Changes

**1.** **Optional String Loading**

- In previous versions **(starting v0.1.0b4)**, all data was loaded as strings by default in ``CSV`` files.

- In **v0.1.0b9**, the ``load_as_string`` parameter allows users to:

    - Keep the default type inference behavior, or 

    - Explicitly load all columns as strings when needed.

**Example:**

```python
from datalab import load_tabular

df = load_tabular('example.csv')  # keeps original datatypes
df = load_tabular('example.csv', load_as_string = True)   # loads all data with string datatype
```

- CSV loading tests for forced string conversion **have been removed**, reflecting the new optional behavior.

- Enhances flexibility for workflows with mixed-type datasets, avoiding **unnecessary type coercion**.

**2. Missing Data Handler Refinement**

- Renamed ``MissingHandler`` **-->** ``MissingnessHandler`` **(module & class)** for consistency with other missingness-related modules.

- Added ``MissingnessHandler`` to ``__init__.py`` for direct imports:

```python
from datalabx import MissingnessHandler
```

### 💡 Key Notes for Users

- 🔄 **Breaking Change:** Any existing code or imports using ``MissingHandler`` must be updated to ``MissingnessHandler``.

- ✅ Optional string loading gives **full control over column datatypes at load time**, replacing the previous forced behavior.

- This release focuses on **flexibility, clarity**, and **API consistency**.

---

##  v0.1.0b8 - Feb 17, 2026

**Status:** Beta (pre-release - TestPyPI only)

DataLab **v0.1.0b8** enhances **missing data handling**, finalizes the **visualization API refactor**, and continues to **improve documentation**, **type hints**, and **stability**.

#### ⚠️ Important Updates

- Data loading module ``loader``renamed to ``data_loader`` for clarity.

- Visualization methods now consistently return ``(Figure, Axes)`` tuples, instead of ``None``.

- ``MissingHandler`` methods fully support extra placeholder values.

- **Python 3.10+** is now the minimum supported version.

- Removed ``get_element_from_split_text()`` from ``TextCleaner`` **(previously added in b7)**.

### 🚀 Major Changes

1. **Visualization API Refactor (Behavior Change)** 
    - Instead of returning ``None``, all Visualization methods (Missingness, Numerical and Categorical) now return:

        ```python
        (matplotlib.figure.Figure, matplotlib.axes.Axes)
        ```
    - ``plot_box()`` now supports both **vertical and horizontal orientations**.

    - ``plot_missing()`` behavior updated for improved flexibility.

    - **API Return Types Reference** updated to reflect these changes. (see [DataLab API Return Types Reference](DataLabX_API_RETURN_TYPES.md))

    - Visualization return-type tests rewritten to match the new tuple outputs.

2. **Missing Data Handling Improvements**
    - ``MissingHandler`` class updated so **all methods accept extra placeholder values**.
    - All missing handling methods refactored for **better consistency and logging.**
    - Logging added for extra placeholders in ``MissingnessDiagnosis``.
    - Enhanced error handling for the how parameter in ``drop_missing_columns()`` and ``drop_missing_rows()`` methods

3. **Python Compatibility**

    - Minimum supported Python version updated to **3.10+**``(previously >=3.12)``.
    - **README** and **pyproject.toml** updated accordingly.

### ✨ Added

- **DataLab Data Handling Policy** explaining how DataLab perceives and manages data mutations (see [DataLab Data Handling Policy](DataLabX_DATA_HANDLING_POLICY.md)).

- **DataLab Data Handling Report** explaining how DataLab currently handles data in modules and functions (see [DataLab Data Handling Report](DataLabX_DATA_HANDLING_REPORT.md)).

- Type hints and logger added/refined across diagnosis and visualization classes.


### 💡 Improved

- Refactored ``Diagnosis`` classes for formatting, type hints, and consistency.

- ``Diagnosis.detect_column_types()`` fixed to detect **PyArrow string types** correctly.

- Directory formatting improved with underscores for consistency.

- **Documentation** and **example images** restructured for clarity and usability.

### 🐛 Fixed

- Bug in ``detect_outliers()`` resolved.

- Removed unnecessary logging from ``CategoricalDiagnosis``.

- Minor fixes in visualization methods, outlier detection, and missing data handling.

### ⚠️ Removed

- ``get_element_from_split_text()`` method in ``TextCleaner`` **(introduced in v0.1.0b7)** removed temporarily for stability.

### 🔄 Renamed

- ``loader`` module renamed to ``data_loader`` for clarity and consistency during imports, to ensure users can still do:

    ```python
    from datalab import load_tabular
    ```

### 💡 Key Notes for Users

- **Breaking Change:** Visualization methods now return **(Figure, Axes)**. 
    
    Update your code accordingly:

    ```python
    fig, ax = NumericalVisualizer.plot_histogram(...)
    ```

- **MissingHandler improvements:** Extra placeholders are now fully supported.

- **Python 3.10+** is now required; earlier versions are not supported.

- **get_element_from_split_text()** removed temporarily; adjust any dependent code.

- ``loader`` module renamed to ``data_loader``, update any import statements.

This release stabilizes visualization, diagnosis, and missing data workflows ahead of the first official stable release **(v0.1.0)**.

---


##  v0.1.0b7 - Feb 08, 2026

**Status:** Beta (pre-release - TestPyPI only)

DataLab **v0.1.0b7** focuses on **critical bug fixes, improved documentation, contributions workflow, and stability**.

#### ⚠️ Major fix:

This release **resolves a blocking import issue** that prevented DataLab from running in environments without ipykernel, making the library usable in both **Jupyter Notebooks** and **Non-Jupyter** setups.

### 🚀 Major Changes

- **Fixed critical Import bug affecting Non-Jupyter Notebook environments (no ipykernel required).**

- Consolidated and polished foundations content, moving concepts to foundations markdown files.

- Added DataLab contribution guides and templates: 

  - ``CONTRIBUTING.md`` (see [Contributing to DataLabX](CONTRIBUTING.md))

  - GitHub issue template for ``Bug Reports`` (see [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md)) 
  
  - Github issue template for ``Feature Requests`` (see [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md))

- Added ``CODE_OF_CONDUCT.md`` (see [Code of Conduct](CODE_OF_CONDUCT.md))

- Maintainer review notes for contributions workflow.

- Added ``DataLab Foundations`` (see [DataLabX Foundations](foundations/foundations.md))

### ✨ Added

- ``get_element_from_split_text()`` method in ``TextCleaner``.

- **Exploring Dirty Numerical Data Guide** (see [Exploring Dirty Numerical Data Workflow Guide](guides/DataLab_Workflow_Guides/Dirty_Data_Diagnosis/Exploring_Dirty_Numerical_Data.ipynb))

- Return type tests for **visualizations, computations, and statistics**.

- Centralized example images and assets for missingness visualizations.

- **Code of Conduct** file.

- **CONTRIBUTING** file
 
- **bug report** and **feature requests** template


### 💡 Improved

- README updated for clarity, foundational concepts, and contributions workflow.

- Documentation restructured with improved formatting, paths, and image references.

- Refactored ``MissingnessDiagnosis`` and other classes for logging consistency and placeholder handling.

- Markdown fixes in notebooks and docstrings for better pdoc rendering.

- Separate ``API`` and ``Foundational`` docs.

- Removed ``concepts`` from ``docs`` and renamed to ``foundations``, which are the thinking layer of DataLab.

### 🐛 Fixed

- Fixed plotting bugs in ``NumericalVisualizer.plot_kde()`` and ``NumericalVisualizer.plot_box()`` methods.

- Corrected ``NumericalDiagnosis.detect_outliers()`` to keep only valid outliers.

- **Resolved import errors for environments without Jupyter (ipykernel).**

- Fixed minor formatting and path issues in documentation and example images.

### 💡 Key Notes for Users

- **Critical upgrade**: This release resolves the blocking bug in non-Jupyter environments.

- **Documentation & contributions**: Guides and templates now included for easier community contributions.

- **Stability:** Bug fixes and logging improvements increase confidence in core API behavior.

- **Pre-release reminder:** APIs remain mostly stable; feedback is welcome ahead of the first official stable release.

---

## v0.1.0b6 - Feb 01, 2026

**Status:** Beta (pre-release - TestPyPI only)

DataLab **v0.1.0b6** is a **stabilization and correctness release** that fixes issues introduced in v0.1.0b4, with a strong focus on **API reliability, type-safety, testing, and documentation clarity**.

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

- **Recommended upgrade:** v0.1.0b6 supersedes v0.1.0b4.

- **API clarity:** Users can now rely on a single, authoritative return-type reference.

- **Stability:** Improved testing and bug fixes increase confidence in API behavior.

- **Pre-release reminder:** APIs are nearing stability ahead of ``v0.1.0.``

---

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

## v0.1.0a4 - Dec 26, 2025 
**Status:** Alpha (pre-release - TestPyPI only)  

**v0.1.0a4** focused on **missing data visualization, initial diagnosis workflows, and documentation improvements**.  

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
