---
name: Bug Report
about: Report an unexpected behavior you observed in DataLab (pre-release)
title: "[BUG]"
labels: bug
assignees: 
---

![DataLab Logo](../../assets/DataLab_logo.png)

# 🐞 Bug Report

Please fill out the sections below to help us reproduce and fix the issues related to DataLab.

---

## Describe the bug

A clear and concise description of what the bug is.

**Example:**

> DataLab is throwing an error while converting cleaned numerical data into numerical datatypes.

## To Reproduce

Steps to reproduce the behavior (minimal reproducible example preferred):

1. Import datalab
2. Run specific code
3. Observe unexpected output

```python
# Example code that triggers the bug
import datalab

# Your code here
```

## Expected behavior

What you expected will happen.

**Example:**

> DataLab should return a pandas DataFrame with all columns having **string** datatype while loading data from CSV files.

## Screenshots / Output:

Include traceback, screenshots, or logs if applicable.
If possible, copy and paste the full Python error traceback.

## Environment

- DataLab version: (run ``python -c "import datalab; print(datalab.__version__)"``)
- Python version: 
- OS:
- Additional packages / versions (if relevant):

## Additional context

Any other information that might help diagnose the problem, e.g., dataset specifics, unusual file formats, edge cases, etc.
