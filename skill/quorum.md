---
name: quorum
category: qc
description: QuorUM (Quality Optimized Reads from the University of Maryland) is an error corrector for Illumina reads. It is distributed and used with MaSuRCA, or it can be used independently.
tags: ["quorum", "qc"]
author: oxo-call-community
source_url: "http://www.genome.umd.edu/quorum.html"
---

## Concepts

- **Tool Overview**: QuorUM (Quality Optimized Reads from the University of Maryland) is an error corrector for Illumina reads. It is distributed and used with MaSuRCA, or it can be used independently. (version 1.1.1)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda quorum`

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

