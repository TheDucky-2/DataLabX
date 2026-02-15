"""TESTING DATA VISUALIZATION PACKAGE RETURN TYPES."""

"""A test ensuring that NumericalVisualizer module returns None."""

import matplotlib

def test_numerical_visualizer_return_types():

    import pandas as pd
    from datalab import NumericalVisualizer, ColumnConverter

    df = pd.DataFrame({
        "age": [23, 25, 29, 31, 35, 38, 42, 45, 47, 50, 120, 3],  
        "monthly_income": [
            2800, 3000, 3200, 3500, 3800, 4000,
            4200, 4500, 4800, 5200, 50000, 100    
        ],
        "account_balance": [
            1500, 2000, 1800, 2200, 2500, 2700,
            3000, 3200, 3500, 3800, 250000, -900   
        ],
        "num_transactions": [
            5, 7, 9, 12, 14, 16, 18, 20, 22, 25, 300, 0   
        ]
    })

    df = ColumnConverter(df).to_numerical_forced()
    
    viz = NumericalVisualizer(df)

    histogram = viz.plot_histogram()
    kde = viz.plot_kde()
    qq = viz.plot_qq()
    box = viz.plot_box()

    # ensuring that the output of the method is a tuple
    assert isinstance(histogram, tuple)
    assert isinstance(kde, tuple)
    assert isinstance(qq, tuple)
    assert isinstance(box, tuple)
    
    # the first element in the tuple must be a matplotlib figure object
    assert isinstance(histogram[0], matplotlib.figure.Figure)
    assert isinstance(kde[0], matplotlib.figure.Figure)
    assert isinstance(qq[0], matplotlib.figure.Figure)
    assert isinstance(box[0], matplotlib.figure.Figure)

    # the second element in the tuple must be a matplotlib axes object
    assert isinstance(histogram[1], matplotlib.axes.Axes)
    assert isinstance(kde[1], matplotlib.axes.Axes)
    assert isinstance(qq[1], matplotlib.axes.Axes)
    assert isinstance(box[1], matplotlib.axes.Axes)


"""A test ensuring that Missingness Visualizer module returns None."""

    # the second element in the tuple must be a matplotlib axes o
def test_missingness_visualizer_return_types():
    import pandas as pd
    from datalab import MissingnessVisualizer, ColumnConverter

    df = pd.DataFrame({
        "age": [
            56.0, 69.0, pd.NA, 46.0, 60.0, pd.NA,
            34.0, 41.0, pd.NA, 52.0, 28.0, pd.NA
        ],
        "income": [
            73892.87, pd.NA, 47897.33, 49346.65, 167409.01, pd.NA,
            32000.00, 45000.00, pd.NA, 51000.00, 28000.00, pd.NA
        ],
        "expenses": [
            55599.65, 30006.45, 25023.24, pd.NA, 124105.98, pd.NA,
            21000.00, 32000.00, 18000.00, pd.NA, 15000.00, pd.NA
        ],
        "savings": [
            17417.10, 28868.98, pd.NA, pd.NA, 44924.78, pd.NA,
            2000.00, 5000.00, pd.NA, 8000.00, pd.NA, pd.NA
        ],
        "loan_amount": [
            18809.37, 14792.73, 13678.63, 5425.38, pd.NA, pd.NA,
            8000.00, 12000.00, 3000.00, pd.NA, 5000.00, pd.NA
        ],
        "credit_score": [
            727.91, 740.04, 703.44, 623.24, 698.57, pd.NA,
            650.00, 670.00, pd.NA, 710.00, pd.NA, pd.NA
        ],
        "num_of_dependents": [
            0.0, 3.0, 2.0, 5.0, 0.0, pd.NA,
            1.0, 2.0, pd.NA, 0.0, 1.0, pd.NA
        ],
        "years_at_job": [
            22.0, 0.0, 13.0, 4.0, 0.0, pd.NA,
            2.0, 6.0, pd.NA, 10.0, 1.0, pd.NA
        ],
        "risk_score": [
            0.13, 0.12, 0.24, 0.15, 0.00, pd.NA,
            0.30, 0.18, pd.NA, 0.10, pd.NA, pd.NA
        ]
    })

    df = ColumnConverter(df).to_numerical_forced()

    missingness_viz = MissingnessVisualizer(df).plot_missing()

    assert isinstance(missingness_viz, tuple)

    # the first element in the tuple must be a matplotlib figure object
    assert isinstance(missingness_viz[0], matplotlib.figure.Figure)

    # the second element in the tuple must be a matplotlib axes object
    assert isinstance(missingness_viz[1], matplotlib.axes.Axes)

"""A test ensuring that Categorical Visualizer module returns None."""

def test_categorical_visualizer_return_types():
    import pandas as pd
    from datalab import CategoricalVisualizer, ColumnConverter

    df = pd.DataFrame({
    "gender": [
        "Male", "Female", "Female", "Male", None, "Female",
        "Male", "Other", None, "Female", "Male", None
    ],
    "marital_status": [
        "Single", "Married", "Married", "Divorced", None, "Single",
        "Single", "Married", None, "Widowed", "Single", None
    ],
    "education_level": [
        "Bachelor", "Master", "Bachelor", None, "PhD", None,
        "High School", "Bachelor", None, "Master", "High School", None
    ],
    "employment_type": [
        "Salaried", "Salaried", "Self-Employed", "Salaried", None, None,
        "Contract", "Salaried", None, "Self-Employed", "Contract", None
    ],
    "city": [
        "New York", "San Francisco", "New York", None, "Chicago", None,
        "Austin", "New York", None, "San Francisco", "Austin", None
    ]
    })

    categorical_viz = CategoricalVisualizer(df).plot_frequency()

    # ensuring that the output of the method is a tuple
    assert isinstance(categorical_viz, tuple)

    # the first element in the tuple must be a matplotlib figure object
    assert isinstance(categorical_viz[0], matplotlib.figure.Figure)

    # the second element in the tuple must be a matplotlib axes object
    assert isinstance(categorical_viz[1], matplotlib.axes.Axes)






