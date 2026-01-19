![DataLab logo](DataLab_logo_images/DataLab_logo.png)

# 📊 DataLab (v0.1 Pre-Release)

A beginner-friendly Python library for understanding, diagnosing, and preparing real-world data.

## What is DataLab?

DataLab is a **Python** library designed to make data understanding, diagnosis, cleaning, and preprocessing **intentional, explainable, and beginner-safe** - without sacrificing correctness or performance.

It is built for:

- Beginners learning data science

- Students from non-technical backgrounds

- Analysts and researchers

- Data scientists who want a structured, unified workflow

- Anyone who wants well-understood data before analysis or modeling

DataLab focuses on building strong data foundations:

- **Tabular Data** (v0.1 -> v0.2)

- **Graph Data** (coming v0.3)

- **Machine Learning** (coming v0.4+)

**Goal:**

Provide a single, guided ecosystem for understanding and preparing data - with simple APIs, strong defaults, and human-friendly documentation.

## What makes DataLab different?

Real-world data is messy. Often, numbers aren’t really numbers, text has hidden symbols, units, or placeholders, and missing values are everywhere.  

Most libraries assume your data is already clean - DataLab doesn’t.

Instead, it helps you **see what’s really in your data** before taking action:

- Detect hidden formatting issues and inconsistencies  
- Reveal missing values and patterns  
- Identify outliers and extreme values  
- Understand skewness and distributions  

By **visualizing and explaining the data first**, you make safer cleaning decisions, avoid silent mistakes, and build a solid foundation for analysis or modeling.

## How DataLab Works

DataLab is built around a simple idea:

``Different types of data need different ways of thinking.``

With DataLab, you can:

- Automatically detect column types (numerical, categorical, datetime)

- Run type-specific workflows instead of one-size-fits-all functions

- Diagnose, clean, preprocess, and visualize data independently

- Focus on understanding data behavior before taking action

By separating workflows by data type, DataLab keeps **analysis clear, structured, and beginner-safe - while remaining powerful for advanced users**.

## Current Version: v0.1 (Pre-Release)

This early release focuses on **Tabular Data**, including:

- Data loading

- Data diagnosis

- Missingness analysis

- Numerical & categorical workflows

- Cleaning and preprocessing

- Computation

- **Matplotlib**-based visualizations (including missingness plots)

- Beginner-friendly documentation, API guides, and workflow notebooks

DataLab currently supports **Pandas** and partially **Polars** (used internally for performance in few methods).

## Installation (v0.1 Pre-Release)

DataLab is available on **TestPyPI** for early testing and feedback.

This allows you to try DataLab without cloning the repository.

You can now Install DataLab pre-release using **pip**:

``pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple datalab-pre-release==0.1.0a4``

### Why this long command? 

That is because DataLab itself is downloaded from TestPyPI, while required dependencies (such as pandas) are downloaded from **PyPI**.

### Importing DataLab

You can simply import datalab after installing it like this:

        import datalab

### Installation Video:

A short **Installation & Getting Started** video is available below:

👉 https://youtu.be/RC4SzXxRSHk 

### Updating to the Latest TestPyPI Version

If you already installed an earlier pre-release version of DataLab from TestPyPI, you can upgrade to the latest test version using:

``pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple datalab-pre-release``

This ensures you always get the most recent pre-release version available on TestPyPI.

**⚠️ Note:**

This is a pre-release version and is not yet intended for production use.

## Project Structure:

```
datalab/
│
├── datalab/                    # Main Python package
│   ├── tabular/
│   │   ├── data_loader/
│   │   ├── data_diagnosis/
│   │   ├── data_cleaning/
│   │   ├── data_preprocessing/
│   │   ├── computations/
│   │   ├── data_visualization/
│   │   ├── data_analysis/      # (To be added in v0.2)
│   │   ├── machine_learning/   # (To be added in v0.4)
│   │   └── utils/
│   │
│   └── graph/                  # (To be added in v0.3)
│
├── docs/                       # Beginner-friendly documentation (includes Interpretation Guides)
│
├── guides/               # API Usage & Workflow Guide notebooks for each step
│
├── pyproject.toml
├── requirements.txt
├── LICENSE
└── README.md
```

## Features in v0.1:

**✔️ 1. Data Loading**

- CSV, Excel, JSON and Parquet support

- Automatic file type detection

**✔️ 2. Data Diagnosis**

- Dataset overview (shape, columns, dtypes, memory usage)

- Column type detection

- Cardinality and duplicate detection

- Numerical & categorical diagnosis

- Dirty data diagnosis

**✔️ 3. Missingness Diagnosis and Visualization**

- Missing value statistics

- Pattern analysis

- Missing Data Plots (via **missingno**)

**✔️ 4. Cleaning & Preprocessing**

- Numerical, categorical, and basic text workflows

- Missing data handling (guided)

- Pandas <-> Polars utilities

**✔️ 5. Computation**

- Descriptive statistics

- Distribution analysis

- Outlier detection

- Correlation

- Performance-optimized helpers

**✔️ 6. Visualization**

- Histograms

- Boxplots

- KDE plots

- QQ Plots

- Categorical visualizations (bar charts, line plots etc.)

- Missingness visualizations (bar charts, matrix, heatmaps and dendrograms)

**✔️ 7. Documentation & Workflow Guides**

- Friendly documentation

- Beginner-first explanations

- Visual examples

- Step-by-step workflows

- Conceptual guides explaining **why, not just how**

## 🧭 Roadmap:

**v0.1**

- Tabular base
- Diagnosis
- Cleaning
- Preprocessing
- Computation
- Viz + Docs
- Usage Notebooks
- Workflow Notebooks
  
**v0.2**

- Text workflows
- More computation tools
- Included analysis
- Improved tabular viz
- More diagnosis tools
- Improved cleaning & preprocessing
  
**v0.3**

- Graph Data Package
- Using igraph (fast) with optional NetworkX converters

**v0.4**

- Machine Learning (sklearn workflows)
  
**v0.5**

- Full library review + stability
  
## Why would I even use DataLab?

Because most data problems don’t come from bad models - **they come from poor data understanding**.

DataLab is built to feel like:

> Someone sitting next to you, explaining what your data is doing and why.

DataLab is built with:

- Conceptual understanding before automation

- Real-world messy data

- Clear explanations and safe defaults

- Modular, reusable workflows

- Performance without complexity

If you’re new to data… OR switching careers… OR want to understand data deeply…

**DataLab is built for you.**

## 🤝 Contributions

DataLab is currently in early development stage.

Suggestions, ideas, feedbacks and contributions are absolutely welcome!

## ✉️ Contact & Support

For questions, suggestions, feedbacks or issues related to **DataLab**, you can reach us at:

**Email:** [datalab.project@protonmail.com](mailto:datalab.project@protonmail.com)

Even though it is a pre-release, we still aim to respond within 72 hours.

## ⚠️ AI Usage Disclosure

AI tools were used selectively during the development of DataLab to:

- Learn and clarify data concepts.
- Explore alternative implementation approaches and edge cases.
- Generate realistic, messy datasets to simulate real-world data scenarios for testing, research, and validation.

All core design decisions, code implementation, documentation, visualizations, and examples were written, reviewed, and integrated by the author.

AI was used as a **support and learning tool** - **not as a replacement for thinking, understanding, authorship, or ownership.**

