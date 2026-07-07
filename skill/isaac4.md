---
name: isaac4
category: alignment
description: Ultra-fast whole-genome alignment for Illumina sequencing platforms
tags: [isaac4, alignment, Illumina, whole-genome]
author: oxo-call-community
source_url: "https://github.com/Illumina/Isaac4"
---

## Concepts

- **Tool Overview**: isaac4 (v04.18.11.09) - Illumina's ultra-fast read aligner optimized for whole-genome sequencing data
- **Core Algorithm**: Implements Burrows-Wheeler Transform (BWT) with advanced seed-and-extend strategy
- **Performance**: Designed for speed with minimal memory footprint, ideal for large-scale sequencing projects
- **Multi-threading**: Native parallel processing support for multi-core architectures
- **Input/Output**: Supports FASTQ, BAM input; produces sorted BAM output with mapping quality scores
- **Advanced Features**: Local alignment, paired-end support, duplicate marking, base quality recalibration

## Pitfalls

- **Illumina Specific**: Optimized for Illumina sequencing data; may not perform optimally with other platforms
- **Memory Management**: Requires careful memory allocation for large reference genomes
- **Index Building**: Preprocessing step required for reference genome indexing; time-consuming for large genomes
- **Parameter Tuning**: Default parameters may need adjustment for specific data types (e.g., low-quality reads)
- **Read Length Limitations**: Performance degrades with reads >300bp; consider alternative aligners for long reads
- **Variant Calling Integration**: Requires post-processing for optimal variant calling results

## Examples

### Basic paired-end alignment
**Args:** `isaac4 align -r hg38.fasta -b sample_R1.fastq.gz sample_R2.fastq.gz -o aligned.bam`
**Explanation:** Aligns paired-end Illumina reads to human reference genome hg38.

### With duplicate marking
**Args:** `isaac4 align -r reference.fasta -b reads.fastq -o output.bam --mark-duplicates`
**Explanation:** Performs alignment and marks PCR duplicates in a single pass.

### Variant calling pipeline
**Args:** `isaac4 align -r ref.fasta -b R1.fastq R2.fastq -o sorted.bam && isaac4 variant -r ref.fasta -i sorted.bam -o variants.vcf`
**Explanation:** Complete pipeline from alignment to variant calling.

### Large cohort processing
**Args:** `isaac4 align -r genome.fasta -b batch_list.txt -o ./output/ --threads 16`
**Explanation:** Processes multiple samples in batch mode with 16 threads for parallelization.

### Base quality recalibration
**Args:** `isaac4 align -r ref.fasta -b reads.fastq -o recalibrated.bam --recalibrate-quals`
**Explanation:** Performs alignment with on-the-fly base quality score recalibration.

### Targeted sequencing
**Args:** `isaac4 align -r ref.fasta -b exome_reads.fastq -o exome.bam --target-bed regions.bed`
**Explanation:** Aligns reads only to targeted regions specified in BED file for exome sequencing.