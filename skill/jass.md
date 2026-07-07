---
name: jass
category: utility
description: Computation of joint statistics over sets of GWAS results.
tags: [jass, utility, GWAS, statistics, genetics]
author: oxo-call-community
source_url: "http://statistical-genetics.pages.pasteur.fr/jass/"
---

## Concepts

- **Tool Overview**: jass (v2.3) - A tool for computing joint statistics across multiple GWAS datasets to identify shared genetic signals.
- **Meta-analysis**: Combines results from multiple GWAS studies.
- **Joint Statistics**: Computes combined statistics including Fisher's method, Stouffer's method, and weighted Z-scores.
- **Correlation Adjustment**: Accounts for correlation between studies.
- **Heterogeneity Testing**: Tests for heterogeneity across studies.
- **Visualization**: Generates Manhattan plots and forest plots for results.

## Pitfalls

- **Study Heterogeneity**: Differences in study design can affect meta-analysis results.
- **Population Stratification**: Population differences between studies must be accounted for.
- **Overlapping Samples**: Overlapping samples between studies can inflate significance.
- **Missing Data**: Missing SNP data across studies requires careful handling.
- **Publication Bias**: Publication bias can affect meta-analysis results.
- **Threshold Selection**: Choosing appropriate significance thresholds is critical.

## Examples

### Basic meta-analysis
**Args:** `jass --input gwas1.txt gwas2.txt gwas3.txt --output meta_results.txt`
**Explanation:** Performs meta-analysis across multiple GWAS datasets.

### Fisher's method
**Args:** `jass --input *.txt --output results.txt --method fisher`
**Explanation:** Uses Fisher's combined probability test for meta-analysis.

### Weighted Z-score
**Args:** `jass --input *.txt --output results.txt --method weighted-z`
**Explanation:** Uses weighted Z-score method accounting for study sizes.

### Heterogeneity test
**Args:** `jass --input *.txt --output results.txt --heterogeneity`
**Explanation:** Tests for heterogeneity across studies using I² and Q statistics.

### Generate Manhattan plot
**Args:** `jass --input *.txt --output results.txt --plot manhattan.png`
**Explanation:** Generates Manhattan plot of meta-analysis results.

### Set significance threshold
**Args:** `jass --input *.txt --output results.txt --threshold 5e-8`
**Explanation:** Filters results to only include SNPs with p-value < 5e-8.