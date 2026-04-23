---
name: samclip
category: alignment
description: Filter SAM file for soft and hard clipped alignments
tags: ["samclip", "alignment", "sam"]
author: oxo-call-community
source_url: "https://github.com/tseemann/samclip"
---

## Concepts

- **Tool Overview**: Filter SAM file for soft and hard clipped alignments (version 0.4.0)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda samclip`

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

