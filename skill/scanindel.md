---
name: scanindel
category: alignment
description: ScanIndel is a python program to detect indels (insertions and deletions) from NGS data by re-align and de novo assemble soft clipped reads.
tags: ["scanindel", "alignment"]
author: oxo-call-community
source_url: "https://github.com/cauyrd/ScanIndel"
---

## Concepts

- **Tool Overview**: ScanIndel is a python program to detect indels (insertions and deletions) from NGS data by re-align and de novo assemble soft clipped reads. (version 1.3)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda scanindel`

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

