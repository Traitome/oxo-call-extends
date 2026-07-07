---
name: eqtlbma
category: utility
description: "Package to detect eQTLs jointly in multiple subgroups (e.g. tissues) via Bayesian Model Averaging."
tags: [eqtlbma, utility, eQTL, Bayesian, gene-expression]
author: oxo-call-community
source_url: "https://github.com/timflutre/eqtlbma"
---

## Concepts

- **Tool Overview**: eQTLBMA is a statistical package for detecting expression quantitative trait loci (eQTLs) across multiple subgroups or tissues using Bayesian Model Averaging.
- **Core Function**: Identifies genetic variants associated with gene expression levels, accounting for heterogeneity across multiple subgroups.
- **Input/Output**: Input: Genotype data (VCF/PLINK), gene expression data, subgroup labels. Output: eQTL associations, posterior probabilities, effect sizes.
- **Algorithm**: Uses Bayesian Model Averaging to combine evidence across multiple models, accounting for subgroup-specific effects.
- **Key Features**: Multi-subgroup analysis, Bayesian inference, posterior probability estimation, heterogeneity detection, batch correction.
- **Installation**: `conda install -c bioconda eqtlbma`

## Pitfalls

- **Sample Size**: Requires sufficient sample size for reliable statistical inference.
- **Subgroup Balance**: Unequal subgroup sizes may affect power.
- **Prior Specification**: Choice of priors can influence results.
- **Computation Time**: Bayesian inference can be computationally intensive.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic eQTL analysis
**Args:** `eqtlbma --geno genotypes.vcf --expr expression.txt --groups groups.txt --out results/`
**Explanation:** Detects eQTLs across multiple subgroups.

### With covariates
**Args:** `eqtlbma --geno genotypes.vcf --expr expression.txt --groups groups.txt --cov covariates.txt --out results/`
**Explanation:** Includes covariates in eQTL analysis.

### Posterior probabilities
**Args:** `eqtlbma --geno genotypes.vcf --expr expression.txt --groups groups.txt --posterior --out results/`
**Explanation:** Outputs posterior probabilities for each eQTL.

### Heterogeneity test
**Args:** `eqtlbma --geno genotypes.vcf --expr expression.txt --groups groups.txt --heterogeneity --out results/`
**Explanation:** Tests for heterogeneity across subgroups.

### Batch processing
**Args:** `eqtlbma --geno genotypes.vcf --expr expression.txt --groups groups.txt --batch config.txt --out results/`
**Explanation:** Processes multiple gene sets in batch mode.