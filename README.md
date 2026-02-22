![datalabx logo](assets/datalabx_logo.png)

[![API Docs](https://img.shields.io/badge/API-Documentation-blue)](https://theducky-2.github.io/datalabx)
![TestPyPI version](https://img.shields.io/badge/TestPyPI-0.1.0b9-orange)
![Status](https://img.shields.io/badge/Status-Beta-yellow)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/github/license/TheDucky-2/datalabx)

**A diagnosis-first data quality and preparation framework for real-world data.**

DataLabX is a Python library designed to help you understand, diagnose, and safely prepare messy datasets - before analysis or modeling.

Most data failures don’t happen during modeling.
They happen earlier: **during data understanding, cleaning, and unsafe transformations.**

DataLabX exists to fix that.

## What is DataLabX?

**DataLabX is a structured framework for working with messy, real-world data.**

It is designed for datasets where:

- Values are inconsistent, invalid, or misleading

- Missing data appears in many hidden forms

- Column types are unclear or mixed

- Blind automation is risky

Instead of guessing or silently coercing data, datalabx focuses on:

- **Clarity**

- **Control**

- **Explainability**

datalabx helps you understand what your data is doing before deciding what to do with it.

## Who is DataLabX for?

DataLabX is built for:

- Analysts & Data Scientists working with messy, real-world datasets

- Researchers & Engineers needing structured data diagnostics

- Beginners who want safe, guided workflows

- Advanced users who want transparency instead of black boxes

**If you care about well-understood data, DataLabX is for you.**

## Core Philosophy

**Diagnosis-first, not automation-first.**

``DataLabX assumes that your data is dirty by default.``

Instead of hiding problems, it:

- detects them

- explains them

- lets you decide what to do

DataLabX is built around a simple idea: 

> Different data types need different thinking

DataLabX separates workflows by data type:

- Numerical

- Categorical

- Text

- Datetime

- (Graph data coming soon)

This keeps workflows:

- **clear**

- **safe**

- **reproducible**

## What makes DataLabX different?

- Designed for extremely messy datasets **(≈77–90% invalid or inconsistent values)**

- Tested on datasets with **5-10 million rows**

- **Type-aware** diagnosis and cleaning

- **Regex-based detection** of hidden issues

- Structured, **beginner-safe APIs**

- Human-friendly documentation

DataLabX combines:

- **power for advanced users**

- **safety and clarity for beginners**

## How DataLabX Works

With DataLabX, you typically:

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

DataLabX is available on **TestPyPI** for early testing and feedback.

You can now Install datalabx pre-release using **pip**:

``pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple datalab-pre-release==0.1.0b9``

### Why this long command? 

That is because DataLabX itself is downloaded from TestPyPI, while required dependencies (such as pandas) are downloaded from **PyPI**.

### Importing DataLabX
```python
import datalab
```

### Installation Video

**Installation and Getting Started Video**

👉 https://youtu.be/RC4SzXxRSHk 

### Updating to the Latest TestPyPI Version

If you already installed an earlier pre-release version of datalabx from TestPyPI, you can upgrade to the latest test version using:

``pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple datalab-pre-release``

This ensures you always get the most recent pre-release version available on TestPyPI.

**⚠️ Note:**

This is a pre-release version and is not yet intended for production use.

## Project Structure:

```
datalabx/
│
├── datalabx/                # Main Python package
│   ├── tabular/
│   │   ├── data_loader/
│   │   ├── data_diagnosis/
│   │   ├── data_cleaning/
│   │   ├── data_preprocessing/
│   │   ├── computations/
│   │   ├── data_visualization/
│   │   ├── data_analysis/         # (To be added in v0.2)
│   │   └── utils/
│   │
│   └── graph/              # (To be added in v0.3)
│
├── docs/                 # API documentation
├── foundations/          # datalabx Foundational concepts
├── guides/               # API Usage & Workflow Guide notebooks for each step
├── assets/               # Images, logos, diagrams
│   └── datalabx_logo.png
├── DataLabX_API_RETURN_TYPES.md     # Public API Return Types Reference
├── DataLabX_DATA_HANDLING_POLICY.md # DataLabX's policy on data handling
├── DataLabX_DATA_HANDLING_REPORT.md # DataLabX's current report on data handling
├── CHANGELOG.md                     
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── MANIFEST.in
└── README.md
```

## Features in v0.1:

**✔️ 1. Data Loading** : CSV, Excel, JSON and Parquet, Automatic file type detection.

**✔️ 2. Data Diagnosis** : Shape, columns, dtypes, memory usage, duplicates, cardinality, Numerical & Categorical diagnosis, Dirty data diagnosis.

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

## Why would I even use datalabx?

**Because most data problems don’t come from bad models - they come from poor data understanding.**

DataLabX is built to feel like:

> Someone sitting next to you, explaining what your data is doing and why.

## 🤝 Contributions

DataLabX is in early development. Ideas, feedback, and contributions are absolutely welcome!

If you’d like to contribute, please follow our contribution guidelines:

- **Read the contributing guide:** [CONTRIBUTING.md](CONTRIBUTING.md) ->  explains DataLabX's philosophy, workflow, and how to make meaningful contributions.  
- **Report a bug:** Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md) to submit any issues or unexpected behavior.  
- **Request a feature:** Use the [feature request template](.github/ISSUE_TEMPLATE/feature_request.md) to propose new functionality.  

Following these steps helps ensure your contributions align with datalabx’s diagnosis-first philosophy and saves time for both - you and the maintainers.

## ✉️ Contact & Support

For questions, suggestions, feedbacks or issues related to **DataLabX**, you can reach us at:

**Email:** [DataLabX@protonmail.com](mailto:DataLabX@protonmail.com)

We aim to respond within 72 hours.

## ⚠️ AI Usage Disclosure

AI tools were used selectively to:

- clarify concepts

- explore edge cases

- generate realistic messy datasets for testing

All core design, implementation, documentation, and decisions were made by the author.

AI was used as a **support and learning tool** - **not as a replacement for thinking, understanding, authorship, or ownership.**

