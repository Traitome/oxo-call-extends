---
name: admixture
category: population-genomics
description: ADMIXTURE is a software tool for maximum likelihood estimation of individual ancestries from multilocus SNP genotype datasets.
tags: [admixture, population-genomics, ancestry, snp, genotype, structure]
author: oxo-call-community
source_url: "http://www.genetics.ucla.edu/software/admixture/index.html"
---

## Concepts

- **Tool Overview**: Maximum likelihood estimation tool for individual ancestries from multilocus SNP genotype data. Version 1.3.0.
- **Core Function**: Estimates individual ancestry proportions (admixture fractions) assuming K ancestral populations using a maximum likelihood approach.
- **Input/Output**: Input is PLINK BED/BIM/FAM format genotype data; output is ancestry proportions (.Q) and allele frequencies (.P) files.
- **Installation**: Install via bioconda: `conda install -c bioconda admixture`
- **Platform Support**: Linux (x86_64) and macOS (x86_64)
- **Model-Based**: Uses a statistical model (similar to STRUCTURE) for ancestry estimation, unlike PCA which is descriptive.
- **Cross-Validation**: Supports cross-validation (--cv) to select the optimal number of ancestral populations K.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Input Format**: Requires PLINK BED format (binary). Convert VCF to PLINK format using PLINK before running ADMIXTURE.
- **Linked SNPs**: ADMIXTURE assumes independent markers. Remove linked SNPs via LD pruning before analysis.
- **K Selection**: No single best K. Use cross-validation error (--cv) to compare K values. Lowest CV error suggests optimal K.
- **Computational Cost**: Large datasets with many K values are computationally expensive. Use --cv for systematic K selection.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Run ADMIXTURE with K=3
**Args:** `input.bed 3`
**Explanation:** Estimates ancestry proportions assuming 3 ancestral populations. Output files: input.3.Q (ancestry fractions) and input.3.P (allele frequencies).

### Run with cross-validation for K selection
**Args:** `--cv input.bed 3`
**Explanation:** Runs ADMIXTURE with K=3 and computes cross-validation error. Run for multiple K values and select the K with lowest CV error.

### Run with multiple K values
**Args:** `--cv input.bed 2 && --cv input.bed 3 && --cv input.bed 4 && --cv input.bed 5`
**Explanation:** Runs ADMIXTURE for K=2 through K=5 with cross-validation. Compare CV errors to select optimal K.

### Run with supervised mode
**Args:** `--supervised input.bed 3`
**Explanation:** Runs in supervised mode using predefined population labels. Requires population information in the FAM file.

### Run with bootstrapping
**Args:** `-B 100 input.bed 3`
**Explanation:** Performs 100 bootstrap replicates for standard error estimation of ancestry proportions. Computationally intensive.
