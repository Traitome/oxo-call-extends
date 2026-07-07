---
name: echidna
category: single-cell
description: "Mapping genotype to phenotype through joint probabilistic modeling of single-cell gene expression and chromosomal copy number variation."
tags: [echidna, single-cell, copy-number-variation, gene-expression, probabilistic-modeling]
author: oxo-call-community
source_url: "https://github.com/azizilab/echidna"
---

## Concepts

- **Tool Overview**: Echidna is a computational tool that integrates single-cell gene expression and copy number variation data to map genotype-phenotype relationships.
- **Core Function**: Uses joint probabilistic modeling to identify how copy number variations affect gene expression patterns in single cells.
- **Input/Output**: Input: Single-cell RNA-seq data (UMI counts), copy number profiles. Output: Integrated genotype-phenotype maps, significance scores.
- **Algorithm**: Implements Bayesian hierarchical modeling to jointly model gene expression and copy number variation.
- **Key Features**: Integrative analysis, probabilistic modeling, single-cell resolution, statistical significance testing, visualization.
- **Installation**: `pip install echidna-sc`

## Pitfalls

- **Data Quality**: Requires high-quality single-cell data with minimal dropout.
- **CNV Calling**: Depends on accurate copy number variation calls.
- **Computation Time**: Bayesian modeling can be computationally intensive.
- **Memory Usage**: Large single-cell datasets require significant RAM.
- **Model Assumptions**: Assumes CNV-expression relationships follow expected patterns.

## Examples

### Basic integration
**Args:** `echidna integrate --rna rna_counts.csv --cnv cnv_profiles.csv --output results/`
**Explanation:** Integrates RNA-seq and CNV data.

### With quality filtering
**Args:** `echidna integrate --rna rna_counts.csv --cnv cnv_profiles.csv --min-cells 10 --output results/`
**Explanation:** Filters genes with fewer than 10 expressing cells.

### Differential expression analysis
**Args:** `echidna diffexp --rna rna_counts.csv --cnv cnv_profiles.csv --output de_results.csv`
**Explanation:** Performs differential expression analysis based on CNV status.

### Visualization
**Args:** `echidna plot --input results/ --output plot.pdf`
**Explanation:** Generates visualization of genotype-phenotype relationships.

### Significance testing
**Args:** `echidna test --rna rna_counts.csv --cnv cnv_profiles.csv --output sig_results.csv`
**Explanation:** Tests statistical significance of CNV-expression associations.