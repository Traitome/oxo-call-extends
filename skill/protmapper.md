---
name: protmapper
category: alignment
description: Map protein sites to human reference sequence.
tags: ["protmapper", "alignment"]
author: oxo-call-community
source_url: "https://protmapper.readthedocs.io"
---

## Concepts

- **Tool Overview**: Map protein sites to human reference sequence. (version 0.0.29)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda protmapper`

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

