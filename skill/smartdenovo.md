---
name: smartdenovo
category: assembly
description: Ultra-fast de novo assembler using long noisy reads
tags: [smartdenovo, assembly]
author: oxo-call-community
source_url: "https://github.com/ruanjue/smartdenovo"
---

## Concepts

- **Tool Overview**: smartdenovo (v1.0.0) - Ultra-fast de novo assembler using long noisy reads
- **Core Function**: Ultra-fast de novo assembler using long noisy reads
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda smartdenovo`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `smartdenovo -i <reads.fastq> -o <output_dir>`
**Explanation:** Run smartdenovo with typical input and output options.
