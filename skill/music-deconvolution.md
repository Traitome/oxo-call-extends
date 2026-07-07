---
name: music-deconvolution
category: expression
description: Multi-subject single cell deconvolution
tags: [music-deconvolution, deconvolution, single-cell, bulk-tissue, cell-type-proportion, expression]
author: oxo-call-community
source_url: "https://github.com/xuranw/MuSiC"
---

## Concepts

- **Tool Overview**: MuSiC v0.1.1 (Multi-subject Single Cell Deconvolution) estimates cell type proportions in bulk tissue samples by leveraging single-cell RNA-seq data from multiple subjects as a reference. It handles technical noise and biological variation across subjects.
- **Core Function**: Takes bulk gene expression data and single-cell reference expression matrices from multiple donors, then computes estimated cell type proportions for each bulk sample. Particularly useful for understanding tissue cellular composition.
- **Algorithm**: Uses weighted non-negative least squares regression with cross-cell type variance weighting. Accounts for cell-specific expression patterns and subject-specific effects. Works with any cell type annotations in the reference.
- **Input Format**: Expects bulk expression matrix (genes x samples) and single-cell reference (genes x cells) with cell type labels. Both should be in tab-delimited or matrix market format.
- **Output**: Returns estimated cell type proportions for each bulk sample, along with goodness-of-fit metrics. Proportions sum to 1 across cell types for each sample.
- **Strengths**: Handles single-cell data from multiple subjects (accounting for inter-subject variation), is robust to noise and dropouts common in scRNA-seq, and works with any cell type annotation scheme.

## Pitfalls

- **Gene Name Consistency**: Bulk and single-cell expression matrices must use consistent gene identifiers (e.g., gene symbols or Ensembl IDs). Mismatched gene names will cause errors or poor results.
- **Cell Type Annotation**: Single-cell reference must have accurate cell type labels. MuSiC trusts these annotations completely - errors in labeling propagate to deconvolution results.
- **Dropout Sensitivity**: While MuSiC is designed to be robust to scRNA-seq dropouts, extremely sparse data may still produce unreliable estimates. Check quality metrics in output.
- **Subject Matching**: MuSiC uses multi-subject single-cell data to improve robustness. At minimum, single-cell reference from representative subjects is needed.
- **Normalized Data**: MuSiC expects raw count data or appropriate normalization. Using pre-normalized data (like TPM) may give incorrect results.
- **Differential Expression**: Cell type proportions from deconvolution are suitable for association studies but not directly for differential expression analysis.

## Examples

### Basic deconvolution
**Args:** `--bulk bulk_expr.tsv --sc sc_ref.tsv --output proportions.tsv`
**Explanation:** Standard deconvolution using bulk expression and single-cell reference. Outputs estimated cell type proportions for each bulk sample.

### Specify cell type labels column
**Args:** `--bulk bulk.tsv --sc sc.tsv --celltype_col CellType --output proportions.tsv`
**Explanation:** Indicates which column in the single-cell file contains cell type labels. MuSiC will use this column to identify groups for deconvolution.

### Select informative marker genes
**Args:** `--bulk bulk.tsv --sc sc.tsv --markers markers.txt --output proportions.tsv`
**Explanation:** Uses a pre-specified list of marker genes for deconvolution instead of automatically selecting. Useful for focused analysis or reproducible pipelines.

### Cross-validation for robustness
**Args:** `--bulk bulk.tsv --sc sc.tsv --cv_fold 5 --output proportions.tsv`
**Explanation:** Performs cross-validation to assess deconvolution robustness. Helps evaluate how reliable the estimates are given the reference data quality.

### Output detailed metrics
**Args:** `--bulk bulk.tsv --sc sc.tsv --output proportions.tsv --details metrics.tsv`
**Explanation:** Saves additional metrics including per-sample R² values, weight distributions, and gene-specific statistics for quality assessment.
