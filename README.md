# 📊 DataLab (v0.1 Pre-Release)

A Friendly, Beginner-Focused Library for Understanding Data

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

## Current Version: v0.1 (Pre-Release)

This is an early development release focusing on the Tabular Data Package, including:

- Data loading

- Data diagnosis

- Missingness analysis

- Numerical & categorical workflows

- Data cleaning

- Preprocessing

- Computation helpers

- **Matplotlib**-based visualization (including Missingness viz)

- Detailed beginner friendly documentation + API usage guides + workflow notebooks

Even in v0.1, DataLab already supports **Pandas** and partially **Polars** (internally used for performance in some methods).

## Installation (Coming Soon)

DataLab is not yet published to PyPI.

The library is currently under active development (v0.1-pre).

Once v0.1 is released, you will be able to install it using:

```pip install datalab```

For now, if you want early access, please clone the repo:

```git clone https://github.com/yourusername/DataLab.git```

```cd DataLab```

## Project Structure:

```
datalab/
│
├── datalab/                    # Main Python package
│   ├── Tabular/
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
│   └── Graph/                  # (To be added in v0.3)
│
├── docs/                       # Beginner-friendly documentation (includes Interpretation Guides)
│
├── guides/               # Workflow notebooks for each step
│
├── pyproject.toml
├── requirements.txt
└── README.md
```

**⚠️ Note:**

The library is not yet ready for production use.

Editable development installation instructions will be added once the API stabilizes.

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

- Numerical & Catgeorical Data diagnosis

**✔️ 3. Missingness Diagnosis and Visualization**

Uses **missingno** internally to visualize:

- Missingness Stats

- Missing value patterns

- Missingness Heatmaps

- Missingness distributions

✔️ 4. Cleaning & Preprocessing

DataLab offers Cleaning and Preprocessing for:

- Numerical Data

- Categorical Data

- Datetime Data (in v0.2)

- Missing value handling

- Text (basic)

- Pandas <-> Polars conversion utilities

**✔️ 5. Computation Helpers**

Includes:

- Statistics

- Distributions

- Outlier detection

- Performance-optimized helpers

- Early Polars-based computation engine

**✔️ 6. Visualization**

Simple, beginner-friendly plots using Matplotlib:

- Histograms

- Boxplots

- KDE Plot

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
- Usage notebooks
  
**v0.2**

- Text workflows
- More computation tools
- Include analysis
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
- Complete tabular + graph ecosystem
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

DataLab is in early development stage.

Suggestions, ideas, feedbacks and contributions are absolutely welcome!
