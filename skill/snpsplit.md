---
name: snpsplit
category: utility
description: SNPsplit is an allele-specific alignment sorter which is designed to read in alignment files in SAM/BAM format and determine the allelic origin of reads that cover known SNP positions.
tags: [snpsplit, utility, bam, sam]
author: oxo-call-community
source_url: "https://github.com/FelixKrueger/SNPsplit"
---

## Concepts

- **Tool Overview**: snpsplit (v0.6.0) - SNPsplit is an allele-specific alignment sorter which is designed to read in alignment files in SAM/BAM format and determine the allelic origin of reads that cover known SNP positions.
- **Core Function**: SNPsplit is an allele-specific alignment sorter which is designed to read in alignment files in SAM/BAM format and determine the allelic origin of reads that cover known SNP positions.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snpsplit`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snpsplit -i <input_file> -o <output_file>`
**Explanation:** Run snpsplit with typical input and output options.
