---
name: ucsc-chaincleaner
category: alignment
description: Remove chain-breaking alignments from chains that break nested chains.
tags: [ucsc-chaincleaner, alignment]
author: oxo-call-community
source_url: "http://hgdownload.cse.ucsc.edu/admin/exe/"
---

## Concepts

- **Tool Overview**: ucsc-chaincleaner (v455) - Remove chain-breaking alignments from chains that break nested chains.
- **Core Function**: Remove chain-breaking alignments from chains that break nested chains.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda ucsc-chaincleaner`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
