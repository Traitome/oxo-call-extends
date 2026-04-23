---
name: referee
category: qc
description: Quality scoring for reference genomes
tags: ["referee", "qc"]
author: oxo-call-community
source_url: "https://github.com/gwct/referee"
---

## Concepts

- **Tool Overview**: Quality scoring for reference genomes (version 1.2)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda referee`

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

