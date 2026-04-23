---
name: bbknn
category: expression
description: BBKNN - Batch balanced K-nearest neighbors for single-cell batch correction
tags: [batch-correction, single-cell, knn, integration]
author: oxo-call-community
source_url: "https://github.com/Teichlab/bbknn"
---

## Concepts

- **Tool Overview**: BBKNN (Batch Balanced KNN) corrects batch effects in single-cell RNA-seq data by modifying the KNN graph to balance connections across batches.

- **Graph-Based Correction**: Modifies the neighborhood graph used by UMAP/t-SNE to ensure balanced batch representation.

- **Lightweight**: Minimal parameter tuning required compared to other batch correction methods.

- **Scanpy Integration**: Designed to work seamlessly with Scanpy single-cell analysis framework.

- **Preserves Biology**: Aims to remove batch effects while preserving biological variation.

## Pitfalls

- **Over-Correction**: May over-correct when biological differences align with batch structure.

- **Batch Definition**: Requires correct batch labels. Mislabeling leads to poor correction.

- **Pre-Processing**: Requires proper normalization and PCA before applying BBKNN.

- **Nearest Neighbors**: Number of neighbors affects results. Test different values.

## Examples

### Basic batch correction
**Args:** `python -c "import scanpy as sc; import bbknn; adata=sc.read('data.h5ad'); bbknn.bbknn(adata, batch_key='batch'); sc.tl.umap(adata); adata.write('corrected.h5ad')"`
**Explanation:** Applies BBKNN batch correction to single-cell data using Scanpy.

### Custom neighbors
**Args:** `python -c "import bbknn; bbknn.bbknn(adata, batch_key='batch', n_pcs=30, neighbors_within_batch=25)"`
**Explanation:** Uses 30 PCs and 25 neighbors per batch for finer control.

### Within-batch neighbors only
**Args:** `python -c "import bbknn; bbknn.bbknn(adata, batch_key='batch', neighbors_within_batch=15, n_pcs=50)"`
**Explanation:** Uses more PCs and fewer neighbors for datasets with subtle batch effects.
