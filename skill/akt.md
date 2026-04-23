---
name: akt
category: population-genomics
description: Ancestry and Kinship Tools for statistical genetics analysis of whole-genome sequenced samples
tags: [ancestry, kinship, relatedness, population-genetics, vcf, bcftools]
author: oxo-call-community
source_url: "https://github.com/Illumina/akt"
---

## Concepts

- **Tool Overview**: AKT (Ancestry and Kinship Toolkit) provides statistical genetics routines for analyzing large cohorts of whole-genome sequenced samples using htslib API.
- **Core Function**: Detects related samples, determines ancestry, calculates variant correlations, checks Mendelian consistency, and performs sample clustering.
- **Input/Output**: Input: BCF/VCF files (works seamlessly with bcftools). Output: Relatedness statistics, ancestry assignments, QC reports.
- **Integration**: Uses htslib API for I/O, compatible with bcftools workflow and standard VCF/BCF formats.
- **Installation**: Install via bioconda: `conda install -c bioconda akt`

## Pitfalls

- **Sample Size**: Statistical power for kinship detection depends on sample size - larger cohorts provide more reliable estimates.
- **Variant Density**: Requires sufficient variant density - use appropriately filtered VCFs with good coverage.
- **Population Structure**: Ancestry inference accuracy depends on reference panel quality and population representation.
- **Memory Scaling**: Large cohorts may require significant memory - consider batching for very large sample sets.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available subcommands and options for AKT.

### Detect related samples
**Args:** `relatedness -i samples.vcf -o relatedness.tsv`
**Explanation:** Calculates kinship coefficients to identify related individuals in the cohort.

### Estimate ancestry
**Args:** `ancestry -i samples.vcf -r reference_panel.vcf -o ancestry.tsv`
**Explanation:** Infers population ancestry for each sample using reference panel.

### Check Mendelian consistency
**Args:** `mendelian -i trio.vcf -p pedigree.txt -o mendelian_errors.tsv`
**Explanation:** Identifies Mendelian inconsistencies in parent-child trios.

### Calculate variant correlations
**Args:** `correlation -i variants.vcf -o correlation_matrix.tsv`
**Explanation:** Computes pairwise correlation between variants across samples.

### Sample clustering
**Args:** `cluster -i samples.vcf -o clusters.tsv`
**Explanation:** Performs sample clustering based on genetic similarity.

### Full QC workflow
**Args:** `qc -i cohort.vcf -o qc_report/`
**Explanation:** Runs comprehensive quality control including relatedness, ancestry, and consistency checks.

### Filter by kinship threshold
**Args:** `relatedness -i samples.vcf -t 0.125 -o close_relatives.tsv`
**Explanation:** Identifies samples with kinship coefficient >0.125 (second-degree relatives or closer).
