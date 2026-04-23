---
name: scrublet
category: annotation
description: Doublet prediction in single-cell RNA-sequencing data
tags: [scrublet, annotation]
author: oxo-call-community
source_url: "https://github.com/allonkleinlab/scrublet"
---

## Concepts

- **Tool Overview**: scrublet (v0.2.3) - Doublet prediction in single-cell RNA-sequencing data
- **Core Function**: Doublet prediction in single-cell RNA-sequencing data
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda scrublet`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `scrublet -i <input.fasta> -o <output.gff>`
**Explanation:** Run scrublet with typical input and output options.
