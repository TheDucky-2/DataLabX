# Step 6: Understanding the Data
## **A Short Preview Before Handling Missing Values**

So far, we have learned a lot about what is Missingness (Missing data) and how it looks like.

We now know: 

- Which values count as missing (pandas built-in + placeholders).

- Which missing values exist in which columns. 

- How missing data can be explored in rows and columns.

- How different pairs or groups of columns may be missing data together.

However, before we decide what to do with those missing values, we need to understand something even more important:

**What does the data itself look like when it is wholly present along with missing values?**

Because missing values do not exist in isolation by themselves, they exist within real data - numbers, categories, dates, and text.

If we don’t understand that data first, any action we take on missing values would just be guesswork.

## But, what does 'Understanding the Data' mean?

Understanding the data does not mean cleaning our data or making any changes to it.

It simply means **observing and understanding how values behave**.

Example:

- Are most values in a column same or are they very different?

- Are values evenly spread out or are they piling up in one place?

- Are there values in a column that appear very rarely?

- Are there values that look extremely large or extremely small compared to the rest?

These questions actually help us understand the shape and behavior of our data.

In DataLab, this understanding comes from ``Data Diagnosis`` and ``Data Visualization``.

Behind the scenes, this involves mathematical computations like counts, summaries, and statistics - but as a user, you don’t need to think about those yet.

You will mostly see the results, not the calculations themselves.

## How is this related to Missing Data?

Imagine we went out and asked for age and income of 20 people we met randomly.

Let's say this is the data we get:

| Row | Age | Income |
|-----|-----|--------|
| 1   | 22  | 32000  |
| 2   | 25  | 34000  |
| 3   | 27  | 27000  |
| 4   | 29  | 36000  |
| 5   | 31  |   -    |
| 6   | 33  | 38000  |
| 7   | 35  | 40000  |
| 8   | 16  |   0    |
| 9   | 39  | 42000  |
| 10  | 41  | 45000  |
| 11  | 43  |  NaN   |
| 12  | 45  | 48000  |
| 13  | 47  |  NaN   |
| 14  | 49  | 750000 |
| 15  | 52  |  NaN   |
| 16  | 43  |  NaN   |
| 17  | 45  | 48000  |
| 18  | 47  | 500000 |
| 19  | 49  | 750000 |
| 20  | 52  | 1000000|


We can see that out of these 20 rows:

- Incomes of 10 people fall within a range, let's say between 20,000 and 50,000.

- We met 4 people with incomes that are very large, like 500,000 - 1,000,000.

- We met 6 people who chose not to share their income and due to that, some values are missing. 

We know that income of 10 people in our data is between 20,000 - 50,000, 6 people did not answer and only 4 people had incomes between 500,000 - 1,000,000

However, the average income is coming out to be 226,000. 

Now, saying that 'Average income of these 20 people is 226,000' **would be misleading**.

That is because it is giving us a sense that everyone is earning around 226,000, but we know that most people are earning between 20,000 - 50,000.

``In order to ensure we avoid situations like this during missing data handling, this step exists.``

## What will we explore Ahead?

In this section, we will be exploring very simple concepts like:

- How values are distributed in a column

- Whether values lean more toward one side

- Whether some values are unusually large or small

- How often values appear

We will be working with **Diagnosis** and **Visualization** modules from DataLab to help us answer these questions. 

We will be learning and understanding these ideas using:

- Beginner-Friendly language

- Visual examples (like the ones in earlier steps)

- Annotated plots 

- DataLab Usage examples

After we finish this section, we will return to Missing Data Handling and complete the workflow with confidence.