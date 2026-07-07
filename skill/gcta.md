---
name: gcta
category: variant-calling
description: GCTA (Genome-wide Complex Trait Analysis) estimates heritability and performs GWAS using mixed linear model methods
tags: [gcta, heritability, GWAS, mixed linear model, GREML, GRM, SNP, genetics, genomics]
author: oxo-call-community
source_url: "https://yanglab.westlake.edu.cn/software/gcta/"
---

## Concepts

- **Tool Overview**: GCTA (Genome-wide Complex Trait Analysis) is a software package for genome-wide complex trait analysis. Originally developed to estimate SNP-based heritability using GREML method, now supports diverse GWAS and population genetics analyses.
- **Core Function**: GCTA estimates the proportion of phenotypic variance explained by all genome-wide SNPs using genetic relationship matrices (GRM) and restricted maximum likelihood (REML) methods.
- **Input Format**: GCTA works primarily with PLINK format files (.bed, .bim, .fam). Also supports Oxford format (.gen, .sample) for BOLT-LMM and other tools.
- **Heritability Estimation**: GREML (Genomic Restricted Maximum Likelihood) calculates SNP-based heritability (h2SNP) from GRM and phenotype data. Supports both quantitative and binary traits with prevalence specification.
- **GRM Construction**: The --make-grm option constructs genetic relationship matrices from SNP data. Options include --make-grm-alg for algorithm selection (0=Yang's method, 1=Yang's method with normalization).
- **GWAS Methods**: Supports multiple association methods: fastGWA (sparse GRM), fastGWA-GLMM (binary traits), MLMA (dense GRM), MLMA-LOCO (leave-one-chromosome-out).
- **COJO**: Conditional and joint association analysis using GWAS summary statistics. Identifies independent signals in regions of linkage disequilibrium.
- **Installation**: Download from https://yanglab.westlake.edu.cn/software/gcta/. Linux/Mac: `chmod +x gcta64 && ./gcta64`. Windows: gcta64.exe. Requires 64-bit systems. Bioconda: `conda install -c bioconda gcta`.
- **Multi-threading**: Use --thread-num or -t to specify thread count for parallel computation of GRM construction and REML analysis.

## Pitfalls

- **64-bit requirement**: GCTA is a 64-bit application. Ensure your system supports 64-bit executables. 32-bit systems cannot run GCTA.
- **PLINK file dependencies**: All three PLINK files (.bed, .bim, .fam) must be present in the same directory with consistent sample IDs. Missing files cause errors.
- **Sample overlap**: GRM and phenotype files must have exactly matching samples. Sample order matters. Use --keep or --remove to filter samples before analysis.
- **REMl convergence**: GREML may fail to converge with small sample sizes (<1000) or highly polygenic traits. Check .log files for convergence warnings.
- **Binary trait heritability**: For case-control studies, specify --prevalence for liability threshold model. Omitting prevalence gives observed scale heritability which is upwardly biased.
- **Memory usage**: GRM construction and storage scales with sample size (O(n^2) for n samples). Large cohorts (n>100,000) require substantial RAM (>32GB).
- **Autosome only**: Use --autosome to restrict analysis to autosomes. Sex chromosome analysis requires --chr 23, 24 options for X and Y.
- **LD Score regression**: For GREML power calculation, LD Score regression uses summary statistics. Ensure adequate SNP density for accurate LD Score estimation.

## Examples

### Build genetic relationship matrix
**Args:** `./gcta64 --bfile test --autosome --make-grm --out test_grm --thread-num 16`
**Explanation:** Constructs a genetic relationship matrix from PLINK files using autosomal SNPs. The --thread-num 16 enables parallel processing with 16 threads. Output creates test_grm.bin (GRM binary), test_grm.id (sample IDs), and test_grm.log files.

### Estimate heritability with GREML
**Args:** `./gcta64 --grm test_grm --pheno test.phen --reml --out heritability_result --thread-num 16`
**Explanation:** Performs REML analysis to estimate SNP-based heritability. Reads GRM from test_grm files and phenotype from test.phen. Outputs heritability estimate, standard error, and log-likelihood to heritability_result.

### GREML with covariates
**Args:** `./gcta64 --grm test_grm --pheno test.phen --qcovar PCs.txt --reml --out result --thread-num 16`
**Explanation:** Adds quantitative covariates (principal components from --qcovar) to correct for population stratification. Multiple covariate files can be specified. REML estimates variance explained by both SNPs and covariates.

### Heritability for binary trait
**Args:** `./gcta64 --grm test_grm --pheno binary_trait.phen --reml --prevalence 0.3 --out result`
**Explanation:** For case-control studies, --prevalence 0.3 specifies disease prevalence for liability threshold transformation. Without prevalence, heritability is estimated on observed scale which overestimates true heritability.

### Bivariate GREML for genetic correlation
**Args:** `./gcta64 --grm test_grm --pheno trait1.phen --pheno trait2.phen --reml --out bivariate_result`
**Explanation:** Estimates genetic correlation between two traits using bivariate REML. Outputs genetic covariance, heritabilities for both traits, and genetic correlation (rho_G) with standard errors.

### GWAS with fastGWA
**Args:** `./gcta64 --bfile dataset --pheno phenotype.txt --fastGWA --out gwas_results --thread-num 16`
**Explanation:** Performs genome-wide association analysis using fastGWA method with sparse GRM. Suitable for large biobank datasets (n>10,000). Uses mixed linear model to account for population structure and relatedness.

### Conditional analysis with COJO
**Args:** `./gcta64 --bfile dataset --gwas-summary sumstats.txt --cojo-file cojo_snps.txt --cojo-window 10000 --out cojo_results`
**Explanation:** Identifies independent association signals using conditional analysis. The --cojo-window 10000 specifies 10kb region for LD calculation. Requires reference LD structure from the dataset.

### PCA and population structure
**Args:** `./gcta64 --bfile dataset --autosome --make-grm --out grm && ./gcta64 --grm grm --pca 20 --out pca_result`
**Explanation:** First constructs GRM, then performs PCA decomposition to extract top 20 principal components. PCo plot and eigenvalues are output for visualizing population structure and correcting for stratification in GWAS.

### Estimate inbreeding coefficients
**Args:** `./gcta64 --bfile dataset --autosome --outlier-n 0 --make-grm --grm-cutoff 0.05 --out inbreeding`
**Explanation:** Calculates inbreeding coefficients (F) for each sample. Samples with F > 0.05 are flagged as potential inbreeding cases. Useful for quality control in population genetics studies.

### Search LD friends for target SNPs
**Args:** `./gcta64 --bfile dataset --ld-score-calc --ld-wind 10000 --out ld_scores`
**Explanation:** Computes LD scores for all SNPs using a 10kb window. LD scores are used for heritability estimation via LD Score regression and for identifying genomic regions with excessive signal.

### GSMR for Mendelian randomization
**Args:** `./gcta64 --bfile dataset --gwas-summary exposure.gwas --gwas-outcome outcome.gwas --gsmr --out gsmr_results`
**Explanation:** Performs generalized summary-data-based Mendelian randomization analysis to infer causal relationships between exposure and outcome traits. Uses GWAS summary statistics and instrumental variables.
