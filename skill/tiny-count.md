---
name: tiny-count
category: analysis
description: tiny-count - Fast and lightweight sequence read counter.
tags: [tiny-count, read-counting, fastq, lightweight, sequencing]
author: oxo-call-community
source_url: "https://github.com/compbio/tiny-count"
---

## Concepts

- **Tool Overview**: tiny-count - A fast, memory-efficient tool for counting sequence reads and generating basic statistics.
- **Core Function**: Counts reads, calculates quality statistics, and provides summary reports for sequencing data.
- **Input**: FASTQ files from sequencing experiments.
- **Output**: Read counts, quality statistics, GC content, summary reports.
- **Installation**: `pip install tiny-count` or `conda install -c bioconda tiny-count`
- **Use Case**: Quick quality checks, read counting, preliminary data assessment.

## Pitfalls

- **Basic Statistics**: Provides basic statistics only - not a full QC tool.
- **Single-ended**: May require paired-end handling for paired data.

## Examples

### Count reads
**Args:** `tiny-count -i reads.fastq.gz -o stats.txt`
**Explanation:** Count reads and generate basic statistics.

### Multiple files
**Args:** `tiny-count -i sample1.fastq sample2.fastq -o multi_sample_stats/`
**Explanation:** Process multiple FASTQ files and generate combined statistics.
