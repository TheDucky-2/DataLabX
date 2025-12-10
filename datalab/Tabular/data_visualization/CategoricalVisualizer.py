from .DataVisualizer import DataVisualizer
from ..data_diagnosis import CategoricalDiagnosis
import pandas as pd
import matplotlib.pyplot as plt

class CategoricalVisualizer(DataVisualizer):

    def __init__(self, df: pd.DataFrame, columns: list|type(None) = None):
        super().__init__(df, columns)

        self.df.select_dtypes(include = 'number')
        
        if columns is None:
            self.columns = df.columns

        else: 
            self.columns = [column for column in df.columns if column in self.df.columns]

    def visualize_frequency(self,
                            method:str ='count',
                            viz_type: str = 'bar',
                            title: str=None,
                            xlabel: str=None,
                            ylabel: str=None,
                            figsize: tuple =(6, 4)):
        '''
        Visualize frequency for each column of Categorical DataFrame

            Parameters:
            -----------

            Optional:

                method : str (default is 'count')

                    Available methods:

                    - 'count': Visualizes the count of unique values in each category (default)
                    - 'percent': Visualizes the percentage of values in each category
                
                viz_type : str (default is 'bar')

                    Available viz_type:

                    - 'bar'	    Vertical bar chart (default)
                    - 'line'	Line plot 
                    - 'barh'	Horizontal bar chart
                    - 'hist'	Histogram
                    - 'box'	    Boxplot
                    - 'kde'	    Kernel density estimate
                    - 'area'	Area plot
                    - 'pie"	    Pie chart

                xlabel : str or type(None)
                    Label for x-axis.

                ylabel : str 
                    Label for y-axis.

                title : str 
                    Title of the plot. Adds column name by default.

                figsize : tuple (default is (6, 4))
                    Size of the figure (width, height) in inches.

            Returns:
            --------
                None
                    This function is intended for visualization only. 
                    It only displays the plot and does not return anything.

            Usage Recommendations:
            ----------------------
                Use this method of visualization only for categorical data.

            Considerations:
            ---------------
                Do not use this function as default or using viz_type as 'bar' if there are many unique categories.
                
                Use viz_type as 'hist' if you have many-many unique categories, otherwise you'll have to wait for a long-long time. 
        
        '''
        for column in self.df[self.columns]:

            (CategoricalDiagnosis(self.df).show_frequency(method=method)[column]).plot(kind=viz_type)

            if title:
                plt.title(f'{title}: {column}')
            else:
                plt.title(f'{viz_type} of {column}')

            if xlabel:
                plt.xlabel(xlabel)
            else:
                plt.xlabel(column)

            if ylabel:
                plt.ylabel(ylabel)
            else:
                plt.ylabel(f'{method} of {column}')

            plt.show()