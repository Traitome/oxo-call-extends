---
name: graphmap
category: bioinformatics
description: GraphMap is a highly sensitive and accurate mapper designed for long, error-prone sequencing reads from technologies like Oxford Nanopore and PacBio.
tags: [graphmap, long-reads, alignment, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/isovic/graphmap"
---

## Concepts

- **Long Read Alignment**: GraphMap specializes in mapping long, error-prone sequencing reads to reference genomes.

- **High Sensitivity**: Designed to handle high error rates typical of long-read sequencing technologies.

- **Graph-Based Alignment**: Uses graph-based approaches to improve alignment accuracy for complex genomic regions.

- **Structural Variation Detection**: Capable of detecting structural variations from long-read alignments.

- **Multiple Input Formats**: Supports various input formats including FASTQ, FASTA, and BAM.

- **Performance Optimization**: Optimized for speed and memory usage with parallel processing support.

## Pitfalls

- **Memory Requirements**: Aligning many long reads may require significant memory. Consider downsampling.

- **Reference Index**: Requires indexed reference genome. Index generation can be time-consuming for large genomes.

- **Read Quality**: Very low-quality reads may produce incorrect alignments. Preprocess reads carefully.

- **Computational Time**: Aligning long reads is computationally intensive. Expect longer run times.

- **Parameter Tuning**: Adjust parameters based on read length, error rate, and desired sensitivity.

## Examples

### Align reads to reference
**Args:** `graphmap align -r reference.fasta -d reads.fastq -o alignments.sam`
**Explanation:** Aligns long reads to a reference genome.

### Output BAM format
**Args:** `graphmap align -r reference.fasta -d reads.fastq -o alignments.bam -b`
**Explanation:** Outputs alignments in BAM format instead of SAM.

### Adjust sensitivity
**Args:** `graphmap align -r reference.fasta -d reads.fastq -s high -o alignments.sam`
**Explanation:** Sets high sensitivity mode for more accurate but slower alignment.

### Detect structural variations
**Args:** `graphmap sv -r reference.fasta -a alignments.bam -o sv_calls.vcf`
**Explanation:** Detects structural variations from aligned reads.

### Parallel processing
**Args:** `graphmap align -r reference.fasta -d reads.fastq -t 8 -o alignments.sam`
**Explanation:** Uses 8 threads for parallel alignment.

### Generate alignment statistics
**Args:** `graphmap stats -a alignments.bam -o stats.txt`
**Explanation:** Generates statistics about the alignments.

### Filter low-quality alignments
**Args:** `graphmap filter -a alignments.bam -q 20 -o filtered.bam`
**Explanation:** Filters out alignments with quality score below 20.