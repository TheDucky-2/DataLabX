"""Computes distribution related statistics in one or multiple columns of a DataFrame."""

from .Computation import Computation
from .Statistics import Statistics

import pandas as pd

class Distribution(Computation):

    def __init__(self, df: pd.DataFrame, columns:list = None):
        """
        Initializing Distribution Computation.

        Parameters
        -----------
        df: pd.DataFrame
            A pandas DataFrame

        columns: list, optional
            A list of columns you wish to compute distribution in, default is None.
        """
        import pandas as pd

        super().__init__(df, columns)

        self.df = df

        if columns is None:
            self.columns = self.df.columns.tolist()
        else:

            self.columns = [column for column in columns if column in self.df.columns] 
    
    def compute_histogram(self, n_bins: int =30, density: bool =False) -> pd.DataFrame:
        """
        Pre-Compute histogram for each numerical column of your DataFrame.

        Parameters
        -----------
        n_bins : int, optional
            Number of bins to use in the histogram, by default 30.
        
        density :bool, optional 
            Density is used when we want to see histogram in terms of proabability distributions like normal, exponential or uniform and all, by default False.
            
            If False, 
                It usually shows how many values fall in each bin
            If True, 
                It usually shows how likely values are to fill within each range - i.e., the probability density.
                The total area under the histogram equals to 1.

        Returns
        --------
            dict 
            A dictionary of of each column as key, and precomputed bins with bin_centers and counts of the histogram for that column as value
    
        Usage Recommendation
        --------------------
            Use this function to convert columns into numeric values for later calculations.
        
        Considerations
        ---------------
            This function converts non-convertible values into np.nan (Not a Number) by default.

        Examples:
        
        >>> Distribution(df).compute_histogram(n_bins=50) 

        >>> Distribution(df).compute_histogram(density=True)
        """ 
        import numpy as np

        computed_bins = {}

        for column in self.df[self.columns]:

            max_value, min_value = self.df[column].max(), self.df[column].min()

            # Computing bin boundaries

            bin_boundaries = np.linspace(min_value, max_value, n_bins+1) # taking +1 to include last element as part of the boundary

            # Computing occurrence counts of values falling between bin boundaries

            counts, _ = np.histogram(self.df[column], bins = bin_boundaries, density=density)

            # Computing center values of the bins

            ## # bin_boundaries[:-1] is the beginning of boundary 
            ## # bin_boundaries[1:] is the end of boundary
            bin_centers = 0.5 * (bin_boundaries[1:] + bin_boundaries[:-1]) 

            computed_bins[column] = pd.DataFrame({
                
                    'bin_centers' : bin_centers,
                    'counts' : counts
                } )
            
        return computed_bins

    def raw_kurtosis(self) -> pd.Series :
        """
        Computes the raw kurtosis for each numerical column of your DataFrame.

        Raw Kurtosis:

            1. It measures how the tails or peaks of a distribution differ from a normal distribution (bell-curve)
            2. It observes whether the data has more or fewer outliers (extreme values) than a normal distribution.
            3. For a normal distribution, kurtosis value is very close to 3

            - kurtosis > 3 means the data has heavy tails (more outliers).
            - kurtosis ~ 3 means the data is close to normal.
            - kurtosis < 3 means the data has light tails (fewer outliers).

        Formula:

            raw_kurtosis = (average of (x - mean)^4) / (variance^2)

        Returns:
            pd.Series
            A pandas series of raw kurtosis values for each numerical column of your DataFrame

        Usage Recommendation:
            1. Use raw kurtosis if you are comparing several distributions mathematically.
            2. Use excess kurtosis if you are comparing to a normal distribution
        """ 

        n = len(self.df)

        df_mean = Statistics(self.df).mean()
        df_std_dev = Statistics(self.df).standard_deviation()

        fourth_central_moment = (((self.df - df_mean)**4).sum())/n

        raw_kurtosis = fourth_central_moment / ((df_std_dev)**4)

        return raw_kurtosis

    def excess_kurtosis(self) -> pd.Series :
        """
        Computes the excess kurtosis for each numerical column of your DataFrame.

        Excess Kurtosis:

            1. It measures how the tails or peaks of a distribution differ from a normal distribution (bell-curve)
            2. It observes whether your data has many outliers (extreme values).
            3. For a normal distribution, excess kurtosis value is very close to 0

            - kurtosis > 0 means the data has heavy tails (more outliers).
            - kurtosis ~ 0 means the data is close to normal.
            - kurtosis < 0 means the data has light tails (fewer outliers).

        Formula
        --------
            excess kurtosis = raw kurtosis - 3

        Returns
        --------
        pd.Series
            A pandas Series

        Usage Recommendation
        ---------------------
            1. Use excess kurtosis if you are comparing to a normal distribution
            2. Use raw kurtosis if you are comparing several distributions mathematically.
        """

        raw_kurtosis = Distribution(self.df).raw_kurtosis()

        excess_kurtosis = raw_kurtosis - 3

        return excess_kurtosis

    def compute_KDE(self, bandwidth_method ='silverman')-> pd.DataFrame:
        import numpy as np
        import pandas as pd
        from scipy.signal import fftconvolve
        """
        Computes the KDE (Kernel Density) for each numerical column of the
        DataFrame.

        Intuition:
        ----------

            KDE is just a smoothened histogram where bars are now curves
            Instead of showing counts per bin, KDE uses a smooth “kernel” (a bell-shaped curve) to estimate the probability distribution.

        Formula:
        --------

            K(x)= e^-x^2/2(h^2) , where h is the Bandwidth that controls how wide the bump should be

        Parameters:
        -----------

        Optional:

            bandwidth_method: str (default is 'Silverman')

            Bandwidth methods available:

            For Normal Distribution:

                - 'silverman' : 1.06 * std * (n ** (-1/5))
                - 'scott':              std * (n ** (-1/5)) , same as silverman without the optimized constant 1.06

            For Skewed Distribution:

                - 'robust': (IQR/1.349) * (n ** (-1/5)) , uses IQR instead of standard deviation

        Returns:
        --------
            pd.DataFrame
            A pandas DataFrame of KDE values

        Usage Recommendation:
            1. Use this function when you want to compute KDE values, for visualization or analysis
            2. Use 'silverman' or 'scott' as bandwidth method if your data has normal distribution.
            3. Use 'robust' if your data has skewed distribution.

        Considerations:
            This function calculates bandwidth (width of bump) separately for each column, which is why it is a bit slower.
        """
        n = len(self.df)
        std_dev =Statistics(self.df).standard_deviation()

        IQR = Statistics(self.df).IQR()
        
        KDE_dict = {}

        for column in self.df[self.columns]:


            if bandwidth_method == 'scott':

                Bandwidth = std * (n ** (-1/5))
                
            elif bandwidth_method == 'silverman':

                Bandwidth = 1.06 * std * (n ** (-1/5))

            else:
            # robust scott, uses IQR instead of standard deviation
                Bandwidth = (IQR/1.349) * (n ** (-1/5))

            # importing the Distrubution computation and using bin centers to compute KDE since it is easier that way
            bin_centers = Distribution(self.df).compute_histogram()[column]['bin_centers']
            counts = Distribution(self.df).compute_histogram()[column]['counts']
            
            # calculating grid size using bin_centers 
            grid_size = len(bin_centers)

            #### CALCULATING KERNEL (Bump) FUNCTION 

            # creating an artifical axis around zero, for kernel
            x_axis = np.linspace(-3 * Bandwidth[column], 3 * Bandwidth[column], grid_size)
            
            # creating kernel for making the curve
            kernel = np.exp((-x_axis**2)/(2 * Bandwidth[column]**2))
            
            # making sure all values add up to 1
            kernel/=kernel.sum()

            # Using Fourier's for convolution (sliding across histogram like in neural nets)
            KDE = fftconvolve(counts, kernel, mode='same')

            KDE_dict[column] = KDE

        return pd.DataFrame(KDE_dict)

    def skewness(self):
        """
        Computes the skewness (if data is being pulled in one direction).

        Skewness:
        
        - Values near 0 means the data is roughly symmetric.
        - Positive values indicate that data is being pulled towards right direction.
        - Negative values indicate taht data is being pulled towards left direction.

        Formula
        -------
            skewness = (1/n) * sum of ((x - mean of x)/std dev of x)**3

        Returns
        -------
            pd.Series
            A pandas Series
        
        Usage Recommendation
        ---------------------
            Use this function for checking the shape of your data (whether it follows normal distribution or non-normal distribution).
        """ 

        return self.df.skew()

