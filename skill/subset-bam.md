---
name: subset-bam
category: utility
description: A tool to subset a 10x Genomics BAM file based on a tag, most commonly the cell barcode tag.
tags: [subset-bam, utility, bam]
author: oxo-call-community
source_url: "https://github.com/10XGenomics/subset-bam/blob/v1.1.0/README.md"
---

## Concepts

- **Tool Overview**: subset-bam (v1.1.0) - A tool to subset a 10x Genomics BAM file based on a tag, most commonly the cell barcode tag.
- **Core Function**: A tool to subset a 10x Genomics BAM file based on a tag, most commonly the cell barcode tag.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda subset-bam`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `subset-bam -i <input_file> -o <output_file>`
**Explanation:** Run subset-bam with typical input and output options.
