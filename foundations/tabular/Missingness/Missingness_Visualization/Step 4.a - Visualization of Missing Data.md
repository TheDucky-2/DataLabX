# STEP 4.a : Visualizing Missing Data (Missingness Visualization)

In the previous steps, we focused on understanding what is missing data before touching the data itself:

**Step 1:** We learned what values actually count as missing (built-in + placeholders).

**Step 2:** We explored how much data is missing at the column level.

**Step 3:** We explored missing data at the row level.

Now that we understand and have explored missing data, the next natural step is to see it visually.

## What is this step about?

This step is about ``exploring missing data patterns visually``.

Instead of reading numbers or tables now, we will use simple visualizations (images) to quickly answer questions like:

- Is my missing data scattered randomly or is it in groups?

- Are some columns missing together?

- Is missingness of data increasing over time or following a pattern?

This step does not clean or modify your original data.

> However, this step does create a copy of your data and converts your placeholder values into built-in missing values.

## Why are my placeholder values converted to Pandas built-in missing values?

datalabx converts your placeholder values like **MISSING, ERROR, UNKNOWN** or anything else into **NaN** (Not a Number) automatically, for **visualization purposes only**.

This is done because datalabx uses ``missingno`` library under the hood for creating intuitive and widely-used missing data visualizations.

However, **missingo** only supports pandas built-in missing values, and does not consider placeholder values as missing data.

That is why all user decided missing values like:

    ['MISSING', '?', '-', 'Unknown' or anything else] are converted to -> NaN 

## Why visualize missing data Now, after so many steps?

Missing data visualization only makes sense after we know:

- What values are identified as missing

- Which placeholders represent missingness

- How missingness is distributed across rows and columns

If we jumped directly to visualization without those steps, the plots could be misleading (we will explore this too!).

That’s why datalabx follows this order:

    Understand → Explore → Visualize → Decide

## Visualizing Missing Data in datalabx

datalabx allows us to explore our missing data by creating easy to understand plots.

These plots are simple, fast, and very effective for real-world datasets.

datalabx also allows us to:

- Include both pandas missing values (NaN, NaT)

- Include our own placeholder values

However, placeholders are converted only and only for visualization (**original data remains absolutely unchanged**).

## But, what are these 'Easy to Understand' plots?

datalabx supports the most commonly used plots for visualizing missing data.

These are:

- **Bar plot** 

This looks like "**Bars of chocolates standing together, side-by-side**".

It shows how much data is missing vs how much data is not missing, per column.

- **Matrix plot**

This looks like "**Some of these chocolate bars have zebra stripes. A few of them have too many stripes!**"

This plot shows patterns of missing data across all the rows of DataFrame.

- **Heatmap**

This looks like **stairs with colors - 'red' steps mean a lot of people step there, 'blue' steps mean almost nobody does.**

This shows which columns are missing data together.

- **Dendrogram**

This looks like **matchsticks lying on a table - you keep adding the most similar ones into the same pile**.

This shows which columns have missing values in similar places.

## **datalabx Usage**

We can begin visualizing our missing data by importing ``MissingnessVisualizer`` class from datalabx.

    from datalabx import MissingnessVisualizer

## Bar Plot

We can create a bar plot of missing data using ``plot_missing()`` method from **MissingnessVisualizer** class.

This method does not return anything and is meant for **visualization only**.

**Example:**

    MissingnessVisualizer(df).plot_missing()

**Output:**

> Here is an annotated image of **bar plot** used for better understanding of the plot:

![Bar Plot of Missing Data](/assets/docs/tabular/Missingness/Missingness_Viz/Bar_Plot_of_Missing_Data.png)

We can see:

- Column *'customer_id'* has a full bar, which means it is full and does not have missing data.
- Columns *'signup_date'* and *'event_timestamp'* have less than 500 rows missing, out of 500000.
- Columns *'email'*, *'notes'* and *'phone_number'* have a lot of missing data. 
- Column *'phone_number'* is the shortest bar of chocolate as it is missing most of the data.

> Whatever missing data we saw in the image above, is for pandas built-in missing values.

However, we can also pass in our own placeholders and let us see if we can notice any change in missing data. 

## Bar Plot - With Placeholders:

We can create a bar plot of missing data with placeholders using ``plot_missing()`` method and passing extra placeholders like this:

**Example:**

    MissingnessVisualizer(df).plot_missing(extra_placeholders = [-999, -1, '-999', '?'])

