---
name: qcumber
category: qc
description: Quality control, quality trimming, adapter removal and sequence content check of NGS data.
tags: ["qcumber", "qc"]
author: oxo-call-community
source_url: "https://gitlab.com/RKIBioinformaticsPipelines/QCumber"
---

## Concepts

- **Tool Overview**: Quality control, quality trimming, adapter removal and sequence content check of NGS data. (version 2.0.4)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda qcumber`

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

