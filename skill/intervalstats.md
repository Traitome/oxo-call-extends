---
name: intervalstats
category: utility
description: Tool for assessing similarity between sets of genomic intervals
tags: [intervalstats, utility, genomics, intervals]
author: oxo-call-community
source_url: "http://sonorus.princeton.edu/IntervalStats/"
---

## Concepts

- **Tool Overview**: intervalstats (v1.01) is a tool for statistical analysis of genomic interval sets
- **Core Function**: Assesses similarity and computes statistical significance of overlaps between interval sets
- **Statistical Methods**: Supports Fisher's exact test, Jaccard index, and overlap significance
- **Input Format**: Accepts BED format interval files
- **Installation**: `conda install -c bioconda intervalstats`

## Pitfalls

- **Input Format**: Requires properly formatted BED files
- **Genome Size**: Accurate statistics require genome size information
- **Multiple Testing**: Multiple comparisons may require correction
- **Interval Overlap**: Overlapping intervals in input can affect statistics
- **Performance**: Large interval sets may be computationally intensive

## Examples

### Calculate overlap statistics
**Args:** `intervalstats -a peaks.bed -b genes.bed -g genome.sizes`
**Explanation:** Computes statistical significance of overlap between peaks and genes.

### Jaccard index
**Args:** `intervalstats -a set1.bed -b set2.bed -m jaccard`
**Explanation:** Calculates Jaccard similarity index between two interval sets.

### Fisher's exact test
**Args:** `intervalstats -a intervals1.bed -b intervals2.bed -g hg19.chrom.sizes -m fisher`
**Explanation:** Performs Fisher's exact test on interval overlaps.

### Report all statistics
**Args:** `intervalstats -a peaks.bed -b regions.bed -g genome.txt -m all`
**Explanation:** Computes all available statistical measures.

### Output to file
**Args:** `intervalstats -a a.bed -b b.bed -g genome.sizes -o results.txt`
**Explanation:** Writes results to output file instead of stdout.

### Verbose output
**Args:** `intervalstats -a peaks.bed -b genes.bed -g genome.sizes -v`
**Explanation:** Provides detailed output including intermediate calculations.