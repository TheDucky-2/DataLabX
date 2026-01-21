# Step 7.b: Understanding Skewness, Kurtosis, and Outliers

In the previous steps, we learnt:

- What is a distribution (**how will we distribute these candies - with whom? and how much?**).

- Two main types of distributions (**Normal** and **Non-Normal**).

We now know:

- Some distributions are balanced and have a center (middle) -> Normal Distribution

- Some distributions pile up in one place and are pulled more toward one side -> Non-Normal Distribution

In this step, we will slowly name and understand these patterns, without changing the data or doing any complex calculations.

These ideas help us answer an important question:

**Why is my data looking the way it does?**

And this understanding will later help us decide how to safely handle missing values.

## Why check how our data looks before Handling Missing Data?

DataLab understands that missing values do not exist by themselves.

They exist inside real data that may be:

- Skewed 

- Influenced by outliers

- Containing rare but important values

If we handle missing data without understanding these patterns:

- We may hide extreme values (outliers) and lose the important information they may represent.

- We may make rare values disappear

- We may make the data appear more '**normal**' than it actually is

That is why this step exists.

We will be exploring how the data behaves, before deciding how to change it.

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

When we tried to draw a curve through these bars, we can see a pattern that is looking like a tail going in the right direction.

``This kind of pattern is called Skewness. It can appear in either direction: left or right.``

**Skewness** sounds like a complex word, but it is very simple and all it means is this:

- Is our data leaning more toward one side instead of being balanced.

- If most values are small and a few values are very large, the data is pulled to the right (like in example above!).

- If most values are large and a few values are very small, the data is pulled to the left (**imagine the tail going in left direction**).

We don’t really need extra calculation to notice this.

We will be able to easily notice skewness by:

- Looking at a histogram (**like these examples we have seen till now!**)

- Then checking where most values are grouped together or spread out.

- Noticing if either of the sides have a **long tail**.

## But, How is Skewness related to missing data?

We can see that in the examples above:

- If we consider where most values are (47), the average number of candies distributed must be 1.
 
- However, a few large (6 candies) or small values can pull this average away from where most data actually is (**pulls average towards right, in our examples**).

- This can make 'average' misleading. 

- It's like saying, **"On average, everyone got 1 candy"**. But we know, a few even got 4, 5 and 6 candies.

Skewness directly affects how safe it is to replace missing numbers with mean (average value) or median (middle value).

That is the reason this concept is especially important before handling missing data as we want to **avoid changing the shape of our original data.**

**Great!** 

We now know:

- Skewness means "Is my data leaning towards one side?"

- Whether most values are large or small determine the direction of skewness (right or left).

- How skewness directly affects missing data.

## Outliers (We have a rough intuition of this too!)

Let's say we had candies remaining with us that we took home, after distributing the candies at school.

Our little brother took 15 candies out of the bag for himself.

Let us see what that would look like visually:

<img src = "example_images/Example_Outliers.png" alt = "Outliers Example" width = "600">

While looking at this distribution, we can notice that **15 candies is very different and very far from the rest (1 - 6)**.

``These values that are very far from most other values are called outliers.``

Let us look at another visual example by drawing a **Curve** through these bars:

<img src = "example_images/Outlier_curve.png" width = "700">

Outliers are not incorrect or wrong values. They can be values that are:

- Real but are rare

- Important or unusual events

- Errors or edge cases

At this stage, we do not remove or change them, but will only observe them.

## How are Outliers related to missing data?

Before handling missing data, we need to know:

- Do any outliers exist?

- Is their occurrence rare or common?

- Do they seem meaningful or are something we can get rid of?

Existence of outliers matter for missing data handling because:

- Outliers can heavily influence averages (average value) as they can pull numbers either too high or too low, so missing values may be filled with unrealistic numbers.

- Outliers can really change how distributions look by changing the shape, causing missing values to be filled in inaccurately.

- Outliers can make the numbers look less similar to each other, affecting how missing values are to be handled.

That is why **removing or filling missing data without looking at outliers can hide important information.**

## Kurtosis (How Extreme are my Extremes?)

Let's say that after taking 15 candies, our little brother shared the remaining candies among his friends.

Let us see what that would look like visually:

<img src = "example_images/Example_kurtosis.png" width = "800">

We can see:

- Most people (47) got 1 candy.

- A few people (13) got many more candies (between 3-6 candies).

- A few people (5) got an extremely high number of candies (between 13-16) as compared to most common number (1).

These extremely high number of candies (13- 16) represent outliers.

That is how two datasets (previous example and this one), both have outliers, but still feel very different.

One dataset may have:

- Only one or two extreme values (**first example**)

Another dataset may have:

- Many extreme values (**second example**)

``This idea that if i have extremes, how extreme they really are, is what is called kurtosis.``

## But, how do we define Kurtosis?

Kurtosis simply means:

- How extreme are the extreme values in a dataset (**Are extreme values just a bit far or very very far?**)

- How often the extreme values appear (**Is there only one extreme value or many extreme values?**)

- If extreme values appear many times, it is called **high-kurtosis.**

- If extreme values appear only a few times, it is called **low-kurtosis**.

We don’t need to do heavy math to understand kurtosis right now.

We can usually get a good idea by:

- Looking at how tall or sharp the distribution is (**Are most values very close together or far?**)

- Checking how many values are far away from the center

Even without math doing, we can already see that if we try to get average number of candies, it will definitely be more than 1, **even when 1 is the most common value.**

We are only building intuition right now and we will explore how to check all these using datalab while handling missing data.

## How is Kurtosis related to missing data?

Kurtosis helps us understand how much the extreme values matter in our data.

In datasets with **high kurtosis**:

- Most values are very close together.

- A few values are very far away from the rest.

These extreme values usually have a big impact on the data.

If some values are missing in such data:

- We may accidentally lose important extreme values.

- Filling missing values with an average can hide how extreme the data really is.

- The data may start to look more **normal** than it really is

In datasets with **low kurtosis**:

- Extreme values are rare or not very far from the center.

- Missing values usually have less impact.

- Simple methods for handling missing data are safer.

That is why checking kurtosis is important before handling missing data as it helps us understand **how careful we need to be when filling or removing missing values.**

## So, What Comes Next?

We now know:

- How our data is distributed

- What skewness looks like

- How outliers behave

- How extreme values can affect the summary of our data.

We also explored distributions, skewness, outliers and kurtosis visually.

In the next step, we will:

- Use 'Easy to Understand' visuals like Histograms (we have been looking at these), QQ plots and KDE plots.

- Use DataLab’s methods to verify whether data distribution is following a normal or non-normal pattern.

- Connect these observations directly to missing value handling decisions

- Once this understanding is complete, we will return to Missing Data Handling with clarity and intention.

