The pseudo-code is trying to accomplish the following:

1. It is storing the smallest and the largest values (**peak**) along with their index.

2. It continues looking for highest and smallest values until the sign upon product of current value and previous value is positive.

3. It is only adding the index and the peak to the output, when the resulting sign upon product of current and previous value is negative.

4. The output with code as it is: **[(1, 4), (4, -9), (7, 12), (9, -4)]**

5. However, as it is only adding the output when the sign changes to negative, it never includes the last value 7, at index 15 and misses registering the full output as: **[(1, 4), (4, -9), (7, 12), (9, -4), (15, 7)]**

