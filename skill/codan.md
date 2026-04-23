---
name: codan
category: expression
description: CDS prediction in eukaryotic transcripts.
tags: [codan, expression]
author: oxo-call-community
source_url: "https://github.com/pedronachtigall/CodAn"
---

## Concepts

- **Tool Overview**: codan (v1.2) - CDS prediction in eukaryotic transcripts.
- **Core Function**: CDS prediction in eukaryotic transcripts.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda codan`

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
