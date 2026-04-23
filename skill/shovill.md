---
name: shovill
category: assembly
description: Microbial assembly pipeline for Illumina paired-end reads
tags: [shovill, assembly]
author: oxo-call-community
source_url: "https://github.com/tseemann/shovill"
---

## Concepts

- **Tool Overview**: shovill (v1.4.2) - Microbial assembly pipeline for Illumina paired-end reads
- **Core Function**: Microbial assembly pipeline for Illumina paired-end reads
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shovill`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shovill -i <reads.fastq> -o <output_dir>`
**Explanation:** Run shovill with typical input and output options.
