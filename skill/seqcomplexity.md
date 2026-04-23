---
name: seqcomplexity
category: utility
description: Calculates Per-Read and Total Sequence Complexity from FastQ file.
tags: [seqcomplexity, utility, fastq]
author: oxo-call-community
source_url: "https://github.com/stevenweaver/seqcomplexity"
---

## Concepts

- **Tool Overview**: seqcomplexity (v0.1.2) - Calculates Per-Read and Total Sequence Complexity from FastQ file.
- **Core Function**: Calculates Per-Read and Total Sequence Complexity from FastQ file.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seqcomplexity`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seqcomplexity -i <input_file> -o <output_file>`
**Explanation:** Run seqcomplexity with typical input and output options.
