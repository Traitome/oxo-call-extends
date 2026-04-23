---
name: angsd
category: population-genomics
description: ANGSD - Analysis of Next Generation Sequencing Data with genotype uncertainty-aware methods
tags: [population-genetics, sfs, fst, genotype-likelihood, ngs, snp-calling]
author: oxo-call-community
source_url: "http://www.popgen.dk/angsd/index.php/ANGSD"
---

## Concepts

- **Tool Overview**: ANGSD performs population genetic analyses on NGS data while accounting for genotype uncertainty, particularly important for low-depth sequencing. Version 0.940.
- **Genotype Likelihoods**: Core approach uses genotype likelihoods instead of called genotypes, avoiding biases from hard genotype calls in low-coverage data.
- **Major Analyses**: Site frequency spectra (SFS), Fst, Tajima's D, theta estimation, PCA, admixture analysis, association testing, IBD/IBS estimation.
- **Input Formats**: Accepts BAM/CRAM files (mapped reads), VCF (genotype probabilities), and Beagle format (imputed genotypes).
- **Multi-Threaded**: Supports multi-threaded processing for efficient analysis of large datasets with many samples.
- **SNP Calling**: Probabilistic SNP calling using genotype likelihoods with configurable filters for quality, depth, and minor allele frequency.
- **Downstream Tools**: Works with related tools: realSFS (SFS estimation), ANGSD-wrapper, ngsAdmix, PCAngsd for extended analyses.

## Pitfalls

- **Not a BAM Manipulator**: ANGSD is for analysis, not BAM file manipulation. Use SAMtools for BAM operations.
- **Memory Usage**: Large BAM files with many samples require substantial memory. Use -nThreads carefully to balance speed and memory.
- **Filter Combinations**: Multiple filters (-minMapQ, -minQ, -minInd, -minMaf) interact. Test combinations on small regions first.
- **Reference Bias**: Ancient DNA and damaged samples may show reference bias. Use appropriate genotype likelihood models.
- **SFS Estimation**: Requires careful selection of -doSaf and -doMajorMinor options. Incorrect settings produce biased SFS.
- **Low Coverage**: Methods are designed for low coverage but extremely low coverage (<2x) may still have limited power.

## Examples

### Estimate allele frequencies from BAM files
**Args:** `angsd -out output -bam bam_list.txt -GL 1 -doMaf 1 -doMajorMinor 1 -nThreads 10`
**Explanation:** Estimates minor allele frequencies from BAM files using SAMtools genotype likelihood model (GL 1). 10 threads for parallel processing. Basic population genetics analysis.

### Call SNPs with quality filters
**Args:** `angsd -out snps -bam bam_list.txt -GL 1 -doMaf 1 -doMajorMinor 1 -minMapQ 30 -minQ 20 -minInd 5 -minMaf 0.05 -SNP_pval 1e-6`
**Explanation:** SNP calling with filters: mapping quality ≥30, base quality ≥20, present in ≥5 individuals, MAF ≥5%, SNP p-value ≤1e-6. Stringent filtering for high-confidence SNPs.

### Estimate Site Frequency Spectrum
**Args:** `angsd -out saf -bam bam_list.txt -GL 1 -doSaf 1 -doMajorMinor 1 -anc reference.fa -nThreads 8`
**Explanation:** Estimates SFS using ancestral reference sequence. Output used with realSFS for folded/unfolded SFS and demographic inference. Requires ancestral sequence for unfolded SFS.

### Calculate Fst between populations
**Args:** `angsd -out pop1 -bam pop1_bams.txt -GL 1 -doSaf 1 -doMajorMinor 1; angsd -out pop2 -bam pop2_bams.txt -GL 1 -doSaf 1 -doMajorMinor 1; realSFS pop1.saf.idx pop2.saf.idx -P 8 > fst_estimate.txt`
**Explanation:** Two-step Fst calculation: estimate SFS for each population separately, then compute Fst using realSFS. 8 threads for parallel computation.

### Calculate Tajima's D
**Args:** `angsd -out tajima -bam bam_list.txt -GL 1 -doSaf 1 -doMajorMinor 1 -doThetas 1 -nThreads 6`
**Explanation:** Estimates theta statistics including Tajima's D. Detects deviations from neutral evolution. Negative values suggest population expansion or positive selection.

### PCA analysis
**Args:** `angsd -out pca -bam bam_list.txt -GL 1 -doMajorMinor 1 -doMaf 1 -doCov 1 -nThreads 8`
**Explanation:** Generates covariance matrix for PCA analysis. Use with ngsPCA or import into R for visualization. Useful for detecting population structure.

### Association testing
**Args:** `angsd -out assoc -bam bam_list.txt -GL 1 -doMaf 1 -doMajorMinor 1 -doAsso 1 -y phenotype.txt -nThreads 10`
**Explanation:** Performs association testing between SNPs and phenotype. Phenotype file contains 0/1 for case/control. Uses genotype likelihood-based test for low-coverage data.

### Genotype likelihood output
**Args:** `angsd -out beagle -bam bam_list.txt -GL 1 -doGlf 2 -doMajorMinor 1 -doMaf 1 -nThreads 8`
**Explanation:** Outputs genotype likelihoods in Beagle format for downstream imputation or analysis with other tools. Format 2 = Beagle format.