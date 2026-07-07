---
name: combined-pvalues
category: epigenomics
description: Combine and correct p-values in BED files with spatial autocorrelation
tags: [combined-pvalues, p-values, spatial-correlation, chip-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/brentp/combined-pvalues"
---

## Concepts

- **Tool Overview**: combined-pvalues is a library for combining, analyzing, grouping and correcting p-values in BED files, with unique corrections for spatial autocorrelation in genomic data.
- **Core Function**: Combines p-values from multiple tests while accounting for spatial correlation between genomic regions, essential for ChIP-Seq and tiling array analysis.
- **Algorithm**: Implements Fisher's method, Stouffer's method, and other p-value combination techniques with spatial autocorrelation correction.
- **Input**: BED files with p-values, genomic intervals, and associated statistics.
- **Output**: Combined p-values with corrected significance values.
- **Application**: ChIP-Seq analysis, tiling array data, ATAC-Seq, and any spatially correlated genomic data.
- **Installation**: Install via bioconda: `conda install -c bioconda combined-pvalues`

## Pitfalls

- **Spatial Correlation**: Ignoring spatial correlation leads to inflated false positives.
- **P-value Distribution**: Assumes uniform p-value distribution under null hypothesis.
- **Multiple Testing**: Requires appropriate multiple testing correction.
- **BED Format**: Requires properly formatted BED files with p-value columns.
- **Independence Assumption**: Standard methods assume independence; spatial correction is crucial.

## Examples

### Combine p-values from BED file
**Args:** `combined-pvalues -i regions.bed -c 4 -o combined.bed`
**Explanation:** Combines p-values from column 4 of BED file.

### With spatial autocorrelation correction
**Args:** `combined-pvalues -i regions.bed -s -o corrected.bed`
**Explanation:** Applies spatial autocorrelation correction to p-values.

### Group by genomic regions
**Args:** `combined-pvalues -i regions.bed -g genes.bed -o grouped.bed`
**Explanation:** Groups and combines p-values by genomic regions.

### Display help
**Args:** `combined-pvalues --help`
**Explanation:** Shows all available options and usage information.