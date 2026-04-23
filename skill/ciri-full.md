---
name: ciri-full
category: expression
description: Full length circRNA reconstruction and quantification using BSJ and reverse overlap (RO) features.
tags: [ciri-full, expression]
author: oxo-call-community
source_url: "https://ciri-cookbook.readthedocs.io/en/latest/CIRI-full.html"
---

## Concepts

- **Tool Overview**: ciri-full (v2.1.2) - Full length circRNA reconstruction and quantification using BSJ and reverse overlap (RO) features.
- **Core Function**: Full length circRNA reconstruction and quantification using BSJ and reverse overlap (RO) features.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda ciri-full`

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
