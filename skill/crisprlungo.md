---
name: crisprlungo
category: expression
description: A software pipeline for analyzing single-anchor amplicon sequencing and quantifying complex genome editing outcomes
tags: [crisprlungo, expression]
author: oxo-call-community
source_url: "https://github.com/pinellolab/CRISPRlungo"
---

## Concepts

- **Tool Overview**: crisprlungo (v0.1.14) - A software pipeline for analyzing single-anchor amplicon sequencing and quantifying complex genome editing outcomes
- **Core Function**: A software pipeline for analyzing single-anchor amplicon sequencing and quantifying complex genome editing outcomes
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda crisprlungo`

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
