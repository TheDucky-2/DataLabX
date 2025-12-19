# Tabular Data Loader:
-------------------

## Welcome to the first step of DataLab!

Tabular data means data arranged in rows and columns of a table like this:


| age | income      | expenses       | debt           | score | savings_ratio |
|-----|-------------|----------------|----------------|-------|---------------|
| 45  | NaN         | 21337.207586   | 2,077,881.000  | 49    | 0.431159      |
| 38  | 17182.443452| 3621.209282    | 3,752.960      | 60    | 0.789249      |
| NaN | 23497.048535| 16516.059771   | NaN            | NaN   | 0.297101      |

Examples:

- Excel Spreadsheets
- Pandas DataFrame
- csv files, etc.

DataLab works mainly with pandas DataFrames, so almost all functions in datalab will return a pandas DataFrame.

### Tabular Data File Types Supported:

DataLab can automatically detect and load:

- CSV
- Excel (.xlsx, .xls)
- JSON
- Parquet

You don’t need to specify the file type — DataLab figures it out for you.

### DataLab Usage:

You can load tabular data using the load_tabular() function from the data loader package of datalab.

### **Examples:**

    from DataLab import load_tabular

    >>>   
        df = load_tabular('random_csv_file.csv')

    >>>   
        df = load_tabular_data('example.xlsx')

    >>>   
        df = load_tabular_data('some/path/to/my/csv/file.parquet')

    >>>   
        df = load_tabular_data('example.json')


**OR you can use an alias like:**

    import DataLab as dl

    >>>     
        df = dl.load_tabular('random_csv_file.csv')

    >>>   
        df = dl.load_tabular_data('example.xlsx')

    >>>   
        df = dl.load_tabular_data('some/path/to/my/csv/file.parquet')

    >>>   
        df = dl.load_tabular_data('example.json')








