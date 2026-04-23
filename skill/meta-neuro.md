---
name: meta-neuro
category: utility
description: Medial Tractography Analysis (MeTA)
tags: [meta-neuro, utility]
author: oxo-call-community
source_url: "https://github.com/USC-LoBeS/meta"
---

## Concepts

- **Tool Overview**: meta-neuro v2.0.1 - MeTA is a workflow implemented to minimize microstructural heterogeneity in diffusion MRI (dMRI) metrics by extracting and parcellating the core volume along the bundle length in the voxel-space directly while effectively preserving bundle shape and efficiently capturing the regional variation within and along white matter (WM) bundles..
- **Core Function**: Medial Tractography Analysis (MeTA)
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda meta-neuro`

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
