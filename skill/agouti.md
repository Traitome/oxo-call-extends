---
name: agouti
category: expression
description: Annotation of Genomic and Transcriptomic Intervals
tags: [agouti, expression]
author: oxo-call-community
source_url: "https://github.com/zywicki-lab/agouti"
---

## Concepts

- **Tool Overview**: agouti (v1.0.3) - Annotation of Genomic and Transcriptomic Intervals
- **Core Function**: Annotation of Genomic and Transcriptomic Intervals
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda agouti`

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
