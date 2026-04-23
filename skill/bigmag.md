---
name: bigmag
category: metagenomics
description: BIgMAG - Dashboard for extracting insights from MAG quality metrics
tags: [mag, metagenome-assembled-genome, quality, visualization]
author: oxo-call-community
source_url: "https://github.com/jeffe107/BIgMAG"
---

## Concepts
- **Tool Overview**: BIgMAG is a dashboard tool for extracting insights from Metagenome-Assembled Genome (MAG) quality metrics. It helps researchers evaluate and visualize the quality of their metagenomic assemblies.
- **MAG Quality**: Evaluates metrics like completeness, contamination, N50, GC content, and strain heterogeneity.
- **Visualization**: Provides interactive dashboards for exploring quality metrics across multiple MAGs.
- **Applications**: Quality assessment of metagenomic assemblies, comparison of binning results, and selection of high-quality MAGs for downstream analysis.

## Pitfalls
- **Input Format**: Requires quality metrics in specific format (e.g., from CheckM or BUSCO).
- **Quality Thresholds**: Appropriate quality thresholds depend on the research question and downstream applications.

## Examples
### Generate quality dashboard
**Args:** `bigmag -i checkm_results.tsv -o dashboard.html`
**Explanation:** Creates an interactive dashboard from CheckM quality metrics.

### Compare multiple binning results
**Args:** `bigmag -i metabat2.tsv concoct.tsv maxbin.tsv -labels MetaBAT2 CONCOCT MaxBin -o comparison.html`
**Explanation:** Compares MAG quality across different binning tools.
