![DataLab logo](assets/DataLab_logo.png)

# 📊 DataLab
[![API Docs](https://img.shields.io/badge/API-Documentation-blue)](https://theducky-2.github.io/DataLab)
![TestPyPI version](https://img.shields.io/badge/TestPyPI-0.1.0b6-orange)
![Status](https://img.shields.io/badge/Status-Beta-yellow)
![Python](https://img.shields.io/badge/python-3.12+-blue)
![License](https://img.shields.io/github/license/TheDucky-2/DataLab)

**A diagnosis-first data quality and preparation framework for real-world data.**

DataLab is a Python library designed to help you understand, diagnose, and safely prepare messy datasets - before analysis or modeling.

Most data failures don’t happen during modeling.
They happen earlier: **during data understanding, cleaning, and unsafe transformations.**

DataLab exists to fix that.

## What is DataLab?

**DataLab is a structured framework for working with messy, real-world data.**

It is designed for datasets where:

- Values are inconsistent, invalid, or misleading

- Missing data appears in many hidden forms

- Column types are unclear or mixed

- Blind automation is risky

Instead of guessing or silently coercing data, DataLab focuses on:

- **Clarity**

- **Control**

- **Explainability**

DataLab helps you understand what your data is doing before deciding what to do with it.

## Who is DataLab for?

DataLab is built for:

- Analysts & Data Scientists working with messy, real-world datasets

- Researchers & Engineers needing structured data diagnostics

- Beginners who want safe, guided workflows

- Advanced users who want transparency instead of black boxes

**If you care about well-understood data, DataLab is for you.**

## Core Philosophy

**Diagnosis-first, not automation-first.**

``DataLab assumes that your data is dirty by default.``

Instead of hiding problems, it:

- detects them

- explains them

- lets you decide what to do

DataLab is built around a simple idea: 

> Different data types need different thinking

DataLab separates workflows by data type:

- Numerical

- Categorical

- Text

- Datetime

- (Graph data coming soon)

This keeps workflows:

- **clear**

- **safe**

- **reproducible**

## What makes DataLab different?

- Designed for extremely messy datasets **(≈77–90% invalid or inconsistent values)**

- Tested on datasets with **5-10 million rows**

- **Type-aware** diagnosis and cleaning

- **Regex-based detection** of hidden issues

- Structured, **beginner-safe APIs**

- Human-friendly documentation

DataLab combines:

- **power for advanced users**

- **safety and clarity for beginners**

## How DataLab Works

With DataLab, you typically:

- Load data

- Diagnose structure, types, and issues

- Analyze missingness and inconsistencies

- Apply type-specific cleaning & preprocessing

- Compute statistics and distributions

- Visualize behavior and patterns

**Each step is explicit, modular, and explainable.**

## Current Version: v0.1 (Pre-Release)

#### Focus in v0.1

Tabular data workflows, including:

- Data loading (CSV, Excel, JSON, Parquet)

- Data diagnosis & dirty data detection

- Missingness analysis & visualization

- Numerical & categorical workflows

- Cleaning & preprocessing

- Statistical computations

- Matplotlib-based visualizations

- Beginner-friendly documentation & workflow guides

**Pandas** is fully supported.
**Polars** is used internally for performance in selected components.

## Installation (v0.1 Pre-Release)

DataLab is available on **TestPyPI** for early testing and feedback.

You can now Install DataLab pre-release using **pip**:

``pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple datalab-pre-release==0.1.0b6``

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

**v0.1** - Tabular data foundations

**v0.2** - Text workflows & advanced analysis

**v0.3** - Graph data workflows

**v0.4** - Machine learning workflows

**v0.5** - API review & stabilization

## Why would I even use DataLab?

**Because most data problems don’t come from bad models - they come from poor data understanding.**

DataLab is built to feel like:

> Someone sitting next to you, explaining what your data is doing — and why.

## 🤝 Contributions

DataLab is in early development.
Ideas, feedback, and contributions are absolutely welcome!

## ✉️ Contact & Support

For questions, suggestions, feedbacks or issues related to **DataLab**, you can reach us at:

**Email:** [datalab.project@protonmail.com](mailto:datalab.project@protonmail.com)

We aim to respond within 72 hours.

## ⚠️ AI Usage Disclosure

AI tools were used selectively to:

- clarify concepts

- explore edge cases

- generate realistic messy datasets for testing

All core design, implementation, documentation, and decisions were made by the author.

AI was used as a **support and learning tool** - **not as a replacement for thinking, understanding, authorship, or ownership.**

