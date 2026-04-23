---
name: sap
category: alignment
description: Pairwise structure alignment via double dynamic programming
tags: ["sap", "alignment"]
author: oxo-call-community
source_url: "https://github.com/mathbio-nimr-mrc-ac-uk/SAP"
---

## Concepts

- **Tool Overview**: Pairwise structure alignment via double dynamic programming (version 1.1.3)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda sap`

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

