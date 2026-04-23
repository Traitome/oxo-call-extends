---
name: porechop
category: qc
description: Adapter removal and demultiplexing of Oxford Nanopore reads
tags: ["porechop", "qc"]
author: oxo-call-community
source_url: "https://github.com/rrwick/Porechop?tab=readme-ov-file#how-it-works"
---

## Concepts

- **Tool Overview**: Adapter removal and demultiplexing of Oxford Nanopore reads (version 0.2.4)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda porechop`

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

