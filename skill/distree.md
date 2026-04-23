---
name: distree
category: population-genomics
description: A tool to calculate distances between phylogenetic trees.
tags: [distree, population-genomics, phylogenetics, tree-comparison]
author: oxo-call-community
source_url: "https://github.com/PathoGenOmics-Lab/distree"
---

## Concepts

- **Tool Overview**: distree v1.0.0 - Tool for calculating distances between phylogenetic trees.
- **Core Function**: Computes tree distance metrics (Robinson-Foulds, etc.) between phylogenetic trees.
- **Input/Output**: Expects Newick tree files; outputs pairwise tree distances.
- **Installation**: `conda install -c bioconda distree`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires Newick format tree files.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `distree --tree1 tree1.nwk --tree2 tree2.nwk --output distance.txt`
**Explanation:** Calculates distance between two phylogenetic trees.
