![DataLab logo](DataLab_logo_images/DataLab_logo.png)

# Change Logs

All versions listed below `0.1.0` are **pre-releases published to TestPyPI only**.

The first stable public release on PyPI will be **0.1.0**.

## [0.1.0a4] - 2025-12-26
**Status:** Alpha (pre-release - TestPyPI only)


### Added

- Completed **Missingness Visualization** workflow with updated docs:

  - Bar plots
  - Matrix plots
  - Heatmaps
  - Dendrograms

- Support for **custom missing value placeholders** across missingness diagnostics and visualizations.

- Annotated example images for all missingness plots to help users build intuition.

- Beginner-friendly, step-by-step documentation explaining *what* each plot shows and *why* it matters.

### Fixed

- **Column Type Conversion** to leave non-convertible values as they are, instead of silently coercing them into NaNs to maintain data integrity and prevent data-loss.

- Fixed issues with **Distribution** module in ``computations`` sub-package and **NumericalVisualizer** module in ``data_visualization`` sub-package.

- Versioning metadata issue on TestPyPI

### Improved

- Improved column type conversion logic to ensure accurate missingness detection and visualization results.

- Missing data visualizations to accept parameters for making understandable visualizations.

- Clear separation between:

  - Exploring & visualizing missing data

  - Handling missing data (intentionally deferred)

- Better explanations of **patterns of missing data & relationships** across rows, columns, and groups of columns.

### Documentation

- Added an intentional pause before handling missing values, explaining why early filling/dropping can be misleading.

- Introduced **Step 6: Understanding the Data (Preview)** to bridge missingness analysis with:

  - Distributions
  - Skewness
  - Outliers
  - Frequency

- Clarified that **computations happen behind the scenes**, and users will mainly interact with interpreted results.

- Documentation now follows a connected, story-driven workflow rather than isolated examples.

### Deferred

- Missing data handling logic is intentionally postponed until after data diagnosis and visualization steps.
