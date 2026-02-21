![datalabx logo](/assets/datalabx_logo.png)

# 🌱 Foundations

**Foundations are the thinking layer of datalabx.**

They explain ``how datalabx reasons about messy, real-world data - not just how to call functions or run workflows``.

While API documentation tells you what you can do,
Foundations explain **why things behave the way they do**, **what patterns to look for**, and **how to interpret what you see**.

If you want to understand your data deeply, not just process it - this is where you start.

---

## What are datalabx Foundations?

*datalabx Foundations are hand-written, concept-driven documents that helps you explore **data understanding and diagnosis**.*

They focus on:

* How to **think** about messy real-world data
* How to **interpret diagnostics and visualizations**
* Why certain workflows exist
* What conclusions are ***safe* vs *dangerous***
* How different data types require different reasoning

These documents are:

* **API-agnostic**
* **Narrative and visual**
* **Designed for humans, not machines**
* **Stable across versions**

Foundations do **not** assume clean data.
They assume real data - inconsistent, incomplete, and often misleading.

---

## What Foundations are Not

Foundations are **not**:

* API reference documentation
* Quickstart or installation guides
* Step-by-step 'click here' tutorials
* Auto-generated docs

Those live elsewhere.

Foundations exist because **most data failures come from misunderstanding data, not from bad code**.

---

## Why Foundations exist

Many data tools assume that once data is loaded, the hard part is over.

**In real-world work, that is where the real work begins.**

Real datasets commonly contain:

- unclear, mixed, or wrongly inferred column types

- hidden invalid values, placeholders, and domain dependent missingness patterns

- inconsistent representations within the same column

- dirty numerical and categorical data behaving differently

- missingness that is structural, patterned, or misleading

- unsafe transformations applied too early

- visualizations that look correct but hide important details

These problems do not occur due to incorrect API usage - **They come from incorrect assumptions about what the data actually represents.**

> Foundations exist to make those assumptions visible.

datalabx’s Foundations cover how to reason about tabular data before, during, and after diagnosis, including:

- how data is loaded and interpreted

- how column types are inferred, mis-inferred, and corrected

- how dirty data manifests differently across data types

- how diagnosis outputs should be read, trusted, or questioned

- how missingness appears, increases silently, and misleads

- how visualizations help and sometimes distort - understanding

- how safe handling decisions depend on context, not defaults

Each of these requires judgment, not just function calls.

**Foundations exist because these ideas cannot be expressed meaningfully through API reference documentation alone.**

---

## How Foundations are organized

Foundations are structured by **data type and reasoning domain**, not by API surface.

#### Structure:

```
foundations/
├── tabular/
│   ├── data-loading/
│   ├── data-diagnosis/
│   └── missingness/
│       ├── overview
│       ├── diagnosis
│       ├── visualization
│       └── handling
```

Each section builds intuition gradually:

* clear language
* real-world examples
* annotated visualizations
* metaphors where helpful
* explicit reasoning

You are encouraged to **read linearly**, not skim.

---

## How Foundations relate to other datalabx materials

| Section              | Purpose                                      | Focus / Examples                                  |
|----------------------|----------------------------------------------|---------------------------------------------------|
| **API Documentation**| Describes *what functions exist and how to call them* | Generated automatically (via `pdoc`)              |
| **Guides**           | Show *applied, end-to-end usage*              | Notebooks and practical walkthroughs              |
| **Foundations**      | Explain *how to think about data itself*      | Concepts, interpretation, reasoning                |

These layers are **intentionally separate** to avoid confusion and duplication.

---

## Who should read Foundations?

Foundations are written for:

* Analysts & Data Scientists working with messy data
* Beginners who want **safe, explainable workflows**
* Advanced users who want **clarity instead of black boxes**
* Anyone who has ever felt - ``“Why does my data behave like this?”``

You do **not** need to be an expert to read **Foundations.**
You only need curiosity and patience.

---

## A note on style and intent

Foundations are intentionally:

* slower
* more descriptive
* more visual
* more explanatory

This is deliberate.

datalabx is built to feel like:

> Someone sitting next to you, explaining what your data is doing and why.

Foundations are where that voice lives.

---

## Versioning & scope

Foundations evolve alongside datalabx, but they are **not tightly coupled to specific APIs**.

As datalabx grows (text data, graph data, ML workflows),
Foundations will grow too - without rewriting how existing data concepts work.

---

## Where to go next

If you are new to datalabx:

- Start with **Foundations -> Tabular -> Tabular Foundations** (see [Tabular Foundations](tabular/tabular_foundations.md))
- Then move into data loading, diagnosis and missingness

If you already use datalabx:

- Use Foundations to **interpret results**
- Revisit sections when something feels unclear or suspicious

``Understanding data is not a one-time task.``

---

**Foundations are not optional reading. They are the reason datalabx exists.**

