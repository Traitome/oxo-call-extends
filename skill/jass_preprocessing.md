---
name: jass_preprocessing
category: utility
description: Harmonizing raw GWAS summary statistics for further analysis with jass.
tags: [jass_preprocessing, utility, GWAS, preprocessing, statistics]
author: oxo-call-community
source_url: "http://statistical-genetics.pages.pasteur.fr/jass_preprocessing/"
---

## Concepts

- **Tool Overview**: jass_preprocessing (v2.2) - A tool for preprocessing and harmonizing raw GWAS summary statistics for meta-analysis.
- **Data Harmonization**: Standardizes GWAS summary statistics across studies.
- **SNP ID Mapping**: Maps different SNP identifiers to a common reference.
- **Strand Alignment**: Ensures consistent strand orientation across datasets.
- **Quality Control**: Filters low-quality SNPs and checks for consistency.
- **Format Standardization**: Converts various input formats to a standardized format.

## Pitfalls

- **Reference Genome Mismatch**: Using different reference genomes can cause issues.
- **SNP ID Variation**: Different studies may use different SNP naming conventions.
- **Strand Ambiguity**: Ambiguous strand information can lead to errors.
- **Missing Data**: Missing values in GWAS summary statistics require handling.
- **Allele Order**: Inconsistent allele ordering between studies.
- **Population Differences**: Population-specific SNPs may need special handling.

## Examples

### Basic preprocessing
**Args:** `jass_preprocessing --input gwas_raw.txt --output gwas_clean.txt`
**Explanation:** Preprocesses raw GWAS summary statistics.

### Specify reference genome
**Args:** `jass_preprocessing --input gwas.txt --output clean.txt --ref hg38`
**Explanation:** Uses hg38 as reference genome for SNP mapping.

### Handle strand ambiguity
**Args:** `jass_preprocessing --input gwas.txt --output clean.txt --resolve-strand`
**Explanation:** Attempts to resolve strand ambiguity using reference.

### Filter by quality
**Args:** `jass_preprocessing --input gwas.txt --output clean.txt --min-info 0.8`
**Explanation:** Filters SNPs with imputation quality < 0.8.

### Multiple input files
**Args:** `jass_preprocessing --input study1.txt study2.txt --output merged.txt`
**Explanation:** Preprocesses and merges multiple GWAS datasets.

### Output detailed report
**Args:** `jass_preprocessing --input gwas.txt --output clean.txt --report preprocessing_report.txt`
**Explanation:** Generates detailed preprocessing report.