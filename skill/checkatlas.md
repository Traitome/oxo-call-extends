---
name: checkatlas
category: single-cell
description: Quality control tool for single-cell atlases
tags: [checkatlas, single-cell, atlas, quality-control, bioinformatics]
author: oxo-call-community
source_url: "https://checkatlas.readthedocs.io/"
---

## Concepts

- **Tool Overview**: Checkatlas is a quality control tool for assessing single-cell atlas data quality.
- **Core Function**: Provides comprehensive QC metrics and visualizations for single-cell RNA-seq atlases.
- **Features**: Cell type annotation validation, batch effect detection, doublet detection, and quality metrics.
- **Input**: Single-cell expression matrices and metadata files.
- **Output**: QC reports with metrics and visualizations.
- **Application**: Single-cell atlas quality assessment and validation.
- **Installation**: Install via bioconda: `conda install -c bioconda checkatlas`

## Pitfalls

- **Data Format**: Requires specific input format (AnnData, Seurat object).
- **Annotation Quality**: Depends on accurate cell type annotations.
- **Computational Resources**: Large atlases may require significant memory.
- **Normalization**: Requires properly normalized data.

## Examples

### Run QC on atlas
**Args:** `checkatlas -i atlas.h5ad -o qc_report/`
**Explanation:** Performs quality control analysis on single-cell atlas.

### Generate summary
**Args:** `checkatlas --summary -i atlas.h5ad -o summary.txt`
**Explanation:** Generates summary statistics for atlas.

### Visualize QC metrics
**Args:** `checkatlas --visualize -i atlas.h5ad -o plots/`
**Explanation:** Generates QC visualization plots.

### Display help
**Args:** `checkatlas --help`
**Explanation:** Shows all available options and usage information.