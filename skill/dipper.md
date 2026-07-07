---
name: dipper
category: population-genomics
description: DIPPER - Ultrafast phylogenetic tree reconstruction on GPUs.
tags: [dipper, population-genomics, phylogenetics, gpu, tree-reconstruction]
author: oxo-call-community
source_url: "https://github.com/TurakhiaLab/DIPPER"
---

## Concepts

- **Tool Overview**: DIPPER (v0.1.4+) is an ultrafast phylogenetic tree reconstruction tool using GPU acceleration.
- **Core Function**: Reconstructs large phylogenetic trees (up to 10M taxa) using distance-based methods on GPUs.
- **Input/Output**: Input: Multiple sequence alignments or distance matrices. Output: Phylogenetic trees (Newick format).
- **Algorithm**: Uses FastME or neighbor-joining algorithms accelerated on GPU hardware.
- **Key Features**: GPU acceleration, ultra-fast tree building, supports large datasets (10M+ taxa), memory efficient, multiple output formats.
- **Installation**: `conda install -c bioconda dipper`

## Pitfalls

- **Hardware Requirements**: Requires GPU for optimal performance.
- **Input Format**: Must provide aligned sequences or pre-computed distance matrix.
- **Memory Usage**: Large datasets require significant GPU memory.
- **Alignment Quality**: Poor alignments affect tree accuracy.
- **Algorithm Selection**: Choosing appropriate algorithm for dataset size.

## Examples

### Reconstruct phylogenetic tree
**Args:** `dipper --input alignment.fa --output tree.nwk`
**Explanation:** Reconstructs phylogenetic tree using GPU acceleration.

### Use distance matrix
**Args:** `dipper --input distances.tsv --output tree.nwk --matrix`
**Explanation:** Use pre-computed distance matrix for tree building.

### With bootstrap support
**Args:** `dipper --input alignment.fa --output tree.nwk --bootstrap 100`
**Explanation:** Compute bootstrap support values for tree nodes.

### Large dataset mode
**Args:** `dipper --input alignment.fa --output tree.nwk --large`
**Explanation:** Use optimized mode for large datasets.

### Multiple output formats
**Args:** `dipper --input alignment.fa --output tree.nwk --format newick,nexus`
**Explanation:** Generate tree in multiple formats.