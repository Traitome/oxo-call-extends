---
name: craq
category: alignment
description: Pinpoint assembly errors for genomic assessing and correcting.
tags: [craq, alignment]
author: oxo-call-community
source_url: "https://github.com/JiaoLaboratory/CRAQ"
---

## Concepts

- **Tool Overview**: craq (v1.10) - Pinpoint assembly errors for genomic assessing and correcting.
- **Core Function**: CRAQ (Clipping Reveals Assembly Quality) is a reference-free genome assembly evaluator that can assess the accuracy of assembled genomic sequences and provide detailed assembly quality assessment from...
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda craq`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
