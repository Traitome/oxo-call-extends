---
name: ucsc-bigwigcorrelate
category: analysis
description: UCSC bigWigCorrelate - Tool for correlating BigWig signals.
tags: [ucsc-bigwigcorrelate, ucsc, bigwig, correlation, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bigWigCorrelate - A tool for calculating correlations between BigWig signals.
- **Core Function**: Computes correlation coefficients between multiple BigWig files.
- **Input**: Multiple BigWig files.
- **Output**: Correlation matrix.
- **Installation**: Part of UCSC utilities
- **Use Case**: Comparative analysis, signal correlation, multi-sample analysis.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Chromosome Consistency**: Requires matching chromosome names.

## Examples

### Calculate correlations
**Args:** `bigWigCorrelate file1.bw file2.bw file3.bw > correlations.txt`
**Explanation:** Calculate correlations between BigWig files.

### With regions
**Args:** `bigWigCorrelate -regions=regions.bed file*.bw > correlations.txt`
**Explanation:** Calculate correlations over specified regions.
