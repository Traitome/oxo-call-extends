---
name: umap
category: dimensionality-reduction
description: UMAP - Uniform Manifold Approximation and Projection.
tags: [umap, dimensionality-reduction, visualization, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/lmcinnes/umap"
---

## Concepts

- **Tool Overview**: UMAP - A dimensionality reduction technique for data visualization.
- **Core Function**: Projects high-dimensional data into lower dimensions.
- **Input**: Feature matrix.
- **Output**: Low-dimensional embedding.
- **Installation**: Install via pip
- **Use Case**: Data visualization, clustering, bioinformatics.

## Pitfalls

- **Parameter Sensitivity**: Results depend on hyperparameters.
- **Computation Time**: May be slow for large datasets.

## Examples

### Run UMAP
**Args:** `umap --input data.csv --output embedding.csv`
**Explanation:** Compute UMAP embedding.

### With custom parameters
**Args:** `umap --input data.csv --output embedding.csv --n-neighbors 15 --min-dist 0.1`
**Explanation:** Customize UMAP parameters.
