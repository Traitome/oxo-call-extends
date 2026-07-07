---
name: mrbayes
category: utility
description: Bayesian Inference of Phylogeny using Markov chain Monte Carlo methods.
tags: [mrbayes, utility, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/NBISweden/MrBayes"
---

## Concepts

- **Tool Overview**: MrBayes v3.2.7 performs Bayesian inference of phylogenetic trees.
- **Core Function**: Estimates posterior distribution of model parameters using MCMC.
- **Bayesian Inference**: Uses Bayesian statistical methods for tree reconstruction.
- **MCMC Methods**: Markov Chain Monte Carlo for posterior sampling.
- **Model Selection**: Supports various evolutionary models.
- **Input/Output**: Accepts sequence alignments; outputs phylogenetic trees and statistics.

## Pitfalls

- **Computational Time**: MCMC analysis can be computationally intensive.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require careful parameter adjustment.
- **Convergence Check**: Requires checking MCMC convergence.
- **Prior Specification**: Priors can affect results significantly.
- **Long Runs**: May require long MCMC runs for convergence.

## Examples

### Run Bayesian inference
**Args:** `mb input.nex`
**Explanation:** Runs MrBayes with input NEXUS file.

### With multiple chains
**Args:** `mb -n 4 input.nex`
**Explanation:** Uses 4 MCMC chains.

### Specify model
**Args:** `mb -m GTR+G input.nex`
**Explanation:** Uses GTR model with gamma distribution.

### Set run length
**Args:** `mb -l 1000000 input.nex`
**Explanation:** Runs MCMC for 1,000,000 generations.

### Check convergence
**Args:** `mb -c trace.txt`
**Explanation:** Analyzes MCMC trace for convergence.