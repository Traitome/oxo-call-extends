---
name: nanoblaster
category: alignment
description: Basic Local Alignment and Search Tool for Oxford Nanopore Long Sequences.
tags: [nanoblaster, alignment, nanopore, blast, long-reads]
author: oxo-call-community
source_url: "https://github.com/ruhulsbu/NanoBLASTer"
---

## Concepts

- **Tool Overview**: NanoBLASTer v0.16 - BLAST-like tool for Oxford Nanopore long sequences.
- **Core Function**: Performs local alignment searches optimized for noisy Nanopore long reads.
- **Input/Output**: Takes Nanopore FASTQ and reference FASTA; outputs alignments in tabular format.
- **Installation**: `conda install -c bioconda nanoblaster`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Optimized for Nanopore long reads.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-q reads.fastq -r reference.fasta -o results.tsv`
**Explanation:** Aligns Nanopore reads against reference database.
