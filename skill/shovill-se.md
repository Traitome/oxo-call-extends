---
name: shovill-se
category: assembly
description: An fork of Shovill (microbial assembly pipeline for Illumina paired-end reads) that supports single-end reads.
tags: [shovill-se, assembly]
author: oxo-call-community
source_url: "https://github.com/rpetit3/shovill"
---

## Concepts

- **Tool Overview**: shovill-se (v1.1.0se) - An fork of Shovill (microbial assembly pipeline for Illumina paired-end reads) that supports single-end reads.
- **Core Function**: An fork of Shovill (microbial assembly pipeline for Illumina paired-end reads) that supports single-end reads.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda shovill-se`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `shovill-se -i <reads.fastq> -o <output_dir>`
**Explanation:** Run shovill-se with typical input and output options.
