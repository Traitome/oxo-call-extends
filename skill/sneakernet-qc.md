---
name: sneakernet-qc
category: qc
description: A QC pipeline for raw reads
tags: [sneakernet-qc, qc]
author: oxo-call-community
source_url: "https://github.com/lskatz/sneakernet"
---

## Concepts

- **Tool Overview**: sneakernet-qc (v0.27.2) - A QC pipeline for raw reads
- **Core Function**: A QC pipeline for raw reads
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sneakernet-qc`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sneakernet-qc -i <input.fastq> -o <output_dir>`
**Explanation:** Run sneakernet-qc with typical input and output options.
