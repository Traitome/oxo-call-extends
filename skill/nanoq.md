---
name: nanoq
category: qc
description: Ultra-fast quality control and summary reports for nanopore reads
tags: [nanoq, qc, nanopore, quality-control, fast]
author: oxo-call-community
source_url: "https://github.com/esteinig/nanoq"
---

## Concepts

- **Tool Overview**: Nanoq v0.10.0 - ultra-fast quality control for Nanopore reads.
- **Core Function**: Generates rapid QC summary reports for Nanopore read data with minimal overhead.
- **Input/Output**: Takes FASTQ files; outputs QC statistics and summary reports.
- **Installation**: `conda install -c bioconda nanoq`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Supports gzipped and plain FASTQ.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq.gz -o report.txt`
**Explanation:** Generates QC report for Nanopore reads.

### Filter reads
**Args:** `-i reads.fastq.gz --min-len 1000 --min-qual 10 -o filtered.fastq`
**Explanation:** Filters and reports on reads meeting quality/length thresholds.
