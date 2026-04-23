---
name: targqc
category: qc
description: Target capture coverage QC
tags: [targqc, qc]
author: oxo-call-community
source_url: "https://github.com/vladsaveliev/TargQC"
---

## Concepts

- **Tool Overview**: targqc (v1.8.1) - Target capture coverage QC
- **Core Function**: Target capture coverage QC
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda targqc`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `targqc -i <input.fastq> -o <output_dir>`
**Explanation:** Run targqc with typical input and output options.
