---
name: qualrepair
category: qc
description: Update the FASTQ quality scores from a subsequence FASTQ.
tags: ["qualrepair", "qc", "fastq"]
author: oxo-call-community
source_url: "https://github.com/clintval/qualrepair"
---

## Concepts

- **Tool Overview**: Update the FASTQ quality scores from a subsequence FASTQ. (version 1.0.0)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda qualrepair`

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

