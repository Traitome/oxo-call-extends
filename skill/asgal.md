---
name: asgal
category: alignment
description: A graph aligner
tags: [asgal, alignment]
author: oxo-call-community
source_url: "https://asgal.algolab.eu/"
---

## Concepts

- **Tool Overview**: asgal (v1.1.8) - A graph aligner
- **Core Function**: A graph aligner
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda asgal`

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
