---
name: scanorama
category: single-cell
description: Scanorama - panoramic stitching of heterogeneous single-cell transcriptomic data
tags: ["scanorama", "single-cell", "integration", "batch-correction"]
author: oxo-call-community
source_url: "https://github.com/brianhie/scanorama/"
---

## Concepts

- **Tool Overview**: Scanorama (v1.7.4) is a tool for integrating and stitching together heterogeneous single-cell transcriptomic datasets from different experiments or conditions.
- **Core Function**: Identifies shared cell populations across datasets and performs batch correction for seamless integration.
- **Algorithm**: Uses mutual nearest neighbors and canonical correlation analysis for dataset integration.
- **Input/Output**: Accepts gene expression matrices from multiple datasets and produces integrated embeddings.
- **Batch Correction**: Removes technical variation while preserving biological differences.
- **Applications**: Single-cell data integration, multi-omics analysis, and cell type comparison across experiments.

## Pitfalls

- **Computational Resources**: High memory and CPU requirements for large datasets.
- **Batch Effects**: May not perfectly remove all batch effects.
- **Parameter Tuning**: Requires careful adjustment for optimal integration.
- **Memory Usage**: May require significant memory for large datasets.
- **Time Complexity**: Integration of many datasets can be time-consuming.
- **Biological Variation**: May inadvertently remove true biological variation.

## Examples

### Basic integration
**Args:** `scanorama_integrate.py --datasets dataset1.h5ad dataset2.h5ad --output integrated.h5ad`
**Explanation:** Integrates multiple single-cell datasets.

### With PCA
**Args:** `scanorama_integrate.py --datasets dataset1.h5ad dataset2.h5ad --pca -o integrated.h5ad`
**Explanation:** `--pca` uses PCA for dimensionality reduction.

### Batch correction only
**Args:** `scanorama_correct.py --input dataset.h5ad --batch batch_info.txt -o corrected.h5ad`
**Explanation:** Performs batch correction on single dataset.

### Output embeddings
**Args:** `scanorama_integrate.py --datasets datasets/*.h5ad --embeddings -o embeddings.tsv`
**Explanation:** Outputs integrated embeddings in TSV format.

### K-nearest neighbors
**Args:** `scanorama_integrate.py --datasets datasets/*.h5ad --k 20 -o integrated.h5ad`
**Explanation:** `--k 20` sets k=20 for nearest neighbor search.

### Verbose logging
**Args:** `scanorama_integrate.py --datasets datasets/*.h5ad -v -o integrated.h5ad`
**Explanation:** `-v` enables verbose output for debugging.

### Save plots
**Args:** `scanorama_integrate.py --datasets datasets/*.h5ad --plot -o integrated.h5ad`
**Explanation:** `--plot` generates visualization plots.