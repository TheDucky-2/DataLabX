![DataLab logo](/assets/DataLab_logo.png)

# How DataLab Thinks About Data Changes

This document exists to communicate how DataLab thinks about **data, changes, and safety**.

It is written in **plain language** and is meant to be readable even if you are new to data work.

You do not need to know anything about internal libraries, backends, or implementation details to understand this document.

---

## Why this document exists

Most problems with real-world data do not come from broken code. They come from **wrong assumptions about what the data means**.

Many tools change how data is stored or represented without clearly explaining whether the **meaning** of the data has changed.

This makes it really hard to know when the data is safe to trust.

This document exists to make one thing very clear:

> **DataLab is designed to preserve what your data means.**

Everything else follows from that idea.

---

## Two really important ideas -> Meaning and Representation

When working with data, it helps to separate two concepts:

### 1. Data Meaning

**Meaning** is what the data represents in the real world.

This includes:

- Actual values present in a dataset
- Whether a value is missing or present
- Categories and labels
- How rows and columns relate to each other
- How the data should be interpreted

``"If the meaning changes, then the data itself has changed."``

---

### 2. Data Representation

**Representation** is how that meaning is stored or expressed inside a system.

This includes:

- File formats
- Internal placeholders for missing values **(like NA, nan, None or null)**
- Data types chosen for performance or memory reasons
- Internal layouts used by different tools

> Representation exists to help computers work efficiently. Meaning exists to help humans understand the data.

These two things are related, but they are **not the same**.

---

## What DataLab cares about the most

DataLab always prioritizes **data meaning** over representation.

This means:

- DataLab may change *how* data is stored internally
- but **it should not change what the data represents**

Unless a step is clearly labeled as **cleaning** or **preprocessing**, DataLab treats your data as **observational**.

Observational means:

- Data is being inspected, not altered
- Meaning of data should remain the same
- Results should help you understand the data, not reshape it

---

## What DataLab guarantees

Unless a transformation is **explicitly documented** as cleaning or preprocessing:

- Meaning of your data must remain intact
- Any changes must be explainable
- Silent changes to meaning are not allowed

In simple terms:

> If DataLab changes what your data *means*, it will tell you.

---

## But, when are the changes allowed?

There *are* times when data should change.

These include:

- Cleaning dirty values
- Converting types on purpose
- Preparing data for analysis or modeling

When DataLab does this:

- The step is explicit
- The behavior is documented
- The intent is clear

> Nothing meaning-changing should happen quietly or by accident.

---

## Why this matters in practice

Many confusing data problems happen when representation changes are mistaken for meaning changes, or the other way around.

When this distinction is unclear:

- Missing values appear to change unexpectedly
- Values look different even though their meaning did not change
- Diagnostics become hard to trust
- Small misunderstandings grow into serious errors

DataLab makes this distinction clear so you can reason about your data with confidence.

---

## How this connects back to DataLab’s philosophy

DataLab follows a **diagnosis-first** approach.

This means:

- Understand the data before changing it
- Make assumptions visible
- Prefer clarity over convenience

Understanding **what changed** and **what did not**, is essential to understanding your data.

This document defines the rules that make that understanding possible.
