def test_data_loader():
    
    import tempfile
    from datetime import datetime
    import pandas as pd

    from datalabx import DataLoader

    data = {
        "ID": [101, '102A', 103, 104, 105, 'Unknown'],
        "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan", None],
        "Age": [25, 30, 35, '28','     40'  , ''],
        "Salary": [50000.0, 60000.5, 75000.0, 62000.0, 80000.75333333, '40000.34'],
        "Department": ["HR", "Engineering$$", "Marketing", "Finance", "Engineering", "Finance"],
        "StartDate": [
            datetime(2020, 5, 1),
            datetime(2019, 8, 15),
            datetime(2021, 3, 20),
            datetime(2018, 11, 30),
            datetime(2022, 1, 10),
            datetime(2025, 1, 10)
        ],
        "Remote": [True, False, True, False, True, False]
    }

    df = pd.DataFrame(data)

    for col in df.columns:
        df[col] = df[col].astype(str)

    with tempfile.NamedTemporaryFile(mode='w+', suffix='.csv', delete=False) as temp_csv:
        df.to_csv(temp_csv.name, index=False)
        csv_file = temp_csv.name

    with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as temp_excel:
        df.to_excel(temp_excel.name, index=False)
        excel_file = temp_excel.name

    with tempfile.NamedTemporaryFile(suffix = '.parquet', delete=False) as temp_parquet:
        df.to_parquet(temp_parquet.name, index=False)
        parquet_file = temp_parquet.name

    with tempfile.NamedTemporaryFile(suffix = '.json', delete=False) as temp_json:
        df.to_json(temp_json.name, index=False)
        json_file = temp_json.name

    csv_df = DataLoader(csv_file).load_tabular()
    excel_df = DataLoader(excel_file).load_tabular()
    parquet_df = DataLoader(parquet_file).load_tabular()
    json_df = DataLoader(json_file).load_tabular()

    assert isinstance(csv_df, pd.DataFrame)
    assert isinstance(excel_df, pd.DataFrame)
    assert isinstance(parquet_df, pd.DataFrame)
    assert isinstance(json_df, pd.DataFrame)

test_data_loader()