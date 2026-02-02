"""A test ensuring that Statistics module returns a pandas Series"""

def test_statistics_output_type():

    import pandas as pd
    from datalab import Statistics, ColumnConverter

    df = pd.DataFrame(
        {'age': [56.0, 69.0, 46.0, pd.NA, 60.0],
        'income': [73892.87, 62617.96, 47897.33, 49346.65, 167409.01],
        'expenses': [55599.65, 30006.45, 25023.24, 22799.82, 124105.98],
        'savings': [17417.1, 28868.98, 24674.45, pd.NA, 44924.78],
        'loan_amount': [18809.37, 14792.73, 13678.63, 5425.38, 30292.05],
        'credit_score': [727.91, 740.04, 703.44, 623.24, 698.57],
        'num_of_dependents': [0.0, 3.0, 2.0, 5.0, 0.0],
        'years_at_job': [22.0, 0.0, 13.0, 4.0, 0.0],
        'risk_score': [0.13, 0.12, 0.24, 0.15, 0.0]}
    )   

    df = ColumnConverter(df).to_numerical_forced()
    
    stats = Statistics(df)

    assert isinstance(stats.iqr(), pd.Series)
    assert isinstance(stats.max(), pd.Series)
    assert isinstance(stats.min(), pd.Series)
    assert isinstance(stats.mean(), pd.Series)
    assert isinstance(stats.median(), pd.Series)
    assert isinstance(stats.standard_deviation(), pd.Series)
    assert isinstance(stats.median_absolute_deviation(), pd.Series)
    assert isinstance(stats.scaled_median_absolute_deviation(), pd.Series)
    assert isinstance(stats.quantiles(0.25), pd.Series)
    assert isinstance(stats.range(), pd.Series)
    assert isinstance(stats.variance(), pd.Series)



    