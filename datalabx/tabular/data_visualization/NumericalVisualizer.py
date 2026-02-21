"""Class and methods for Numerical Plots (histogram, QQ plot, KDE and Box plot)."""

from ..computations import Distribution
import pandas as pd
from ..utils.Logger import datalabx_logger
import matplotlib.figure as Figure
import matplotlib.axes as Axes

logger = datalabx_logger(name=__name__.split('.')[-1])

# removing underscores in column names if they exist, for plot Titles.
def remove_underscores(column):
    """Remove underscores from column name. """
    
    column = " ".join(column.split('_'))

    return column

class NumericalVisualizer():

    def __init__(self, df: pd.DataFrame, columns: list|type(None) = None):
        """Initializing Numerical Visualizer.
        
        Parameters
        -----------
        df : pd.DataFrame
            A pandas DataFrame.

        columns : list, optional
            List of columns you wish to visualize, by default None.
        
        """
        # getting the elements of parent DataVisualizer class

        self.df = df.select_dtypes(include = 'number')
        
        if columns is None:
            self.columns = self.df.columns.tolist()
        else: 
            self.columns = [column for column in columns if column in self.df.columns]

        logger.info(f'Numerical Visualizer initialized.')
        
    def plot_histogram(self,
                  bins: int=30,
                  title: str=None,
                  xlabel: str=None,
                  ylabel: str=None,
                  figsize: tuple =(6, 4),
                  **kwargs)-> tuple[Figure, Axes]:
        """
        Visualize histogram for one or multiple columns of Numerical DataFrame.

        Parameters
        -----------
        bins : int , optional
            Number of bins you wish to visualize, default is 30.

        xlabel : str, optional
            Label for x-axis, default is None.

        ylabel : str, optional 
            Label for y-axis, default is None.

        title : str, optional
            Title of the plot, default is None.

        figsize : tuple, optional 
            Size of the figure (width, height) in inches, default is (6,4)

        **kwargs : dict
            Dictionary of keyword arguments passed to ``matplotlib.pyplot.hist``.

        Returns
        --------
        None        
            This function is intended for visualization only and does not return anything. 

        Usage Recommendation
        ----------------------
            Use this method of visualization only for numerical data.
        
        Example
        -------
        >>> NumericalVisualizer(df).plot_box()
        """ 
        import matplotlib.pyplot as plt

        for column in self.df[self.columns]:

            fig, ax = plt.subplots(figsize=figsize)

            ax.hist(self.df[column],bins=bins, edgecolor='black', **kwargs)

            if title:
                ax.set_title(f'{title}')
            else:
                ax.set_title(f'Histogram of {remove_underscores(column)}')

            if xlabel:
                ax.set_xlabel(xlabel)
            else:
                ax.set_xlabel(column)

            if ylabel:
                ax.set_ylabel(ylabel)
            else:
                ax.set_ylabel(f'Number of values')

            return fig, ax

    def plot_box(self, 
                orientation : str = 'vertical',
                xlabel:str|type(None) = None,
                ylabel:str|type(None) = None,
                title:str|type(None) = None,
                figsize:tuple = (6, 4),
                **kwargs)-> tuple[Figure, Axes]:

        """
        Visualize box plot for one or multiple columns of Numerical DataFrame.

        Parameters
        ----------
        orientation : str , optional
            Orientation of the boxplots, default is 'v'.

            Options are:

            - 'vertical' or 'v'
            - 'horizontal' or 'h'

        xlabel : str, optional
            Label for x-axis, default is None.

        ylabel : str
            Label for y-axis, default is None.

        title : str, optional
            Title of the plot, default is None.

        figsize : tuple, optional
            Size of the figure (width, height) in inches, default is (6, 4).

        **kwargs : dict
            Dictionary of keyword arguments passed to ``matplotlib.pyplot.boxplot``.

        Returns
        --------
        None
            This function is intended for visualization only and does not return anything.

        Usage Recommendation
        ----------------------
            Use this method of visualization only for numerical data.

        Example
        -------
        >>> NumericalVisualizer(df).plot_box()
        """
        import matplotlib.pyplot as plt

        if orientation not in ['horizontal', 'vertical']:
            raise ValueError(f"orientation must be 'horizontal' or 'vertical', got {orientation}")

        # making sure that the orientation starts with vertical or 'v' by default.
        # if it will be anything other than vertical, it will default to horizontal
        vert = (orientation.lower().startswith('v'))

        for column in self.df[self.columns]:

            fig, ax = plt.subplots(figsize=figsize) # defauls to figsize of (6, 4) inches. (6 X 4)
        
            # keeping it simple by 
            ax.boxplot(self.df[column], orientation=orientation, **kwargs)

            if title:
                ax.set_title(f'{title}: {column}')
            else:
                ax.set_title(f'Boxplot of {remove_underscores(column)}')

            if vert:
                ax.set_xticks([1])
                ax.set_xticklabels([column])

                if xlabel:
                    ax.set_xlabel(xlabel)

                if ylabel:
                    ax.set_ylabel(ylabel)

            else:
                ax.set_yticks([1])
                ax.set_yticklabels([column])

                if xlabel:
                    ax.set_xlabel(xlabel)
                
                if ylabel:
                    ax.set_ylabel(ylabel)

            return fig,ax

    def plot_kde(self, bandwidth_method: str ='robust',
                  title: str=None,
                  xlabel: str=None,
                  ylabel: str=None,
                  figsize: tuple =(6, 4),
                  **kwargs)-> tuple[Figure, Axes]:
        """
        Visualize Kernel Density Estimation plot (curves, including bell curve) for one or multiple columns of DataFrame.

        Parameters:
        -----------
        bandwidth_method: 'str' 
            The method you wish to use for computing KDE, default is 'robust'.

            Methods available:

            For Normal Distribution:

                - 'silverman'
                - 'scott'

            For Skewed Distribution:

                - 'robust' (uses robust scott)

        xlabel : str, optional
            Label for x-axis, default is None.

        ylabel : str
            Label for y-axis, default is None.

        title : str, optional
            Title of the plot, default is None.

        figsize : tuple, optional
            Size of the figure (width, height) in inches, default is (6, 4).

        **kwargs : dict
            Dictionary of keyword arguments passed to ``matplotlib.pyplot.plot``.

        Returns
        --------
        None
            This function is intended for visualization only and does not return anything.

        Usage Recommendation
        ----------------------
            Use this method of visualization only of numerical data.

        Considerations:
        ---------------
            This function uses ``compute_KDE()`` and ``compute_histogram()`` from Distribution class of the Computation Package

        Example
        -------
        >>> NumericalVisualizer(df).plot_kde()
        """
        import matplotlib.pyplot as plt

        # compute_KDE() returns a DataFrame
        kde_df= Distribution(self.df).compute_kde(bandwidth_method=bandwidth_method)

        for column in self.df[self.columns]:
            # using bin_centers from histogram computation as values for x-axis.
            x= Distribution(self.df).compute_histogram()['bin_centers'][column].dropna()

            # using KDE values for y-axis.
            y = kde_df[column]

            fig, ax = plt.subplots(figsize=figsize)
            # plotting using plot 		
            ax.plot(x, y, label=column, **kwargs)
            
            if title:
                ax.set_title(f'{title}: {column}')
            else:
                ax.set_title(f'Kernel Density Estimation plot of {remove_underscores(column)}')

            if xlabel:
                ax.set_xlabel(xlabel)
            else:
                ax.set_xlabel(column)

            if ylabel:
                ax.set_ylabel(ylabel)
            else:
                ax.set_ylabel('Count')

            ax.legend()

            return fig, ax

    def plot_qq(self, distribution_type: str = 'norm', title: str =None, points_color: str = 'green')-> tuple[Figure, Axes]:
        """
        Visualize Quantile-Quantile plot (QQ plot) for one or multiple columns of Numerical DataFrame.

        Parameters:
        -----------

        distribution_type: str (default is 'norm')
            Type of Distribution you would like to see.

        title : str, optional
            Title of the plot, default is None. 

        points_color : str, optional
            Color of data points, default is 'green'.

        Returns
        --------
        None
            This function is intended for visualization only and does not return anything.

        Usage Recommendation
        ----------------------
            Use this method of visualization only of numerical data.

        Example
        --------
        >>> NumericalVisualizer(df).plot_qq()
        """
        import matplotlib.pyplot as plt
        
        from scipy import stats

        if distribution_type is None:
            raise ValueError(f'Unknown distribution: {distribution_type}')
            
        distribution_name = getattr(stats, distribution_type, None)

        for column in self.df[self.columns]:

            fig, ax = plt.subplots()
            
            # using probplot to create a QQ plot
            stats.probplot(self.df[column], dist=distribution_name, plot=ax)

            if title:
                ax.set_title(title)
            else:
                ax.set_title(f'QQ plot of {remove_underscores(column)}')
            
            # setting color of data points

            ax.get_lines()[0].set_color(points_color)   # points

            return fig, ax
        


