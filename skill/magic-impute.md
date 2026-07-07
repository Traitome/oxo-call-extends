---
name: magic-impute
category: utility
description: Markov Affinity-based Graph Imputation of Cells
tags: [magic-impute, utility, single-cell, imputation]
author: oxo-call-community
source_url: "https://github.com/KrishnaswamyLab/MAGIC"
---

## Concepts

- **Tool Overview**: magic-impute v3.0.0 - MAGIC (Markov Affinity-based Graph Imputation of Cells) is a method for denoising and imputing single-cell RNA-seq data.
- **Core Function**: Uses Markov affinity graphs to impute missing values and denoise single-cell transcriptomics data.
- **Input/Output**: Input: Gene expression matrix (CSV, TSV, AnnData); Output: Imputed expression matrix.
- **Installation**: `conda install -c bioconda magic-impute`
- **Graph-based Imputation**: Constructs Markov affinity graphs to propagate information across similar cells.
- **Denoising**: Reduces technical noise while preserving biological variation.

## Pitfalls

- **Parameter Tuning**: Incorrect k-nearest neighbors or t-values affect imputation quality.
- **Computational Resources**: Memory-intensive for large datasets.
- **Batch Effects**: May amplify batch effects if not properly normalized.
- **Over-imputation**: Can over-smooth true biological variation.
- **Data Format**: Requires properly formatted input matrices.
- **Preprocessing**: Raw data requires normalization before imputation.

## Examples

### Basic imputation
**Args:** `magic --input expression.csv --output imputed.csv`
**Explanation:** Imputes missing values in gene expression matrix.

### With custom k-neighbors
**Args:** `magic --input expression.csv --output imputed.csv --k 20`
**Explanation:** Uses 20 nearest neighbors for graph construction.

### Multiple imputation steps
**Args:** `magic --input expression.csv --output imputed.csv --t 3`
**Explanation:** Performs 3 diffusion steps.

### With PCA initialization
**Args:** `magic --input expression.csv --output imputed.csv --pca 50`
**Explanation:** Uses 50 PCA components for initialization.

### Verbose mode
**Args:** `magic --input expression.csv --output imputed.csv --verbose`
**Explanation:** Provides detailed processing information.

### Save as AnnData
**Args:** `magic --input expression.h5ad --output imputed.h5ad`
**Explanation:** Processes and saves AnnData object.