---
name: qualimap
category: alignment
description: Quality control of alignment sequencing data and its derivatives like feature counts
tags: ["qualimap", "alignment"]
author: oxo-call-community
source_url: "http://qualimap.bioinfo.cipf.es/"
---

## Concepts

- **Tool Overview**: Quality control of alignment sequencing data and its derivatives like feature counts (version 2.3)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda qualimap`

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

