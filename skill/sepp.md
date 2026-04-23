---
name: sepp
category: population-genomics
description: SATe-enabled phylogenetic placement.
tags: [sepp, population-genomics]
author: oxo-call-community
source_url: "https://github.com/smirarab/sepp/blob/v4.5.6/README.md"
---

## Concepts

- **Tool Overview**: sepp (v4.5.6) - SATe-enabled phylogenetic placement.
- **Core Function**: SATe-enabled phylogenetic placement.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sepp`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sepp -i <input.vcf> -o <output_dir>`
**Explanation:** Run sepp with typical input and output options.
