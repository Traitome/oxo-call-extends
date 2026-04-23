---
name: seer
category: annotation
description: sequence element (kmer) enrichment analysis
tags: [seer, annotation]
author: oxo-call-community
source_url: "https://github.com/johnlees/seer"
---

## Concepts

- **Tool Overview**: seer (v1.1.4) - sequence element (kmer) enrichment analysis
- **Core Function**: sequence element (kmer) enrichment analysis
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seer`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seer -i <input.fasta> -o <output.gff>`
**Explanation:** Run seer with typical input and output options.
