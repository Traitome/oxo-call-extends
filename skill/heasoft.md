---
name: heasoft
category: alignment
description: NASA High Energy Astrophysics Software (HEAsoft)
tags: [heasoft, alignment, SAM]
author: oxo-call-community
source_url: "https://heasarc.gsfc.nasa.gov/docs/software/heasoft"
---

## Concepts

- **Tool Overview**: heasoft (v6.35.2) - NASA High Energy Astrophysics Software (HEAsoft)
- **Core Function**: Provides functionality for alignment tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda heasoft`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
