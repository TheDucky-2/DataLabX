##  v0.1.0b9 - Feb 17, 2026

**Status:** Beta (pre-release - TestPyPI only)

datalabx **v0.1.0b9** introduces **optional string-only data loading** and a **refined missing data handler API**, providing more flexibility and consistency for users.

#### ⚠️ Important Updates

- CSV files are **no longer forced to load all columns as strings**; loading as strings is now **completely optional**.

- ``MissingHandler`` class renamed to ``MissingnessHandler`` for consistency with other Missingness modules.

### 🚀 Major Changes

**1.** **Optional String Loading**

- In previous versions **(from v0.1.0b4)**, all data was loaded as strings by default.

- In **v0.1.0b9**, the ``load_as_string`` parameter allows users to:

    - Keep the default type inference behavior, or 

    - Explicitly load all columns as strings when needed.

**Example:**

```python
from datalabx import load_tabular

df = load_tabular('example.csv', load_as_string = False)  # keeps original datatypes
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



B10

renamed ``data_loader`` module to ``DataLoader``.

renamed ``load_as_string`` param to ``load_csv_as_string`` to remove ambiguity

improved error handling during csv and excel files

REFACTORED code and converted ``data_loader`` from single function module to ``DataLoader`` class

``DataLoader`` accepts file path and file type, optional as parameters

``DataLoader('example.csv').load_tabular()``

Excel files are also loaded as polars dataframes and converted to pandas 

datalabx now fully loads polars based dataframes and convertd to pandas for user facing api

datalabx is now fully class based...except for utils

It will be released on pypi for feedback


``
