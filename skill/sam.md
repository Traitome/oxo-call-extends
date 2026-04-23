---
name: sam
category: alignment
description: SAM - Sequence Alignment and Modeling System
tags: ["sam", "alignment", "sam"]
author: oxo-call-community
source_url: "https://compbio.soe.ucsc.edu/sam2src/"
---

## Concepts

- **Tool Overview**: SAM - Sequence Alignment and Modeling System (version 3.5)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda sam`

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

