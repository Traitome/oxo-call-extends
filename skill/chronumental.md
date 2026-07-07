---
name: chronumental
category: phylogenetics
description: Make time trees from large phylogenetic divergence trees
tags: [chronumental, phylogenetics, time-tree, divergence, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/theosanderson/chronumental"
---

## Concepts

- **Tool Overview**: Chronumental transforms large phylogenetic divergence trees into time-calibrated trees.
- **Core Function**: Estimates divergence times from phylogenetic trees using molecular clock approaches.
- **Algorithm**: Uses maximum likelihood or Bayesian methods to estimate node ages from sequence divergence.
- **Input**: Phylogenetic tree in Newick format and sequence alignment or divergence data.
- **Output**: Time-calibrated phylogenetic tree with branch lengths in time units.
- **Application**: Molecular clock analysis, evolutionary timeline estimation, and comparative genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda chronumental`

## Pitfalls

- **Tree Quality**: Requires well-resolved phylogenetic tree for accurate time estimation.
- **Clock Assumption**: Relies on molecular clock hypothesis; may not hold for all datasets.
- **Calibration Points**: Requires fossil or other calibration points for absolute time estimation.
- **Sequence Divergence**: Saturation may affect deep divergence estimates.
- **Computational Time**: May be slow for very large trees.

## Examples

### Generate time tree
**Args:** `chronumental -i tree.newick -o time_tree.newick`
**Explanation:** Generates time-calibrated tree from phylogenetic divergence tree.

### With calibration points
**Args:** `chronumental -i tree.newick -c calibrations.txt -o time_tree.newick`
**Explanation:** Uses calibration points for absolute time estimation.

### From alignment
**Args:** `chronumental -a alignment.fasta -o time_tree.newick`
**Explanation:** Generates time tree directly from sequence alignment.

### Display help
**Args:** `chronumental --help`
**Explanation:** Shows all available options and usage information.