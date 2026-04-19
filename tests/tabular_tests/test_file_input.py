def test_file_input():

    from datalabx import DataLoader
    import tempfile
    from pathlib import Path
    import pytest

    with tempfile.TemporaryDirectory() as tempdir:
        path = Path(tempdir)

        ## ===FILES with Bad Data ====#

        csv_path = path / "a.csv"
        csv_path.write_text("id,value,flag\n"
            "1,100,True\n"
            "2,,False\n"
            "3,abc,True\n"
            "4,400\n"
            ",500,False\n")

        json_path=path / "b.json"
        
        json_path.write_text("""[{
        "id": 1,
        "name": "Alice",
        "value": 100,
        "active": true
    },
    {
        "id": 2,
        "name": "Bob",
        "value": "200",
        "active": "yes"
    },
    {
        "id": 3,
        "name": null,
        "value": null
    },
    {
        "id": 4,
        "name": "Charlie",
        "value": -1,
        "extra": "unexpected_field"}]""")

        txt_path=path / "b.txt"
        txt_path.write_text(
            "ok line\n"
            "\n"
            "ERROR: missing value\n"
            "12345 random noise ### $$$\n")

        
        csv_df = DataLoader(str(csv_path)).load_tabular()
        txt_df = DataLoader(str(txt_path)).load_tabular()
        json_df = DataLoader(str(json_path)).load_tabular()

        assert csv_df is not None
        assert txt_df is not None
        assert json_df is not None

test_file_input()
        