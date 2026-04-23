---
name: bali-phy
category: utility
description: BAli-Phy - Bayesian estimation of phylogenies and multiple sequence alignments
tags: [phylogenetics, multiple-alignment, bayesian, mcmc]
author: oxo-call-community
source_url: "https://github.com/bredelings/BAli-Phy"
---

## Concepts

- **Tool Overview**: BAli-Phy performs Bayesian estimation of phylogenies and multiple sequence alignments simultaneously, treating alignment as a parameter to be estimated.

- **Joint Estimation**: Simultaneously estimates tree topology, branch lengths, and alignment, avoiding biases from fixed alignments.

- **MCMC Sampling**: Uses Markov Chain Monte Carlo to sample from the posterior distribution of trees and alignments.

- **Uncertainty Quantification**: Provides posterior distributions for all parameters, enabling uncertainty quantification.

- **Model Flexibility**: Supports various substitution models and indel models.

## Pitfalls

- **Computational Cost**: MCMC sampling is computationally expensive. Long chains required for convergence.

- **Convergence Assessment**: Must assess MCMC convergence carefully. Use multiple chains and diagnostic tools.

- **Prior Sensitivity**: Results may be sensitive to prior choices. Test different priors.

- **Dataset Size**: Large datasets may be impractically slow. Consider reducing alignment size.

## Examples

### Basic phylogeny estimation
**Args:** `bali-phy sequences.fasta --output results/`
**Explanation:** Runs Bayesian phylogenetic analysis with alignment uncertainty.

### Specify substitution model
**Args:** `bali-phy sequences.fasta --model GTR+Gamma --output results/`
**Explanation:** Uses GTR+Gamma substitution model for nucleotide sequences.

### Set MCMC iterations
**Args:** `bali-phy sequences.fasta --iterations 1000000 --output results/`
**Explanation:** Runs 1 million MCMC iterations for better convergence.

### Multiple chains
**Args:** `bali-phy sequences.fasta --chains 4 --output results/`
**Explanation:** Runs 4 independent MCMC chains for convergence assessment.

### Protein sequences
**Args:** `bali-phy proteins.fasta --alphabet amino-acid --output results/`
**Explanation:** Analyzes protein sequences with amino acid substitution model.
