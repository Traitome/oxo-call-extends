---
name: snikt
category: qc
description: Identify and remove adapter/systemic contamination in metagenomic sequencing DNA/RNA data.
tags: [snikt, qc]
author: oxo-call-community
source_url: "https://github.com/piyuranjan/SNIKT"
---

## Concepts

- **Tool Overview**: snikt (v0.5.0) - Identify and remove adapter/systemic contamination in metagenomic sequencing DNA/RNA data.
- **Core Function**: Identify and remove adapter/systemic contamination in metagenomic sequencing DNA/RNA data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snikt`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snikt -i <input.fastq> -o <output_dir>`
**Explanation:** Run snikt with typical input and output options.
