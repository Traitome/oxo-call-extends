---
name: sina
category: population-genomics
description: Reference based multiple sequence alignment
tags: [sina, population-genomics]
author: oxo-call-community
source_url: "https://sina.readthedocs.io"
---

## Concepts

- **Tool Overview**: sina (v1.7.2) - Reference based multiple sequence alignment
- **Core Function**: Reference based multiple sequence alignment
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sina`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sina -i <input.vcf> -o <output_dir>`
**Explanation:** Run sina with typical input and output options.
