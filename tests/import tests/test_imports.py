## Basic tests to check whether datalab modules are importing.
def testing_datalab_imports():

    modules = ['datalab',
               'datalab.tabular.data_loader',
               'datalab.tabular.data_diagnosis',
               'datalab.tabular.data_cleaner',
               'datalab.tabular.data_preprocessor',
               'datalab.tabular.data_visualization',
               'datalab.tabular.data_analysis',
               'datalab.tabular.computations',
               'datalab.tabular.utils'] 
    
    for module in modules:
        try:
            __import__(module)

        except ModuleNotFoundError as error:
            print(f'Module not found {module}: {error}')
            raise error

    print("Imported datalab modules successfully!")

