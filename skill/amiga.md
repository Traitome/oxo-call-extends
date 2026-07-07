---
name: amiga
category: utility
description: Automated analysis of microbial growth assays using Gaussian Process regression
tags: [amiga, microbial-growth, growth-assays, Gaussian-Process, microbiology]
author: oxo-call-community
source_url: "https://firasmidani.github.io/amiga"
---

## Concepts

- **Tool Overview**: AMiGA (Analysis of Microbial Growth Assays) is a user-friendly software for automated analysis of high-throughput microbial growth assays using Gaussian Process regression.
- **Core Function**: Fits growth curves without assumptions about their shape, pools replicates, infers biologically meaningful growth parameters (carrying capacity, exponential growth rate, lag phase), quantifies death phases, characterizes diauxic shifts, and statistically tests for differential growth.
- **Input/Output**: Inputs: Plate reader data files (tabular format), metadata mapping files; Outputs: Summary statistics, growth parameter estimates, visualizations, statistical test results.
- **Installation**: Available via Bioconda (`conda install -c bioconda amiga`) or PyPI (`pip install amiga-growth`).
- **Features**: Gaussian Process regression for robust curve fitting, support for atypical growth shapes, batch analysis, diauxic shift detection, and both command-line and Python API access.

## Pitfalls

- **Data Format**: Ensure input data matches expected plate reader format with time and OD columns for each well.
- **Starting OD**: Zero or negative OD values require special handling; AMiGA automatically adjusts baseline but may affect parameter estimation.
- **Computational Time**: Fitting curves with GP regression takes ~1 minute per 96-well plate; use `--time-step-size` to thin data for speed.
- **Background Subtraction**: Use `--subtract-blanks` or `--subtract-control` flags to account for media background or control growth.
- **Replicate Pooling**: Ensure replicates are properly identified in metadata for accurate summary statistics.

## Examples

### Fit growth curves
**Args:** `amiga fit -i growth_data.txt`
**Explanation:** Fits growth curves using Gaussian Process regression and generates summary statistics including OD metrics and growth parameters.

### Subtract blank controls
**Args:** `amiga fit -i growth_data.txt --subtract-blanks`
**Explanation:** Subtracts growth curves from blank media wells before fitting to account for background OD.

### Analyze multiple plates
**Args:** `amiga batch -i plate_data/ -o results/`
**Explanation:** Batch processes all growth curve files in the specified directory.

### Detect diauxic shifts
**Args:** `amiga fit -i growth_data.txt --detect-diauxie`
**Explanation:** Identifies and characterizes diauxic shifts in growth curves.

### Generate visualization
**Args:** `amiga plot -i fitted_data.txt -o plots/`
**Explanation:** Generates visualizations of growth curves and parameter distributions.

### Compare growth conditions
**Args:** `amiga compare -i fitted_data.txt -m metadata.txt -o comparison_results.txt`
**Explanation:** Performs statistical tests for differential growth under distinct experimental conditions.