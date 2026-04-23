---
name: nanosplit
category: qc
description: Perform splitting of Oxford Nanopore sequencing data in a fail and pass dataset.
tags: [nanosplit, qc, nanopore, splitting, filtering]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanosplit"
---

## Concepts

- **Tool Overview**: NanoSplit v0.1.4 - splits Nanopore data into pass/fail datasets.
- **Core Function**: Separates Nanopore reads into pass and fail categories based on quality thresholds.
- **Input/Output**: Takes FASTQ files; outputs pass and fail FASTQ files.
- **Installation**: `conda install -c bioconda nanosplit`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires FASTQ with quality scores.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -o output_dir`
**Explanation:** Splits reads into pass and fail FASTQ files.
