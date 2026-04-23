---
name: rcx-tk
category: qc
description: This package adjusts and cleans the metadata file provided by a user.
tags: ["rcx-tk", "qc"]
author: oxo-call-community
source_url: "https://github.com/RECETOX/rcx-tk"
---

## Concepts

- **Tool Overview**: This package adjusts and cleans the metadata file provided by a user. (version 0.2.0)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rcx-tk`

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

