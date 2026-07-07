---
name: diego
category: expression
description: DIEGO - Differential alternative splicing detection using compositional data analysis.
tags: [diego, expression, splicing, differential, compositional-data]
author: oxo-call-community
source_url: "http://www.bioinf.uni-leipzig.de/Software/DIEGO"
---

## Concepts

- **Tool Overview**: diego (v0.1.2+) is a tool for detecting differential alternative splicing events using Aitchison's compositional data geometry.
- **Core Function**: Identifies differential splicing events by treating splice isoform counts as compositional data, avoiding issues with normalization.
- **Input/Output**: Input: Isoform-level read counts, sample group information. Output: Differential splicing events with statistical significance.
- **Algorithm**: Uses Aitchison's log-ratio transformation for compositional data analysis of splice isoform proportions.
- **Key Features**: Compositional data analysis, differential splicing detection, handles zero counts, multiple testing correction, visualization support.
- **Installation**: `conda install -c bioconda diego`

## Pitfalls

- **Input Requirements**: Requires isoform-level read count data, not gene-level counts.
- **Zero Counts**: Special handling required for isoforms with zero counts in some samples.
- **Sample Size**: Requires sufficient biological replicates for statistical power.
- **Normalization**: Does not require traditional normalization due to compositional approach.
- **Computational Time**: May be slow for large datasets with many isoforms.

## Examples

### Detect differential splicing
**Args:** `diego --counts counts.tsv --groups groups.tsv --output diff_splicing.tsv`
**Explanation:** Detects differential alternative splicing between conditions using compositional data analysis.

### With custom contrast
**Args:** `diego --counts counts.tsv --groups groups.tsv --output diff_splicing.tsv --contrast groupA-groupB`
**Explanation:** Specify custom contrast for differential analysis.

### Generate visualization
**Args:** `diego --counts counts.tsv --groups groups.tsv --output diff_splicing.tsv --plot splicing_plot.png`
**Explanation:** Generate visualization of splicing patterns.

### Adjust significance threshold
**Args:** `diego --counts counts.tsv --groups groups.tsv --output diff_splicing.tsv --fdr 0.05`
**Explanation:** Set FDR threshold for significance testing.

### Handle zero counts
**Args:** `diego --counts counts.tsv --groups groups.tsv --output diff_splicing.tsv --pseudocount 0.1`
**Explanation:** Add pseudocount to handle zero counts in compositional analysis.