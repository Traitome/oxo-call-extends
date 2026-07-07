---
name: dist_est
category: population-genomics
description: dist_est - Estimation of Rates-Across-Sites Distributions in Phylogenetic Substitution Models.
tags: [dist_est, population-genomics, phylogenetics, rates-across-sites, substitution-model]
author: oxo-call-community
source_url: "https://github.com/abacus-gene/dist_est"
---

## Concepts

- **Tool Overview**: dist_est (v1.1+) is a tool for estimating rates-across-sites distributions in phylogenetic models.
- **Core Function**: Estimates the distribution of substitution rates across sites in phylogenetic analyses.
- **Input/Output**: Input: Multiple sequence alignments (FASTA/PHYLIP). Output: Rate distribution parameters, site-specific rates.
- **Algorithm**: Uses maximum likelihood or Bayesian methods to estimate rate distributions.
- **Key Features**: Rate distribution estimation, site-specific rate calculation, supports multiple models, visualization, statistical testing.
- **Installation**: `conda install -c bioconda dist_est`

## Pitfalls

- **Input Requirements**: Requires aligned sequences.
- **Alignment Quality**: Poor alignments affect rate estimation.
- **Model Selection**: Appropriate substitution model selection is critical.
- **Computational Time**: May be slow for large datasets.
- **Convergence**: MCMC methods require proper convergence diagnostics.

## Examples

### Estimate rate distribution
**Args:** `dist_est --alignment sequences.fa --output rates.txt`
**Explanation:** Estimates rate distribution across sites.

### With specific model
**Args:** `dist_est --alignment sequences.fa --output rates.txt --model GTR`
**Explanation:** Use GTR substitution model for rate estimation.

### Site-specific rates
**Args:** `dist_est --alignment sequences.fa --output rates.txt --site-rates`
**Explanation:** Output site-specific substitution rates.

### Bayesian estimation
**Args:** `dist_est --alignment sequences.fa --output rates.txt --bayesian`
**Explanation:** Use Bayesian method for rate estimation.

### Generate visualization
**Args:** `dist_est --alignment sequences.fa --output rates.txt --plot rates.png`
**Explanation:** Generate visualization of rate distribution.