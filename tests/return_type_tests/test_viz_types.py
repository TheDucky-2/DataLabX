import pytest

def test_viz_types():
    from datalabx import MissingnessVisualizer, CategoricalVisualizer, NumericalVisualizer 
    from datalabx import DataLoader

    import tempfile 
    from datetime import datetime
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")

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
    "Remote": [True, False, True, False, True, False]}

    df = pd.DataFrame(data)

    for col in df.columns:
        df[col] = df[col].astype(str)

    with tempfile.NamedTemporaryFile(mode='w+', suffix='.csv', delete=False) as temp_csv:
        df.to_csv(temp_csv.name, index=False)
        csv_file = temp_csv.name

        csv_df = DataLoader(csv_file).load_tabular()

        assert isinstance(MissingnessVisualizer(csv_df).plot_missing(),tuple)

        assert isinstance(NumericalVisualizer(csv_df).plot_histogram(),tuple)
        assert isinstance(NumericalVisualizer(csv_df).plot_box(),tuple)
        assert isinstance(NumericalVisualizer(csv_df).plot_kde(),tuple)
        assert isinstance(NumericalVisualizer(csv_df).plot_qq(),tuple)

        assert isinstance(CategoricalVisualizer(csv_df).plot_frequency(),tuple)

test_viz_types()