---
name: mashtree
category: utility
description: Creates phylogenetic trees using Mash distances for whole-genome comparison.
tags: [mashtree, phylogenetics, tree building, MinHash]
author: oxo-call-community
source_url: "https://github.com/lskatz/mashtree"
---

## Concepts

- **Tool Overview**: Mashtree constructs phylogenetic trees using Mash distances.
- **Core Function**: Computes pairwise distances and builds trees without full alignment.
- **Distance Calculation**: Uses MinHash to estimate genome distances efficiently.
- **Tree Construction**: Implements neighbor-joining or UPGMA algorithms.
- **Input/Output**: Accepts FASTA/Q files, produces Newick format trees.
- **Installation**: `conda install -c bioconda mashtree`

## Pitfalls

- **Computational Time**: Large datasets require significant computation time.
- **Memory Usage**: High memory requirements for large numbers of sequences.
- **Tree Resolution**: May not resolve closely related strains with high similarity.
- **Parameter Sensitivity**: k-mer size and sketch parameters affect tree topology.
- **Outgroup Selection**: Rooting trees requires appropriate outgroup selection.
- **Sequence Quality**: Low-quality sequences can distort tree topology.

## Examples

### Build tree from FASTA files
**Args:** `mashtree *.fasta > tree.nwk`
**Explanation:** Creates phylogenetic tree from all FASTA files.

### Specify output file
**Args:** `mashtree --outtree tree.nwk *.fasta`
**Explanation:** Writes tree to specified output file.

### Use neighbor-joining
**Args:** `mashtree --method nj *.fasta > tree.nwk`
**Explanation:** Uses neighbor-joining algorithm for tree construction.

### Custom k-mer size
**Args:** `mashtree -k 31 *.fasta > tree.nwk`
**Explanation:** Uses 31-mers for MinHash computation.

### Parallel processing
**Args:** `mashtree --cpus 8 *.fasta > tree.nwk`
**Explanation:** Uses 8 threads for parallel computation.

### Add bootstrap support
**Args:** `mashtree --bootstrap 100 *.fasta > tree.nwk`
**Explanation:** Computes bootstrap support with 100 replicates.
