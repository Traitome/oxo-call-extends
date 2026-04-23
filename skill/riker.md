---
name: riker
category: qc
description: High-performance tools next generation sequencing QC.
tags: ["riker", "qc"]
author: oxo-call-community
source_url: "https://github.com/fulcrumgenomics/riker/blob/v0.1.0/README.md"
---

## Concepts

- **Tool Overview**: High-performance tools next generation sequencing QC. (version 0.1.0)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda riker`

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

