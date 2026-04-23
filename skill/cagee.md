---
name: cagee
category: population-genomics
description: Analyzes changes in gene expression accounting for phylogenetic history
tags: [cagee, gene-expression, evolution, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/hahnlab/CAGEE"
---

## Concepts

- **Tool Overview**: CAGEE analyzes evolutionary changes in gene expression with phylogenetic context.
- **Core Function**: Tests for significant expression changes while accounting for phylogenetic relationships.
- **Input**: Gene expression data and species phylogeny.
- **Output**: Genes with significant expression changes per branch.
- **Model**: Uses phylogenetic comparative methods for expression evolution.
- **Installation**: Install via bioconda: `conda install -c bioconda cagee`

## Pitfalls

- **Tree Required**: Requires properly rooted phylogenetic tree.
- **Expression Normalization**: Input data should be properly normalized.
- **Branch Lengths**: Tree must have meaningful branch lengths.

## Examples

### Run expression evolution analysis
**Args:** `cagee -i expression.tsv -t species_tree.nwk -o results/`
**Explanation:** Tests for significant expression changes across phylogeny.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
