---
name: bamcmp
category: alignment
description: Tools for deconvolving host and graft reads using full-length alignments and their scores.
tags: [bamcmp, alignment, BAM]
author: oxo-call-community
source_url: "https://github.com/CRUKMI-ComputationalBiology/bamcmp"
---

## Concepts

- **Tool Overview**: bamcmp (v2.2) - Tools for deconvolving host and graft reads using full-length alignments and their scores.
- **Core Function**: Tools for deconvolving host and graft reads using full-length alignments and their scores.
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda bamcmp`

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
