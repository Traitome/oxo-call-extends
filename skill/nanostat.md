---
name: nanostat
category: qc
description: Calculate statistics for Oxford Nanopore sequencing data and alignments
tags: [nanostat, qc, nanopore, statistics, summary]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanostat"
---

## Concepts

- **Tool Overview**: NanoStat v1.6.0 - calculates statistics for Nanopore data and alignments.
- **Core Function**: Generates summary statistics for Nanopore reads including read lengths, qualities, and yields.
- **Input/Output**: Takes FASTQ, BAM, or sequencing_summary.txt; outputs statistics report.
- **Installation**: `conda install -c bioconda nanostat`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Supports FASTQ, BAM, and sequencing summary formats.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Stats from FASTQ
**Args:** `-i reads.fastq.gz -o stats.txt`
**Explanation:** Calculates read statistics from FASTQ file.

### Stats from BAM
**Args:** `-b aligned.bam -o alignment_stats.txt`
**Explanation:** Calculates alignment statistics from BAM file.
