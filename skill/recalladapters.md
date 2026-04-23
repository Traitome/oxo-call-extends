---
name: recalladapters
category: qc
description: recalladapters - A tool to recall adapters for PacBio data
tags: ["recalladapters", "qc"]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/pbbioconda"
---

## Concepts

- **Tool Overview**: recalladapters - A tool to recall adapters for PacBio data (version 9.0.0)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda recalladapters`

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

