![DataLab logo](assets/DataLab_logo.png)

# 📊 DataLab - Pre-Release
[![API Docs](https://img.shields.io/badge/API-Documentation-blue)](https://theducky-2.github.io/DataLab)
![TestPyPI version](https://img.shields.io/badge/TestPyPI-0.1.0b4-orange)
![Status](https://img.shields.io/badge/Status-Beta-yellow)
![Python](https://img.shields.io/badge/python-3.12+-blue)
![License](https://img.shields.io/github/license/TheDucky-2/DataLab)

A diagnosis-first **data quality and preparation framework**, implemented as a Python library.

It is designed for working with messy, **real-world datasets**where most failures occur before modeling - during data understanding, cleaning, and unsafe transformations.

## What is DataLab?

DataLab is a **Python framework** exposed as a library designed for **serious, real-world data analysis**.

It is designed for extremely messy datasets **(≈77–90% invalid or inconsistent values)** and scales to millions of rows, while providing a **structured, well-documented, and beginner-safe API**.

The focus is on **clarity and control over data behavior**, not blind automation.

It is built for:

- Analysts and data scientists working with messy, real-world datasets

- Researchers and engineers needing structured data diagnostics

- Anyone who wants well-understood data before analysis or modeling

DataLab focuses on building strong data foundations:

- **Tabular Data** (v0.1 -> v0.2)

- **Graph Data** (coming v0.3)

- **Machine Learning** (coming v0.4+)

**Goal:**

Provide a single, guided ecosystem for understanding and preparing data - with simple APIs, strong defaults, and human-friendly documentation.

## What makes DataLab different?

Real-world data is messy. 

Numbers may not be numeric, text can hide symbols or replacements, and missing data often comes in many forms.

``DataLab assumes your data is dirty by default.``

It allows:

- Full, type-aware detection of numerical, categorical, and datetime columns

- Regex-based diagnostics for hidden issues

DataLab has been designed and tested on extremely dirty datasets **(~5-10 million rows)**.

This allows safe, intentional, and reproducible workflows.

DataLab combines power for advanced users with accessibility for beginners, ensuring workflows are safe, structured, and explainable.

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

DataLab currently supports **Pandas** and partially **Polars** (used internally for performance in Dirty Data Diagnosis and Cleaning).

## Installation (v0.1 Pre-Release)

DataLab is available on **TestPyPI** for early testing and feedback.

You can now Install DataLab pre-release using **pip**:

``pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple datalab-pre-release==0.1.0b4``

### Why this long command? 

That is because DataLab itself is downloaded from TestPyPI, while required dependencies (such as pandas) are downloaded from **PyPI**.

### Importing DataLab
```python
import datalab
```

### Installation Video

**Installation and Getting Started Video**

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

**✔️ 1. Data Loading** : CSV, Excel, JSON and Parquet, Automatic file type detection.

**✔️ 2. Data Diagnosis** : shape, columns, dtypes, memory usage, duplicates, cardinality, Numerical & Categorical diagnosis, Dirty data diagnosis.

**✔️ 3. Missingness Diagnosis and Visualization** : Missing data stats, Pattern analysis, Missing data plots (via **missingno**).

**✔️ 4. Cleaning & Preprocessing** : Numerical and Categorical workflows, Missing data handling.

**✔️ 5. Computation** : Descriptive stats, distribution, outliers detection, correlation.

**✔️ 6. Visualization** : Histograms, Boxplots, KDE, QQ plots, categorical plots, missingness plots(using **missingno**).

**✔️ 7. Documentation & Workflow Guides** : Friendly documentation, visual examples, workflow guides explaining **why, not just how**.

## 🧭 Roadmap:

**v0.1**: Tabular base, diagnosis, cleaning, preprocessing, computation, visualizations, workflow guides.

**v0.2**: Text workflows, improved analysis & visualization, advanced cleaning.

**v0.3**: Graph Data Package (igraph, NetworkX).

**v0.4**: Machine Learning workflows (sklearn).

**v0.5**: Full library review & stability


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

If you’re new to data... OR an expert... OR... just want well understood data

**DataLab is built for you**.

## 🤝 Contributions

DataLab is currently in early development stage.

Suggestions, ideas, feedbacks and contributions are absolutely welcome!

## ✉️ Contact & Support

For questions, suggestions, feedbacks or issues related to **DataLab**, you can reach us at:

**Email:** [datalab.project@protonmail.com](mailto:datalab.project@protonmail.com)

Even though it is a pre-release, we still aim to respond within 72 hours.

## ⚠️ AI Usage Disclosure

AI tools were used selectively during the development of DataLab to:

- Clarify data concepts.
- Explore alternative implementation approaches and edge cases.
- Generate realistic, messy datasets to simulate real-world data scenarios for testing, research, and validation.

All core design decisions, code implementation, documentation, visualizations, and examples were written, reviewed, and integrated by the author.

AI was used as a **support and learning tool** - **not as a replacement for thinking, understanding, authorship, or ownership.**

