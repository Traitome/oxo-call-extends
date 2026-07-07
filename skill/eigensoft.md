---
name: eigensoft
category: population-genomics
description: "The EIGENSOFT package implements methods for analyzing population structure and performing stratification correction"
tags: [eigensoft, population-genomics, PCA, population-structure, stratification]
author: oxo-call-community
source_url: "https://github.com/DReichLab/EIG"
---

## Concepts

- **Tool Overview**: EIGENSOFT is a comprehensive package for analyzing population structure using principal component analysis (PCA) and correcting for population stratification in genetic association studies.
- **Core Function**: Performs PCA on genotype data, detects population structure, and corrects for stratification in association testing.
- **Input/Output**: Input: Genotype data (EIGENSTRAT format, VCF). Output: PCA results, corrected genotypes, association statistics.
- **Algorithm**: Uses singular value decomposition (SVD) for PCA, smartpca for population structure analysis, and linear mixed models for stratification correction.
- **Key Features**: PCA computation, population stratification detection, association testing with correction, LD pruning, outlier removal.
- **Installation**: `conda install -c bioconda eigensoft`

## Pitfalls

- **Data Format**: Requires specific EIGENSTRAT format conversion before analysis.
- **LD Pruning**: Linkage disequilibrium pruning is essential for accurate PCA.
- **Population Outliers**: Outlier samples can distort PCA results.
- **Computation Time**: Large datasets require significant computation time.
- **Interpretation**: PCA results require careful biological interpretation.

## Examples

### Convert VCF to EIGENSTRAT
**Args:** `convertf -p par.convertfile`
**Explanation:** Converts VCF genotype data to EIGENSTRAT format.

### Run PCA analysis
**Args:** `smartpca -p par.pcafile`
**Explanation:** Performs principal component analysis on genotype data.

### Association testing
**Args:** `smartpca -p par.assocfile -a`
**Explanation:** Runs association testing with PCA correction.

### LD pruning
**Args:** `smartpca -p par.ldprunfile -l`
**Explanation:** Performs linkage disequilibrium pruning before PCA.

### Outlier detection
**Args:** `smartpca -p par.outlierfile -o`
**Explanation:** Detects and removes population outliers.