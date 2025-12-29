# Step 7.b: Understanding Skewness, Kurtosis, and Outliers

In the previous steps, we learnt:

- What is a distribution (**how will we distribute these candies - with whom? and how much?**).

- Two main types of distributions (**Normal** and **Non-Normal**).

We now know:

- Some distributions are balanced and have a center(middle) -> Normal Distribution

- Some distributions pile up in one place and are pulled more toward one side -> Non-Normal Distribution

In this step, we will slowly name and understand these patterns, without changing the data or doing any complex calculations.

These ideas help us answer an important question:

**Why is my data looking the way it does?**

And this understanding will later help us decide how to safely handle missing values.

## Skewness (We already have a rough intuition of this!)

Let us go back to our candy example.

<img src = "example_images/Annotated_distribution.png" alt = "Annotated Distribution" width = "700">

We can see:

- Most people received 1 candy and these are grouped together in one place.
- A few people received many more candies and these are spread out in one direction. 

Let us look at another visual example by drawing a **Curve** through these bars:

**Example Curve:**

<img src="example_images/Example_curve.png" alt="Distribution curve" width="700">
<br>
<br>

When we tried to a draw curve through these bars, we can see a pattern that is looking like a tail going in the right direction.

This kind of pattern is called **Skewness**. It can appear in either direction: **left** or **right**.

**Skewness** sounds like a complex word, but it is very simple and all it means is this:

- Is our data leaning more toward one side instead of being balanced.

- If most values are small and a few values are very large, the data is pulled to the right (like in example above!).

- If most values are large and a few values are very small, the data is pulled to the left (**imagine the tail going in left direction**).

We don’t really need extra calculation to notice this. We will be able to notice skewness by:

- Looking at a histogram (**like these examples we have seen till now!**)

- Then checking where most values are grouped together or spread out.

- Noticing if either of the sides have a **long tail**.

## But, How is this related to missing data?

We can see that in the examples above:

- If we consider where most values are (47), the average number of candies distributed must be 1.
 
- However, a few large (6 candies) or small values can pull this average away from where most data actually is (**pulls average towards right, in our examples**).

- This can make 'average' misleading. 

- It's like saying, **"On average, everyone got 1 candy"**. But we know, a few even got 4, 5 and 6 candies.

Skewness directly affects how safe it is to replace missing numbers with mean (average value) or median (middle value).

That is the reason this concept is especially important before handling missing data as we want to avoid changing the shape of our original data.

**Great!** 

We now know:

- Skewness means "Is my data leaning towards one side?"

- Whether most values large or most values small determine the direction of skewness.

- And, how skewness directly affects missing data.
