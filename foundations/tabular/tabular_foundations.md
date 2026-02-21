# ▦ Tabular Foundations

Tabular data is the core of most real-world datasets. 

Understanding it thoroughly is critical before any cleaning, analysis, or modeling.

This section of **Foundations** explains how to reason about tabular data - **not just how to use the API.**

It helps us answer questions like:

- What do column types really represent?

- How does dirty data manifest in numerical vs categorical columns?

- Where does missingness occur, and how can it mislead interpretation?

- How do visualizations reflect or distort the true structure of data?

- What decisions are safe to automate, and what needs judgment?

## Structure - Tabular Foundations

```
tabular/
├── data-loading/       # How data enters datalabx and is interpreted
├── data-diagnosis/     # Understanding columns, types, duplicates, and dirty data
└── missingness/        # Diagnosis, visualization, and handling of missing values
    ├── What_is_Missingness.md        # Key concepts and terminology
    ├── diagnosis       # Detecting missing data and patterns
    ├── visualization   # Interpreting plots and annotated examples
    └── handling        # Safe strategies to handle missing values
```

Each topic builds intuition for real-world tabular data.

**datalabx provides examples, annotated visualizations, and reasoning guidance to help you make safe, informed decisions.**

## How do I get started?

This is how you can get started with **Tabular Foundations**:

- Start with **Data Loading** to understand how data enters datalabx.

- Explore **Data Diagnosis** to see how types, duplicates, and structure are detected.

- Explore **Dirty Data Diagnosis** to recognize common inconsistencies.

- Examine the **Missingness** section to learn about different types of missing data in real-world datasets and how to interpret missingness patterns.

- Review **Visualization** to understand what plots are showing - and what they might hide.

- Choose **Cleaning and Handling** strategies depending on the type of data, the patterns detected, and the insights from diagnosis and visualization.

Other topics such as computations, cleaning, and visualization will be added in future versions of Foundations.  
For the full API reference in the meantime, see [datalabx API Docs](https://theducky-2.github.io/datalabx).


**Reading Tabular Foundations is not about memorizing functions - it’s about learning to see your data clearly.**
