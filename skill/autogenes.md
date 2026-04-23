---
name: autogenes
category: expression
description: AutoGeneS - Automatic gene selection for bulk deconvolution of cell type proportions
tags: [deconvolution, gene-selection, cell-type-proportions, bulk-rna-seq]
author: oxo-call-community
source_url: "https://github.com/theislab/AutoGeneS"
---

## Concepts

- **Tool Overview**: AutoGeneS automatically selects optimal gene sets for bulk tissue deconvolution to estimate cell type proportions from bulk RNA-seq data.

- **Multi-Objective Optimization**: Uses evolutionary algorithms to optimize gene sets for multiple criteria including specificity, correlation, and variance.

- **Reference-Based**: Requires single-cell reference data to identify marker genes for each cell type.

- **Deconvolution Support**: Selected genes improve accuracy of downstream deconvolution tools like CIBERSORT, MuSiC, or Bisque.

## Pitfalls

- **Reference Quality**: Gene selection quality depends on single-cell reference data completeness and accuracy.

- **Cell Type Granularity**: Very similar cell types may be difficult to distinguish even with optimal gene selection.

- **Computation Time**: Evolutionary optimization can be slow for large gene sets and many cell types.

- **Validation Required**: Selected genes should be validated on independent datasets before production use.

## Examples

### Basic gene selection
**Args:** `autogenes select --reference sc_reference.h5ad --output selected_genes.txt`
**Explanation:** Selects optimal marker genes from single-cell reference for deconvolution.

### Specify number of genes
**Args:** `autogenes select --reference sc_reference.h5ad --n-genes 100 --output genes.txt`
**Explanation:** Selects exactly 100 marker genes optimized for deconvolution accuracy.

### Multi-objective optimization
**Args:** `autogenes select --reference sc_reference.h5ad --objectives specificity correlation --output genes.txt`
**Explanation:** Optimizes gene set for both specificity and correlation criteria simultaneously.

### Parallel processing
**Args:** `autogenes select --reference sc_reference.h5ad --n-jobs 8 --output genes.txt`
**Explanation:** Uses 8 parallel jobs to speed up evolutionary optimization.

### Custom cell types
**Args:** `autogenes select --reference sc_reference.h5ad --cell-types "T cells,B cells,Monocytes" --output genes.txt`
**Explanation:** Selects genes for specific cell types only, ignoring others in reference.
