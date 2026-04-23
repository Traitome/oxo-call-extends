---
name: pycoqc
category: qc
description: PycoQC computes metrics and generates interactive QC plots for Oxford Nanopore technologies sequencing data
tags: ["pycoqc", "qc"]
author: oxo-call-community
source_url: "https://a-slide.github.io/pycoQC/"
---

## Concepts

- **Tool Overview**: PycoQC computes metrics and generates interactive QC plots for Oxford Nanopore technologies sequencing data (version 2.5.2)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pycoqc`

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

