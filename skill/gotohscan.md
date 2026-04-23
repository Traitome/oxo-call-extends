---
name: gotohscan
category: alignment
description: A search tool that finds shorter sequences (usually genes) in large database sequences (chromosomes, genomes, ..) by computing all semi-global alignments.
tags: [gotohscan, alignment]
author: oxo-call-community
source_url: "https://www.bioinf.uni-leipzig.de"
---

## Concepts

- **Tool Overview**: gotohscan (v2.0) - A search tool that finds shorter sequences (usually genes) in large database sequences (chromosomes, genomes, ..) by computing all semi-global alignments.
- **Core Function**: Provides functionality for alignment tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda gotohscan`

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
