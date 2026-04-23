---
name: seq2c
category: utility
description: Cohort based copy number calling in gene regions
tags: [seq2c, utility]
author: oxo-call-community
source_url: "https://github.com/AstraZeneca-NGS/Seq2C"
---

## Concepts

- **Tool Overview**: seq2c (v2019.05.30) - Cohort based copy number calling in gene regions
- **Core Function**: Cohort based copy number calling in gene regions
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seq2c`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seq2c -i <input_file> -o <output_file>`
**Explanation:** Run seq2c with typical input and output options.
