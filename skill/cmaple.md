---
name: cmaple
category: utility
description: Maximum Parsimonious Likelihood Estimation in C/C++
tags: [cmaple, maximum-likelihood, phylogenetics, c-cpp, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/iqtree/cmaple/wiki"
---

## Concepts

- **Tool Overview**: cmaple is a C/C++ implementation of Maximum Parsimonious Likelihood Estimation for phylogenetic analysis.
- **Core Function**: Performs maximum likelihood estimation with parsimony-based optimization for phylogenetic tree inference.
- **Algorithm**: Combines parsimony and likelihood approaches for efficient tree estimation.
- **Input**: Multiple sequence alignments (FASTA, PHYLIP formats).
- **Output**: Phylogenetic trees with likelihood scores.
- **Application**: Phylogenetic inference, evolutionary analysis, and tree reconstruction.
- **Installation**: Install via bioconda: `conda install -c bioconda cmaple`

## Pitfalls

- **Sequence Alignment**: Requires high-quality multiple sequence alignments.
- **Computational Resources**: May require significant resources for large datasets.
- **Memory Usage**: May require significant memory for complex analyses.
- **Parameter Tuning**: May require adjustment of likelihood parameters.
- **Model Selection**: Requires appropriate substitution model selection.

## Examples

### Infer phylogenetic tree
**Args:** `cmaple -i alignment.fasta -o tree.nwk`
**Explanation:** Infers phylogenetic tree using maximum parsimonious likelihood.

### With model specification
**Args:** `cmaple -i alignment.fasta -m GTR -o tree.nwk`
**Explanation:** Uses GTR substitution model for likelihood calculation.

### With bootstrap
**Args:** `cmaple -i alignment.fasta -b 100 -o tree.nwk`
**Explanation:** Performs 100 bootstrap replicates.

### Display help
**Args:** `cmaple --help`
**Explanation:** Shows all available options and usage information.