---
name: aligncov
category: alignment
description: Obtain tidy alignment coverage info from sorted BAM files
tags: [aligncov, alignment, BAM]
author: oxo-call-community
source_url: "https://github.com/pcrxn/aligncov"
---

## Concepts

- **Tool Overview**: aligncov (v0.0.2) - Obtain tidy alignment coverage info from sorted BAM files
- **Core Function**: Obtain tidy alignment coverage info from sorted BAM files
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda aligncov`

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
