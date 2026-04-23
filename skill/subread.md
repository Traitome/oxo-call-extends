---
name: subread
category: alignment
description: High-performance read alignment, quantification, and mutation discovery.
tags: [subread, alignment]
author: oxo-call-community
source_url: "https://subread.sourceforge.net/SubreadUsersGuide.pdf"
---

## Concepts

- **Tool Overview**: subread (v2.1.1) - High-performance read alignment, quantification, and mutation discovery.
- **Core Function**: High-performance read alignment, quantification, and mutation discovery.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda subread`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `subread -i <input.fasta> -r <reference.fasta> -o <output.sam>`
**Explanation:** Run subread with typical input and output options.
