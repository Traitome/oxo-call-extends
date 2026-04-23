---
name: quast
category: qc
description: Quality Assessment Tool for Genome Assemblies.
tags: ["quast", "qc"]
author: oxo-call-community
source_url: "https://quast.sourceforge.net/docs/manual.html"
---

## Concepts

- **Tool Overview**: Quality Assessment Tool for Genome Assemblies. (version 5.3.0)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda quast`

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

