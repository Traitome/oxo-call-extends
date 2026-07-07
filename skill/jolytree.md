---
name: jolytree
category: alignment
description: Fast alignment-free phylogenetic reconstruction from genome sequences.
tags: [jolytree, alignment, phylogenetics, genomics, tree]
author: oxo-call-community
source_url: "https://research.pasteur.fr/fr/software/jolytree/"
---

## Concepts

- **Tool Overview**: jolytree (v2.1) - A fast alignment-free phylogenetic reconstruction tool for genome sequences.
- **Alignment-Free**: Uses k-mer based approaches instead of sequence alignment.
- **Genome Comparison**: Compares whole genomes efficiently.
- **Phylogenetic Trees**: Constructs phylogenetic trees from genomic data.
- **Scalable**: Handles large datasets with many genomes.
- **Distance Metrics**: Implements various distance metrics for genome comparison.

## Pitfalls

- **Genome Quality**: Low-quality genomes can affect tree accuracy.
- **k-mer Selection**: Choosing appropriate k-mer size is critical.
- **Horizontal Transfer**: Horizontal gene transfer can confound phylogenetic signals.
- **Genome Size**: Very different genome sizes can affect comparison.
- **Computational Resources**: Large datasets require significant resources.
- **Tree Validation**: Requires validation with other methods.

## Examples

### Build phylogenetic tree
**Args:** `jolytree -i genomes/ -o tree.nwk`
**Explanation:** Builds phylogenetic tree from genome sequences in directory.

### Specify k-mer size
**Args:** `jolytree -i genomes/ -o tree.nwk -k 21`
**Explanation:** Uses k-mer size of 21 for genome comparison.

### Generate distance matrix
**Args:** `jolytree -i genomes/ -d distances.txt -o tree.nwk`
**Explanation:** Outputs pairwise distance matrix along with tree.

### Use specific distance metric
**Args:** `jolytree -i genomes/ -o tree.nwk -m jaccard`
**Explanation:** Uses Jaccard distance metric for comparison.

### Bootstrap analysis
**Args:** `jolytree -i genomes/ -o tree.nwk --bootstrap 100`
**Explanation:** Performs bootstrap analysis with 100 replicates.

### Root tree
**Args:** `jolytree -i genomes/ -o tree.nwk --root outgroup.fasta`
**Explanation:** Roots tree using specified outgroup genome.