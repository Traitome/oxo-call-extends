---
name: cellqc
category: expression
description: Cellqc standardizes the qualiy control of single-cell RNA-Seq (scRNA) data to render clean feature count matrices.
tags: [cellqc, expression]
author: oxo-call-community
source_url: "https://github.com/lijinbio/cellqc"
---

## Concepts

- **Tool Overview**: cellqc (v0.1.0) - Cellqc standardizes the qualiy control of single-cell RNA-Seq (scRNA) data to render clean feature count matrices.
- **Core Function**: Cellqc standardizes the qualiy control of single-cell RNA-Seq (scRNA) data to render clean feature count matrices.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cellqc`

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
