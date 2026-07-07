---
name: gemma
category: variant-calling
description: GEMMA - Genome-wide Efficient Mixed Model Association for GWAS using linear mixed models.
tags: [gemma, GWAS, linear-mixed-models, association-analysis]
author: oxo-call-community
source_url: "https://github.com/genetics-statistics/GEMMA"
---

## Concepts
- **Linear Mixed Models**: Implements LMMs for genome-wide association studies.
- **GWAS Analysis**: Performs genome-wide association analysis.
- **Genetic Relationship Matrix**: Constructs and uses GRM for association testing.
- **Population Structure**: Controls for population structure and relatedness.
- **Efficient Computation**: Optimized for large-scale GWAS datasets.

## Pitfalls
- **Sample Size**: Requires large sample sizes for reliable results.
- **Memory Usage**: Large datasets require significant memory.
- **Computational Time**: LMM analysis can be computationally intensive.
- **Parameter Tuning**: Requires careful parameter adjustment.
- **Data Quality**: Requires high-quality genotype and phenotype data.

## Examples
### Build genetic relationship matrix
**Args:** `gemma -bfile genotype -gk 1 -o grm`
**Explanation:** Constructs a genetic relationship matrix from genotype data.

### Run GWAS with LMM
**Args:** `gemma -bfile genotype -pheno phenotype.txt -lm 4 -o gwas_results`
**Explanation:** Performs GWAS using linear mixed model with GRM.

### Bivariate analysis
**Args:** `gemma -bfile genotype -pheno phenotypes.txt -notsnp -bivariate 1 2 -o bivariate_results`
**Explanation:** Performs bivariate GWAS analysis for two phenotypes.

### Estimate heritability
**Args:** `gemma -bfile genotype -pheno phenotype.txt -reml -o heritability`
**Explanation:** Estimates SNP-based heritability using REML.

### Association test with covariates
**Args:** `gemma -bfile genotype -pheno phenotype.txt -covar covariates.txt -lm 4 -o gwas_results`
**Explanation:** Runs GWAS with covariates to control for confounding.