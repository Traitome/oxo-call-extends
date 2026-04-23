---
name: reaper
category: qc
description: Tool for demultiplexing, trimming and filtering sequencing data.
tags: ["reaper", "qc"]
author: oxo-call-community
source_url: "https://www.ebi.ac.uk/~stijn/reaper/reaper.html"
---

## Concepts

- **Tool Overview**: Tool for demultiplexing, trimming and filtering sequencing data. (version 16.098)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda reaper`

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

