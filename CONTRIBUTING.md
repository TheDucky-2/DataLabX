![DataLab logo](assets/DataLab_logo.png)

# Contributing to DataLab

First of all: **Thank you so much for considering contributing to DataLab.**

That already means you care about **data quality, correctness, and understanding** - which is exactly why this project exists.

This document is intentionally **opinionated**.

DataLab is a **diagnosis-first framework** built to handle **extremely messy, real-world data** safely and transparently.

Contributions are absolutely welcome, but they must respect that philosophy.

If you are looking to:

- Quickly add features without understanding the core intent of DataLab
- Automate every existing process
- Silently coerce data “to just make it work”

This project may not be a good fit - and that is completely okay.

---

## 📊 What DataLab Is (and Isn't)

Before writing any code, it’s important to understand the core intent of DataLab.

### DataLab **is**:

- Diagnosis-first, not automation-first  
- Explicit over implicit  
- Conservative about transformations  
- Designed for datasets with **very high levels of dirtiness (~77–90%)**  
- Built to *explain* what data is doing before changing it  
- Opinionated about **safety, clarity, and reproducibility**

### DataLab **is not**:

- An auto-cleaning black box  
- A one-liner convenience wrapper that “just works”  
- A modeling or AutoML framework  
- Optimized for easy, clean datasets  
- Designed to silently fix data without surfacing decisions  

If a proposed contribution conflicts with these principles, it will likely be rejected - **even if the code is correct**.

---

## 🧠 Contributor Mindset (This Matters More Than Code)

DataLab treats **data understanding as a first-class problem**. Contributions should reflect that.

Before contributing, ask yourself:

- Does this make data behavior **more visible**?
- Does this reduce ambiguity for the user?
- Does this avoid silent coercion or hidden defaults?
- Can a beginner understand what this does and *why*?
- Would I trust this behavior on a dataset where **90% of values are invalid**?

If the answer to these questions is unclear, the contribution likely needs rethinking.

💡 Questions or partial ideas are welcome - issues are a space for discussion, not just polished proposals.

---

## 🧱 Project Structure & Boundaries

DataLab is intentionally modular and **type-aware**.

### High-level structure

| Sub-Package | Responsibility | Data Mutation Rules |
|------------|----------------|---------------------|
| `data_loader` | Load data without premature type assumptions and preserve dirty values | Loads all values **as strings by default** to prevent silent data type coercion. |
| `data_diagnosis` | Diagnose structure, dirtiness, missingness, and distributions | **Must not modify data** (observational only) |
| `data_cleaning` | Apply explicit, documented cleaning steps | **May transform DataFrames**, but changes must be visible, explainable, and non-silent |
| `data_preprocessing` | Transform data for downstream analysis | **May change datatypes or structure**, but must be intentional, auditable, and reproducible |
| `computations` | Compute descriptive statistics and summaries | **Must not mutate data** |
| `data_visualization` | Produce visualizations only | **Must not mutate data** and must return `None` |

### Important boundaries

1. **Diagnosis modules must never modify data**

- Diagnosis is observational only. 
- These modules may inspect, analyze, and report issues, but they must not change values, dtypes, or structure.

2. **Visualization modules must return None**

- Visualizations are side-effect only (they render plots).
- Visualization modules should not modify data except where **explicitly documented** and required by **third-party visualization constraints** (e.g., ``missingness viz via missingno``).

3. **Cleaning and preprocessing must be explicit and reversible where possible**

- All transformations must be intentional, documented, and inspectable.
- Cleaning functions should avoid silent coercion and allow users to understand, reproduce, or change decisions without losing context.

4. **Public APIs must return documented, stable types**

- Public methods must adhere to the documented return-type contract.
- Any change in return types requires updating documentation and tests.

Breaking these boundaries is considered a **design issue**, not just a bug.

---

## 📐 API Stability & Return Types

DataLab maintains a **public API return-type contract** (see the [DataLab API Return Types reference](DataLab_API_RETURN_TYPES.md)).

Before submitting a PR:

