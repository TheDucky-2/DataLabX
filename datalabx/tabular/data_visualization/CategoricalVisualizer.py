"""Class and methods for visualizing Categorical data."""

from ..data_diagnosis import CategoricalDiagnosis
from ..utils.Logger import datalabx_logger

import pandas as pd

import matplotlib.figure as Figure
import matplotlib.axes as Axes

logger = datalabx_logger(name = __name__.split('.')[-1])

class CategoricalVisualizer():
    """
    Initializing Categorical Visualizer.
    
    Parameters
    -----------
    df : pd.DataFrame
        A pandas DataFrame.

    columns : list, optional
        List of columns you wish to visualize, by default None.
    """

    def __init__(self, df: pd.DataFrame, columns: list|None = None):
    
        self.df = df.select_dtypes(include = ['string', 'object', 'category'])

        if columns is None:
            self.columns = self.df.columns.tolist()
        else: 
            self.columns = [column for column in columns if column in self.df.columns]

    def plot_frequency(self,
                            method:str ='count',
                            viz_type: str = 'bar',
                            title: str | None =None,
                            xlabel: str | None =None,
                            ylabel: str | None =None,
                            figsize: tuple| None =(6, 4))-> tuple[Figure, Axes]:
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

        xlabel : str or None, optional
            Label for x-axis, default is None.

        ylabel : str or None, optional
            Label for y-axis, default is None.

        title : str or None, optional
            Title of the plot, default is None.

        figsize : tuple or None, optional
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
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=figsize)

        for column in self.df[self.columns]:

            (CategoricalDiagnosis(self.df).show_frequency(method=method)[column]).plot(kind=viz_type)

            if title:
                ax.set_title(f'{title}: {column}')
            else:
                ax.set_title(f'{viz_type} of {column}')

            if xlabel:
                ax.set_xlabel(xlabel)
            else:
                ax.set_xlabel(column)

            if ylabel:
                ax.set_ylabel(ylabel)
            else:
                ax.set_ylabel(f'{method} of {column}')
                
            return fig, ax