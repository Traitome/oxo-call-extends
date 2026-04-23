---
name: deltapd
category: population-genomics
description: DeltaPD is a tool used to determine outliers in a gene tree when compared against a reference tree.
tags: [deltapd, population-genomics, phylogenetics, outlier-detection]
author: oxo-call-community
source_url: "https://github.com/Ecogenomics/DeltaPD"
---

## Concepts

- **Tool Overview**: DeltaPD v0.1.5 - Tool for detecting outlier genes in phylogenetic trees by comparing gene trees against a reference species tree.
- **Core Function**: Identifies genes with unusual evolutionary patterns by measuring phylogenetic distance between gene and reference trees.
- **Input/Output**: Expects Newick tree files; outputs outlier gene classifications with distance metrics.
- **Installation**: `conda install -c bioconda deltapd`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires properly rooted Newick tree files.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `deltapd --reference species.nwk --input genes/ --output outliers.tsv`
**Explanation:** Identifies outlier gene trees compared to reference tree.
