---
name: dinopy
category: utility
description: Python library for reading and writing FASTA/FASTQ files with dinucleotide analysis.
tags: [dinopy, utility, fasta, fastq, dinucleotide]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: dinopy - Python library for FASTA/FASTQ file I/O with dinucleotide analysis capabilities.
- **Core Function**: Reads and writes FASTA/FASTQ files with support for dinucleotide frequency analysis.
- **Input/Output**: Expects FASTA/FASTQ files; outputs processed sequences and dinucleotide statistics.
- **Installation**: `conda install -c bioconda dinopy`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires valid FASTA or FASTQ format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dinopy --input reads.fq --output stats.tsv`
**Explanation:** Analyzes dinucleotide frequencies in FASTQ file.
