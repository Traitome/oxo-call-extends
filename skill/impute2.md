---
name: impute2
category: variant-analysis
description: Genotype imputation and haplotype phasing tool for genome-wide association studies
tags: [impute2, genotype-imputation, haplotype-phasing, GWAS]
author: oxo-call-community
source_url: "https://mathgen.stats.ox.ac.uk/impute/impute_v2.html"
---

## Concepts

- **Tool Overview**: IMPUTE2 (v2.3.2) is a widely used genotype imputation and haplotype phasing program developed by the University of Oxford. It uses Hidden Markov Models (HMM) to infer missing genotypes and phase haplotypes.
- **Core Function**: Imputes unobserved genotypes using reference haplotypes (e.g., from 1000 Genomes Project), enabling genome-wide association studies with sparse genotype data.
- **Input/Output**: Accepts IMPUTE format (.gen, .haps), VCF, and genetic map files. Outputs imputed genotypes with quality scores and posterior probabilities.
- **Phasing Mode**: Can perform classical phasing analysis to infer haplotypes from observed genotypes using the `-phase` option.
- **Reference Panels**: Supports multiple reference panels including phased (1000 Genomes) and unphased data, allowing hybrid imputation strategies.

## Pitfalls

- **Reference Panel Compatibility**: Ensure reference panel matches study population ancestry for accurate imputation.
- **Genetic Map Requirements**: Must provide genetic map file with recombination rates for accurate HMM modeling.
- **Memory Constraints**: Large datasets may require significant memory; use `-o_gz` flag to compress output.
- **Allele Strand Alignment**: SNPs with ambiguous strand (A/T, C/G) require strand files or `-align_by_maf_g` option.
- **Computational Intensity**: Whole-genome imputation is computationally heavy; consider splitting by chromosome or using `-k` parameter to optimize.

## Examples

### Basic genotype imputation
**Args:** `impute2 -g target_data.gen -m genetic_map.txt -h reference.haps -l reference.legend -int 1 5000000 -o imputed_output`
**Explanation:** Imputes genotypes in chromosome 1 region (1-5Mb) using reference haplotypes and genetic map.

### Run phasing only
**Args:** `impute2 -phase -g genotypes.gen -m genetic_map.txt -o phased_output`
**Explanation:** Performs haplotype phasing without imputation using the `-phase` flag.

### Compress output file
**Args:** `impute2 -g target_data.gen -m map.txt -h ref.haps -o_gz -o output.impute2.gz`
**Explanation:** Uses `-o_gz` flag to compress output with gzip, useful for large datasets.

### Combine phased and unphased reference panels
**Args:** `impute2 -m map.txt -h phased.haps -l phased.legend -g_ref unphased.gen -int 20.4e6 20.5e6 -o combined_impute`
**Explanation:** Combines phased and unphased reference panels for improved accuracy and coverage.

### Adjust MCMC parameters
**Args:** `impute2 -g data.gen -m map.txt -h ref.haps -k 100 -burnin 5 -iter 20 -Ne 20000 -o output`
**Explanation:** Sets 100 conditioning states, 5 burn-in iterations, 20 main iterations, and effective population size of 20,000.

### Predict genotyped SNPs
**Args:** `impute2 -g data.gen -m map.txt -h ref.haps -pgs -no_sample_qc_info -o output`
**Explanation:** Uses `-pgs` flag to replace original genotypes with LD-based predictions for quality improvement.