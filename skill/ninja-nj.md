---
name: ninja-nj
category: phylogenetics
description: NINJA-NJ is a fast Neighbor-Joining algorithm for large-scale phylogenetic reconstruction.
tags: [ninja-nj, phylogenetics, neighbor-joining, tree-building]
author: oxo-call-community
source_url: "https://github.com/TravisWheelerLab/NINJA"
---

## Concepts

- **Tool Overview**: NINJA-NJ performs fast Neighbor-Joining tree construction for large datasets.
- **Core Function**: Builds phylogenetic trees from distance matrices.
- **Algorithm**: Implements efficient Neighbor-Joining algorithm for large-scale data.
- **Input Format**: Accepts FASTA sequences or distance matrices.
- **Output**: Produces Newick format phylogenetic trees.
- **Use Case**: Phylogenetic analysis, evolutionary biology, and metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Tree building can be computationally intensive.
- **Distance Matrix**: Requires appropriate distance calculation.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Tree Validation**: Results should be validated with other methods.

## Examples

### Display help
**Args:** `ninja-nj --help`
**Explanation:** Shows available options and usage instructions.

### Build tree from sequences
**Args:** `ninja-nj -i sequences.fasta -o tree.newick`
**Explanation:** Builds phylogenetic tree from FASTA sequences.

### Build tree from distance matrix
**Args:** `ninja-nj -d distance.matrix -o tree.newick`
**Explanation:** Builds tree from precomputed distance matrix.

### Bootstrapping
**Args:** `ninja-nj -i sequences.fasta -b 100 -o tree.newick`
**Explanation:** Performs 100 bootstrap replicates.

### Threads
**Args:** `ninja-nj -i sequences.fasta -t 8 -o tree.newick`
**Explanation:** Uses 8 threads for parallel processing.

### Output support values
**Args:** `ninja-nj -i sequences.fasta -s -o tree.newick`
**Explanation:** Includes bootstrap support values in tree.

### Verbose mode
**Args:** `ninja-nj -i sequences.fasta -v -o tree.newick`
**Explanation:** Runs with verbose output.