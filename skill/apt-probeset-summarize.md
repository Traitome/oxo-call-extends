---
name: apt-probeset-summarize
category: expression
description: From Affymetrix Power Tools package. apt-probeset-summarize is program for analyzing expression arrays including 3' IVT and exon arrays. Supports background correction (MAS5,RMA), normalization (linear scaling, quantile, sketch), and summarization (PLIER, RMA, MAS5) methods.
tags: [apt-probeset-summarize, expression]
author: oxo-call-community
source_url: "https://downloads.thermofisher.com"
---

## Concepts

- **Tool Overview**: apt-probeset-summarize (v2.10.0) - From Affymetrix Power Tools package. apt-probeset-summarize is program for analyzing expression arrays including 3' IVT and exon arrays. Supports background correction (MAS5,RMA), normalization (linear scaling, quantile, sketch), and summarization (PLIER, RMA, MAS5) methods.
- **Core Function**: From Affymetrix Power Tools package. apt-probeset-summarize is program for analyzing expression arrays including 3' IVT and exon arrays. Supports background correction (MAS5,RMA), normalization (linear scaling, quantile, sketch), and summarization (PLIER, RMA, MAS5) methods.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda apt-probeset-summarize`

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
