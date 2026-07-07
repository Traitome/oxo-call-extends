---
name: ucsc-fastqstatsandsubsample
category: utility
description: UCSC fastqStatsAndSubsample - Tool for FASTQ statistics and subsampling.
tags: [ucsc-fastqstatsandsubsample, ucsc, fastq, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC fastqStatsAndSubsample - A tool for FASTQ statistics and subsampling.
- **Core Function**: Generates statistics and creates subsamples from FASTQ files.
- **Input**: FASTQ file.
- **Output**: Statistics report and/or subsampled FASTQ.
- **Installation**: Part of UCSC utilities
- **Use Case**: Quality control, data subsampling, sequencing analysis.

## Pitfalls

- **File Format**: Requires proper FASTQ format.
- **Memory**: May require significant memory for large files.

## Examples

### Generate statistics
**Args:** `fastqStatsAndSubsample input.fastq > stats.txt`
**Explanation:** Generate FASTQ statistics.

### Subsample reads
**Args:** `fastqStatsAndSubsample -subsample=10000 input.fastq > subsample.fastq`
**Explanation:** Extract 10,000 random reads.
