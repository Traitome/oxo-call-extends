---
name: prinseq
category: qc
description: PRINSEQ can be used to filter, reformat, or trim your genomic and metagenomic sequence data
tags: ["prinseq", "qc"]
author: oxo-call-community
source_url: "http://prinseq.sourceforge.net/"
---

## Concepts

- **Tool Overview**: PRINSEQ can be used to filter, reformat, or trim your genomic and metagenomic sequence data (version 0.20.4)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda prinseq`

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

