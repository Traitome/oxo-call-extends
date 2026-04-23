---
name: bolt-lmm
category: population-genomics
description: Efficient large cohorts genome-wide Bayesian mixed-model association testing
tags: [bolt-lmm, gwas, association, mixed-model, population]
author: oxo-call-community
source_url: "https://alkesgroup.broadinstitute.org/BOLT-LMM/"
---

## Concepts

- **Tool Overview**: BOLT-LMM performs efficient genome-wide association analysis using a mixed model for large cohorts.
- **Core Function**: Computes association statistics while controlling for population structure and relatedness.
- **Algorithm**: Uses a variance-components mixed model with efficient REML estimation.
- **Input**: PLINK format genotype files and phenotype data.
- **Output**: Association statistics with p-values and effect sizes.
- **Installation**: Install via bioconda: `conda install -c bioconda bolt-lmm`

## Pitfalls

- **Sample Size**: Designed for large cohorts (>5000 samples); smaller datasets may not benefit.
- **Missing Data**: Excludes SNPs with high missing rates; adjust --genoMiss threshold.
- **LD Score**: Uses LD score regression for calibration; ensure sufficient SNP count.
- **Memory Usage**: Large datasets require significant memory; use --bgenFile for BGEN input.
- **Phenotype**: Quantitative traits recommended; binary traits need special handling.

## Examples

### Basic GWAS analysis
**Args:** `bolt --bfile=genotype --phenoFile=phenotypes.txt --phenoCol=trait1 --lmm --out=results`
**Explanation:** Runs mixed-model association for trait1 on PLINK binary genotype files.

### Multiple phenotypes
**Args:** `bolt --bfile=genotype --phenoFile=phenotypes.txt --phenoCol=trait1 --phenoCol=trait2 --lmm --out=multi_results`
**Explanation:** Tests association for multiple phenotypes in a single run.

### Using BGEN format
**Args:** `bolt --bfile=genotype --bgenFile=data.bgen --sampleFile=data.sample --phenoFile=pheno.txt --lmm --out=bgen_results`
**Explanation:** Uses BGEN format for memory-efficient analysis of large datasets.

### Covariate adjustment
**Args:** `bolt --bfile=genotype --phenoFile=pheno.txt --covarFile=covariates.txt --covarCol=PC1 --covarCol=PC2 --lmm --out=adj_results`
**Explanation:** Adjusts for principal components and other covariates in the model.

### Output association statistics
**Args:** `bolt --bfile=genotype --phenoFile=pheno.txt --lmm --statsFile=assoc.stats --out=results`
**Explanation:** Writes association statistics to specified output file.

### Set random seed
**Args:** `bolt --bfile=genotype --phenoFile=pheno.txt --lmm --seed=12345 --out=results`
**Explanation:** Sets random seed for reproducible results.
