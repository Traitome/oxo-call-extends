---
name: cafe
category: population-genomics
description: Computational Analysis of gene Family Evolution
tags: [cafe, gene-family, evolution, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/hahnlab/CAFE5"
---

## Concepts

- **Tool Overview**: CAFE analyzes changes in gene family size across a phylogeny.
- **Core Function**: Tests whether gene family expansions or contractions are significant given phylogenetic history.
- **Input**: Gene family counts and species tree with branch lengths.
- **Output**: Significantly expanded/contracted gene families per branch.
- **Model**: Uses birth-death model for gene family evolution.
- **Installation**: Install via bioconda: `conda install -c bioconda cafe`

## Pitfalls

- **Tree Format**: Requires Newick tree with branch lengths in expected number of gene changes.
- **Count Table**: Gene family counts must be properly formatted.
- **Lambda Value**: May need to estimate lambda (birth-death rate) from data.
- **Multiple Testing**: Apply correction for testing many gene families.

## Examples

### Run CAFE analysis
**Args:** `cafe5 -i gene_families.tsv -t species_tree.nwk -o cafe_results/`
**Explanation:** Tests for significant gene family expansions/contractions.

### Estimate lambda parameter
**Args:** `cafe5 -i gene_families.tsv -t tree.nwk --estimate_lambda -o lambda_results/`
**Explanation:** Estimates birth-death rate parameter from gene family data.

### Run with fixed lambda
**Args:** `cafe5 -i gene_families.tsv -t tree.nwk -l 0.01 -o cafe_results/`
**Explanation:** Runs analysis with specified lambda value.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
