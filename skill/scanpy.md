---
name: scanpy
category: programming
description: Scanpy - Single-Cell Analysis in Python, scales to >1M cells
tags: ["scanpy", "programming", "single-cell", "RNA-seq"]
author: oxo-call-community
source_url: "https://scanpy.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: Scanpy (v1.7.2) is a Python library for efficient single-cell RNA-seq analysis that scales to over 1 million cells.
- **Core Function**: Provides comprehensive tools for preprocessing, visualization, clustering, and differential expression analysis of single-cell data.
- **Algorithm**: Implements efficient data structures and algorithms for large-scale single-cell analysis.
- **Input/Output**: Uses AnnData format for data representation and supports multiple file formats.
- **Scalability**: Designed to handle very large single-cell datasets efficiently.
- **Applications**: Single-cell RNA-seq analysis, cell type identification, trajectory analysis, and gene expression visualization.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Learning Curve**: Steep learning curve for beginners.
- **Version Compatibility**: Different versions may have breaking changes.
- **Computational Resources**: May require significant compute resources.
- **Documentation**: Some advanced features have limited documentation.
- **Dependency Management**: Requires careful management of dependencies.

## Examples

### Basic analysis workflow
**Args:** `import scanpy as sc; adata = sc.read_h5ad('data.h5ad'); sc.pp.recipe_zheng17(adata); sc.pp.pca(adata); sc.pp.neighbors(adata); sc.tl.umap(adata); sc.tl.leiden(adata)`
**Explanation:** Complete basic single-cell analysis workflow including preprocessing, PCA, UMAP, and clustering.

### Read data
**Args:** `import scanpy as sc; adata = sc.read_csv('expression.csv').T`
**Explanation:** Reads gene expression matrix from CSV file.

### Preprocessing
**Args:** `sc.pp.filter_cells(adata, min_genes=200); sc.pp.filter_genes(adata, min_cells=3); sc.pp.normalize_total(adata); sc.pp.log1p(adata)`
**Explanation:** Standard preprocessing steps: filtering, normalization, and log transformation.

### Dimensionality reduction
**Args:** `sc.pp.pca(adata, n_comps=50); sc.pp.neighbors(adata); sc.tl.umap(adata)`
**Explanation:** PCA followed by UMAP visualization.

### Clustering
**Args:** `sc.tl.leiden(adata, resolution=1.0); sc.pl.umap(adata, color='leiden')`
**Explanation:** Leiden clustering and visualization.

### Differential expression
**Args:** `sc.tl.rank_genes_groups(adata, 'leiden', method='wilcoxon'); sc.pl.rank_genes_groups(adata, n_genes=20)`
**Explanation:** Differential expression analysis between clusters.

### Trajectory analysis
**Args:** `sc.tl.paga(adata, groups='leiden'); sc.pl.paga(adata); sc.tl.umap(adata, init_pos='paga')`
**Explanation:** PAGA trajectory inference and visualization.