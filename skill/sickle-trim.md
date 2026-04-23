---
name: sickle-trim
category: qc
description: Windowed Adaptive Trimming for fastq files using quality.
tags: [sickle-trim, qc, fastq]
author: oxo-call-community
source_url: "https://github.com/najoshi/sickle/blob/v1.33/README.md"
---

## Concepts

- **Tool Overview**: sickle-trim (v1.33) - Windowed Adaptive Trimming for fastq files using quality.
- **Core Function**: Windowed Adaptive Trimming for fastq files using quality.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sickle-trim`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sickle-trim -i <input.fastq> -o <output_dir>`
**Explanation:** Run sickle-trim with typical input and output options.
