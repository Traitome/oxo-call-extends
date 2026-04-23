---
name: taxadb
category: metagenomics
description: locally query the ncbi taxonomy
tags: [taxadb, metagenomics]
author: oxo-call-community
source_url: "https://github.com/HadrienG/taxadb"
---

## Concepts

- **Tool Overview**: taxadb (v0.12.1) - locally query the ncbi taxonomy
- **Core Function**: locally query the ncbi taxonomy
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda taxadb`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `taxadb -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run taxadb with typical input and output options.
