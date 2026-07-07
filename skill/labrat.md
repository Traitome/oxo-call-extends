---
name: labrat
category: expression
description: Quantifies changes in alternative polyadenylation isoform abundance using RNA-seq
tags: [labrat, expression, RNA-seq, alternative-polyadenylation, isoform, polyA]
author: oxo-call-community
source_url: "https://github.com/TaliaferroLab/LABRAT"
---

## Concepts

- **Alternative Polyadenylation**: Quantifies APA isoform abundance changes
- **RNA-seq Data**: Analyzes RNA sequencing data
- **Isoform Quantification**: Measures expression of polyadenylation isoforms
- **Differential Analysis**: Detects changes in APA usage
- **Poly(A) Sites**: Identifies polyadenylation site usage
- **Transcript Isoforms**: Distinguishes between transcript isoforms

## Pitfalls

- **Poly(A) Site Annotation**: Requires good poly(A) site annotations
- **Coverage Depth**: Low coverage affects quantification accuracy
- **Library Preparation**: Poly(A) selection vs ribo-depletion matters
- **Data Quality**: Poor quality reads affect analysis
- **Annotation Completeness**: Incomplete annotations miss novel sites
- **Statistical Modeling**: Multiple testing requires proper correction

## Examples

### Quantify APA isoforms
**Args:** `labrat quant -i reads.bam -a polyA_sites.bed -o isoforms.txt`
**Explanation:** Quantifies alternative polyadenylation isoforms.

### Differential analysis
**Args:** `labrat diff -i control/ -i treatment/ -o results.txt`
**Explanation:** Compares APA usage between conditions.

### Specify gene list
**Args:** `labrat quant -i reads.bam -a sites.bed -g genes.txt -o results.txt`
**Explanation:** Analyzes only specified genes.

### Set minimum coverage
**Args:** `labrat quant -i reads.bam -a sites.bed --min-cov 10 -o results.txt`
**Explanation:** Requires minimum 10 reads coverage.

### Export visualization
**Args:** `labrat vis -i results.txt -o plots/`
**Explanation:** Creates visualization plots.

### Batch analysis
**Args:** `labrat batch -d samples/ -a sites.bed -o results/`
**Explanation:** Processes multiple samples.