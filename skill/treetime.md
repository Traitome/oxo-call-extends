---
name: treetime
category: analysis
description: TreeTime - Tool for molecular clock analysis and ancestral sequence reconstruction.
tags: [treetime, molecular-clock, phylogenetics, ancestral-reconstruction, evolution]
author: oxo-call-community
source_url: "https://github.com/neherlab/treetime"
---

## Concepts

- **Tool Overview**: TreeTime - A tool for molecular clock analysis and ancestral sequence reconstruction.
- **Core Function**: Estimates evolutionary rates, divergence times, and reconstructs ancestral sequences.
- **Input**: Phylogenetic tree (Newick format), sequence alignment, sampling dates.
- **Output**: Time-calibrated tree, ancestral sequences, evolutionary rates.
- **Installation**: `pip install treetime`
- **Use Case**: Molecular evolution, time-scaled phylogenies, viral evolution.

## Pitfalls

- **Clock Assumption**: Requires molecular clock assumption.
- **Calibration**: Needs temporal calibration points.

## Examples

### Time-calibrate tree
**Args:** `treetime --tree tree.nwk --aln alignment.fasta --dates dates.txt`
**Explanation:** Time-calibrate phylogenetic tree using molecular clock.

### Ancestral reconstruction
**Args:** `treetime ancestral --tree tree.nwk --aln alignment.fasta -o ancestors/`
**Explanation:** Reconstruct ancestral sequences.
