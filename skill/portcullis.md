---
name: portcullis
category: qc
description: Splice junction analysis and filtering from BAM files.
tags: ["portcullis", "qc", "bam", "bam"]
author: oxo-call-community
source_url: "https://ei-corebioinformatics.github.io/portcullis"
---

## Concepts

- **Tool Overview**: Splice junction analysis and filtering from BAM files. (version 1.2.4)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda portcullis`

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

