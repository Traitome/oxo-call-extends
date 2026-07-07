---
name: tree-qmc
category: analysis
description: TreeQMC - Tool for quartet-based phylogenetic tree inference.
tags: [tree-qmc, phylogenetic-tree, quartet-method, phylogenetics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/compbio/tree-qmc"
---

## Concepts

- **Tool Overview**: TreeQMC - A tool for inferring phylogenetic trees using quartet-based methods.
- **Core Function**: Constructs trees by combining quartet topologies using QMC (Quartet MaxCut) algorithm.
- **Input**: Sequence alignments (FASTA), distance matrices.
- **Output**: Phylogenetic trees (Newick format), support values.
- **Installation**: `pip install tree-qmc` or `conda install -c bioconda tree-qmc`
- **Use Case**: Phylogenetic analysis, large-scale tree inference, evolutionary studies.

## Pitfalls

- **Computational Complexity**: May be computationally intensive for large datasets.
- **Memory**: Requires significant memory for large alignments.

## Examples

### Infer tree
**Args:** `tree-qmc -i alignment.fasta -o tree.nwk`
**Explanation:** Infer phylogenetic tree using quartet methods.

### With distance matrix
**Args:** `tree-qmc -d distance_matrix.txt -o tree.nwk`
**Explanation:** Build tree from distance matrix.
