# STEP 4.c : Visualizing Missing Data 
### **(Missingness Visualization Continued)....**

In the previous steps: 

**Step 1:**  We learned what values actually count as missing (built-in + placeholders).

**Step 2:**  We explored how much data is missing at the column level.

**Step 3:**  We explored missing data at the row level.

**Step 4.a:** 

- We explored how we can visualize missing data with 'Easy to Understand' Bar plots.

- We also learnt about optional good stuff that can help us make understandable visualizations.

**Step 4.b:**

- We explored how we can visualize missing data with 'Easy to Understand' Matrix plots and Heatmaps.

- We also learnt about the questions we are trying to answer through these visualizations.

Now that we know about simple bar plots, matrix plots and heatmaps, we will now explore the remaining visualization type.

## Dendrogram:

A dendrogram looks like "**A tree without leaves, made of lines that connect related things.**"

They are very useful in checking groups of columns where data is missing similarly and groups of columns that are missing data differently.

We can create a dendrogram of missing data by using **'dendrogram'** as **viz_type** in ``plot_missing()`` method of **MissingnessVisualizer** class.

Example:

    MissingnessVisualizer(df).plot_missing(viz_type = 'dendrogram')

Output:

> Below is the annotated image of **Dendrogram** used for better understanding of the plot.

![Dendrogram of Missing Data](/assets/docs/tabular/Missingness/Missingness_Viz/Dendrogram_of_missing_data.png)

We can see:

- We have two groups of columns based on similar/different patterns of missing data.

- Columns *'notes'* and *'account_closed_at'* are grouped together separately from the group of rest of the columns.

- Columns *'phone'* and *'email'* connect at a low height almost immediately, which means **They are missing together in the same rows**.

- Columns *'user_id'*, *'age'*, and *'account_created_at'* connect very early and form a small group, which means **Missing data in these columns is almost always present together**.

- Columns related to activity -> [*'session_length_sec'*, *'event_time'*, *'last_seen_at'*, *'country_code'*, *'feedback_score'*, and *'plan_tier'*], are connected together in the middle of the tree, which means **They often appear together and are often missing together**.

- Columns *'notes'* and *'account_closed_at'* remain separate for the longest time and only connect at the very bottom of the tree, which means **They are usually missing and only appear in special cases.**

###  Very Important:
One very important thing to remember in Dendrograms is this:

> ``Columns that connect earlier in the dendrogram behave similarly, and columns that connect later behave differently.``

Great!

We now know that "Columns that have lines with low height connect early and are similar" & "Columns with more height connect later and are different."

> However, this image only shows a Dendrogram of pandas **built-in missing** values.

Let us now explore what happens when we pass a list of placeholders that we consider as missing data:

## Dendrogram - With Placeholders:

We can create a dendrogram of missing data including placeholders by passing **extra_placeholders** in the ``plot_missing()`` method of **MissingnessVisualizer** class.

Example:

    MissingnessVisualizer(df).plot_missing(
        viz_type='dendrogram',
        extra_placeholders = [-999, 'UNKNOWN_DATE', 'CLOSED_UNKNOWN','ERROR', -1]
        )

Output:

> Here is an annotated image of **Dendrogram** used for better understanding of the plot:

![Dendrogram of Missing Data with Placeholders](/assets/docs/tabular/Missingness/Missingness_Viz/Dendrogram_of_Missing_Data_with_Placeholders.png)

We can see:

- We can now see clear separation of two groups we saw earlier, into several sub-groups based on similar/different patterns of missing data.

- Columns *'age'* and *'user_id'* and *'gender'* join each other very early and form a small group (GROUP 1), which means **Missing data in these columns is almost always present together**.

- Columns [*'account_created_at'*, *'billing_amount'* and *'city'*] joined each other first as GROUP 2 and then joined GROUP 1 later, meaning they also have similar missingness however not like columns in GROUP 1.

- Columns [*'session_length_sec'*, *'event_time'*, *'country_code'*,and *'plan_tier'*], also joined each first as GROUP 3 and then joined GROUPS 1 and 2, which means **They often appear together and are often missing together, however differently than GROUPS 1 and 2**.

- Columns [*'event_type*, *'last_seen_at'*, *'feedback_score'*], also joined each first as GROUP 4 and then joined GROUPS 1, 2 and 3 late, which means **They are similar to each other and are often missing together, however they are different from GROUPS 1, 2 and 3**.

- Columns *'phone'* and *'email'* connect at a low height almost immediately however, they join other groups very late, which means **They are missing together in the same rows however, they are not similar at all to other GROUPS in terms of missingness**.

- Columns *'notes'* and *'account_closed_at'* remain separate for the longest time and only connect at the very bottom of the tree, which means **They are usually missing and only appear in special cases.**

Great!

We now know:

- That dendrogram looks like a leafless tree.

- How we can create and understand **Dendrograms** for missing data, using datalabx.

- It helps us see groups of that are similar to each other and different from each other.

- After adding placeholders we consider as missing data, we can see how groups of similar/ different columns change in a dendrogram.

Alright!

I now know what counts as missing data, how to explore and visualize that data.

Now what?

We will explore how to handle missing data in the upcoming steps.

## Summary:

- We can use 'Easy to Understand' plots to easily see where data is missing.

- A bar plot shows how much data is missing in data.

- A matrix plot shows what rows are missing data (black (data present) and white (data missing)) in columns.

- We can notice considerable changes in missing data if we include placeholders.

- A heatmap shows which columns are missing data together.

- A dendrogram shows groups of columns that may have similar or different missing data patterns.