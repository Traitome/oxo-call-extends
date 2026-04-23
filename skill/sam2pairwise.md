---
name: sam2pairwise
category: alignment
description: sam2pairwise takes a SAM file and uses the CIGAR and MD tag to reconstruct the pairwise alignment of each read
tags: ["sam2pairwise", "alignment", "sam"]
author: oxo-call-community
source_url: "https://github.com/mlafave/sam2pairwise/blob/master/README.md"
---

## Concepts

- **Tool Overview**: sam2pairwise takes a SAM file and uses the CIGAR and MD tag to reconstruct the pairwise alignment of each read (version 1.0.0)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda sam2pairwise`

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

