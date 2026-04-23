---
name: qualifilter
category: qc
description: Generate a QC report summarizing key quality metrics and sample pass/fail status according to user-defined thresholds.
tags: ["qualifilter", "qc", "sam"]
author: oxo-call-community
source_url: "https://github.com/buhlentozini/QualiFilter"
---

## Concepts

- **Tool Overview**: Generate a QC report summarizing key quality metrics and sample pass/fail status according to user-defined thresholds. (version 1.0.0)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda qualifilter`

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

