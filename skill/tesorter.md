---
name: tesorter
category: annotation
description: Lineage-level classification of transposable elements using conserved protein domains.
tags: [tesorter, annotation]
author: oxo-call-community
source_url: "https://github.com/zhangrengang/TEsorter/blob/v1.5.1/README.md"
---

## Concepts

- **Tool Overview**: tesorter (v1.5.1) - Lineage-level classification of transposable elements using conserved protein domains.
- **Core Function**: Lineage-level classification of transposable elements using conserved protein domains.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tesorter`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tesorter -i <input.fasta> -o <output.gff>`
**Explanation:** Run tesorter with typical input and output options.
