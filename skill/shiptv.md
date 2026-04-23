---
name: shiptv
category: population-genomics
description: Generate a standalone HTML file with an interactive phylogenetic tree using PhyloCanvas
tags: [shiptv, population-genomics]
author: oxo-call-community
source_url: "https://github.com/peterk87/shiptv"
---

## Concepts

- **Tool Overview**: shiptv (v0.4.1) - Generate a standalone HTML file with an interactive phylogenetic tree using PhyloCanvas
- **Core Function**: Generate a standalone HTML file with an interactive phylogenetic tree using PhyloCanvas
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shiptv`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shiptv -i <input.vcf> -o <output_dir>`
**Explanation:** Run shiptv with typical input and output options.
