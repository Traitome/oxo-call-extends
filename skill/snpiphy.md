---
name: snpiphy
category: population-genomics
description: An automated snp phylogeny pipeline
tags: [snpiphy, population-genomics]
author: oxo-call-community
source_url: "https://github.com/bogemad/snpiphy"
---

## Concepts

- **Tool Overview**: snpiphy (v0.5) - An automated snp phylogeny pipeline
- **Core Function**: An automated snp phylogeny pipeline
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snpiphy`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snpiphy -i <input.vcf> -o <output_dir>`
**Explanation:** Run snpiphy with typical input and output options.
