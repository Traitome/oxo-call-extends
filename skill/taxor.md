---
name: taxor
category: metagenomics
description: Fast and space-efficient taxonomic classification of long reads.
tags: [taxor, metagenomics]
author: oxo-call-community
source_url: "https://github.com/JensUweUlrich/Taxor/blob/0.2.1/README.md"
---

## Concepts

- **Tool Overview**: taxor (v0.2.1) - Fast and space-efficient taxonomic classification of long reads.
- **Core Function**: Fast and space-efficient taxonomic classification of long reads.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda taxor`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `taxor -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run taxor with typical input and output options.
