---
name: sankoff
category: phylogenetics
description: Fast implementation of Sankoff algorithm for phylogenetic tree reconstruction
tags: ["sankoff", "phylogenetics", "multiple-sequence-alignment"]
author: oxo-call-community
source_url: "https://github.com/hzi-bifo/sankoff"
---

## Concepts

- **Tool Overview**: Sankoff (v0.2) is a fast implementation of the Sankoff algorithm for phylogenetic tree construction, enabling weighted parsimony analysis on nucleotide sequences.
- **Core Function**: Performs simultaneous multiple sequence alignment and phylogenetic tree inference using dynamic programming.
- **Algorithm**: Implements nested dynamic programming - outer DP for tree traversal and inner DP for calculating minimum cost at each node across all possible character states.
- **Scoring Matrix**: Uses cost matrix for transitions (purine-purine or pyrimidine-pyrimidine changes) and transversions (purine-pyrimidine changes).
- **Complexity**: Runs in O(n^3 * L) time where n is the number of taxa and L is sequence length, making it feasible for moderate-sized datasets.
- **Applications**: Used for RNA structural alignments, phylogenetic inference, and evolutionary analysis with weighted character changes.

## Pitfalls

- **High Computational Cost**: The O(n^3) complexity limits application to small datasets with fewer than ~20 taxa.
- **Memory Requirements**: Dynamic programming arrays can consume significant memory for large trees.
- **Ambiguous Characters**: Handling ambiguous nucleotides (N, X) requires careful cost matrix configuration.
- **Tree Topology Dependence**: Results depend on input tree topology; incorrect trees produce incorrect alignments.
- **Parameter Sensitivity**: Cost matrix weights significantly affect alignment and tree scores.
- **Local Optima**: Greedy optimization may converge to local rather than global optima.

## Examples

### Basic phylogenetic reconstruction
**Args:** `sankoff -i sequences.fasta -o tree.nwk`
**Explanation:** `-i` input FASTA file with aligned sequences; `-o` output Newick tree file with inferred phylogeny.

### Specify cost matrix
**Args:** `sankoff -i seqs.fasta -c transition:1,transversion:2 -o result.nwk`
**Explanation:** Sets transition cost to 1 and transversion cost to 2, weighting purine/pyrimidine changes differently.

### RNA structural alignment
**Args:** `sankoff -i rna_seqs.fasta -s rna -o aligned.fasta`
**Explanation:** `-s rna` enables RNA-specific mode for simultaneous folding and alignment.

### Calculate parsimony score only
**Args:** `sankoff -i seqs.fasta --score-only`
**Explanation:** Computes the minimum parsimony score without outputting the full alignment or tree.

### Use custom tree topology
**Args:** `sankoff -i seqs.fasta -t guide_tree.nwk -o result.nwk`
**Explanation:** `-t` specifies a guide tree for constrained phylogenetic inference.

### Output alignment with tree
**Args:** `sankoff -i seqs.fasta -o tree.nwk -a aligned.fasta`
**Explanation:** Produces both the phylogenetic tree and the corresponding multiple sequence alignment.

### Verbose mode
**Args:** `sankoff -i seqs.fasta -o tree.nwk -v`
**Explanation:** `-v` enables verbose output showing progress and intermediate calculations.