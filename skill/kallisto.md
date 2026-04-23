---
name: kallisto
category: expression
description: Quantifying abundances of transcripts from RNA-Seq data, or more generally of target sequences using high-throughput sequencing reads.
tags: [kallisto, expression]
author: oxo-call-community
source_url: "https://pachterlab.github.io/kallisto/manual.html"
---

## Concepts

- **Tool Overview**: kallisto (v0.52.0) - Quantifying abundances of transcripts from RNA-Seq data, or more generally of target sequences using high-throughput sequencing reads.
- **Core Function**: Provides functionality for expression tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda kallisto`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
