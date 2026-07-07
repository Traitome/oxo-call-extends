---
name: lollipop
category: metagenomics
description: LolliPop - Deconvolution tool for wastewater genomics
tags: [lollipop, metagenomics, wastewater, deconvolution, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/LolliPop"
---

## Concepts

- **Wastewater Genomics**: Analysis of genomic data from wastewater samples
- **Deconvolution**: Estimating relative abundances of different strains
- **Strain Identification**: Identifying microbial strains in samples
- **SNP Analysis**: Single-nucleotide polymorphism analysis
- **Mixture Analysis**: Analyzing mixed populations
- **Relative Abundance**: Estimating relative proportions of strains

## Pitfalls

- **Sample Quality**: Poor quality samples affect results
- **Reference Database**: Quality of reference database is critical
- **Computational Time**: May be slow for large datasets
- **Memory Usage**: Memory-intensive for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **False Positives**: May produce false positive strain identifications

## Examples

### Run deconvolution
**Args:** `lollipop --input variants.vcf --output results/`
**Explanation:** Runs deconvolution on variant data.

### Reference database
**Args:** `lollipop --input variants.vcf --ref-db reference.fasta --output results/`
**Explanation:** Uses custom reference database.

### Threads
**Args:** `lollipop --input variants.vcf --output results/ --threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum coverage
**Args:** `lollipop --input variants.vcf --output results/ --min-cov 10`
**Explanation:** Sets minimum coverage threshold.

### Output format
**Args:** `lollipop --input variants.vcf --output results.json --format json`
**Explanation:** Outputs results in JSON format.

### Verbose output
**Args:** `lollipop --input variants.vcf --output results/ --verbose`
**Explanation:** Provides detailed output.