---
name: pypints
category: alignment
description: Peak Identifier for Nascent Transcripts Starts (PINTS)
tags: ["pypints", "alignment"]
author: oxo-call-community
source_url: "https://pints.yulab.org"
---

## Concepts

- **Tool Overview**: Peak Identifier for Nascent Transcripts Starts (PINTS) (version 1.2.1)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pypints`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic alignment
**Args:** `-i input.fastq -r reference.fasta -o output.bam`
**Explanation:** Aligns input reads to reference genome.

