---
name: bwkit
category: alignment
description: Self-consistent installation-free package for BWA end-to-end read mapping
tags: [bwkit, bwa, mapping, pipeline]
author: oxo-call-community
source_url: "https://github.com/lh3/bwa/tree/master/bwakit"
---

## Concepts

- **Tool Overview**: bwakit provides an end-to-end solution for BWA read mapping with all dependencies included.
- **Core Function**: Complete mapping pipeline from raw reads to sorted BAM.
- **Features**: Includes BWA, samtools, and helper scripts in one package.
- **Input**: FASTQ files and reference genome.
- **Output**: Sorted and indexed BAM files ready for downstream analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda bwakit`

## Pitfalls

- **Legacy Package**: Newer pipelines may prefer separate BWA + samtools installation.
- **Reference Bundle**: Requires reference genome bundle with ALT contigs for GRCh38.

## Examples

### Run full mapping pipeline
**Args:** `bwa.kit/run-bwamem -t 8 -R '@RG\tID:sample\tSM:sample' reference.fa R1.fq R2.fq | samtools sort -o aligned.bam`
**Explanation:** Runs complete BWA-MEM mapping pipeline with read groups.

### Display help
**Args:** `bwa.kit/run-bwamem --help`
**Explanation:** Shows all available options and usage information.
