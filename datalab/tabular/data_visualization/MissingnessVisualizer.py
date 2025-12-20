from .DataVisualizer import DataVisualizer

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import missingno as msno


class MissingnessVisualizer(DataVisualizer):

    def __init__(self, df: pd.DataFrame, columns:list = None):

        super().__init__(df, columns)

        self.df = df

        if columns is None:
            self.columns = df.columns.to_list()
        # ensuring that the columns passed are in a list
        else:
            self.columns = columns

    def plot_missing(self,
                viz_type: str = 'bar',
                extra_placeholders: list | None =None,
                title: str = None,
                xlabel: str = None,
                ylabel: str = None,
                title_fontsize: int = 24,
                title_padding: int = 20,
                xlabel_fontsize: int = 15,
                xlabel_padding: int = 15,
                ylabel_fontsize: int = 15,
                ylabel_padding: int = 15):
        '''
        Visualize missing values in each column of the DataFrame

        Parameters:
        -----------
            self : pd.DataFrame
                A pandas DataFrame

            viz_type : str or type(None) (default is 'bar')

                How you want to visualize missing values:

                    - 'bar'        : Displays a bar chart of missing vs non-missing values for each column
                    - 'heatmap'    : Creates a correlation heatmap showing how missing values present in one column relate with missing values in another.
                    - 'matrix'     : Displays a matrix plot where each row is a record in the DataFrame, and the column represents a column of the DataFrame
                    - 'dendrogram' : Displays a hierarchical clustering plot that groups columns in the DataFrame based on similar patterns of missing values

            title : str 
                Title of the plot. 
            
            title_fontsize: int (default is 24)
                Font size of Title of the plot.

            title_padding : int (default is 20)
                This means how much space must be allowed around the title.

            xlabel : str or type None
                Label for x-axis.
            
            xlabel_fontsize: int (default is 15)
                Font size of x-axis label.
            
            xlabel_padding : int (default is 15)
                This means how much space must be free around x-axis label.

            ylabel : str or type None
                Label for y-axis.
            
            ylabel_fontsize: int (default is 15)
                Font size of y-axis label.
            
            ylabel_padding : int (default is 15)
                This means how much space must be free around y-axis label.

        Returns:
        --------
            None
                This function does not return anything.
                It is meant for visualization only.

        Usage Recommendations:
        ----------------------
            1. Use 'bar' for plotting the volume of missing data vs non-missing data, before filling/dropping rows or columns with null values. 
            2. Use 'matrix' to identify patterns to see if missing data is missing randomly or in a structured manner 
            3. Use 'heatmap' for revealing relationships between missing values (if missingness is linked across columns).
            4. Use 'dendrogram' for identifying columns grouped together by similarity of missingness

        Considerations:
        ---------------
            1. This function uses missingno library under the hood. Just make sure you have it installed or use 'pip install missingno'
            2. For assistance with handling missing values, use missing_data_guide() along with this function for better decision making.

            '''
        import missingno as msno
        import numpy as np

        visualization_df = self.df.copy()
        
        if extra_placeholders is None:
            extra_placeholders = []

        # getting pandas truly missing values
        pandas_mask = visualization_df.isna()

        # getting placeholder missing values
        placeholder_mask = visualization_df.isin(extra_placeholders)

        # getting both the missing types
        mask = pandas_mask | placeholder_mask

        # since missingno does not have separate support for placeholder values, converting all missing types to np.nan
        visualization_df[mask] = np.nan

        # missingo functions return a matplotlib axes object, so we can modify it like normal matplotlib plots.

        if viz_type == 'heatmap':
            ax =  msno.heatmap(visualization_df)
        
        elif viz_type == 'bar':
            ax = msno.bar(visualization_df)
    
        elif viz_type == 'matrix':
            ax = msno.matrix(visualization_df)
        
        elif viz_type == 'dendrogram':
            ax = msno.dendrogram(visualization_df)

        # if user passes a title, it would be user selected title.abs
        # However, if user does not pass a title, it would default back to viz_type of plot as the title

        if title:
            ax.set_title(title, fontsize = title_fontsize, pad=title_padding)
        else:
            ax.set_title(f'{viz_type} plot of missing data', fontsize = title_fontsize, pad=title_padding)

        if xlabel:
            ax.set_xlabel(xlabel, fontsize = xlabel_fontsize, labelpad = xlabel_padding)
        
        if ylabel:
            ax.set_ylabel(ylabel, fontsize = ylabel_fontsize, labelpad = ylabel_padding)

        # this function does not return anything anymore.
        plt.show()
        