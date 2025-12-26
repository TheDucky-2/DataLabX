# Step 5 - Handling Missing Data

In the previous steps, we have done a lot of important work:

**Step 1:**  We learned what values are identified as missing (pandas built-in + placeholders).

**Step 2:**  We explored how much and what data is missing at the column level.

**Step 3:**  We explored how much and what data is missing at the row level.

**Step 4:** 

- We explored how we can visualize missing data with 'Easy to Understand' **Bar plots**, **Matrix plots**, **Heatmaps** and **Dendrograms**.

- We learnt about the kinds of relationships we are exploring with the help of these visualizations.

- We also learnt about optional good stuff that can help us make understandable visualizations.

**However, we are not handling missing values yet and this is on purpose.**

**That is because we don’t have enough information yet to decide how to do it correctly.**

## But, Haven't we already covered a lot of Steps?

Yes, We have identified what counts as missing values and which columns they exist in.
 
We have also explored rows of both kinds of missing data(**pandas built-in + placeholders**).

We even saw 4 different visualizations of missing data.

So, shouldn’t handling them be really straight forward at this point?

That’s actually a fair question.

> However, the thing is that knowing where and what values are missing is not the same as knowing what to do about them.

At this moment, we can clearly see the gaps in the data but we don’t yet know enough about the data itself to decide:

- What should we do with the missing values - Drop them or Replace them (fill them) with something?

- If we drop them, what should we keep in mind before we drop them?

- If we fill missing values, what should we fill them with?

- Or, is it better to just leave them alone?

If we handle missing values right now, we would mostly be doing guess work.

So instead of just guessing, **we pause here.**

We first take a step back to explore and understand our data better.

Once we have that information, handling missing values becomes clear and intentional, not automatic.

**We will come back to this step shortly.**

## Why can't we handle missing values right now?

When we remove or replace missing data, we are really changing our data.

Once we make the changes, we cannot see or revert back to the original data anymore.

If we rush and make that change too early:

- We may hide values that were unusually big or small, and could help us learn more about our data.

- We may make some values seem more common / appear more often than they actually are.

- We may remove important data without realizing it mattered in our analysis.

Example:

**1.**

    Replacing missing numbers with an average value can actually make everything look more 'normal' than it really is.

**2.**

    Replacing missing text data with the most common value can make rare but helpful values disappear.

**3.**

    Just removing rows of missing data can silently delete the useful information

Because of this, handling missing values too early can lead to wrong or misleading results.

So instead of changing the data now, we first spend time looking at it and understanding more about it.

Once we do that, handling missing values becomes a clear intentional decision, not a guess.

## What Happens Next?

Instead of guessing or applying fixed rules, DataLab follows this order:

- Detect and explore missing data **(DONE)**

- Understand the data itself **(We will explore easy to learn concepts like Distributions, Skewness, Outliers and Frequency)**

- Then we decide how to handle missing values.

When we follow this order, we know we’re making a decision based on our understanding of data, and we can explain our decisions to others.

## We will come back to Missing Data Handling

This section is **not incomplete.** We are intentionally pausing here to learn more about our data.

In the next sections, we will explore:

- Data distributions

- Skewness and kurtosis (with visual examples)

- Outliers

- Frequency

Once those concepts are clear, we will return to missing value handling and complete the workflow with ease.