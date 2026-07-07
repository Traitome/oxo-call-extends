---
name: koeken
category: metagenomics
description: Linear Discriminant Analysis (LEfSe) wrapper for biomarker discovery
tags: [koeken, metagenomics, LEfSe, biomarker, LDA, statistical-analysis]
author: oxo-call-community
source_url: "https://github.com/twbattaglia/koeken"
---

## Concepts

- **LEfSe Analysis**: Implements Linear Discriminant Analysis Effect Size analysis
- **Biomarker Discovery**: Identifies biomarkers that explain biological differences
- **Statistical Testing**: Performs non-parametric statistical tests
- **Effect Size Estimation**: Estimates magnitude of biological differences
- **Visualization**: Generates plots for biomarker visualization
- **Metagenomics Support**: Designed for microbiome and metagenomics data

## Pitfalls

- **Sample Size**: Small sample sizes reduce statistical power
- **Multiple Testing**: Requires correction for multiple comparisons
- **Effect Size Thresholds**: Threshold selection affects biomarker identification
- **Data Normalization**: Proper normalization is critical for accurate results
- **Class Imbalance**: Imbalanced class sizes affect results
- **Biological Interpretation**: Statistical significance doesn't always mean biological relevance

## Examples

### Run LEfSe analysis
**Args:** `koeken -i abundance_table.tsv -c class.txt -o results/`
**Explanation:** Performs LEfSe analysis on abundance data.

### Specify subclass
**Args:** `koeken -i table.tsv -c class.txt -s subclass.txt -o results/`
**Explanation:** Includes subclass variable in analysis.

### Set LDA threshold
**Args:** `koeken -i table.tsv -c class.txt -o results/ --lda 3.0`
**Explanation:** Only reports features with LDA score >= 3.0.

### Generate visualization
**Args:** `koeken -i table.tsv -c class.txt -o results/ --plot`
**Explanation:** Generates LDA effect size bar plot.

### Export biomarkers
**Args:** `koeken -i table.tsv -c class.txt -o results/ --export-biomarkers`
**Explanation:** Exports list of identified biomarkers.

### Batch processing
**Args:** `koeken batch -d tables/ -o results/`
**Explanation:** Processes multiple abundance tables.