---
name: cyntenator
category: alignment
description: progressive gene order alignments
tags: [cyntenator, alignment, BED]
author: oxo-call-community
source_url: "https://github.com/dieterich-lab/cyntenator"
---

## Concepts

- **Tool Overview**: cyntenator (v0.0.r2326) - progressive gene order alignments
- **Core Function**: Cyntenator identifies conserved syntenic blocks between multiple genomes. The program computes Smith-Waterman alignments of sequences, whereby the alphabet consists of all annotated genes and the scor...
- **Input/Output**: BED interval input/output
- **Installation**: `conda install -c bioconda cyntenator`

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