- Ensure return types match the documented API  
- Update the API Return Types reference if behavior changes  
- Add or update tests that enforce return-type guarantees  

Breaking return types without strong justification will block a merge.

---

## 🧪 Testing Philosophy

Testing in DataLab focuses on **correctness, edge cases, and safety** - not just coverage.

Contributions should:

- Include tests for messy and adversarial inputs
- Avoid relying on idealized clean data  
- Explicitly test failure modes and warnings  
- Prefer clarity over clever test setups  

If a feature only works on clean datasets, it is **not ready** for DataLab.

---

## 📝 Documentation Is Not Optional

Documentation is part of the product.

Any change that affects:

- user-facing behavior  
- assumptions  
- defaults  
- return types  

**Must** update:

- docstrings  
- relevant workflow guides  
- API documentation (if public)  

If documentation and code disagree, **documentation wins** until fixed.

---

## 🧩 What Makes a Good First Contribution

If you’re new to the DataLab codebase, **start small**.

The best first contributions improve **clarity, safety, or understanding** without changing core behavior.

Good starting points include:

- Improving error messages, warnings, or logging  
- Clarifying confusing diagnostics or edge cases  
- Fixing incorrect, outdated, or misleading documentation  
- Adding tests that cover messy or unexpected data  
- Small performance improvements that **do not change behavior**

If you’re considering a larger feature or architectural change, please open an issue **before** writing code.

---

## 🔄 How to Contribute to DataLab

Contributing to DataLab is less about adding features quickly and more about making data behavior **clearer, safer, and more understandable**.

Before writing code, contributors are expected to understand **why** a change is needed and how it aligns with DataLab’s diagnosis-first philosophy.

### 1. Start With an Issue

All contributions should begin with an issue.

An issue should clearly explain:

- What problem exists  
- Why it matters for messy, real-world data  
- Which module boundary it belongs to  
- Whether data is observed or transformed  

Feature requests without a clear diagnosis rationale are unlikely to be accepted.

---

### 2. Respect Module Boundaries

Before implementing a change, verify that:

- Diagnosis code does not modify data  
- Visualization code produces side effects only  
- Cleaning and preprocessing steps are explicit and documented  
- Return types remain stable and documented  

Changes that cross module responsibilities should be discussed **before** implementation.

---

### 3. Implement Carefully

When writing code:

- Prefer clarity over cleverness  
- Avoid silent coercion, hidden defaults, or implicit behavior  
- Assume the input data is extremely dirty  
- Make transformations explicit and inspectable  

If behavior could surprise a user, it likely **needs warnings, documentation, or redesign**.

---

### 4. Add Tests for Messy Data

Every contribution should include tests that:

- Cover edge cases and adversarial inputs  
- Avoid relying on clean or idealized datasets  
- Explicitly test failure modes and warnings  
- Enforce documented return types  

A feature that only works on clean data is **not ready** for DataLab.

---

### 5. Update Documentation

Documentation is part of the contribution.

Any change that affects:

- user-facing behavior  
- defaults or assumptions  
- return types  
- workflows  

Must be reflected in relevant docstrings and documentation guides.

If documentation and code disagree, documentation is treated as authoritative until fixed.

---

### 6. Submit a Thoughtful PR

Pull requests should include:

- A clear explanation of intent (not just implementation)  
- A link to the related issue  
- Notes on edge cases, risks, or limitations  
- Confirmation that tests and documentation were updated  

PRs without context or rationale are unlikely to be merged.

---

## Maintainer Review Notes

DataLab is in **pre-release** and prioritizes:

- correctness over velocity  
- safety over convenience  
- understanding over automation  

Not all contributions will be accepted - even well-written ones - **if they conflict with the project’s philosophy.**

Rejections are purely about alignment, not contributor value.

---

## 🤝 Code of Conduct

Be respectful. Be curious. Assume good intent.

DataLab values thoughtful discussion, careful disagreement, and shared learning.

---

## 🚦Final Note

DataLab exists because messy data silently breaks real systems.

If you’re contributing because you care about **understanding before fixing**, you’re in the right place.

Thank you for taking the time to read this - and for respecting the project.
