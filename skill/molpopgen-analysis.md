---
name: molpopgen-analysis
category: population-genomics
description: Deprecated programs for pre-NGS-era population-genetic data analysis.
tags: [molpopgen-analysis, population-genomics]
author: oxo-call-community
source_url: "https://github.com/molpopgen/analysis"
---

## Concepts

- **Tool Overview**: molpopgen-analysis v0.8.8 provides deprecated population genetics tools.
- **Core Function**: Analyzes population genetic data from pre-NGS era.
- **Deprecated Status**: No longer maintained; for historical use only.
- **Sanger Data**: Designed for Sanger sequencing data.
- **Input/Output**: Accepts traditional genetic data formats; outputs population statistics.
- **Population Genetics**: Supports population genetic analysis workflows.

## Pitfalls

- **Deprecated**: Not recommended for modern NGS data.
- **Sanger Specific**: Designed for pre-NGS sequencing data.
- **No Maintenance**: No updates or bug fixes.
- **Outdated Methods**: Uses older statistical methods.
- **Memory Requirements**: Memory usage depends on data size.
- **Data Quality**: Results may be incorrect for NGS data.

## Examples

### Calculate allele frequencies
**Args:** `msms2diffs input.txt > frequencies.txt`
**Explanation:** Calculates allele frequency differences.

### Run Tajima's D test
**Args:** `tajd input.txt > tajd_result.txt`
**Explanation:** Computes Tajima's D statistic.

### Haplotype analysis
**Args:** `hapstats input.txt > haplotype_stats.txt`
**Explanation:** Analyzes haplotype statistics.

### Linkage disequilibrium
**Args:** `ldne input.txt > ld_result.txt`
**Explanation:** Estimates effective population size from LD.

### Population differentiation
**Args:** `fst input.txt > fst_result.txt`
**Explanation:** Calculates FST statistics.