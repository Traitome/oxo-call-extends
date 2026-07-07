---
name: garnet
category: expression
description: Python toolkit for transcription factor (TF) binding motif analysis and gene expression regression modeling.
tags: [garnet, transcription-factor, motif-analysis, gene-expression, chip-seq]
author: oxo-call-community
source_url: "https://fraenkel.mit.edu/GarNet/"
---

## Concepts

- **Tool Overview**: Garnet is a Python toolkit for mapping transcription factor binding motifs to peaks from epigenomics experiments and performing linear regression between motif scores and gene expression values.
- **Core Function**: Integrates ChIP-seq/ATAC-seq peak data with RNA-seq expression data to identify transcription factor regulatory relationships.
- **Input Data**: Takes BED files of genomic peaks (from ChIP-seq/ATAC-seq) and gene expression files (tab-delimited gene name and expression score pairs).
- **Algorithm**: Uses pybedtools to intersect TF motifs with genomic peaks, then performs elastic-net linear regression to model TF-expression relationships.
- **Output**: Returns dataframes of TF-motif-gene associations with regression statistics and optional visualization plots.
- **Installation**: `pip install garnet` or `conda install -c bioconda garnet`
- **Dependencies**: numpy, pandas, matplotlib, statsmodels, pybedtools, jinja2
- **Language**: Python 3
- **Species Support**: Human, mouse, and other organisms with available genome annotations
- **Use Cases**: TF regulatory network inference, ChIP-seq peak annotation, epigenetic regulation analysis

## Pitfalls

- **Peak File Format**: Input peak files must be in standard BED format with chrom, start, end columns. Incorrect formats cause failures in bedtools intersection.
- **Gene ID Matching**: Gene names in expression file must match those in the garnet annotation database. Mismatched IDs result in empty output.
- **Memory Usage**: Large peak files combined with many TF motifs can consume significant memory. Consider filtering peaks by significance first.
- **Motif Score Threshold**: Default motif scoring thresholds may miss weak TF bindings. Adjust based on known TF binding affinities.
- **Regression Convergence**: Elastic-net regression may fail to converge with highly correlated predictors. Check for multicollinearity among TFs.
- **Annotation Database**: Species without pre-built garnet annotation files require manual creation of motif and gene databases.
- **Platform Dependency**: Requires bedtools to be installed and in system PATH for pybedtools to function correctly.

## Examples

### Map TF motifs to peaks
**Args:** `garnet map_peaks(peaks.bed, garnet_file.gff)`
**Explanation:** Intersects genomic peaks with TF motif positions to identify which motifs are present in peak regions.

### Perform TF expression regression
**Args:** `garnet TF_regression(motifs_genes.tsv, expression.tsv, output_dir="results/")`
**Explanation:** Runs elastic-net regression of TF motif scores against gene expression values and generates summary plots.

### Install garnet
**Args:** `pip install garnet`
**Explanation:** Installs garnet and its Python dependencies via pip package manager.

### Run example workflow
**Args:** `python -m garnet --peaks peaks.bed --expression genes.tsv --output results/`
**Explanation:** Complete workflow from peak and expression files to TF regulatory analysis results.

### Create custom garnet file
**Args:** `garnet construct_garnet_file(motifs.bed, genes.gtf, organism="hg38")`
**Explanation:** Builds a custom garnet annotation file combining TF motifs with gene coordinates for a specific genome.
