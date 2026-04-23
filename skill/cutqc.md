---
name: cutqc
category: qc
description: generate aggregated fastqc report of both before and after trimming.
tags: [cutqc, qc, FASTQ]
author: oxo-call-community
source_url: "https://github.com/obenno/cutqc"
---

## Concepts

- **Tool Overview**: cutqc (v0.07) - generate aggregated fastqc report of both before and after trimming.
- **Core Function**: generate aggregated fastqc report of both before and after trimming.
- **Input/Output**: FASTQ input; processed output
- **Installation**: `conda install -c bioconda cutqc`

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
