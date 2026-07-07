---
name: clearcut
category: utility
description: Reference implementation for Relaxed Neighbor Joining (RNJ) phylogenetic tree construction
tags: [clearcut, phylogenetics, neighbor-joining, tree-building, bioinformatics]
author: oxo-call-community
source_url: "http://www.mothur.org"
---

## Concepts

- **Tool Overview**: clearcut is the reference implementation for Relaxed Neighbor Joining (RNJ), a fast algorithm for constructing phylogenetic trees from distance matrices.
- **Core Function**: Builds phylogenetic trees using the Relaxed Neighbor Joining algorithm.
- **Algorithm**: Implements RNJ algorithm for fast tree construction from distance data.
- **Input**: Distance matrix or aligned sequences (FASTA).
- **Output**: Phylogenetic tree in Newick format.
- **Application**: Phylogenetic analysis, evolutionary biology, and sequence comparison.
- **Installation**: Install via bioconda: `conda install -c bioconda clearcut`

## Pitfalls

- **Distance Matrix**: Requires distance matrix or aligned sequences as input.
- **Tree Support**: Does not provide bootstrap support values by default.
- **Sequence Format**: Input sequences must be properly aligned.
- **Memory Usage**: May require significant memory for large datasets.
- **Computational Time**: May take time for large number of sequences.

## Examples

### Build tree from distance matrix
**Args:** `clearcut -i distance_matrix.txt -o tree.newick`
**Explanation:** Constructs phylogenetic tree from distance matrix.

### Build tree from aligned sequences
**Args:** `clearcut -i aligned_sequences.fasta -o tree.newick`
**Explanation:** Constructs phylogenetic tree from aligned FASTA sequences.

### With bootstrapping
**Args:** `clearcut -i aligned_sequences.fasta -b 100 -o tree.newick`
**Explanation:** Performs 100 bootstrap replicates for tree support.

### Display help
**Args:** `clearcut --help`
**Explanation:** Shows all available options and usage information.