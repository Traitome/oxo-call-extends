---
name: reseq2
category: qc
description: Realistic Illumina paired-end sequencing simulator.
tags: ["reseq2", "qc"]
author: oxo-call-community
source_url: "https://berntpopp.github.io/ReSeq2"
---

## Concepts

- **Tool Overview**: Realistic Illumina paired-end sequencing simulator. (version 2.0.3)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda reseq2`

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

