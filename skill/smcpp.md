---
name: smcpp
category: population-genomics
description: SMC++ infers population history from whole-genome sequence data.
tags: [smcpp, population-genomics]
author: oxo-call-community
source_url: "https://github.com/popgenmethods/smcpp"
---

## Concepts

- **Tool Overview**: smcpp (v1.15.4) - SMC++ infers population history from whole-genome sequence data.
- **Core Function**: SMC++ infers population history from whole-genome sequence data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda smcpp`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `smcpp -i <input.vcf> -o <output_dir>`
**Explanation:** Run smcpp with typical input and output options.
