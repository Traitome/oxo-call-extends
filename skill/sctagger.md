---
name: sctagger
category: utility
description: Fast and accurate matching of cellular barcodes across short- and long-reads of single-cell RNA-seq experiments
tags: [sctagger, utility]
author: oxo-call-community
source_url: "https://github.com/vpc-ccg/sctagger"
---

## Concepts

- **Tool Overview**: sctagger (v1.1.1) - Fast and accurate matching of cellular barcodes across short- and long-reads of single-cell RNA-seq experiments
- **Core Function**: Fast and accurate matching of cellular barcodes across short- and long-reads of single-cell RNA-seq experiments
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sctagger`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sctagger -i <input_file> -o <output_file>`
**Explanation:** Run sctagger with typical input and output options.
