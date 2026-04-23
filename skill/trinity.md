---
name: trinity
category: expression
description: Trinity assembles transcript sequences from Illumina RNA-Seq data.
tags: [trinity, expression]
author: oxo-call-community
source_url: "https://github.com/trinityrnaseq/trinityrnaseq/wiki"
---

## Concepts

- **Tool Overview**: trinity (v2.15.2) - Trinity assembles transcript sequences from Illumina RNA-Seq data.
- **Core Function**: Trinity assembles transcript sequences from Illumina RNA-Seq data.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda trinity`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
