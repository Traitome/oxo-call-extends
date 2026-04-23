---
name: stxtyper
category: assembly
description: Accurately type both known and unknown Shiga toxin operons from assembled genomic sequence.
tags: [stxtyper, assembly]
author: oxo-call-community
source_url: "https://github.com/ncbi/stxtyper"
---

## Concepts

- **Tool Overview**: stxtyper (v1.0.25) - Accurately type both known and unknown Shiga toxin operons from assembled genomic sequence.
- **Core Function**: Accurately type both known and unknown Shiga toxin operons from assembled genomic sequence.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stxtyper`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stxtyper -i <reads.fastq> -o <output_dir>`
**Explanation:** Run stxtyper with typical input and output options.
