---
name: snostrip
category: annotation
description: Automatic snoRNA annotation pipeline
tags: [snostrip, annotation]
author: oxo-call-community
source_url: "http://snostrip.bioinf.uni-leipzig.de/help.py"
---

## Concepts

- **Tool Overview**: snostrip (v2.0.2) - Automatic snoRNA annotation pipeline
- **Core Function**: Automatic snoRNA annotation pipeline
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snostrip`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snostrip -i <input.fasta> -o <output.gff>`
**Explanation:** Run snostrip with typical input and output options.
