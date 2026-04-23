---
name: sylph-tax
category: metagenomics
description: Integrating taxonomic information into the sylph metagenome profiler.
tags: [sylph-tax, metagenomics]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/sylph-tax/blob/v1.8.0/README.md"
---

## Concepts

- **Tool Overview**: sylph-tax (v1.8.0) - Integrating taxonomic information into the sylph metagenome profiler.
- **Core Function**: Integrating taxonomic information into the sylph metagenome profiler.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sylph-tax`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sylph-tax -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run sylph-tax with typical input and output options.
