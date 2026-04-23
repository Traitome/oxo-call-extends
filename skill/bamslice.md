---
name: bamslice
category: alignment
description: Extract byte ranges from BAM files and convert to interleaved FASTQ format for parallel processing
tags: [bamslice, alignment, FASTQ, BAM]
author: oxo-call-community
source_url: "https://docs.rs/bamslice"
---

## Concepts

- **Tool Overview**: bamslice (v0.1.7) - Extract byte ranges from BAM files and convert to interleaved FASTQ format for parallel processing
- **Core Function**: bamslice extracts specific byte ranges from BAM files and converts them to interleaved FASTQ format. Designed for parallel processing across compute nodes without requiring pre-indexing. It auto-align...
- **Input/Output**: FASTQ input; processed output
- **Installation**: `conda install -c bioconda bamslice`

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
