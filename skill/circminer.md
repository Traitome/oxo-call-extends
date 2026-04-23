---
name: circminer
category: expression
description: Sensitive and fast computational tool for detecting circular RNAs (circRNAs) from RNA-Seq data.
tags: [circminer, expression]
author: oxo-call-community
source_url: "https://github.com/vpc-ccg/circminer"
---

## Concepts

- **Tool Overview**: circminer (v0.4.2) - Sensitive and fast computational tool for detecting circular RNAs (circRNAs) from RNA-Seq data.
- **Core Function**: Sensitive and fast computational tool for detecting circular RNAs (circRNAs) from RNA-Seq data.
- **Input/Output**: FASTA sequence input/output
- **Installation**: `conda install -c bioconda circminer`

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
