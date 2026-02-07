# Step 7: Understanding Distributions

We are now at the first step of understanding our data.

## What is a Distribution?

Imagine it’s your birthday, and you have a bag of candies.

Assuming there are a total of 60 people including teachers, you give 1-1 candy to each student in your class.

Then, you give a few extra candies to your close friends and your teachers.

If we write down how many candies each person got, it might look like this:

| Person        | Candies |
|---------------|---------|
| Student 1     | 1       |
| Student 2     | 1       |
| Student 3     | 1       |
| More students | 1       |
| Friend 1      | 3       |
| Friend 2      | 4       |
| Teachers      | 5       |

We now know:

- Most people got 1 candy on an average.

- A few people got more and these are the extreme values.

This table of candies shows the distribution - who got what and how often.

``A distribution is simply how things are distributed or shared among a group.``

## Examples:

Let us see what our above example looks like visually:

### Distribution of People

1. Let us first see a distribution of people.

**Example:**

![Example Histogram](/assets/docs/tabular/Missingness/Missingness_Handling/Example_histogram.png)

We can see that out of 60 people:

- We have 47 Students.

- 8 students who are Friends

- 5 Teachers

We can see categories of people present (Students, Friends, Teachers) and number of people present in each category.

### Distribution of Candies

2. Let us now see a distribution of candies

**Example:**

![Example Histogram](/assets/docs/tabular/Missingness/Missingness_Handling/Example_histogram2.png)

We can see:

- We distributed 1 candy to 47 people.

- 2 candies to 0 people.

- 3 candies to 4 people

- 4 candies to 4 people.

- 5 candies to 3 people.

- 6 candies to 2 people.

We can see the number of candies [1,2,3,4,5,6] distributed among the number of people [47, 0, 4, 4, 3, 2]

**This is an example of Distribution**.

## But, why does the Distribution matter?

Like we can see in the example above, looking at a distribution helps us understand our data before doing anything else, including handling missing data.

It helps us answer questions like:

- Are most of the values close to each other/similar or very different?

- Are there any unusual or extreme values?

- Is the data leaning more to one side, or is it balanced? (we will explore this soon)

In our candy example, most people got 1 candy in average and a few got more, which is rare but possible.

This same idea applies to numbers in a dataset whether it is ages, incomes, test scores, or measurements.

## Types of Distributions

Distributions can look different **depending on the data**. 

However, we will focus on two main types:

1. **Normal Distribution**
2. **Non-Normal Distribution**

### **Normal Distribution** (Using the Candy Example)

Imagine, we now have a different birthday in a different class.

This time, we decide to give candies more evenly.

- Most students get 2 candies on an average.
- Some students get 1 candy.
- Some students get 3 candies.
- Very few students get 0 candies or 4 candies.

Let us look at this visually to understand:

![Normal Distribution](/assets/docs/tabular/Missingness/Missingness_Handling/Example_histogram3.png)

We can see:

- 40 people got 2 candies on an average (middle)

- 12 people got 1 candy 

- 12 people got 3 candies. 

- 3 people were not fond of candies, so they got 0 candies (rare).

- 3 people took 4 candies (rare).

As we move away from 2 candies (middle), fewer and fewer students appear.

This pattern is called a **normal distribution**.

We now know:

- Most people received a similar amount

- Very small or very large amounts are rare

- The data feels balanced and symmetrical (right side looks like a copy of the left)

Because of this balance, the average number of candies represents most students pretty well.

In other words, ``a distribution is Normal when most values are near the middle, and extreme values happen rarely.``

### **Non-Normal Distribution** (Using the Candy Example)

Let us go back look to our original example:

- We gave 1 candy to most students.
- A few extra candies to our close friends.
- We gave even more candies to the teachers.

Let us understand that visually:

![Example Histogram](/assets/docs/tabular/Missingness/Missingness_Handling/Example_histogram2.png)

We can see:

- Values are not balanced out on both sides like **normal distribution**.

- Most values are piling up in one place, and a few values are very different.

Because a few people got many candies, the average number of candies moves away from where most people are.

The average becomes higher than 1, even though most people only received 1 candy.

In this case, the data is extending to the right, because a few people receiving many candies is pulling the values in one direction.

This kind of pattern is called a **non-normal distribution**.

In other words, ``a distribution is non-normal when most values are the same, and only a few values are much larger or smaller.``

## Summary:

- A distribution shows how values are shared or spread across a group.

- Looking at distributions helps us understand data before any kind of analysis including handling missing values.

- Some distributions are normal, where most values are near the middle and extremes are rare.

- Some distributions are non-normal, where most values make a group in one place and a few extreme values pull the average value to left or right.

- Understanding distributions helps us know whether most values actually look similar or different.
