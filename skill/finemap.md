---
name: finemap
category: variant-calling
description: "FINEMAP is a program for identifying causal SNPs, estimating their effect sizes, and quantifying heritability contributions from GWAS summary data."
tags: [finemap, variant-calling, GWAS, fine-mapping, causal-SNP, heritability, SNP, genetics, bioinformatics, statistics]
author: oxo-call-community
source_url: "https://www.christianbenner.com"
---

## Concepts

- **Tool Overview**: FINEMAP is a computational tool for fine-mapping causal variants in genomic regions associated with complex traits. It identifies causal SNPs, estimates their effect sizes, and quantifies heritability contributions using GWAS summary statistics and linkage disequilibrium (LD) data.
- **Core Function**: Performs statistical fine-mapping by applying a shotgun stochastic search (SSS) algorithm to identify the most likely causal configurations from GWAS summary statistics combined with LD matrices.
- **Input/Output**: Input: Z-score file (GWAS summary statistics), LD matrix file, master configuration file. Output: Causal SNP assignments with posterior probabilities, effect size estimates, and heritability contributions.
- **Algorithm**: Uses a sparse linear model to represent the association signal as a linear combination of SNP effects. Implements efficient shotgun stochastic search (SSS) for exploring causal configurations, making it computationally faster than exhaustive enumeration methods.
- **Key Features**: Identifies causal SNPs and estimates effect sizes, quantifies heritability contribution per SNP, supportscredible set construction, handles multiple causal SNPs per region, integrates with LDstore2 for LD management, supports stepwise conditional analysis.
- **Installation**: Download from http://www.christianbenner.com or `conda install -c bioconda finemap`. Requires zlib and libopenblas dependencies on Linux.

## Pitfalls

- **LD Matrix Quality**: The accuracy of fine-mapping depends heavily on the quality of the LD matrix. Ensure LD is computed from a reference panel closely matching the GWAS population.
- **Sample Overlap**: FINEMAP assumes no sample overlap between the GWAS and the LD reference panel. Sample overlap can inflate false positives in causal variant identification.
- **Z-Score Requirements**: The Z-score file must contain properly oriented effect alleles. Use the --flip-beta option if allele directions need adjustment.
- **Computational Resources**: While efficient, fine-mapping of large regions with many SNPs can still require substantial memory and CPU time. Use --n-causal-snps to limit the search space.
- **Correlation Threshold**: The --corr-config option (default 0.95) prevents analysis of perfectly correlated SNP pairs. This is a necessary constraint for matrix inversion but may miss some true causal variants in high-LD regions.

## Examples

### Basic fine-mapping with shotgun stochastic search
**Args:** `finemap --sss --in-files master.txt --out results/`
**Explanation:** Runs the standard shotgun stochastic search fine-mapping using input files specified in the master file. This is the most common mode for identifying causal variants.

### Stepwise conditional analysis
**Args:** `finemap --cond --in-files master.txt --dataset 2 --out results/`
**Explanation:** Performs stepwise conditional analysis similar to GCTA COJO. Use this when you want to identify secondary signals after conditioning on the top association.

### Evaluate a single causal configuration
**Args:** `finemap --config --in-files master.txt --out results/`
**Explanation:** Evaluates a single pre-specified causal configuration without performing stochastic search. Useful for testing specific hypotheses about causal variants.

### Set maximum number of causal SNPs
**Args:** `finemap --sss --in-files master.txt --n-causal-snps 3 --out results/`
**Explanation:** Limits the search to configurations with at most 3 causal SNPs. Reduces computational burden and is appropriate when prior knowledge suggests a small number of causal variants.

### Specify convergence criteria
**Args:** `finemap --sss --in-files master.txt --n-convergence 500 --prob-tol 0.001 --out results/`
**Explanation:** Fine-tunes convergence settings: stops when probability mass added is below 0.001 for 500 iterations. Increase n-convergence for more thorough exploration.

### Multi-threaded execution
**Args:** `finemap --sss --in-files master.txt --n-threads 8 --out results/`
**Explanation:** Uses 8 threads for parallel processing. Adjust based on available CPU cores to speed up analysis of large datasets.

### Create master input file
**Args:** `echo "z;ld;snp;config;cred;n_samples" > master.txt`
**Explanation:** The master file specifies input/output files and sample size. Example format:
```
z;ld;snp;config;cred;n_samples
data/locus.z;data/locus.ld;data/locus.snp;data/locus.config;data/locus.cred;50000
```

### Prepare Z-score file
**Args:** `printf "rsid chromosome position allele1 allele2 maf beta se
" > locus.z`
**Explanation:** Z-score file must contain columns: rsid, chromosome, position, allele1, allele2, maf, beta, se. Example:
```
rsid chromosome position allele1 allele2 maf beta se
rs1 10 1 T C 0.35 0.0050 0.0208
rs2 10 2 A G 0.04 0.0368 0.0761
```

### Interpret credible sets
**Args:** `cat results/locus1_sss cred`
**Explanation:** After running FINEMAP, the .cred file contains 95% credible sets of SNPs. Each set has a probability of containing the causal variant. SNPs with high posterior probabilities are strong candidates for functional follow-up.
