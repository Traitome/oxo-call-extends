---
name: narfmap
category: alignment
description: NARFMAP is a fork of the Dragen mapper/aligner Open Source Software.
tags: [narfmap, alignment, dragen, mapping, long-reads]
author: oxo-call-community
source_url: "https://github.com/bioinformaticsorphanage/NARFMAP"
---

## Concepts

- **Tool Overview**: NARFMAP v1.4.2 - fork of Dragen mapper/aligner.
- **Core Function**: Maps and aligns sequencing reads to a reference genome using Dragen-compatible algorithms.
- **Input/Output**: Takes FASTQ reads; outputs aligned BAM files.
- **Installation**: `conda install -c bioconda narfmap`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires FASTQ input and reference FASTA.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-r reference.fasta -1 reads_R1.fastq -2 reads_R2.fastq -o aligned.bam`
**Explanation:** Aligns reads to reference genome.
