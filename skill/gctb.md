---
name: gctb
category: variant-calling
description: GCTB (Genome-wide Complex Trait Bayesian) is a software tool that comprises a family of Bayesian linear mixed models for complex trait analyses using genome-wide SNPs.
tags: [gctb, Bayesian, mixed-models, GWAS, polygenic-risk-score]
author: oxo-call-community
source_url: "https://cnsgenomics.com/software/gctb"
---

## Concepts
- **Bayesian Linear Mixed Models**: GCTB implements Bayesian methods to simultaneously estimate SNP effects and genetic architecture parameters including heritability, polygenicity, and effect size distributions.
- **BSLMM**: Bayesian Sparse Linear Mixed Model that partitions genetic variation into sparse (large effects) and polygenic (small effects) components.
- **SBayesR**: Summary-data BayesR that uses GWAS summary statistics to fit a mixture of normal distributions for SNP effect sizes.
- **SBayesRC**: Extended SBayesR that incorporates functional genomic annotations to improve polygenic prediction accuracy.
- **Genetic Architecture**: Estimates key parameters like SNP-based heritability, polygenicity (proportion of causal SNPs), and effect size distribution.

## Pitfalls
- **Computational Intensity**: MCMC-based methods require significant computational resources for large datasets.
- **Convergence Issues**: MCMC chains may require long run times to reach convergence.
- **LD Pruning**: Input data requires careful LD pruning to avoid computational instability.
- **Sample Size Requirements**: Requires large sample sizes (>10,000) for reliable parameter estimation.
- **Memory Usage**: Large SNP datasets require substantial memory allocation.

## Examples
### Run BSLMM with individual-level data
**Args:** `./gctb --bfile test --pheno test.phen --bslmm --out bslmm_result --burn-in 1000 --nMarkov 10000`
**Explanation:** Runs BSLMM analysis on individual-level genotype data. The --burn-in discards initial MCMC samples, and --nMarkov specifies total Markov chain iterations. Outputs include posterior means of effect sizes and genetic architecture parameters.

### Run SBayesR with summary statistics
**Args:** `./gctb --sbayes R --mldm ./ld_matrix --sumstats test.sumstats --out sbayesr_result --chain-length 10000`
**Explanation:** Performs SBayesR analysis using GWAS summary statistics and precomputed LD matrix. The --mldm specifies the directory containing LD matrix files. Suitable for large-scale biobank data when individual-level genotypes are unavailable.

### Run SBayesRC with functional annotations
**Args:** `./gctb --sbayes RC --mldm ./ld_matrix --sumstats test.sumstats --annot ./annotations.txt --out sbayesrc_result`
**Explanation:** Extends SBayesR by incorporating functional genomic annotations to prioritize SNPs in functional regions. The --annot specifies annotation file with functional category assignments per SNP.

### Estimate SNP-based heritability
**Args:** `./gctb --reml --grm test_grm --pheno test.phen --out heritability --thread-num 8`
**Explanation:** Estimates SNP-based heritability using REML (Restricted Maximum Likelihood). Requires a precomputed genetic relationship matrix (GRM) from GCTA. The --thread-num enables parallel computation.

### Perform genome-wide fine-mapping
**Args:** `./gctb --gwfm --mldm ./ld_matrix --sumstats test.sumstats --out fine_mapping --credible-set 0.95`
**Explanation:** Conducts genome-wide fine-mapping to identify credible sets of causal variants. The --credible-set specifies the posterior probability threshold for inclusion in credible sets (default 0.95).