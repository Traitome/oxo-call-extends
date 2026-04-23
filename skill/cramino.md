---
name: cramino
category: qc
description: A tool for very fast quality assessment of long read cram/bam files.
tags: [cramino, qc, BAM, CRAM]
author: oxo-call-community
source_url: "https://github.com/wdecoster/cramino"
---

## Concepts

- **Tool Overview**: cramino (v1.3.0) - A tool for very fast quality assessment of long read cram/bam files.
- **Core Function**: A tool for very fast quality assessment of long read cram/bam files.
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda cramino`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -o qc_report`
**Explanation:** Perform quality control analysis
