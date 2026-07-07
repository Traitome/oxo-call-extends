---
name: rtg-core
category: alignment
description: RealTimeGenomics Core - Software for alignment and analysis of next-gen sequencing data.
tags: ["rtg-core", "alignment", "sequencing", "RealTimeGenomics"]
author: oxo-call-community
source_url: "https://realtimegenomics.github.io/rtg-core/index.html"
---

## Concepts

- **Tool Overview**: rtg-core (v3.13) is a core component of RealTimeGenomics software suite, providing fundamental utilities for sequence alignment, indexing, and basic variant calling operations.
- **Core Function**: Implements efficient sequence alignment algorithms optimized for speed and accuracy. Supports read mapping, duplicate marking, and basic variant detection.
- **Algorithm**: Uses a seed-and-extend approach with advanced filtering for high-speed alignment. Implements Smith-Waterman and Needleman-Wunsch algorithms for local and global alignment.
- **Input Format**: FASTQ/FASTA reads, BAM/SAM alignments, FASTA reference sequences.
- **Output Format**: BAM alignments, VCF variants, alignment statistics reports.
- **Use Case**: Preprocessing sequencing data, quality control, read mapping for downstream variant analysis.

## Pitfalls

- **Memory requirements**: Large reference genomes require significant RAM for indexing.
- **Index building time**: Reference index creation can be time-consuming for large genomes.
- **Paired-end assumptions**: Default settings assume paired-end reads; single-end requires configuration.
- **Quality score sensitivity**: Poor quality reads may be misaligned or discarded.
- **Resource intensive**: Parallel processing recommended for large datasets.
- **Version compatibility**: Output formats may change between versions; check compatibility with downstream tools.

## Examples

### Build reference index
**Args:** `rtg index -i reference.fasta -o ref_index`
**Explanation:** `-i` input reference FASTA; `-o` output index directory. Creates an index for efficient alignment.

### Align reads to reference
**Args:** `rtg map -i ref_index -q reads.fastq -o aligned.bam`
**Explanation:** `-i` reference index; `-q` input reads; `-o` output BAM file. Performs read mapping.

### Mark duplicates
**Args:** `rtg markdup -i aligned.bam -o deduped.bam`
**Explanation:** Identifies and marks duplicate reads in alignment file.

### Sort BAM file
**Args:** `rtg sort -i aligned.bam -o sorted.bam`
**Explanation:** Sorts BAM file by coordinate for downstream analysis.

### Basic variant calling
**Args:** `rtg call -i ref_index -b aligned.bam -o variants.vcf`
**Explanation:** Calls variants from aligned reads and outputs VCF file.

### Generate alignment stats
**Args:** `rtg stats -i aligned.bam -o stats.txt`
**Explanation:** Generates alignment statistics including mapping rate and coverage metrics.
