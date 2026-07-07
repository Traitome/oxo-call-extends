---
name: dapcy
category: population-genomics
description: sklearn implementation of discriminant analysis of principal components (DAPC) for population genetics
tags: [dapcy, population-genomics, DAPC, population-structure, sklearn]
author: oxo-call-community
source_url: "https://uhasselt-bioinfo.gitlab.io/dapcy"
---

## Concepts

- **Tool Overview**: dapcy (v1.3.1+) is a scikit-learn implementation of Discriminant Analysis of Principal Components (DAPC) for population genetics.
- **Core Function**: Performs DAPC analysis to identify and describe clusters of genetically related individuals.
- **Input/Output**: Input: Genotype matrix, VCF, or PLINK files. Output: Cluster assignments, discriminant functions.
- **Algorithm**: Combines PCA for dimensionality reduction with discriminant analysis for cluster optimization.
- **Key Features**: sklearn-compatible API, handles large datasets, supports cross-validation.
- **Installation**: `conda install -c bioconda dapcy`

## Pitfalls

- **Population Structure**: Requires meaningful population structure for successful analysis.
- **Sample Size**: Small sample sizes may lead to overfitting.
- **Genetic Data Quality**: Results depend on genotype data quality.
- **Cluster Number**: Selecting optimal cluster number requires cross-validation.
- **Interpretation**: Results require biological interpretation.

## Examples

### Run DAPC analysis
**Args:**
```python
import dapcy
import pandas as pd

# Load genotype data
data = pd.read_csv('genotypes.csv')
result = dapcy.dapc(data, n_clusters=3)
print(result.cluster_labels_)
```
**Explanation:** Perform DAPC analysis with 3 clusters.

### Cross-validate cluster number
**Args:**
```python
import dapcy
result = dapcy.find_clusters(data, max_clusters=10, cv=5)
print(result.optimal_clusters)
```
**Explanation:** Find optimal cluster number using cross-validation.

### Access discriminant functions
**Args:**
```python
import dapcy
result = dapcy.dapc(data, n_clusters=3)
print(result.discriminant_functions)
```
**Explanation:** Extract discriminant functions for further analysis.
