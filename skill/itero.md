---
name: itero
category: alignment
description: A pipeline for iterative, guided contig assembly that integrates spades, bwa, and samtools to produce assembled contigs.
tags: [itero, alignment, SAM]
author: oxo-call-community
source_url: "https://github.com/faircloth-lab/itero"
---

## Concepts

- **Tool Overview**: itero (v1.1.2) - A pipeline for iterative, guided contig assembly that integrates spades, bwa, and samtools to produce assembled contigs.
- **Core Function**: Provides functionality for alignment tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda itero`

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
