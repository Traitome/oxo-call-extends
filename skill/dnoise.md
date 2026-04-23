---
name: dnoise
category: utility
description: DNOISE - Denoising tool for sequencing data.
tags: [dnoise, utility, denoising, sequencing]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: DNOISE - Denoising tool for removing noise from sequencing data.
- **Core Function**: Removes sequencing errors and noise from amplicon data.
- **Input/Output**: Expects FASTQ reads; outputs denoised sequences.
- **Installation**: `conda install -c bioconda dnoise`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires sequencing reads in FASTQ format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dnoise --input reads.fq --output denoised.fa`
**Explanation:** Denoises sequencing data to remove errors.
