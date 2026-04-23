---
name: somatem
category: metagenomics
description: Best practices pipeline for long-read metagenomics analysis.
tags: [somatem, metagenomics]
author: oxo-call-community
source_url: "https://github.com/treangenlab/Somatem#readme"
---

## Concepts

- **Tool Overview**: somatem (v0.7.1) - Best practices pipeline for long-read metagenomics analysis.
- **Core Function**: Best practices pipeline for long-read metagenomics analysis.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda somatem`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `somatem -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run somatem with typical input and output options.
