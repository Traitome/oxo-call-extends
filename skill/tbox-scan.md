---
name: tbox-scan
category: metagenomics
description: tbox-scan is for detecting and classifying T-boxes in DNA sequences.
tags: [tbox-scan, metagenomics]
author: oxo-call-community
source_url: "https://tbdb.io"
---

## Concepts

- **Tool Overview**: tbox-scan (v1.0.2) - tbox-scan is for detecting and classifying T-boxes in DNA sequences.
- **Core Function**: tbox-scan is for detecting and classifying T-boxes in DNA sequences.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tbox-scan`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tbox-scan -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run tbox-scan with typical input and output options.
