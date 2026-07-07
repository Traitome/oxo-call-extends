---
name: ddqc
category: expression
description: Biology-centered data-driven quality control for single-cell RNA-seq data.
tags: [ddqc, expression, scRNA-seq, quality-control, preprocessing]
author: oxo-call-community
source_url: "https://github.com/ayshwaryas/ddqc"
---

## Concepts

- **Tool Overview**: ddqc (v1.0+) is a data-driven quality control tool for single-cell RNA-seq that uses biological information to identify and remove low-quality cells. It takes a biology-centered approach rather than using fixed thresholds.
- **Core Function**: Performs adaptive quality control on scRNA-seq data by learning cell quality metrics from the data itself, considering biological variation and technical noise.
- **Input/Output**: Input: AnnData object or count matrix with cell annotations. Output: Filtered AnnData object with QC metrics and diagnostic plots.
- **Algorithm**: Uses clustering and biological marker expression to identify cell types, then applies adaptive thresholds based on cell type-specific characteristics.
- **Key Features**: Adaptive thresholding, cell type-aware QC, mitochondrial content filtering, doublet detection, visualization tools.
- **Installation**: `conda install -c bioconda ddqc`

## Pitfalls

- **Cell Type Heterogeneity**: May require tuning for datasets with diverse cell types.
- **Batch Effects**: Strong batch effects may affect QC threshold learning.
- **Doublet Detection**: Doublet detection may have false positives/negatives.
- **Mitochondrial Thresholds**: Default mitochondrial thresholds may not suit all tissues.
- **Data Format**: Requires proper AnnData format with necessary annotations.

## Examples

### Basic QC filtering
**Args:** `ddqc input.h5ad output.h5ad`
**Explanation:** Perform data-driven QC on scRNA-seq data.

### Specify mitochondrial gene pattern
**Args:** `ddqc input.h5ad output.h5ad --mt-pattern "^MT-"`
**Explanation:** Use custom pattern to identify mitochondrial genes.

### Run with doublet detection
**Args:** `ddqc input.h5ad output.h5ad --detect-doublets`
**Explanation:** Include doublet detection in QC pipeline.