---
name: biopet-seqstat
category: qc
description: Generate statistics from FASTQ files
tags: [fastq, statistics, quality-control]
author: oxo-call-community
source_url: "https://github.com/biopet/seqstat"
---

## Concepts
- **Tool Overview**: SeqStat generates statistics from FASTQ files including base quality distributions, nucleotide counts, read length histograms, and quality encoding detection.
- **Statistics**: Total bases/reads, quality distributions, nucleotide counts, read length histograms, quality encoding detection (Sanger, Solexa, etc.).
- **Merge Mode**: Merges statistics from multiple samples.
- **Applications**: FASTQ quality assessment, sequencing quality control.

## Pitfalls
- **Large Files**: Processing very large FASTQ files can be slow.

## Examples
### Generate FASTQ stats
**Args:** `java -jar SeqStat.jar generate -I reads.fq -o stats.json`
**Explanation:** Generates comprehensive statistics from FASTQ file.
