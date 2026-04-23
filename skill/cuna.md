---
name: cuna
category: utility
description: CUNA: Cytosine Uracil Neural Algorithm for ancient DNA damage detection using nanopore signals.
tags: [cuna, utility]
author: oxo-call-community
source_url: "https://github.com/iris1901/CUNA"
---

## Concepts

- **Tool Overview**: cuna (v0.3.0) - CUNA: Cytosine Uracil Neural Algorithm for ancient DNA damage detection using nanopore signals.
- **Core Function**: CUNA is a deep learning pipeline for detecting cytosine deamination (C→U) events in ancient DNA, using raw nanopore signals. It includes feature extraction, model training, and modification detection.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cuna`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `--input input_file --output output_file`
**Explanation:** Process input and generate output
