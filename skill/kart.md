---
name: kart
category: alignment
description: Kart - a divide-and-conquer algorithm for NGS read alignment.
tags: [kart, alignment, NGS, read mapping, divide-and-conquer]
author: oxo-call-community
source_url: "https://github.com/hsinnan75/Kart"
---

## Concepts

- **Tool Overview**: kart (v2.5.6) - A fast NGS read aligner using divide-and-conquer algorithm.
- **Divide-and-Conquer**: Breaks alignment problem into smaller subproblems.
- **Speed**: Optimized for fast read mapping on large genomes.
- **Accuracy**: Maintains high alignment accuracy while being fast.
- **Parallel Processing**: Supports multi-threaded alignment.
- **Format Support**: Works with standard FASTQ and SAM/BAM formats.

## Pitfalls

- **Memory Usage**: Requires significant memory for large genomes.
- **Index Size**: Genome index can be large.
- **Read Length**: Performance varies with read length.
- **SNP Sensitivity**: May have reduced sensitivity for SNPs.
- **Version Compatibility**: Index format may change between versions.
- **Complex Regions**: Difficult regions may have lower mapping rates.

## Examples

### Build genome index
**Args:** `kart index -i genome.fasta -o genome.idx`
**Explanation:** Builds Kart index from genome FASTA.

### Map single-end reads
**Args:** `kart map -i genome.idx -r reads.fastq -o alignments.sam`
**Explanation:** Maps single-end reads to reference genome.

### Map paired-end reads
**Args:** `kart map -i genome.idx -r1 reads_1.fastq -r2 reads_2.fastq -o alignments.sam`
**Explanation:** Maps paired-end reads to reference genome.

### Output BAM format
**Args:** `kart map -i genome.idx -r reads.fastq -o alignments.bam --bam`
**Explanation:** Outputs alignments in BAM format.

### Parallel processing
**Args:** `kart map -i genome.idx -r reads.fastq -o alignments.sam -t 8`
**Explanation:** Uses 8 threads for parallel alignment.

### Filter by mapping quality
**Args:** `kart map -i genome.idx -r reads.fastq -o alignments.sam -q 30`
**Explanation:** Filters alignments by mapping quality >= 30.