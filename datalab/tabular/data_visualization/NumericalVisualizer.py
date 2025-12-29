# from datalab
from .DataVisualizer import DataVisualizer
from ..computations import Distribution

import pandas as pd

# removing underscores in column names if they exist, for plot Titles.
def remove_underscores(column):
    
    column = " ".join(column.split('_'))

    return column

class NumericalVisualizer(DataVisualizer):

    def __init__(self, df: pd.DataFrame, columns: list|type(None) = None):
        # getting the elements of parent DataVisualizer class
        super().__init__(df, columns)

        self.df = self.df.select_dtypes(include = 'number')
        
        if columns is None:
            self.columns = df.columns

        else: 
            self.columns = [column for column in columns if column in df.columns]

    def plot_histogram(self,
                  bins: int=30,
                  title: str=None,
                  xlabel: str=None,
                  ylabel: str=None,
                  figsize: tuple =(6, 4),
                  **kwargs):
        '''
        Visualize histogram for each column of Numerical DataFrame

        Parameters:
        -----------

        Optional:

            bins : int , (default is 30)
                Number of bins you wish to visualize
            
            xlabel : str or type(None)
                Label for x-axis.

            ylabel : str 
                Label for y-axis.

            title : str 
                Title of the plot. Adds column name by default.

            figsize : tuple (default is (6, 4))
                Size of the figure (width, height) in inches.

            **kwargs : dict
                Dictionary of keyword arguments passed to 'matplotlib.pyplot.boxplot'.

        Returns:
        --------
            None
                This function is intended for visualization only. 
                It only displays the plot and does not return anything.

        Usage Recommendations:
        ----------------------
            Use this method of visualization only for numerical data.
        
        '''

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

            plt.show()

    def plot_box(self, 
                orientation : str = 'vertical',
                xlabel:str|type(None) = None,
                ylabel:str|type(None) = None,
                title:str|type(None) = None,
                figsize:tuple = (6, 4),
                **kwargs):

        import matplotlib.pyplot as plt
        '''
        Visualize box plot for each column of Numerical DataFrame

        Parameters:
        -----------

        Optional:

            orientation : str , (default is 'h')
                Orientation of the boxplots. Whether 'horizontal'/'h' or 'vertical'/'v'
            
            xlabel : str or type(None)
                Label for x-axis.

            ylabel : str 
                Label for y-axis.

            title : str 
                Title of the plot. Adds column name by default.

            figsize : tuple (default is (6, 4))
                Size of the figure (width, height) in inches.

            **kwargs : dict
                Dictionary of keyword arguments passed to 'matplotlib.pyplot.boxplot'.

        Returns:
        --------
            None
                This function is intended for visualization only. 
                It only displays the plot and does not return anything.

        Usage Recommendations:
        ----------------------
            Use this method of visualization only for numerical data.
        '''

        if orientation not in ('horizontal', 'vertical', 'h', 'v'):
            raise ValueError(f"orientation must be horizontal or 'h' OR vertical or 'v', got {orientation}")

        # making sure that the orientation starts with vertical or 'v' by default.
        # if it will be anything other than vertical, it will default to horizontal
        vert = (orientation.lower().startswith('v'))

        for column in self.df[self.columns]:

            fig, ax = plt.subplots(figsize=figsize) # defauls to figsize of (6, 4) inches. (6 X 4)
        
            # keeping it simple by 
            ax.boxplot(self.df[column], vert=vert, **kwargs)

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

            plt.show()


    def plot_KDE(self, bandwidth_method: str ='robust',
                  title: str=None,
                  xlabel: str=None,
                  ylabel: str=None,
                  figsize: tuple =(6, 4),
                  **kwargs):
        '''
        Visualize Kernel Density Estimation plot (curves, including bell curve) for each column of Numerical DataFrame

        Parameters:
        -----------
            self
            A pandas DataFrame

            Optionals:

                bandwidth_method: 'str' (default is 'Silverman')

                bandwidth methods available:

                For Normal Distribution:

                    - 'silverman' 
                    - 'scott'

                For Skewed Distribution:

                    - 'robust' (uses robust scott)

                xlabel : str or type(None)
                    Label for x-axis.

                ylabel : str 
                    Label for y-axis.

                title : str 
                    Title of the plot. Adds column name by default.

                figsize : tuple (default is (6, 4))
                    Size of the figure (width, height) in inches.

                **kwargs : dict
                    Dictionary of keyword arguments to pass into 'matplotlib.pyplot.plot'.

        Returns:
        --------
            None
                This function is intended for visualization only. 
                It only displays the KDE plot and does not return anything.

        Usage Recommendations:
        ----------------------
            Use this method of visualization only for numerical data.

        Considerations:
        ---------------
            This function uses compute_KDE() and compute_histogram() from Distribution class of the Computation Package

            '''
        import matplotlib.pyplot as plt

        # compute_KDE() returns a DataFrame
        kde_df= Distribution(self.df).compute_KDE(bandwidth_method=bandwidth_method)

        for column in self.df[self.columns]:
            # using bin_centers from histogram computation as values for x-axis.
            x= Distribution(self.df).compute_histogram()[column]['bin_centers']

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

            plt.show()

    def plot_QQ(self, distribution_type: str = 'norm', title: str =None, points_color: str = 'green'):

        '''
        Visualize Quantile-Quantile plot (QQ plot) for each column of Numerical DataFrame

        Parameters:
        -----------

        self : pd.DataFrame
            A pandas DataFrame

        Optional:

            distribution_type: str (default is 'norm')
                Type of Distribution you would like to see

            title : str or type None
                Title of the plot. Adds column name by default.

            points_color : str (default is 'green')
                Color of data points

        Returns:
        --------
            None
                This function is intended for visualization only. 
                It only displays the plot and does not return anything.

        Usage Recommendations:
        ----------------------
            Use this method of visualization only for numerical data.

        '''
        from scipy import stats
        import matplotlib.pyplot as plt

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
            
        plt.show()
        


                