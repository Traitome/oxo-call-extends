---
name: coast
category: alignment
description: Alignment search tool that identifies similar proteomes.
tags: [coast, alignment]
author: oxo-call-community
source_url: "https://gitlab.com/coast_tool/COAST"
---

## Concepts

- **Tool Overview**: coast (v0.2.2) - Alignment search tool that identifies similar proteomes.
- **Core Function**: Alignment search tool that identifies similar proteomes.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda coast`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
