---
name: dna_features_viewer
category: utility
description: DNA Features Viewer - Python library for visualizing DNA features.
tags: [dna_features_viewer, utility, visualization, dna, features]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: DNA Features Viewer - Python library for visualizing DNA sequences and annotations.
- **Core Function**: Creates publication-quality visualizations of DNA features, annotations, and sequences.
- **Input/Output**: Expects DNA sequences and annotations; outputs visual diagrams.
- **Installation**: `conda install -c bioconda dna_features_viewer`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires DNA sequences and feature annotations.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dna_features_viewer --record sequence.gb --output plot.png`
**Explanation:** Visualizes DNA features from GenBank record.
