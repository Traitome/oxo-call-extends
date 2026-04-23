---
name: myloasm
category: assembly
description: myloasm - high-resolution metagenome assembly for (noisy) long reads.
tags: [myloasm, assembly, metagenome, long-reads, nanopore]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/myloasm"
---

## Concepts

- **Tool Overview**: myloasm v0.5.1 - high-resolution metagenome assembler for noisy long reads.
- **Core Function**: Assembles metagenomes from noisy long-read data (Nanopore, PacBio) with high resolution.
- **Input/Output**: Takes long-read FASTQ files; outputs assembled contigs.
- **Installation**: `conda install -c bioconda myloasm`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Designed for noisy long reads; may not perform well with short reads.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq.gz -o assembly.fasta`
**Explanation:** Assembles metagenome from long reads.
