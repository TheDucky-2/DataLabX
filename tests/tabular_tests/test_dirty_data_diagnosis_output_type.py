def test_dirty_data_diagnosis_output_type():
    
    import pandas as pd
    from datalabx import DirtyDataDiagnosis

    df = pd.DataFrame(
        {'Age': ['five', '20.673408544550288', '33.56', 'missing'],
        'Salary': ['1.04e+05', '134460.66741276794', 'missing', None],
        'Expenses': ['4735.244618878169',
        '  9533.158420128186  ',
        '4104.95 ',
        '894429'],
        'Height_cm': ['1,55e+02', '1,53e+02', '204', '196.34 cm'],
        'Weight_kg': [None, '12193', '96.50051410846052', '?'],
        'Temperature_C': ['unknown', '2.05e+01', '-1,14e+01', '-1.57e+01'],
        'Purchase_Amount': [None, '2.40e+03', '2877.0871437672777', None],
        'Score': ['30.70', 'one', 'four', '?'],
        'Rating': ['4.888018131992931', '3,33e+00', 'unknown', '4.31'],
        'Debt': ['64,972', '$58,276.81', '  94033.3425007563  ', '27,400cm']}
    )

    diagnosis = DirtyDataDiagnosis(df).diagnose_numbers()

    assert isinstance(diagnosis, dict)
    assert isinstance(diagnosis['Age']['is_dirty'], pd.DataFrame)
