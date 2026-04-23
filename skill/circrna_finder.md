---
name: circrna_finder
category: expression
description: Scripts required for running the pipeline to find circular RNAs from RNA-seq data
tags: [circrna_finder, expression]
author: oxo-call-community
source_url: "https://github.com/orzechoj/circRNA_finder"
---

## Concepts

- **Tool Overview**: circrna_finder (v1.2) - Scripts required for running the pipeline to find circular RNAs from RNA-seq data
- **Core Function**: Scripts required for running the pipeline to find circular RNAs from RNA-seq data
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda circrna_finder`

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
