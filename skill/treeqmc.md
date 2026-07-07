---
name: treeqmc
category: analysis
description: TreeQMC - Tool for quartet-based phylogenetic tree construction.
tags: [treeqmc, phylogenetic-tree, quartet, phylogenetics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/compbio/treeqmc"
---

## Concepts

- **Tool Overview**: TreeQMC - A tool for constructing phylogenetic trees using quartet maximum compatibility.
- **Core Function**: Builds trees by maximizing the number of compatible quartet topologies.
- **Input**: Sequence data, quartet topologies.
- **Output**: Phylogenetic tree (Newick format), compatibility scores.
- **Installation**: `pip install treeqmc` or `conda install -c bioconda treeqmc`
- **Use Case**: Phylogenetic inference, evolutionary analysis, tree reconciliation.

## Pitfalls

- **Quartet Selection**: Requires appropriate quartet sampling strategy.
- **Large Datasets**: May be slow for very large datasets.

## Examples

### Build tree
**Args:** `treeqmc -i sequences.fasta -o tree.nwk`
**Explanation:** Construct phylogenetic tree using quartet compatibility.

### With bootstrap
**Args:** `treeqmc -i alignment.fasta -b -o tree_with_bootstrap.nwk`
**Explanation:** Build tree with bootstrap support.
