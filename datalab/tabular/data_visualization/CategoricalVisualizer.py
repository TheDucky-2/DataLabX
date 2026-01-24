"""Class and methods for visualizing Categorical data."""

from ..data_diagnosis import CategoricalDiagnosis
import pandas as pd
import matplotlib.pyplot as plt

class CategoricalVisualizer():

    def __init__(self, df: pd.DataFrame, columns: list|type(None) = None):
        """Initializing Categorical Visualizer."""

        self.df.select_dtypes(include = ['string', 'object', 'category'])
        
        if columns is None:
            self.columns = df.columns

        else: 
            self.columns = [column for column in columns if column in self.df.columns]

    def visualize_frequency(self,
                            method:str ='count',
                            viz_type: str = 'bar',
                            title: str=None,
                            xlabel: str=None,
                            ylabel: str=None,
                            figsize: tuple =(6, 4)):
        """
        Visualize frequency for each column of Categorical DataFrame.

        Parameters
        -----------
        method : str, optional
            Whether you would like to visualize count or percentage of frequency, default is 'count'.

            Available methods:

            - 'count': Visualizes the count of unique values in each category (default).
            - 'percent': Visualizes the percentage of values in each category.

        viz_type : str, optional
            Type of visualization, default is 'bar'.

            Available viz types:

            - 'bar'   : Vertical bar chart (default)
            - 'line'  : Line plot
            - 'barh'  : Horizontal bar chart
            - 'hist'  : Histogram
            - 'box'   : Boxplot
            - 'kde'   : Kernel density estimate
            - 'area'  : Area plot
            - 'pie"   : Pie chart

        xlabel : str, optional
            Label for x-axis, default is None.

        ylabel : str, optional
            Label for y-axis, default is None.

        title : str, optional
            Title of the plot, default is None.

        figsize : tuple, optional
            Size of the figure (width, height) in inches, default is (6, 4)

        Returns
        --------
        None
                This function is intended for visualization only and does not return anything.

        Usage Recommendation
        ----------------------
            Use this method of visualization only for categorical data.

        Considerations
        ---------------
            1. Do not use the default settings, if there are many unique categories.

            2. Use viz_type as 'hist' if you have many-many unique categories, otherwise processing may be slower.
        """
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