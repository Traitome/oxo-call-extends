---
name: raptor
category: qc
description: Raptor: A fast and space-efficient pre-filter for querying very large collections of nucleotide sequences
tags: ["raptor", "qc"]
author: oxo-call-community
source_url: "https://seqan-raptor.vercel.app"
---

## Concepts

- **Tool Overview**: Raptor: A fast and space-efficient pre-filter for querying very large collections of nucleotide sequences (version 3.0.1)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda raptor`

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

