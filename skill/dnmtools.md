---
name: dnmtools
category: epigenomics
description: DNMtools - Tools for DNA methylation analysis.
tags: [dnmtools, epigenomics, methylation, bisulfite]
author: oxo-call-community
source_url: ""
---

## Concepts

- **Tool Overview**: DNMtools - Collection of tools for analyzing DNA methylation data.
- **Core Function**: Processes and analyzes bisulfite sequencing data for methylation studies.
- **Input/Output**: Expects bisulfite sequencing data; outputs methylation calls and metrics.
- **Installation**: `conda install -c bioconda dnmtools`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires bisulfite sequencing reads or methylation calls.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `dnmtools methcounts --input bs_reads.fq --ref ref.fa --output methylation.bed`
**Explanation:** Analyzes DNA methylation from bisulfite sequencing data.
