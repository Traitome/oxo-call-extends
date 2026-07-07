---
name: dmtools
category: utility
description: DMTools - Utilities for DNA methylation data processing.
tags: [dmtools, utility, methylation, epigenomics, bisulfite]
author: oxo-call-community
source_url: "https://github.com/YongZhang1990/DMRtools"
---

## Concepts

- **Tool Overview**: DMTools is a collection of utilities for DNA methylation data analysis.
- **Core Function**: Processes and analyzes DNA methylation data from bisulfite sequencing.
- **Input/Output**: Input: Methylation call files (BED, BAM, etc.). Output: Processed methylation data, DMRs.
- **Algorithm**: Provides tools for methylation extraction, filtering, and differential analysis.
- **Key Features**: Methylation extraction, DMR detection, quality control, visualization, batch processing.
- **Installation**: `conda install -c bioconda dmtools`

## Pitfalls

- **Input Requirements**: Requires methylation data from bisulfite sequencing.
- **Bisulfite Conversion**: Incomplete conversion affects results.
- **Mapping Quality**: Poor mapping affects methylation calls.
- **Coverage**: Requires sufficient coverage for reliable calls.
- **Normalization**: Appropriate normalization methods are critical.

## Examples

### Extract methylation data
**Args:** `dmtools extract --input meth_calls.bed --output methylation.tsv`
**Explanation:** Extracts and processes methylation data.

### Detect DMRs
**Args:** `dmtools dmr --group1 sample1.bed --group2 sample2.bed --output dmrs.tsv`
**Explanation:** Detect differentially methylated regions between groups.

### Quality control
**Args:** `dmtools qc --input meth_calls.bed --output qc_report.html`
**Explanation:** Generate quality control report for methylation data.

### Filter by coverage
**Args:** `dmtools filter --input meth_calls.bed --output filtered.bed --min-coverage 10`
**Explanation:** Filter methylation calls by minimum coverage.

### Generate visualization
**Args:** `dmtools plot --input methylation.tsv --output meth_plot.png`
**Explanation:** Generate visualization of methylation patterns.