---
name: cnmf
category: expression
description: Consensus NMF for scRNA-Seq data.
tags: [cnmf, expression]
author: oxo-call-community
source_url: "https://github.com/dylkot/cNMF"
---

## Concepts

- **Tool Overview**: cnmf (v1.7.1) - Consensus NMF for scRNA-Seq data.
- **Core Function**: Consensus NMF for scRNA-Seq data.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cnmf`

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
