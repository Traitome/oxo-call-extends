---
name: ciriquant
category: expression
description: Circular RNA quantification pipeline.
tags: [ciriquant, expression]
author: oxo-call-community
source_url: "https://ciri-cookbook.readthedocs.io/en/latest/CIRIquant_0_home.html"
---

## Concepts

- **Tool Overview**: ciriquant (v1.1.3) - Circular RNA quantification pipeline.
- **Core Function**: Circular RNA quantification pipeline.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda ciriquant`

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
