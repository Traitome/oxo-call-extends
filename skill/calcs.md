---
name: calcs
category: alignment
description: Append minimap2's CS tag to a SAM file.
tags: [calcs, alignment, SAM]
author: oxo-call-community
source_url: "https://github.com/akikuno/calcs"
---

## Concepts

- **Tool Overview**: calcs (v0.0.0.9999) - Append minimap2's CS tag to a SAM file.
- **Core Function**: Append minimap2's CS tag to a SAM file.
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda calcs`

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
