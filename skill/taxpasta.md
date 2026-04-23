---
name: taxpasta
category: metagenomics
description: TAXonomic Profile Aggregation and STAndardisation
tags: [taxpasta, metagenomics]
author: oxo-call-community
source_url: "https://github.com/taxprofiler/taxpasta"
---

## Concepts

- **Tool Overview**: taxpasta (v0.7.0) - TAXonomic Profile Aggregation and STAndardisation
- **Core Function**: TAXonomic Profile Aggregation and STAndardisation
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda taxpasta`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `taxpasta -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run taxpasta with typical input and output options.
