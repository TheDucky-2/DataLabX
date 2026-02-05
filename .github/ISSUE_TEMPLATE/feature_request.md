---
name: Feature Request
about: Suggest a new feature or improvement for DataLab
title: "[FEATURE]"
labels: enhancement
assignees: 
---

![DataLab Logo](../../assets/DataLab_logo.png)

# ✨ Feature Request

Please fill out the sections below to suggest a new feature or improvement for DataLab.

---

## Describe the Feature

A clear description of the feature or improvement you’d like to see in DataLab.

**Example:**  
> Add a graph-based workflow that links `DirtyDataDiagnosis` outputs to data visualization for text or categorical patterns.

---

## Motivation / Use Case

Why is this feature important?  
Who will benefit from it?  

**Example:**  
> Currently, text inconsistencies are detected, but visualizing relationships between inconsistent categories is not straightforward.
A graph-based summary could help identify patterns across columns.

---

## Proposed Solution
If you have an idea of how this could be implemented, describe it here.

**Example:**  
 
- Add a new diagnosis class `DiagnosisGraph`  
- Input: output dictionary from `DirtyDataDiagnosis`  
- Output: network graph showing relationships between inconsistent values across columns  
- Integrate with `data_diagnosis` and `data_visualization` workflow  

---

## Additional Context
Any other context, examples, references, or mockups that may help us understand your idea.

**Example:**

- Large datasets where performance matters  
- Integration with guides or notebooks  
- Advanced visualization styles or options  

---

**Note:** DataLab is currently in **pre-release (v0.1)**. 

Feature suggestions are encouraged. Your input and feedback helps guide the roadmap!
