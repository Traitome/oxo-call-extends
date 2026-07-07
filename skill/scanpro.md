---
name: scanpro
category: single-cell
description: ScanPro - Single-Cell Analysis of Proportions
tags: ["scanpro", "single-cell", "proportions", "differential-abundance"]
author: oxo-call-community
source_url: "https://github.com/loosolab/scanpro"
---

## Concepts

- **Tool Overview**: ScanPro (v0.4.1) is a tool for Single-Cell Analysis of Proportions, enabling differential abundance testing of cell type proportions across conditions.
- **Core Function**: Identifies statistically significant changes in cell type proportions between experimental conditions.
- **Algorithm**: Uses regression models to test for differences in cell type composition.
- **Input/Output**: Accepts single-cell data with cell type annotations and produces statistical results.
- **Statistical Testing**: Provides p-values and effect sizes for differential proportion analysis.
- **Applications**: Single-cell RNA-seq analysis, cell type composition comparison, and differential abundance testing.

## Pitfalls

- **Cell Type Annotation**: Requires accurate cell type annotations.
- **Sample Size**: Requires sufficient sample sizes for statistical power.
- **Normalization**: Results depend on proper data normalization.
- **Batch Effects**: May be affected by batch effects in the data.
- **Multiple Testing**: Requires proper multiple testing correction.
- **Assumptions**: Assumes independent and identically distributed observations.

## Examples

### Basic proportion analysis
**Args:** `scanpro analyze -i data.h5ad -c cell_type -g group -o results.csv`
**Explanation:** `-i` input AnnData; `-c` cell type column; `-g` group column; `-o` output results.

### With covariates
**Args:** `scanpro analyze -i data.h5ad -c cell_type -g group --covariates batch,sex -o results.csv`
**Explanation:** `--covariates` specifies confounding variables to adjust for.

### Visualize results
**Args:** `scanpro plot -i results.csv -o plot.png`
**Explanation:** Generates visualization of differential proportion results.

### Multiple comparisons
**Args:** `scanpro analyze -i data.h5ad -c cell_type -g group --contrast "A_vs_B" -o results.csv`
**Explanation:** `--contrast` specifies which groups to compare.

### Verbose mode
**Args:** `scanpro analyze -i data.h5ad -c cell_type -g group -v -o results.csv`
**Explanation:** `-v` enables verbose output for debugging.

### Output JSON
**Args:** `scanpro analyze -i data.h5ad -c cell_type -g group -f json -o results.json`
**Explanation:** `-f json` outputs results in JSON format.

### Save model
**Args:** `scanpro analyze -i data.h5ad -c cell_type -g group --save-model model.pkl -o results.csv`
**Explanation:** `--save-model` saves the fitted model for later use.