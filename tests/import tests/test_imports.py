## Basic tests to check whether datalabx modules are importing.
def test_datalabx_imports():
    import pytest

    modules = ['datalabx',
               'datalabx.tabular.data_loader',
               'datalabx.tabular.data_diagnosis',
               'datalabx.tabular.data_cleaner',
               'datalabx.tabular.data_preprocessor',
               'datalabx.tabular.data_visualization',
               'datalabx.tabular.computations',
               'datalabx.tabular.utils']

    modules_not_found = []
    
    for module in modules:
        try:
            __import__(module)

        except ModuleNotFoundError as error:
            modules_not_found.append(module)

    if modules_not_found:
        pytest.fail(f'The following modules could not be imported: {", ".join(modules_not_found)}')

