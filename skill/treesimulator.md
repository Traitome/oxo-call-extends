---
name: treesimulator
category: simulation
description: TreeSimulator - Tool for simulating phylogenetic trees.
tags: [treesimulator, phylogenetic-tree, simulation, evolution, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/compbio/treesimulator"
---

## Concepts

- **Tool Overview**: TreeSimulator - A tool for simulating phylogenetic trees under various evolutionary models.
- **Core Function**: Generates simulated trees using coalescent, birth-death, and other models.
- **Input**: Simulation parameters, sequence length, model specification.
- **Output**: Simulated trees (Newick format), simulation statistics.
- **Installation**: `pip install treesimulator` or `conda install -c bioconda treesimulator`
- **Use Case**: Phylogenetic method testing, simulation studies, benchmarking.

## Pitfalls

- **Model Assumptions**: Results depend on model assumptions.
- **Parameter Selection**: Requires careful parameter selection.

## Examples

### Simulate tree
**Args:** `treesimulator -m coalescent -n 100 -o simulated_tree.nwk`
**Explanation:** Simulate phylogenetic tree under coalescent model.

### Birth-death model
**Args:** `treesimulator -m birth-death -b 1.0 -d 0.5 -n 50 -o tree.nwk`
**Explanation:** Simulate tree using birth-death model.
