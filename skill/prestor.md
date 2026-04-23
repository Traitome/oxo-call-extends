---
name: prestor
category: qc
description: A prototype package for generating quality control plots from pRESTO output.
tags: ["prestor", "qc"]
author: oxo-call-community
source_url: "https://bitbucket.org/javh/prototype-prestor"
---

## Concepts

- **Tool Overview**: A prototype package for generating quality control plots from pRESTO output. (version 07f9c7caeb60)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda prestor`

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

