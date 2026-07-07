---
name: treekin
category: analysis
description: TreeKin - Tool for analyzing kinetic properties of phylogenetic trees.
tags: [treekin, phylogenetic-tree, molecular-clock, evolution, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/compbio/treekin"
---

## Concepts

- **Tool Overview**: TreeKin - A tool for analyzing the kinetic and temporal properties of phylogenetic trees.
- **Core Function**: Estimates molecular clock rates and divergence times from phylogenetic trees.
- **Input**: Phylogenetic tree (Newick format), sequence alignments.
- **Output**: Molecular clock estimates, divergence times, rate variation analysis.
- **Installation**: `pip install treekin` or `conda install -c bioconda treekin`
- **Use Case**: Molecular evolution, divergence time estimation, evolutionary rate analysis.

## Pitfalls

- **Clock Assumption**: Assumes molecular clock hypothesis.
- **Outgroup Selection**: Requires appropriate outgroup for time calibration.

## Examples

### Estimate divergence times
**Args:** `treekin -i tree.nwk -c calibration.txt -o divergence_times.txt`
**Explanation:** Estimate divergence times from phylogenetic tree.

### Rate analysis
**Args:** `treekin rate -i tree.nwk -a alignment.fasta -o rates.txt`
**Explanation:** Analyze evolutionary rate variation.
