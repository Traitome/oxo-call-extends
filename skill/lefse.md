---
name: lefse
category: metagenomics
description: LDA Effect Size (LEfSe) - biomarker discovery algorithm for metagenomic data
tags: [lefse, metagenomics, biomarker, LDA, bioinformatics, microbiome]
author: oxo-call-community
source_url: "https://github.com/SegataLab/lefse"
---

## Concepts

- **Biomarker Discovery**: Identifies genomic features distinguishing biological conditions
- **LDA Analysis**: Uses Linear Discriminant Analysis for effect size calculation
- **High-dimensional Data**: Handles high-dimensional metagenomic datasets
- **Taxonomic Profiling**: Works with taxonomic abundance data
- **Statistical Testing**: Combines statistical significance with biological relevance
- **Visualization**: Provides visualization of biomarker results

## Pitfalls

- **Multiple Testing**: Multiple testing correction is essential
- **Sample Size**: Small sample sizes may produce false discoveries
- **Data Normalization**: Proper normalization is critical
- **Class Balance**: Uneven class distribution affects results
- **Feature Selection**: Too many features increase false positives
- **Validation**: Results need independent validation

## Examples

### Run LEfSe analysis
**Args:** `lefse_run.py input.txt output.res`
**Explanation:** Identifies biomarkers with significant differential abundance.

### Format input
**Args:** `lefse_format_input.py input.tsv input.in -c 1 -s 2 -u 3 -o 1000000`
**Explanation:** Converts TSV to LEfSe input format.

### Generate visualization
**Args:** `lefse_plot_res.py output.res output.png`
**Explanation:** Creates bar plot of biomarkers.

### Cladogram visualization
**Args:** `lefse_plot_cladogram.py output.res cladogram.png`
**Explanation:** Generates cladogram showing taxonomic distribution.

### Set alpha value
**Args:** `lefse_run.py input.txt output.res --alpha 0.01`
**Explanation:** Uses stricter significance threshold.

### Multi-class analysis
**Args:** `lefse_run.py input.txt output.res --multi_class`
**Explanation:** Handles more than two classes.