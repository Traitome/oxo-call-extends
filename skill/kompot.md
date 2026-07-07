---
name: kompot
category: expression
description: Differential abundance and gene expression analysis using Mahalanobis distance with JAX backend
tags: [kompot, expression, differential-expression, JAX, Mahalanobis, GPU-accelerated]
author: oxo-call-community
source_url: "https://github.com/settylab/kompot"
---

## Concepts

- **Differential Analysis**: Performs differential abundance and expression analysis
- **Gaussian Process Methods**: Uses Gaussian process-based statistical methods
- **Mahalanobis Distance**: Calculates Mahalanobis distance for multivariate comparisons
- **GPU Acceleration**: Uses JAX backend for fast GPU-accelerated computation
- **Batch Effect Correction**: Corrects for batch effects in omics data
- **Confidence Intervals**: Provides uncertainty quantification

## Pitfalls

- **Sample Size**: Small sample sizes affect statistical power
- **GPU Requirements**: GPU recommended for large datasets
- **Data Distribution**: Assumes approximate Gaussian distributions
- **Missing Data**: Cannot handle missing values directly
- **Computational Resources**: Large datasets require significant GPU memory
- **Parameter Tuning**: Hyperparameter selection affects results

## Examples

### Differential expression analysis
**Args:** `kompot de -i expression.tsv -c conditions.txt -o results/`
**Explanation:** Performs differential expression analysis.

### Differential abundance
**Args:** `kompot da -i abundance.tsv -c groups.txt -o results/`
**Explanation:** Analyzes differential abundance between groups.

### GPU acceleration
**Args:** `kompot de -i data.tsv -c conditions.txt -o results/ --gpu`
**Explanation:** Uses GPU acceleration for faster computation.

### With covariates
**Args:** `kompot de -i data.tsv -c conditions.txt -cov covariates.txt -o results/`
**Explanation:** Includes covariates in differential analysis.

### Generate visualizations
**Args:** `kompot visualize -i results/ -o plots/`
**Explanation:** Creates visualization of differential results.

### Batch processing
**Args:** `kompot batch -d datasets/ -o results/`
**Explanation:** Processes multiple datasets in batch mode.