---
name: dipper
category: population-genomics
description: DIPPER - An ultrafast tool for phylogenetic tree reconstruction on GPUs.
tags: [dipper, population-genomics, phylogenetics, gpu, tree-reconstruction]
author: oxo-call-community
source_url: "https://github.com/TurakhiaLab/DIPPER"
---

## Concepts

- **Tool Overview**: DIPPER v0.1.4 - Ultrafast phylogenetic tree reconstruction tool using GPU acceleration.
- **Core Function**: Reconstructs large phylogenetic trees (up to 10M taxa) using distance-based methods on GPUs.
- **Input/Output**: Expects multiple sequence alignments or distance matrices; outputs phylogenetic trees.
- **Installation**: `conda install -c bioconda dipper`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Hardware**: Requires GPU for optimal performance.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dipper --input alignment.fa --output tree.nwk`
**Explanation:** Reconstructs phylogenetic tree using GPU acceleration.
