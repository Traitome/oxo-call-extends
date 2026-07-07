---
name: mammal
category: utility
description: Accelerated Estimation of Frequency Classes in Site-heterogeneous Profile Mixture Models
tags: [mammal, utility, phylogenetics, mixture-models]
author: oxo-call-community
source_url: "https://www.mathstat.dal.ca/~tsusko/doc/mammal.pdf"
---

## Concepts

- **Tool Overview**: mammal v1.1.1 - A tool for accelerated estimation of frequency classes in site-heterogeneous profile mixture models for phylogenetic analysis.
- **Core Function**: Efficiently computes frequency classes for profile mixture models used in phylogenetic inference.
- **Input/Output**: Input: Alignment files, model parameters; Output: Frequency class estimates, log-likelihood values.
- **Installation**: `conda install -c bioconda mammal`
- **Site-heterogeneous Models**: Models that allow different substitution patterns at different sites.
- **Accelerated Computation**: Uses optimized algorithms for faster likelihood calculations.

## Pitfalls

- **Model Complexity**: Complex models require careful parameter tuning.
- **Memory Usage**: Large datasets may require significant memory.
- **Computational Time**: Complex models can be computationally intensive.
- **Alignment Quality**: Poor quality alignments affect model fit.
- **Parameter Sensitivity**: Results may vary with different parameter settings.
- **Convergence**: Models may require many iterations to converge.

## Examples

### Basic model estimation
**Args:** `mammal -i alignment.fasta -o results.txt -m LG+G`
**Explanation:** Estimates frequency classes using LG+G model.

### Site-heterogeneous model
**Args:** `mammal -i alignment.fasta -o results.txt -m C60`
**Explanation:** Uses C60 site-heterogeneous model.

### With bootstrap
**Args:** `mammal -i alignment.fasta -o results.txt -m LG+G -b 100`
**Explanation:** Runs 100 bootstrap replicates.

### Verbose mode
**Args:** `mammal -i alignment.fasta -o results.txt -m LG+G -v`
**Explanation:** Provides detailed logging during estimation.

### Custom parameters
**Args:** `mammal -i alignment.fasta -o results.txt -m LG+G -a 0.5`
**Explanation:** Sets alpha parameter to 0.5.

### Generate tree
**Args:** `mammal -i alignment.fasta -o results.txt -m LG+G --tree`
**Explanation:** Generates phylogenetic tree with estimates.