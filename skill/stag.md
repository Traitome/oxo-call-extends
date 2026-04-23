---
name: stag
category: metagenomics
description: A hierarchical taxonomic classifier for metagenomic sequences
tags: [stag, metagenomics]
author: oxo-call-community
source_url: "https://github.com/zellerlab/stag"
---

## Concepts

- **Tool Overview**: stag (v0.8.3) - A hierarchical taxonomic classifier for metagenomic sequences
- **Core Function**: A hierarchical taxonomic classifier for metagenomic sequences
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stag`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stag -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run stag with typical input and output options.