**Output:**

> Below is an annotated image of **bar plot with placeholders** used for better understanding of the plot:

![Bar Plot of Missing Data with Placeholders](/assets/docs/tabular/Missingness/Missingness_Viz/Bar_Plot_of_Missing_Data_with_Placeholders.png)

We can see:

- Bar for column *'age'* got shorter as placeholder values -999, -1 are now considered missing data.

- For columns *'notes'* and *'phone_number'*, missing data increased drastically just by addition of a few placeholders.

- Looks like someone ate most of the chocolate bar for column *'phone_number'*.

**Great!**

We now know:

1. How we can see **bar** plot or **chocolate bars** of missing data.

2. What missing data vs non-missing data looks like in a bar plot (**did someone eat my chocolate? if yes, how much?**)

Before we move onto another type of "Easy to Understand" plot, let us explore a few useful things that can use in our plots:

## Useful Stuff (For Making Good Looking Visualizations)!
 
Before we know why we even need this useful stuff, let us explore what we miss without it:

> Here is a plot of missing data without good stuff:

![Blank Bar Plot](/assets/docs/tabular/Missingness/Missingness_Viz/Blank_Bar_plot.png) 

We can see:

- Only chocolate bars and numbers on top, left and right with column names at the bottom, but...

- This still looks empty because we don't what this is about and what do these numbers mean.

- This cannot be shared with others yet because it does not communicate the whole story of this figure.

Which is why datalabx allows us to use some optional, however, very **helpful parameters** (just some extra information we can give a method):

### HELPFUL PARAMETERS:

- **viz_type** -> Represents the type of visualization we want to see.

We can pass this in the ``plot_missing()`` method to create these visualization types:

        1. bar (default) 
        2. heatmap    
        3. matrix    
        4. dendrogram

Example:

    MissingnessVisualizer(df).plot_missing(viz_type = 'matrix') -> Creates a Matrix Plot 

- **title** -> Represents Title of the plot. 

Example:

    MissingnessVisualizer(df).plot_missing(title = 'Bar Plot of Missing Data') -> Sets title as 'Bar Plot of Missing Data'

- **title_fontsize** -> We can make the Title of our plot bigger or smaller with this. **(default is 26)**

Example:

    MissingnessVisualizer(df).plot_missing(title = 'Bar Plot of Missing Data', title_fontsize = 26) -> Title size set to 26.

- **title_padding** -> This means how much space must be allowed around the title. **(default is 20)**

Example:

    # this is what padding looks like:

                                                                <PADDING>

    <PADDING>    MissingnessVisualizer(df).plot_missing(title = 'Bar Plot of Missing Data', title_fontsize = 26, title_padding = 20)   <PADDING>

                                                                <PADDING>

- **xlabel** - Label for x-axis. (**when you are walking on the road, you're moving on x-axis**)

Example:

    MissingnessVisualizer(df).plot_missing(xlabel = 'Columns') -> x-axis named as 'Columns' (like in examples above!)

- **xlabel_fontsize** - Represents how big or small should be my x-axis label. **(default is 15)**

Example:

    MissingnessVisualizer(df).plot_missing(xlabel = 'Columns', xlabel_fontsize = 15) -> (like in examples above!)

- **xlabel_padding** - This means how much space must be free around the label of x-axis. **(default is 15)**

Example:

    MissingnessVisualizer(df).plot_missing(xlabel = 'Columns', xlabel_fontsize = 15, xlabel_padding = 15) -> (like in examples above!)

- **ylabel** - Label for y-axis. (**when a lift is taking you up or down, you're moving in y-axis**)

Example:

    MissingnessVisualizer(df).plot_missing(ylabel = 'Total values in a column') -> Y-axis label set to 'Total values in a column'

- **ylabel_fontsize** - Represents how big or small should be my y-axis label. **(default is 15)**
   
Example:

    MissingnessVisualizer(df).plot_missing(ylabel = 'Total values in a column', ylabel_fontsize = 15) -> Y-axis label size set to 15.

- **ylabel_padding** - This means how much space must be free around the label of y-axis. **(default is 15)**

Example:

    MissingnessVisualizer(df).plot_missing(ylabel = 'Total values in a column', ylabel_fontsize = 15, ylabel_padding = 15) -> (like in examples above!)

**Phewwww...**

**That was a lot.**

