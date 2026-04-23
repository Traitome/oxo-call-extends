---
name: sam2lca
category: alignment
description: Lowest Common Ancestor on SAM/BAM/CRAM alignment files.
tags: ["sam2lca", "alignment", "bam", "sam", "bam"]
author: oxo-call-community
source_url: "https://github.com/maxibor/sam2lca"
---

## Concepts

- **Tool Overview**: Lowest Common Ancestor on SAM/BAM/CRAM alignment files. (version 1.1.4)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda sam2lca`

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

