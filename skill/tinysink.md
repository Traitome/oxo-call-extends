---
name: tinysink
category: utility
description: TinySink - Lightweight sequence alignment and mapping tool.
tags: [tinysink, alignment, mapping, lightweight, fast, sequencing]
author: oxo-call-community
source_url: "https://github.com/compbio/tinysink"
---

## Concepts

- **Tool Overview**: TinySink - A lightweight and fast sequence alignment tool for mapping short reads to reference genomes.
- **Core Function**: Performs fast alignment of short sequencing reads with memory-efficient algorithms.
- **Input**: FASTQ reads, reference genome (FASTA).
- **Output**: SAM/BAM alignments, mapping statistics.
- **Installation**: `pip install tinysink` or `conda install -c bioconda tinysink`
- **Use Case**: Quick alignment tasks, lightweight workflows, resource-constrained environments.

## Pitfalls

- **Short Reads**: Optimized for short reads - not suitable for long reads.
- **Sensitivity**: May have lower sensitivity compared to more complex aligners.

## Examples

### Align reads
**Args:** `tinysink -i reads.fastq -r reference.fasta -o aligned.sam`
**Explanation:** Align short reads to reference genome.

### Output BAM
**Args:** `tinysink -1 R1.fastq -2 R2.fastq -r genome.fasta -o aligned.bam`
**Explanation:** Align paired-end reads and output BAM format.
