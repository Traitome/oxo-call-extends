---
name: stringmlst
category: utility
description: Fast k-mer based tool for multi locus sequence typing (MLST) directly from genome sequencing reads
tags: [stringmlst, utility]
author: oxo-call-community
source_url: "https://github.com/jordanlab/stringMLST"
---

## Concepts

- **Tool Overview**: stringmlst (v0.6.3) - Fast k-mer based tool for multi locus sequence typing (MLST) directly from genome sequencing reads
- **Core Function**: Fast k-mer based tool for multi locus sequence typing (MLST) directly from genome sequencing reads
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stringmlst`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stringmlst -i <input_file> -o <output_file>`
**Explanation:** Run stringmlst with typical input and output options.
