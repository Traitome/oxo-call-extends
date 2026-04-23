---
name: riboseq-rust
category: qc
description: Ribo-seq Unit Step Transformation. Tools to characterise the determinants of ribosome profiling read density across mRNA. May be used to examine relative decoding rates and and for quality assessment
tags: ["riboseq-rust", "qc"]
author: oxo-call-community
source_url: "https://lapti.ucc.ie/rust/"
---

## Concepts

- **Tool Overview**: Ribo-seq Unit Step Transformation. Tools to characterise the determinants of ribosome profiling read density across mRNA. May be used to examine relative decoding rates and and for quality assessment (version 1.2)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda riboseq-rust`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Quality check
**Args:** `-i input.fastq -o qc_report`
**Explanation:** Generates quality control metrics and reports.

