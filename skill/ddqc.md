---
name: ddqc
category: expression
description: Biology-centered data-driven quality control for scRNA-seq.
tags: [ddqc, expression]
author: oxo-call-community
source_url: "https://github.com/ayshwaryas/ddqc"
---

## Concepts

- **Tool Overview**: ddqc (v1.0) - Biology-centered data-driven quality control for scRNA-seq.
- **Core Function**: Biology-centered data-driven quality control for scRNA-seq.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda ddqc`

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
