---
name: thesias
category: analysis
description: THESIAS - Haplotype phase and association analysis for population genetics.
tags: [thesias, haplotype, phasing, association, population-genetics, snp]
author: oxo-call-community
source_url: "https://github.com/compbio/thesias"
---

## Concepts

- **Tool Overview**: THESIAS - A tool for haplotype phase estimation and association testing in population genetics studies.
- **Core Function**: Performs haplotype phasing from genotype data and tests for association with phenotypes, particularly valuable for rare variant analysis.
- **Input**: VCF files or genotype matrices, phenotype data.
- **Output**: Haplotype phases, association test results, haplotype frequency estimates.
- **Installation**: Available as R package `thesias`
- **Use Case**: Population genetics, disease association studies, pharmacogenomics.

## Pitfalls

- **Sample Size**: Large sample sizes needed for reliable haplotype estimation.
- **Population Structure**: Population stratification can confound association results.

## Examples

### Haplotype phasing
**Args:** `thesias -g genotypes.vcf -o haplotype_results/`
**Explanation:** Phase haplotypes from genotype data.

### Association testing
**Args:** `thesias -g variants.vcf -p phenotype.txt -o association/`
**Explanation:** Test for association between haplotypes and phenotype.
