# Tabular Data Loader:
-------------------

## Welcome to the first step of DataLab!

Tabular data means data arranged in rows and columns, like a table.

Examples:

- Excel Spreadsheets
- Pandas DataFrame
- csv files

DataLab works mainly with pandas DataFrames, so almost all functions in this library will return a pandas DataFrame.

### Tabular Data File Types Supported:

DataLab can automatically detect and load:

- CSV
- Excel (.xlsx, .xls)
- JSON
- Parquet

You don’t need to specify the file type — DataLab figures it out for you.

### DataLab Usage:

You can load tabular data using the load_tabular() function from the data loader package of this library.

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








