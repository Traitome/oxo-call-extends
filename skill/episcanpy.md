---
name: episcanpy
category: epigenomics
description: "Epigenomics Single-Cell Analysis in Python."
tags: [episcanpy, epigenomics, single-cell, ATAC-seq, scATAC-seq]
author: oxo-call-community
source_url: "https://github.com/colomemaria/epiScanpy"
---

## Concepts

- **Tool Overview**: epiScanpy is a Python library for the analysis of single-cell epigenomics data, particularly scATAC-seq, scDNAme, and other epigenetic assays.
- **Core Function**: Provides tools for preprocessing, quality control, dimensionality reduction, clustering, and visualization of single-cell epigenomics data.
- **Input/Output**: Input: Count matrices, fragment files, peak calls. Output: Analyzed AnnData objects, visualization plots, clustering results.
- **Algorithm**: Implements various dimensionality reduction techniques (PCA, t-SNE, UMAP), clustering algorithms, and differential accessibility analysis.
- **Key Features**: scATAC-seq analysis, integration with scanpy, peak calling, motif analysis, trajectory inference, visualization tools.
- **Installation**: `conda install -c bioconda episcanpy`

## Pitfalls

- **Data Quality**: Requires high-quality single-cell epigenomics data.
- **Memory Usage**: Large datasets require significant memory.
- **Parameter Tuning**: Clustering and dimensionality reduction parameters may need adjustment.
- **Integration Challenges**: Integrating multi-omics data requires careful processing.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic scATAC-seq analysis
**Args:** `import episcanpy as epi; adata = epi.read_atac("fragments.tsv"); epi.pp.quality_control(adata)`
**Explanation:** Reads and performs quality control on scATAC-seq data.

### Dimensionality reduction
**Args:** `epi.pp.pca(adata); epi.pp.neighbors(adata); epi.tl.umap(adata)`
**Explanation:** Performs PCA and UMAP dimensionality reduction.

### Clustering
**Args:** `epi.tl.leiden(adata); epi.pl.umap(adata, color='leiden')`
**Explanation:** Clusters cells using Leiden algorithm and visualizes.

### Differential accessibility
**Args:** `epi.tl.rank_genes_groups(adata, groupby='leiden')`
**Explanation:** Identifies differentially accessible peaks between clusters.

### Motif analysis
**Args:** `epi.tl.motif_enrichment(adata, motifs='JASPAR2020')`
**Explanation:** Performs motif enrichment analysis on accessible regions.