---
name: ldsc
category: population-genomics
description: LD Score regression for heritability and genetic correlation estimation
tags: [ldsc, population-genomics, GWAS, heritability, genetic-correlation]
author: oxo-call-community
source_url: "https://github.com/bulik/ldsc"
---

## Concepts

- **LD Score Regression**: Estimates SNP heritability from GWAS summary stats
- **Genetic Correlation**: Computes genetic correlation between traits
- **GWAS Summary Statistics**: Works with GWAS summary statistics
- **Partitioned Heritability**: Estimates heritability per functional category
- **LD Score Computation**: Computes linkage disequilibrium scores
- **Reference Panel**: Uses reference genotype panel

## Pitfalls

- **Sample Overlap**: Sample overlap between GWAS and reference affects results
- **Population Stratification**: Population structure affects estimates
- **LD Score Quality**: Poor LD scores lead to biased estimates
- **SNP Quality**: Low-quality SNPs should be filtered
- **Sample Size**: Small sample sizes give unreliable estimates
- **Linkage Disequilibrium**: LD structure affects score computation

## Examples

### Calculate LD scores
**Args:** `ldsc.py --l2 --bfile reference --ld-wind-cm 1 --out ld_scores`
**Explanation:** Calculates LD scores from reference panel.

### Estimate heritability
**Args:** `ldsc.py --h2 gwas_sumstats.txt --ref-ld-chr ld_scores/ --w-ld-chr weights/ --out h2_results`
**Explanation:** Estimates SNP heritability.

### Genetic correlation
**Args:** `ldsc.py --rg trait1_sumstats.txt,trait2_sumstats.txt --ref-ld-chr ld_scores/ --w-ld-chr weights/ --out rg_results`
**Explanation:** Computes genetic correlation between traits.

### Partitioned heritability
**Args:** `ldsc.py --h2 gwas_sumstats.txt --ref-ld-chr baselineLD/ --w-ld-chr weights/ --overlap-annot --out partitioned_h2`
**Explanation:** Estimates partitioned heritability.

### Munge sumstats
**Args:** `ldsc.py --munge-sumstats gwas.txt --out munged_sumstats`
**Explanation:** Preprocesses GWAS summary statistics.

### Format reference
**Args:** `ldsc.py --make-bed --bfile reference --out formatted_ref`
**Explanation:** Formats reference panel for LD score computation.