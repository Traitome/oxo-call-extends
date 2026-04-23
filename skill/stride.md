---
name: stride
category: assembly
description: The StriDe Assembler integrates string and de Bruijn graph by decomposing reads within error-prone regions, while extending paire-end read into long reads for assembly through repetitive regions.
tags: [stride, assembly]
author: oxo-call-community
source_url: "https://github.com/ythuang0522/StriDe"
---

## Concepts

- **Tool Overview**: stride (v1.0) - The StriDe Assembler integrates string and de Bruijn graph by decomposing reads within error-prone regions, while extending paire-end read into long reads for assembly through repetitive regions.
- **Core Function**: The StriDe Assembler integrates string and de Bruijn graph by decomposing reads within error-prone regions, while extending paire-end read into long reads for assembly through repetitive regions.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda stride`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `stride -i <reads.fastq> -o <output_dir>`
**Explanation:** Run stride with typical input and output options.
