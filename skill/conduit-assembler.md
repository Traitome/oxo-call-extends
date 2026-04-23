---
name: conduit-assembler
category: expression
description: Long- and short-read hybrid de novo transcriptome assembly
tags: [conduit-assembler, expression]
author: oxo-call-community
source_url: "https://github.com/NatPRoach/conduit"
---

## Concepts

- **Tool Overview**: conduit-assembler (v0.1.2) - Long- and short-read hybrid de novo transcriptome assembly
- **Core Function**: Long- and short-read hybrid de novo transcriptome assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda conduit-assembler`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -r transcriptome.fasta -o quantification`
**Explanation:** Quantify gene expression
