---
name: hmftools-mark-dups
category: utility
description: Mark read duplicates and form consensus sequences
tags: [hmftools-mark-dups, utility, bam, duplicates, consensus, sambamba, samtools]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/mark-dups"
---

## Concepts

- **Tool Overview**: hmftools-mark-dups (v1.1.7) is a Java-based duplicate marking tool from Hartwig Medical Foundation that identifies PCR and optical duplicates in BAM files and generates consensus sequences for improved variant calling accuracy.

- **Duplicate Detection Algorithm**: Uses read position and mapping quality to identify duplicate reads. Unlike Picard MarkDuplicates, it can generate consensus sequences where duplicate reads are combined to reduce PCR bias and improve sensitivity for low-frequency variants.

- **Consensus Sequence Generation**: Forms consensus sequences from duplicate read groups, using base quality scores to resolve disagreements between duplicate reads. This is particularly useful for ultra-deep sequencing applications.

- **Sambamba Integration**: Relies on sambamba (>=1.0.1) for efficient BAM indexing and sorting operations. The workflow coordinates sambamba for position-based duplicate detection across multiple threads.

- **SAMTools Compatibility**: Requires samtools (>=1.17) for sorting and indexing operations. Both sambamba and samtools must be installed and accessible in PATH.

- **Output Formats**: Produces a marked BAM file with duplicate flags set (0x0400 flag), a metrics file with duplicate statistics, and optional consensus FASTQ files for downstream analysis.

## Pitfalls

- **Sambamba PATH Requirement**: The tool calls sambamba as an external command. Sambamba must be installed and in PATH, not just available as a conda dependency. Verify with `which sambamba` before running.

- **Coordinate-Sorted Input**: Input BAM must be coordinate-sorted and indexed. Query-sorted input will produce incorrect duplicate marking. Use `samtools sort -n` for query-name sorting if needed.

- **Memory Usage for Consensus**: Consensus sequence generation is memory-intensive for high-coverage samples. Large WGS samples (100x+) may require 16GB+ RAM for consensus formation.

- **Thread Count Mismatch**: The `-threads` parameter controls both Java threads and sambamba threads. Mismatched thread settings can cause deadlocks or performance degradation.

- **Optical Duplicate Detection**: Optical duplicates require pixel distance parameters that differ between instruments. Default settings are optimized for Illumina NovaSeq; HiSeq users may need to adjust optical duplicate pixel distance.

## Examples

### Basic duplicate marking
**Args:** `mark-dups -input tumor.sorted.bam -output tumor.marked.bam -metrics tumor.dups.metrics`
**Explanation:** Runs standard duplicate marking on a coordinate-sorted BAM file. Duplicates are flagged in the output BAM with the 0x0400 bit set.

### Mark duplicates with consensus generation
**Args:** `mark-dups -input tumor.sorted.bam -output tumor.marked.bam -metrics tumor.dups.metrics -consensus -output_consensus consensus.fastq.gz`
**Explanation:** Generates consensus sequences from duplicate read groups. The consensus FASTQ contains resolved bases where duplicate reads agreed, reducing PCR bias.

### Paired-end tumor-normal marking
**Args:** `mark-dups -input tumor.sorted.bam -reference normal.sorted.bam -output tumor.marked.bam -metrics tumor.dups.metrics`
**Explanation:** Uses matched normal sample to distinguish somatically-acquired variants from germline duplicates. The normal provides baseline for expected read depth.

### High-thread processing for large BAM files
**Args:** `mark-dups -input large_tumor.bam -output marked.bam -metrics metrics.txt -threads 16`
**Explanation:** Uses 16 threads for both Java processing and sambamba operations. Recommended for WGS samples with >500M reads.

### Specify optical duplicate pixel distance for HiSeq
**Args:** `mark-dups -input tumor.bam -output marked.bam -metrics metrics.txt -optical_distance 2500`
**Explanation:** Sets optical duplicate pixel distance to 2500 for HiSeq data. NovaSeq data typically uses higher values (6000-10000) due to different flow cell geometry.

### Output to specific directory
**Args:** `mark-dups -input ./bams/tumor.sorted.bam -output ./marked/tumor.marked.bam -metrics ./qc/tumor.dups.metrics`
**Explanation:** Specifies explicit output paths for marked BAM and metrics file. Creates output directory if it does not exist.
