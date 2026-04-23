---
name: scrubby
category: alignment
description: Read depletion/extraction and database cleaning using k-mer and alignment methods
tags: [scrubby, alignment]
author: oxo-call-community
source_url: "https://github.com/esteinig/scrubby"
---

## Concepts

- **Tool Overview**: scrubby (v0.2.1) - Read depletion/extraction and database cleaning using k-mer and alignment methods
- **Core Function**: Read depletion/extraction and database cleaning using k-mer and alignment methods
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda scrubby`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `scrubby -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run scrubby with typical input and output options.
