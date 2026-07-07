---
name: gsea
category: bioinformatics
description: GSEA (Gene Set Enrichment Analysis) identifies biologically relevant gene sets enriched in a gene expression dataset.
tags: [gsea, gene-set-enrichment, bioinformatics]
author: oxo-call-community
source_url: "https://www.gsea-msigdb.org/gsea"
---

## Concepts

- **Gene Set Enrichment**: GSEA identifies enriched gene sets from expression data.

- **Functional Analysis**: Analyzes functional enrichment of gene sets.

- **Statistical Significance**: Uses permutation testing for statistical significance.

- **Ranking Metric**: Ranks genes based on expression changes.

- **Enrichment Score**: Calculates enrichment scores for gene sets.

- **Visualization**: Generates enrichment plots and heatmaps.

## Pitfalls

- **Gene List Quality**: Results depend on the quality of the input gene list.

- **Gene Set Selection**: Choose appropriate gene sets for analysis.

- **Multiple Testing**: Correct for multiple hypothesis testing.

- **Sample Size**: Small sample sizes may produce unreliable results.

- **Normalization**: Ensure proper normalization of expression data.

## Examples

### Run GSEA analysis
**Args:** `gsea -i expression.txt -g gene_sets.gmt -o results/`
**Explanation:** Performs gene set enrichment analysis.

### Specify gene set database
**Args:** `gsea -i expression.txt -d hallmark -o results/`
**Explanation:** Uses Hallmark gene sets for enrichment.

### Adjust permutation number
**Args:** `gsea -i expression.txt -g gene_sets.gmt -n 1000 -o results/`
**Explanation:** Uses 1000 permutations for significance testing.

### Generate enrichment plot
**Args:** `gsea -i expression.txt -g gene_sets.gmt -p -o plot.png`
**Explanation:** Generates enrichment plot for a gene set.

### Batch processing
**Args:** `gsea batch -d datasets/ -o results/`
**Explanation:** Processes multiple datasets in batch mode.

### Filter by significance
**Args:** `gsea -i expression.txt -g gene_sets.gmt -t 0.05 -o results/`
**Explanation:** Filters results by p-value threshold of 0.05.

### Help command
**Args:** `gsea --help`
**Explanation:** Shows available options and usage information.