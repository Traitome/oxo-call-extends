---
name: qcat
category: qc
description: Qcat is Python command-line tool for demultiplexing Oxford Nanopore reads from FASTQ files.
tags: ["qcat", "qc", "fastq"]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/qcat"
---

## Concepts

- **Tool Overview**: Qcat is Python command-line tool for demultiplexing Oxford Nanopore reads from FASTQ files. (version 1.1.0)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda qcat`

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

