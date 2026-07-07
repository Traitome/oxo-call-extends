---
name: nanoq
category: qc
description: Nanoq - Ultra-fast quality control for Oxford Nanopore sequencing reads
tags: [nanoq, qc, nanopore, quality-control, fast, lightweight]
author: oxo-call-community
source_url: "https://github.com/esteinig/nanoq"
---

## Concepts

- **Tool Overview**: Nanoq v0.10.0 is an ultra-fast quality control tool for Oxford Nanopore sequencing reads. It provides rapid statistics and filtering with minimal computational overhead.
- **Core Function**: Quickly computes quality metrics and filters reads based on length and quality thresholds. Designed for high-throughput processing.
- **Algorithm**: Implements efficient parsing algorithms to process FASTQ files at high speed. Uses minimal memory and processing power.
- **Input Format**: Accepts gzipped or plain FASTQ files. Supports streaming from stdin for pipeline integration.
- **Output**: Produces QC statistics to stdout and filtered FASTQ reads to a specified output file.
- **Use Case**: Rapid quality control for large Nanopore datasets, filtering reads in pipelines, and quick assessment of sequencing quality.

## Pitfalls

- **Streaming Requirement**: Designed for stdin/stdout streaming. May require shell redirection for file-based operations.
- **Basic Statistics**: Provides basic QC metrics but not comprehensive visualization. Use NanoPlot for detailed plots.
- **Quality Score Format**: Assumes standard phred quality scores. Non-standard encodings may produce incorrect results.
- **No Alignment Stats**: Does not provide alignment statistics. Use other tools for mapping metrics.
- **Compression**: Ensure consistent compression when piping between tools.
- **Memory Efficiency**: While memory-efficient, extremely large files may still require careful resource management.

## Examples

### Basic QC report
**Args:** `-i reads.fastq.gz -o report.txt`
**Explanation:** Generates QC report with read statistics from FASTQ file.

### Filter reads by length and quality
**Args:** `-i reads.fastq.gz --min-len 1000 --min-qual 10 -o filtered.fastq`
**Explanation:** Filters reads with minimum length of 1000bp and minimum quality of Q10.

### Stream from stdin
**Args:** `gunzip -c reads.fastq.gz | nanoq --min-len 500 | gzip > filtered.fastq.gz`
**Explanation:** Processes reads through pipeline with length filtering.

### Display summary only
**Args:** `-i reads.fastq.gz --summary`
**Explanation:** Outputs only summary statistics without detailed report.

### Display help
**Args:** `nanoq --help`
**Explanation:** Shows all available options for QC and filtering.
