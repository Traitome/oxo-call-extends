---
name: manc_cojo
category: population-genomics
description: Multi-ancestry conditional and joint analysis (COJO) of GWAS summary statistics.
tags: [manc_cojo, population-genomics, GWAS, COJO]
author: oxo-call-community
source_url: "https://github.com/light156/multi-ancestry-COJO"
---

## Concepts

- **Tool Overview**: manc_cojo v1.1.0 - Manc-COJO extends the COJO (Conditional and Joint analysis) method to multiple ancestries, using population-specific LD to improve independent signal detection.
- **Core Function**: Performs conditional and joint analysis of GWAS summary statistics across multiple ancestral populations.
- **Input/Output**: Input: GWAS summary statistics, LD reference panels; Output: Independent association signals, conditional effects.
- **Installation**: `conda install -c bioconda manc_cojo`
- **Multi-ancestry Analysis**: Handles GWAS data from multiple populations simultaneously.
- **LD-aware**: Uses population-specific linkage disequilibrium information.

## Pitfalls

- **LD Reference Quality**: Poor quality LD reference panels affect results.
- **Population Matching**: Requires matching LD panels to GWAS populations.
- **Sample Size**: Small sample sizes reduce statistical power.
- **Allele Frequency**: Differences in allele frequencies across populations.
- **Computational Resources**: Large datasets require significant memory.
- **Reference Genome**: Must use consistent reference genome across analyses.

## Examples

### Run multi-ancestry COJO
**Args:** `manc_cojo -i gwas_summary.txt -l ld_panels/ -o results/`
**Explanation:** Runs multi-ancestry COJO analysis.

### Single ancestry mode
**Args:** `manc_cojo -i gwas_summary.txt -l ld_panel/ -o results/ --single`
**Explanation:** Runs single-ancestry COJO (GCTA-COJO compatible).

### With ancestry labels
**Args:** `manc_cojo -i gwas_summary.txt -l ld_panels/ -a ancestry.txt -o results/`
**Explanation:** Specifies ancestry labels for each sample.

### Custom significance threshold
**Args:** `manc_cojo -i gwas_summary.txt -l ld_panels/ -o results/ --threshold 5e-8`
**Explanation:** Sets custom significance threshold.

### Verbose mode
**Args:** `manc_cojo -i gwas_summary.txt -l ld_panels/ -o results/ -v`
**Explanation:** Provides detailed logging during analysis.

### Generate Manhattan plot
**Args:** `manc_cojo -i gwas_summary.txt -l ld_panels/ -o results/ --plot`
**Explanation:** Generates Manhattan plot of results.