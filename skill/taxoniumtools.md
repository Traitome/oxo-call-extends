---
name: taxoniumtools
category: population-genomics
description: Taxonium is a tool for exploring trees, including those with millions of nodes. This tool generates files compatible with viewing in Taxonium from inputs like Newick and UShER files.
tags: [taxoniumtools, population-genomics, newick]
author: oxo-call-community
source_url: "https://github.com/theosanderson/taxonium"
---

## Concepts

- **Tool Overview**: taxoniumtools (v2.1.17) - Taxonium is a tool for exploring trees, including those with millions of nodes. This tool generates files compatible with viewing in Taxonium from inputs like Newick and UShER files.
- **Core Function**: Taxonium is a tool for exploring trees, including those with millions of nodes. This tool generates files compatible with viewing in Taxonium from inputs like Newick and UShER files.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda taxoniumtools`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `taxoniumtools -i <input.vcf> -o <output_dir>`
**Explanation:** Run taxoniumtools with typical input and output options.
