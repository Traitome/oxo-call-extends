---
name: king
category: variant-calling
description: Kinship-based INference for Gwas (KING) is a toolset that makes use of high-throughput SNP data typically seen in a genome-wide association study
tags: [king, kinship, GWAS, SNP, relatedness]
author: oxo-call-community
source_url: "http://people.virginia.edu/~wc9c/KING/"
---

## Concepts

- **Kinship Inference**: Estimates pairwise genetic relatedness from SNP data
- **GWAS Analysis**: Essential tool for quality control in genome-wide association studies
- **Relatedness Estimation**: Computes kinship coefficients using SNP genotypes
- **SNP Data Analysis**: Processes large-scale SNP datasets efficiently
- **Population Genetics**: Identifies population structure and cryptic relatedness
- **Statistical Modeling**: Uses moment-based estimators for kinship coefficients

## Pitfalls

- **Sample Quality**: Poor genotyping quality affects kinship estimation accuracy
- **SNP Density**: Insufficient marker density reduces estimation precision
- **Population Stratification**: Population structure can confound relatedness estimates
- **Relatedness Threshold**: Choosing appropriate thresholds for relationship classification
- **Genotyping Errors**: Errors in genotype calling propagate to kinship estimates
- **Computational Resources**: Large datasets require significant memory and processing time

## Examples

### Estimate kinship coefficients
**Args:** `king -b genotypes.bed -o kinship_results`
**Explanation:** Estimates pairwise kinship coefficients from PLINK BED format genotype data.

### Identify relatives
**Args:** `king -b data.bed --related --degree 2 -o relatives`
**Explanation:** Identifies first and second-degree relatives in the dataset.

### Quality control filtering
**Args:** `king -b genotypes.bed --qc --maf 0.05 -o filtered_data`
**Explanation:** Performs quality control filtering with minor allele frequency threshold.

### Principal component analysis
**Args:** `king -b data.bed --pca --numpcs 10 -o pca_results`
**Explanation:** Performs PCA to assess population structure.

### Association testing
**Args:** `king -b genotypes.bed -p phenotype.txt --assoc -o gwas_results`
**Explanation:** Performs basic association testing with kinship correction.

### Visualize kinship matrix
**Args:** `king -b data.bed --kinship --plot -o kinship_plot.pdf`
**Explanation:** Generates a heatmap visualization of the kinship matrix.