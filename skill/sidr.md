---
name: sidr
category: metagenomics
description: Sequence Idenification using Decision tRees; a tool to classify DNA reads using machine learning models.
tags: [sidr, metagenomics]
author: oxo-call-community
source_url: "https://github.com/damurdock/SIDR"
---

## Concepts

- **Tool Overview**: sidr (v0.0.2a2) - Sequence Idenification using Decision tRees; a tool to classify DNA reads using machine learning models.
- **Core Function**: Sequence Idenification using Decision tRees; a tool to classify DNA reads using machine learning models.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sidr`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sidr -i <input.fastq> -d <database> -o <output_dir>`
**Explanation:** Run sidr with typical input and output options.
