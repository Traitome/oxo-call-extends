---
name: satsuma2
category: alignment
description: FFT cross-correlation based synteny aligner, (re)designed to make full use of parallel computing
tags: ["satsuma2", "alignment"]
author: oxo-call-community
source_url: "https://github.com/bioinfologics/satsuma2"
---

## Concepts

- **Tool Overview**: FFT cross-correlation based synteny aligner, (re)designed to make full use of parallel computing (version 20161123)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda satsuma2`

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

