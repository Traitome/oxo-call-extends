---
name: cell-types-analysis
category: single-cell
description: Suite of scripts for analyzing scRNA-seq cell type classification tool outputs
tags: [cell-types-analysis, single-cell, cell-type-classification, scrna-seq, analysis]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/cell-types-analysis"
---

## Concepts

- **Tool Overview**: cell-types-analysis provides scripts for analyzing cell type classification outputs from scRNA-seq tools.
- **Core Function**: Evaluates and compares cell type classification results across different tools.
- **Features**: Classification accuracy assessment, tool comparison, and result visualization.
- **Input**: Cell type classification outputs from various tools.
- **Output**: Comparison reports and performance metrics.
- **Application**: Evaluating cell type annotation tools for single-cell RNA-seq data.
- **Installation**: Install via bioconda: `conda install -c bioconda cell-types-analysis`

## Pitfalls

- **Input Format**: Requires specific output formats from supported classification tools.
- **Reference Data**: Needs gold standard annotations for comparison.
- **Tool Compatibility**: Only supports specific cell type classification tools.
- **Memory Usage**: Large datasets may require significant memory.

## Examples

### Run classification analysis
**Args:** `cell-types-analysis analyze -i predictions/ -r reference.tsv -o results/`
**Explanation:** Analyzes cell type predictions against reference annotations.

### Compare multiple tools
**Args:** `cell-types-analysis compare -i tool1.tsv tool2.tsv tool3.tsv -o comparison/`
**Explanation:** Compares cell type classification results from multiple tools.

### Generate visualization
**Args:** `cell-types-analysis plot -i results.tsv -o plots/`
**Explanation:** Generates visualizations of classification performance.

### Display help
**Args:** `cell-types-analysis --help`
**Explanation:** Shows all available commands and options.