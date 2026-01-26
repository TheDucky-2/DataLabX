"""Computes distribution related statistics in one or multiple columns of a DataFrame."""

from .Computation import Computation
from .Statistics import Statistics

import pandas as pd

class Distribution(Computation):
    """
        Initializing Distribution Computation.

        Parameters
        -----------
        df: pd.DataFrame
            A pandas DataFrame

        columns: list, optional
            A list of columns you wish to compute distribution in, default is None.
    """

    def __init__(self, df: pd.DataFrame, columns:list = None):

        import pandas as pd

        super().__init__(df, columns)

        self.df = df

        if columns is None:
            self.columns = self.df.columns.tolist()
        else:
            self.columns = [column for column in columns if column in self.df.columns] 
    
    def compute_histogram(self, n_bins: int =30, density: bool =False, df_axis: int=1) -> pd.DataFrame:
        """
        Pre-Computes a histogram.

        Parameters
        -----------
        n_bins : int, optional
            Number of bins to use in the histogram, by default 30.

        df_axis: int, optional
            Whether you wish to see a concatenated dataframe column wise or row wise, default is 1.

            Available options:

            - 0 : Shows a concatenated dataframe row wise.
            - 1 : Shows a concatenated dataframe column wise (default).
        
        density :bool, optional 
            Density is used when we want to see histogram in terms of proabability distributions like normal, exponential or uniform and all, by default False.
            
            If False, 
                It usually shows how many values fall in each bin
                
            If True, 
                It usually shows how likely values are to fill within each range - i.e., the probability density.
                The total area under the histogram equals to 1.

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame 
    
        Usage Recommendation
        --------------------
            Use this function if you want a pre-computed histogram for calculations.
        
        Considerations
        ---------------
            This function returns a Concatenated DataFrame of counts, bin_edges and bin_centers of a histogram.

        Example
        ---------
        >>> Distribution(df).compute_histogram(n_bins=50) 

        >>> Distribution(df).compute_histogram(density=True)
        """ 

        if not isinstance(n_bins, int):
            raise TypeError(f'n_bins (number of bins) must be an int, got {type(n_bins).__name__}')

        if not isinstance(density, bool):
            raise TypeError(f'density must be a bool, got {type(density).__name__}')

        if not isinstance(df_axis, int):
            raise TypeError(f'df_axis must be a bool, got {type(df_axis).__name__}')

        if df_axis not in [0, 1]:
            raise ValueError(f"df_axis must either be 0 (for combining df row-wise) or 1 (for combining df column-wise), got {df_axis}")

        import numpy as np

        counts_dict = {}
        bin_edges_dict = {}
        bin_centers_dict = {}

        for col in self.df[self.columns]:
            
            # computing counts and bin edges
            counts, bin_edges = np.histogram(self.df[col], bins = n_bins, density=density)

            # computing bin centers
            bin_centers = 0.5 * (bin_edges[1:] + bin_edges[:-1])

            counts_dict[col] = counts
            bin_edges_dict[col] = bin_edges
            bin_centers_dict[col] = bin_centers

        counts_df = pd.DataFrame(counts_dict)
        bin_edges_df = pd.DataFrame(bin_edges_dict)
        bin_centers_df = pd.DataFrame(bin_centers_dict)

        # returning a concatenated df
        histogram_df = pd.concat({"counts": counts_df, "bin_edges" : bin_edges_df, "bin_centers" : bin_centers_df}, axis=df_axis, ignore_index=False)

        return histogram_df

    def raw_kurtosis(self) -> pd.DataFrame :
        """
        Computes the raw kurtosis for each numerical column of your DataFrame.

        Raw Kurtosis:

            1. It measures how the tails or peaks of a distribution differ from a normal distribution (bell-curve)
            2. It observes whether the data has more or fewer outliers (extreme values) than a normal distribution.
            3. For a normal distribution, kurtosis value is very close to 3

            - kurtosis > 3 means the data has heavy tails (more outliers).
            - kurtosis ~ 3 means the data is close to normal.
            - kurtosis < 3 means the data has light tails (fewer outliers).

        Formula
        --------
            raw_kurtosis = (average of (x - mean)^4) / (variance^2)

        Returns
        --------
        pd.Series
            A pandas Series

        Usage Recommendation
        ---------------------
            1. Use raw kurtosis if you are comparing several distributions mathematically.
            2. Use excess kurtosis if you are comparing to a normal distribution

        Example
        ---------
        >>> Distribution(df).raw_kurtosis()
        """ 
        n = len(self.df)

        mean = Statistics(self.df).mean()
        std_dev = Statistics(self.df).standard_deviation()

        fourth_central_moment = (((self.df - mean)**4).sum())/n

        raw_kurtosis = fourth_central_moment / ((std_dev)**4)

        return raw_kurtosis.to_frame(name='raw_kurtosis')

    def excess_kurtosis(self) -> pd.DataFrame :
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
        
        Example
        ---------
        >>> Distribution(df).excess_kurtosis()
        """

        raw_kurtosis = Distribution(self.df).raw_kurtosis()

        excess_kurtosis = raw_kurtosis['raw_kurtosis'] - 3

        return excess_kurtosis.to_frame(name='excess_kurtosis')

    def compute_kde(self, bandwidth_method:str ='silverman',n_bins: int =30, density: bool =False)-> pd.DataFrame:

        import numpy as np
        import pandas as pd
        from scipy.signal import fftconvolve
        """
        Computes the KDE (Kernel Density Estimation).

        KDE is just a smoothened histogram where bars are converted into curves
        Instead of showing counts per bin, KDE uses a smooth “kernel” (a bell-shaped curve) to estimate the probability distribution.

        Formula
        --------
            K(x)= e^(-x^2/2(h^2)) , where h is the Bandwidth that controls how wide the bump should be

        Parameters
        -----------
        bandwidth_method: str, optional
            Bandwidth method decides how wide each bump is when smoothing data for KDE, default is 'silverman'.

            Bandwidth methods available:

            For Normal Distribution

            - 'silverman' : 1.06 * std * (n ** (-1/5)) 
            - 'scott':  std * (n ** (-1/5)) , same as silverman without the optimized constant 1.06

            For Skewed Distribution

            - 'robust': (IQR/1.349) * (n ** (-1/5)) , uses IQR instead of standard deviation

        n_bins : int, optional
            Number of bins to use in the histogram, by default 30.
        
        density :bool, optional 
            Density is used when we want to see histogram in terms of probability instead of raw counts, by default False.
            
            If False, 
                It usually shows count of values that fall in each bin
                
            If True, 
                It usually shows how likely values are to fill within each range - i.e., the probability density.
                The total area under the histogram equals to 1.

        Returns
        --------
        pd.DataFrame
            A pandas DataFrame 

        Usage Recommendation
        --------------------
            1. Use this function when you want to compute KDE values, for visualization or analysis
            2. Use 'silverman' or 'scott' as bandwidth method if your data has normal distribution.
            3. Use 'robust' if your data has skewed distribution.

        Considerations
        ---------------
            This function calculates bandwidth (width of bump) separately for each column, which is why it is a bit slower.
        
        Example
        -------
        >>> Distribution(df).compute_kde()

        >>> Distribution(df).compute_kde('scott', n_bins = 50)
        """
        from .Statistics import Statistics

        n = len(self.df)

        std_dev =Statistics(self.df).standard_deviation()

        IQR = Statistics(self.df).iqr()

        histogram = Distribution(self.df).compute_histogram(n_bins=n_bins, density=density)
        
        KDE_dict = {}

        for column in self.df[self.columns]:

            if bandwidth_method == 'scott':

                bandwidth = std_dev[column] * (n ** (-1/5))
                
            elif bandwidth_method == 'silverman':

                bandwidth = 1.06 * std_dev[column] * (n ** (-1/5))

            else:
                # robust scott, uses IQR instead of standard deviation
                bandwidth = (IQR[column]/1.349) * (n ** (-1/5))

            bw = float(bandwidth)

            if not np.isfinite(bw) or bw<=0:
                raise ValueError(f'Invalid bandwidth for column {column}: {bw}')

            # importing the Distrubution computation and using bin centers to compute KDE since it is easier that way
            bin_centers = histogram['bin_centers'][column].dropna()
            counts = histogram['counts'][column].dropna()
            
            # calculating grid size using bin_centers 
            grid_size = len(bin_centers)

            # creating an artifical axis around zero, for kernel
            x_axis = np.linspace(-3 * bw, 3 * bw, grid_size)

            x_axis = np.asarray(x_axis, dtype=float)
            
            # creating kernel for making the curve
            kernel = np.exp((-x_axis**2)/(2 * bw**2))
            
            # making sure all values add up to 1
            kernel/=kernel.sum()

            # Using Fourier's for convolution (sliding across histogram like in neural nets)
            KDE = fftconvolve(counts, kernel, mode='same')

            KDE_dict[column] = KDE

        return pd.DataFrame(KDE_dict)
