---
name: backspinpy
category: expression
description: backSPIN - Clustering algorithm for single-cell RNA-seq data
tags: [single-cell, clustering, rna-seq, cell-type-identification]
author: oxo-call-community
source_url: "https://github.com/linnarsson-lab/BackSPIN"
---

## Concepts

- **Tool Overview**: backSPIN is a clustering algorithm designed for single-cell RNA-seq data, using a biclustering approach to simultaneously group cells and genes.

- **Biclustering**: Simultaneously clusters cells and genes, identifying co-expressed gene modules in cell subpopulations.

- **Iterative Splitting**: Uses iterative binary splitting to create hierarchical cluster structure.

- **Single-Cell Focus**: Designed specifically for the noise and sparsity characteristics of single-cell data.

## Pitfalls

- **Preprocessing Required**: Requires normalized expression matrix. Raw counts need preprocessing.

- **Parameter Sensitivity**: Number of splitting iterations affects results. Test multiple values.

- **Scalability**: May be slow for very large datasets (>10,000 cells).

## Examples

### Basic clustering
**Args:** `backspin clustering --input expression_matrix.tsv --output clusters.tsv`
**Explanation:** Runs backSPIN biclustering on single-cell expression matrix.

### Specify split levels
**Args:** `backspin clustering --input expression_matrix.tsv --splits 5 --output clusters.tsv`
**Explanation:** Performs 5 levels of binary splitting for hierarchical clustering.

### Output gene clusters
**Args:** `backspin clustering --input expression_matrix.tsv --output-genes gene_clusters.tsv --output clusters.tsv`
**Explanation:** Outputs both cell and gene cluster assignments.
