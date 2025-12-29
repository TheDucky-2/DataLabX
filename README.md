![DataLab logo](https://github.com/TheDucky-2/DataLab/blob/main/DataLab_logo_images/DataLab_logo.png)

# 📊 DataLab (v0.1 Pre-Release)

A Beginner-Friendly Library for Understanding Data

## What is DataLab?

DataLab v0.1 is a **Python** library designed to make data understanding, diagnosis, cleaning, and preprocessing simple, intuitive, and beginner-friendly — without sacrificing performance.

It is built for:

- Beginners in data science

- Students coming from non-technical backgrounds

- Analysts and researchers

- Data scientists who want a fast, unified workflow

- Anyone who wants clean, reliable, well-diagnosed data before analysis or modeling

DataLab focuses on the foundation of data science:

- Tabular Data (v0.1 -> v0.2)
- Graph Data (coming v0.3)
- Machine Learning (coming v0.4+)
  
**Goal:** 

Bring all essential data tools under one roof, with simple APIs, strong defaults, and friendly documentation.

## How DataLab Works

DataLab makes working with data simple, intuitive and beginner-friendly.

It understands that different types of data - numbers, categories, and date-time need different handling.

With DataLab, you can:

- Automatically detect column types -> No need to check manually

- Run workflows for each data type -> Numerical, Categorical, and Date-Time are handled separately

- Clean, prepare and visualize data independently -> For easy data understanding

- Focus on insights -> Spend your time exploring data, not writing repetitive code.

By handling different types of data separately, DataLab keeps your workflow simple and organized.

That makes it easy for beginners and professionals to explore and understand their data.

## Current Version: v0.1 (Pre-Release)

This is an early development release focusing on the Tabular Data Package, including:

- Data loading

- Data diagnosis

- Missingness analysis

- Numerical & categorical workflows

- Data cleaning

- Preprocessing

- Computation

- **Matplotlib**-based visualization (including Missingness viz)

- Detailed beginner friendly documentation + API usage guides + workflow notebooks

Even in v0.1, DataLab already supports **Pandas** and partially **Polars** (internally used for performance in some methods).

## Installation (v0.1 Pre-Release)

DataLab is currently in early pre-release (v0.1) and is available on TestPyPI for testing and feedback.

This allows you to try DataLab without cloning the repository.

You can now Install DataLab pre-release using **pip**:

``pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple datalab-pre-release==0.1.0a4``

### Why this long command? 

That is because DataLab itself is downloaded from TestPyPI, while required dependencies (such as pandas) are downloaded from PyPI.

### Importing DataLab

You can simply import datalab after installing it like this:

        import datalab

### Installation Video:

You can also watch the 4-minute **Installation & Getting-Started with DataLab** video on Youtube, using the link below:

👉 https://youtu.be/RC4SzXxRSHk 

### Updating to the Latest TestPyPI Version

If you already installed an earlier pre-release version of DataLab from TestPyPI, you can upgrade to the latest test version using:

``pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple datalab-pre-release``

This ensures you always get the most recent pre-release version available on TestPyPI.

**⚠️ Note:**

The library is not yet ready for production use.

Editable development installation instructions will be added once the API stabilizes.

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

DataLab automatically detects and loads:

- csv files

- Excel files (xlsx, xls)

- JSON

- Parquet files

**✔️ 2. Data Diagnosis**

Understand your dataset in minutes:

- Data preview

- Shape, columns, dtypes

- Index info

- Memory usage

- Column type detection (numerical, categorical, datetime)

- Cardinality

- Duplicate detection

- Numerical & Categorical Data diagnosis

**✔️ 3. Missingness Diagnosis and Visualization**

Uses **missingno** internally to visualize:

- Missingness Stats

- Missing value patterns

- Missingness Heatmaps

- Missingness distributions

**✔️ 4. Cleaning & Preprocessing**

DataLab offers Cleaning and Preprocessing for:

- Numerical Data

- Categorical Data

- Datetime Data (in v0.2)

- Missing Data

- Text (basic)

- Pandas <-> Polars conversion utilities

**✔️ 5. Computation**

Includes:

- Statistics

- Distributions

- Outlier detection

- Correlation

- Performance-optimized helpers

- Early Polars-based computation engine

**✔️ 6. Visualization**

Simple, beginner-friendly plots using Matplotlib:

- Histograms

- Boxplots

- Kernel Density Estimation Plot

- Missingness viz (via missingno)

- Categorical Data viz

✔️ 7. Documentation & Workflow Guides

DataLab includes:

- Friendly documentation

- Visual examples

- Step-by-step workflows

- Guides explaining why and how, not just how to code

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
  
**v0.6 -> v1.0**

- Deep Learning (PyTorch + JAX optimizations)
- GNNs / GATs (Graph Neural Networks using PyG)
- Complete Tabular + Graph Ecosystem
- Backend auto-selection (Polars/Pandas)
  
## Why would I even use DataLab?

Because DataLab goes by the philosophy that data science should feel like someone is sitting next to you, guiding you step-by-step.

DataLab is built with:

- Beginner-friendly language

- Real-world messy data testing

- Clean modular engineering

- Reusable workflows

- Performance in mind

- Clear explanations

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

AI was used as a support and learning tool - not as a replacement for thinking, understanding, authorship, or ownership of the library.

