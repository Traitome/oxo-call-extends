---
name: bayescode
category: population-genomics
description: BayesCode - Mutation-Selection phylogenetic codon models for detecting adaptive evolution
tags: [bayescode, population-genomics, phylogenetic, codon-models, adaptive-evolution]
author: oxo-call-community
source_url: "https://github.com/ThibaultLatrille/bayescode/wiki"
---

## Concepts

- **Tool Overview**: BayesCode (v1.3.4) uses mutation-selection phylogenetic codon models to detect site-specific adaptive evolution or infer long-term effective population size.
- **Core Function**: Applies Bayesian mutation-selection models to detect adaptive evolution and estimate population parameters.
- **Codon Models**: Uses codon-level substitution models to analyze evolutionary patterns.
- **Adaptive Evolution**: Detects site-specific positive selection across phylogenetic trees.
- **Population Size**: Infers long-term effective population size from sequence data.
- **Input/Output**: Accepts FASTA alignments and tree files; outputs selection statistics.
- **Installation**: `conda install -c bioconda bayescode`.

## Pitfalls

- **Sequence Quality**: Requires high-quality alignments for accurate inference.
- **Computational Time**: MCMC sampling can be computationally intensive.
- **Convergence Check**: MCMC chains require convergence validation.
- **Model Selection**: Choice of model affects results; consider model comparison.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Detect adaptive evolution
**Args:** `bayescode -i alignment.fasta -t tree.nwk -o results/`
**Explanation:** Runs mutation-selection model to detect adaptive evolution.

### Infer population size
**Args:** `bayescode -i alignment.fasta -t tree.nwk --pop-size -o results/`
**Explanation:** Infers long-term effective population size.

### Specify model parameters
**Args:** `bayescode -i alignment.fasta -t tree.nwk --omega 0.5 -o results/`
**Explanation:** Sets initial omega parameter for selection strength.

### Number of iterations
**Args:** `bayescode -i alignment.fasta -t tree.nwk --iter 100000 -o results/`
**Explanation:** Runs MCMC with specified number of iterations.

### Sample from posterior
**Args:** `bayescode -i alignment.fasta -t tree.nwk --sample 1000 -o results/`
**Explanation:** Samples 1000 posterior estimates.

### Generate convergence diagnostics
**Args:** `bayescode -i alignment.fasta -t tree.nwk --diagnostics -o results/`
**Explanation:** Outputs convergence diagnostics for MCMC.

### Display help
**Args:** `bayescode --help`
**Explanation:** Shows all available command-line options and usage information.