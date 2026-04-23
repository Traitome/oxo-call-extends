---
name: discount
category: utility
description: DISCOunt - k-mer counting tool.
tags: [discount, utility, k-mer, counting]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: DISCOunt - Fast k-mer counting tool for sequencing data.
- **Core Function**: Counts k-mer occurrences in sequencing reads efficiently.
- **Input/Output**: Expects FASTQ files; outputs k-mer count tables.
- **Installation**: `conda install -c bioconda discount`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires FASTQ format reads.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `discount --input reads.fq --kmer 31 --output kmers.tsv`
**Explanation:** Counts k-mer occurrences in sequencing data.
