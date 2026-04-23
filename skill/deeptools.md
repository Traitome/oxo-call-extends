---
name: deeptools
category: qc
description: A set of user-friendly tools for normalization and visualization of deep-sequencing data.
tags: [deeptools, qc, visualization, coverage, normalization]
author: oxo-call-community
source_url: "https://github.com/deeptools/deepTools"
---

## Concepts

- **Tool Overview**: deepTools v3.5.6 - Comprehensive suite for analysis and visualization of deep sequencing data including BAM/BW coverage analysis.
- **Core Function**: Normalizes, processes, and visualizes sequencing data with tools for coverage plots, heatmaps, PCA, and more.
- **Input/Output**: Expects BAM/BIGWIG/BED files; outputs coverage plots, heatmaps, matrices, and QC metrics.
- **Installation**: `conda install -c bioconda deeptools`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires indexed BAM files for most operations.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available commands and subtools.

### Compute coverage
**Args:** `bamCoverage -b sample.bam -o coverage.bw`
**Explanation:** Converts BAM to BIGWIG coverage file.

### Generate heatmap
**Args:** `plotHeatmap -m matrix.gz -o heatmap.png`
**Explanation:** Creates heatmap from computed matrix.
