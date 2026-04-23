---
name: curare
category: expression
description: A Customizable and Reproducible Analysis Pipeline for RNA-Seq Experiments.
tags: [curare, expression]
author: oxo-call-community
source_url: "https://github.com/pblumenkamp/Curare"
---

## Concepts

- **Tool Overview**: curare (v0.6.0) - A Customizable and Reproducible Analysis Pipeline for RNA-Seq Experiments.
- **Core Function**: Curare is a freely available analysis pipeline for reproducible, high-throughput, bacterial RNA-Seq experiments. Define standardized pipelines customized for your specific workflow without the necessi...
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda curare`

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
