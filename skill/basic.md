---
name: basic
category: expression
description: BASIC is a semi-de novo assembly method for assembling BCR and TCR genes from single cell RNA-seq data.
tags: [basic, expression]
author: oxo-call-community
source_url: "http://ttic.uchicago.edu/~aakhan/BASIC/"
---

## Concepts

- **Tool Overview**: basic (v1.5.1) - BASIC is a semi-de novo assembly method for assembling BCR and TCR genes from single cell RNA-seq data.
- **Core Function**: BASIC is a semi-de novo assembly method for assembling BCR and TCR genes from single cell RNA-seq data.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda basic`

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
