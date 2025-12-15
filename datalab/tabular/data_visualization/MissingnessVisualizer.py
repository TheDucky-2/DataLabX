from .DataVisualizer import DataVisualizer

import pandas as pd
import matplotlib

class MissingnessVisualizer(DataVisualizer):

    def __init__(self, df: pd.DataFrame, columns:list = None):

        super().__init__(df, columns)

        self.df = df

        if columns is None:
            self.columns = df.columns.to_list()
        # ensuring that the columns passed are in a list
        else:
            self.columns = columns

    def plot_missing(self, viz_type: str|None = 'bar') -> matplotlib.axes.Axes:  # viz : alias for 'visualization'
        '''
        Visualize missing values in each column of the DataFrame

        Parameters:
        -----------
            df : pd.DataFrame
                A pandas DataFrame

            viz_type : str or type(None) (default is None)

                How you want to visualize missing values:
                    - 'bar'        : Displays a bar chart of missing vs non-missing values for each column
                    - 'heatmap'    : Creates a correlation heatmap showing how missing values present in one column relate with missing values in another.
                    - 'matrix'     : Displays a matrix plot where each row is a record in the DataFrame, and the column represents a column of the DataFrame
                    - 'dendrogram' : Displays a hierarchical clustering plot that groups columns in the DataFrame based on similar patterns of missing values

        Returns:
        --------
            matplotlib.axes.Axes
                A matplotlib axes object of the generated plot

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
        import matplotlib
        
        if viz_type is not None:

            if viz_type == 'heatmap':
                return msno.heatmap(self.df)
            
            elif viz_type == 'bar':
                return msno.bar(self.df)
            
            elif viz_type == 'matrix':
                return msno.matrix(self.df)
            
            elif viz_type == 'dendrogram':
                return msno.dendrogram(self.df)
