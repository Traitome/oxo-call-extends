---
name: treebest
category: analysis
description: TreeBest - Tool for phylogenetic tree construction and analysis.
tags: [treebest, phylogenetic-tree, phylogenetics, tree-construction, evolution]
author: oxo-call-community
source_url: "https://github.com/compbio/treebest"
---

## Concepts

- **Tool Overview**: TreeBest - A tool for constructing and analyzing phylogenetic trees.
- **Core Function**: Builds phylogenetic trees using various methods and performs tree analysis.
- **Input**: Sequence alignments (FASTA), distance matrices.
- **Output**: Phylogenetic trees (Newick format), tree statistics, visualization data.
- **Installation**: `pip install treebest` or `conda install -c bioconda treebest`
- **Use Case**: Phylogenetic analysis, evolutionary biology, comparative genomics.

## Pitfalls

- **Alignment Quality**: Tree quality depends on input alignment quality.
- **Computation Time**: Large datasets may be computationally intensive.

## Examples

### Build tree
**Args:** `treebest build -i alignment.fasta -o tree.nwk`
**Explanation:** Build phylogenetic tree from sequence alignment.

### Analyze tree
**Args:** `treebest analyze -i tree.nwk -o analysis.txt`
**Explanation:** Analyze phylogenetic tree properties.
