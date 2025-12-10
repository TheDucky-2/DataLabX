# Numerical Diagnosis
----------------------

Numerical diagnosis means using numbers to understand what is happening in your data.

It is like a check-up of the numbers in your data, where you look at important numbers to see if something looks normal or strange.

# What are these Important Numbers?
-----------------------------------
When we diagnose Numerical data (numbers), we usually look for:

1. Mean               -> the average value
2. Median             -> the middle value
3. Mode               -> the most occurring value
4. Minimum            -> the minimum value
5. Maximum            -> the maximum value
6. Range              -> the difference between maximum and minimum value (means how much your data is spread out)
7. Standard deviation -> how much the values vary
8. Skewness           -> Is my data extending to the left or right?
9. Kurtosis           -> If my data is extending to the left or right, are these tails heavy or light?
10. Outliers          -> what values lie at the end of these tails

These numbers help us see the shape, spread, and behavior of the data.

### What Can I Diagnose?
------------------------
DataLab allows you to diagnose your numerical data(numbers) using NumericalDiagnosis class.

Numerical Diagnosis allows you to:

- Check if your data has normal or non-normal distribution (is like a bell curve or not)
- Check Sparsity (Imagine having a lot of zeros in your data)
- Detect Outliers (Values that are far-far from average value)
- Check Skewness (Imagine non-symmetrical data)




     |
   10|        /\ 
    9|       /  \
    8|      /    \
    7|     /      \
    6|    /        \
    5|   /          \
    4|__/            \_____________
       left  center     long tail →

            |
   10|                      /\ 
    9|                     /  \
    8|                    /    \
    7|                   /      \
    6|                  /        \
    5|                 /          \
    4|____ ___________/            \
        ← long tail      center   right

   10|           /\ 
    9|          /  \
    8|         /    \
    7|        /      \
    6|       /        \
    5|      /          \
    4|_____/            \_____
        left   center   rightData