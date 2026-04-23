---
name: djinn
category: utility
description: Convert linked-read data between formats (10x, stLFR, TELLseq).
tags: [djinn, utility, linked-read, barcode, format-conversion]
author: oxo-call-community
source_url: "https://github.com/pdimens/djinn"
---

## Concepts

- **Tool Overview**: djinn v2.4 - Format converter for linked-read sequencing data (10x, stLFR, TELLseq).
- **Core Function**: Converts between different linked-read FASTQ formats and barcode styles.
- **Input/Output**: Expects linked-read FASTQ files; outputs converted files in target format.
- **Installation**: `conda install -c bioconda djinn`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires linked-read data with specific barcode format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `djinn convert --input reads.fq --from 10x --to stlfr --output converted.fq`
**Explanation:** Converts linked-read data between formats.
