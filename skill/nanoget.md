---
name: nanoget
category: qc
description: Functions to extract information from Oxford Nanopore sequencing data and alignments.
tags: [nanoget, qc, nanopore, extraction, statistics]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanoget"
---

## Concepts

- **Tool Overview**: NanoGet v1.19.4 - extracts information from Oxford Nanopore data and alignments.
- **Core Function**: Extracts statistics and information from Nanopore FASTQ, BAM, and sequencing summary files.
- **Input/Output**: Takes FASTQ, BAM, or sequencing_summary.txt; outputs extracted metrics.
- **Installation**: `conda install -c bioconda nanoget`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Supports multiple Nanopore output formats.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Extract from FASTQ
**Args:** `-i reads.fastq.gz -o stats.tsv`
**Explanation:** Extracts read statistics from FASTQ file.

### Extract from BAM
**Args:** `-b aligned.bam -o alignment_stats.tsv`
**Explanation:** Extracts alignment statistics from BAM file.
