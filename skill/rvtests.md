---
name: rvtests
category: variant_analysis
description: Rare variant test software for next generation sequencing data.
tags: ["rvtests", "rare variants", "GWAS", "association testing", "bioinformatics"]
author: oxo-call-community
source_url: "https://github.com/zhanxw/rvtests"
---

## Concepts

- **Tool Overview**: rvtests (v2.0.7) is a comprehensive software package for analyzing rare genetic variants in next-generation sequencing data. It implements various statistical tests for rare variant association studies.
- **Core Function**: Performs rare variant association testing using collapsing methods, burden tests, and variance-component tests. Supports both quantitative and binary phenotypes.
- **Algorithm**: Implements multiple statistical methods including SKAT (Sequence Kernel Association Test), burden tests, and combined tests for rare variant analysis.
- **Input Format**: VCF files with genotype data, phenotype files with sample information, optional covariate files.
- **Output Format**: Association test results in tabular format with p-values and effect sizes, optional Manhattan plots.
- **Use Case**: GWAS analysis for rare variants, exome sequencing studies, identifying disease-associated rare variants, population genetics research.

## Pitfalls

- **Sample size requirements**: Rare variant analysis requires large sample sizes for statistical power.
- **Quality control**: Strict quality control of variants is essential to avoid false positives.
- **Population stratification**: Requires proper correction for population structure.
- **Multiple testing**: Need to account for multiple comparisons across many variants.
- **Missing data**: Missing genotypes can affect test performance.
- **Reference panel requirements**: Some methods require external reference panels for allele frequency information.

## Examples

### Basic burden test
**Args:** `rvtests --vcf input.vcf --pheno phenotype.txt --out results --burden`
**Explanation:** Runs burden test for rare variant association.

### SKAT test
**Args:** `rvtests --vcf input.vcf --pheno phenotype.txt --out results --skat`
**Explanation:** Runs Sequence Kernel Association Test.

### Combined test
**Args:** `rvtests --vcf input.vcf --pheno phenotype.txt --out results --combined`
**Explanation:** Runs combined burden and SKAT test.

### With covariates
**Args:** `rvtests --vcf input.vcf --pheno phenotype.txt --covar covariates.txt --out results --burden`
**Explanation:** `--covar` specifies covariate file for adjustment.

### Filter by MAF
**Args:** `rvtests --vcf input.vcf --pheno phenotype.txt --out results --burden --maf 0.01`
**Explanation:** `--maf` maximum minor allele frequency for rare variants.

### Gene-based testing
**Args:** `rvtests --vcf input.vcf --pheno phenotype.txt --out results --burden --gene-based`
**Explanation:** `--gene-based` performs gene-level association testing.

### Binary phenotype
**Args:** `rvtests --vcf input.vcf --pheno phenotype.txt --out results --burden --binary`
**Explanation:** `--binary` specifies binary phenotype.
