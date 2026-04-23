---
name: microscape
category: qc
description: Downstream analysis tools for amplicon sequencing — filtering, ordination, phylogeny, networks
tags: [microscape, qc]
author: oxo-call-community
source_url: "https://github.com/rec3141/microscape"
---

## Concepts

- **Tool Overview**: microscape v0.1.0 - microscape provides downstream analysis tools for amplicon sequencing data, designed to work with papa2's output. Includes sequence table QC filtering, MIMARKS metadata loading, taxonomic renormalization, phylogenetic tree construction (MAFFT + NJ), Bray-Curtis ordination (t-SNE/PCA), SparCC-style correlation networks, and JSON export for visualization..
- **Core Function**: Downstream analysis tools for amplicon sequencing — filtering, ordination, phylogeny, networks
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda microscape`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
