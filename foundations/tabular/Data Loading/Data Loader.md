# 📥 Tabular Data Loader

## Welcome to the first step of DataLab!

Tabular data means data arranged in rows and columns of a table like this:


| age | income      | expenses       | debt           | score | savings_ratio |
|-----|-------------|----------------|----------------|-------|---------------|
| 45  | NaN         | 21337.207586   | 2,077,881.000  | 49    | 0.431159      |
| 38  | 17182.443452| 3621.209282    | 3,752.960      | 60    | 0.789249      |
| NaN | 23497.048535| 16516.059771   | NaN            | NaN   | 0.297101      |

**Examples:**

- Excel Spreadsheets
- Pandas DataFrames
- csv files, etc.

> DataLab works mainly with pandas DataFrames.

### Supported Tabular Data File Types

DataLab can automatically detect and load:

- CSV
- Excel (.xlsx, .xls)
- JSON
- Parquet

We don’t need to specify the file type - DataLab figures it out for us.

### DataLab Usage:

We can load tabular data using the ``load_tabular()`` function from ``DataLoader`` class of ``datalab``.

This function returns a **pandas DataFrame**.

```python
from datalab import DataLoader

df = DataLoader('example.csv').load_tabular()
```

### Data Loading Examples

#### --- Without Any Extra Parameters ---

```python
from DataLab import DataLoader

# Loading a CSV file
df = DataLoader('some_random_file.csv').load_tabular()

# Loading an Excel file 
df = DataLoader('some_random_file.excel').load_tabular()

# Loading a Parquet file
df = DataLoader('some_random_file.parquet').load_tabular()

# Loading a JSON object 
df = DataLoader('some_random_file.json').load_tabular()
```

#### --- Using Extra Parameters ---

```python
df = DataLoader('some_random_file.csv').load_tabular(load_csv_as_string = True)

df = DataLoader('some_random_file.csv').load_tabular(array_type='numpy')

df = DataLoader('some_random_file.csv').load_tabular(conversion_threshold=3000000)

df = DataLoader('some_random_file.excel').load_tabular(array_type='pyarrow', conversion_threshold=1000000)
```

---









