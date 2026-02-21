def test_datetime_column_conversion():
    import datalabx
    from datalabx import ColumnConverter
    import pandas as pd

    test_df = pd.DataFrame({
        "age": [70, 21, 60, 28, 22, 49, 78, 63, 64, 61],
        "gender": ["M", "M", "M", "F", "M", "M", "F", "F", "F", "M"],
        "account_created_at": [
            "2018-07-08 00:00:00",
            "2018-06-17 00:00:00",
            "2021-07-06 00:00:00",
            "2022-08-18 00:00:00",
            "2023-07-27 00:00:00",
            "2020-05-22 00:00:00",
            "UNKNOWN_DATE",
            "2015-05-23 00:00:00",
            "2023-06-19 00:00:00",
            "2021-03-30 00:00:00",
        ],
        "event_time": [
            "2020-08-16 08:33:00",
            None,
            "2020-08-23 00:24:00",
            "2021-09-05 00:05:00",
            "2019-09-04 18:20:00",
            "2018-07-24 19:31:00",
            None,
            "2018-12-13 03:59:00",
            "2024-04-21 07:33:00",
            "2018-12-01 00:41:00",
        ],
    })

    test_df = ColumnConverter(test_df, ['account_created_at', 'event_time']).to_datetime()

    assert isinstance (test_df['account_created_at'][0], str)
    assert isinstance (test_df['account_created_at'][1], str)
    assert isinstance (test_df['event_time'][0], str)

    assert test_df['account_created_at'][6] == 'UNKNOWN_DATE'

    assert pd.isna(test_df['event_time'][1])

    test_df_forced = ColumnConverter(test_df,['account_created_at', 'event_time']).to_datetime_forced()

    assert isinstance (test_df_forced['account_created_at'][0], pd.Timestamp)
    assert isinstance (test_df_forced['account_created_at'][1], pd.Timestamp)
    assert isinstance (test_df_forced['event_time'][0], pd.Timestamp)

    assert pd.isna(test_df_forced['account_created_at'][6])

    assert pd.isna(test_df_forced['event_time'][1])

