---
name: nanospring
category: utility
description: NanoSpring is a compression tool for nanopore reads in Fastq files
tags: [nanospring, utility, nanopore, compression, fastq]
author: oxo-call-community
source_url: "https://github.com/qm2/NanoSpring"
---

## Concepts

- **Tool Overview**: NanoSpring v0.2 - compression tool for Nanopore FASTQ reads.
- **Core Function**: Compresses Nanopore FASTQ files using reference-based or de novo compression.
- **Input/Output**: Takes FASTQ files; outputs compressed archives.
- **Installation**: `conda install -c bioconda nanospring`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires Nanopore FASTQ format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Compress
**Args:** `-i reads.fastq -o compressed.nss`
**Explanation:** Compresses Nanopore FASTQ file.

### Decompress
**Args:** `-d compressed.nss -o reads.fastq`
**Explanation:** Decompresses NanoSpring archive back to FASTQ.
