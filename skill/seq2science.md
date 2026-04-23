---
name: seq2science
category: utility
description: Automated preprocessing of Next-Generation-Sequencing data.
tags: [seq2science, utility]
author: oxo-call-community
source_url: "https://vanheeringen-lab.github.io/seq2science"
---

## Concepts

- **Tool Overview**: seq2science (v1.2.5) - Automated preprocessing of Next-Generation-Sequencing data.
- **Core Function**: Automated preprocessing of Next-Generation-Sequencing data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda seq2science`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `seq2science -i <input_file> -o <output_file>`
**Explanation:** Run seq2science with typical input and output options.
