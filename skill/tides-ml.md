---
name: tides-ml
category: annotation
description: Tool for ORF-calling and ORF-classification using ML approaches.
tags: [tides-ml, annotation]
author: oxo-call-community
source_url: "https://github.com/xxmalcala/TIdeS"
---

## Concepts

- **Tool Overview**: tides-ml (v1.3.5) - Tool for ORF-calling and ORF-classification using ML approaches.
- **Core Function**: Tool for ORF-calling and ORF-classification using ML approaches.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tides-ml`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tides-ml -i <input.fasta> -o <output.gff>`
**Explanation:** Run tides-ml with typical input and output options.
