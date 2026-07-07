---
name: strobealign
category: alignment
description: Align short reads using dynamic seed size with strobemers.
tags: [strobealign, short-read-alignment, strobemers, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ksahlin/strobealign"
---

## Concepts

- **Tool Overview**: strobealign (v0.17.0) is a short-read aligner that uses dynamic seed size with strobemers for improved alignment accuracy.
- **Core Function**: Aligns short sequencing reads to reference genomes using strobemer-based seeding.
- **Algorithm**: Uses strobemers (dynamic-length seeds) for sensitive and efficient alignment.
- **Input/Output**: Input: FASTQ reads, reference genome; Output: SAM/BAM alignment file.
- **Applications**: Short-read sequencing alignment, variant calling, genome analysis.
- **Installation**: `conda install -c bioconda strobealign` or download from GitHub.

## Pitfalls

- **Read Length**: Optimal for specific read lengths; may not perform well with very long reads.
- **Reference Size**: Large reference genomes require significant memory.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Alignment of large datasets can be slow.
- **Parameter Tuning**: Incorrect parameters affect alignment quality.
- **Index Building**: Requires reference index building before alignment.

## Examples

### Display help
**Args:** `strobealign --help`
**Explanation:** Shows available options and usage information.

### Basic read alignment
**Args:** `strobealign -r reference.fasta -i reads.fastq -o alignment.sam`
**Explanation:** Align reads to reference genome.

### With paired-end reads
**Args:** `strobealign -r reference.fasta -1 read1.fastq -2 read2.fastq -o alignment.sam`
**Explanation:** Align paired-end reads to reference.

### Verbose mode
**Args:** `strobealign -r reference.fasta -i reads.fastq -o alignment.sam -v`
**Explanation:** Run with detailed logging for debugging.

### Output BAM
**Args:** `strobealign -r reference.fasta -i reads.fastq -o alignment.bam --bam`
**Explanation:** Output alignment in BAM format.

### Custom parameters
**Args:** `strobealign -r reference.fasta -i reads.fastq -o alignment.sam -k 15`
**Explanation:** Use k-mer size of 15 for seeding.

### Batch processing
**Args:** `strobealign -r reference.fasta -i batch/ -o results/`
**Explanation:** Process multiple read files together.

### Filter by quality
**Args:** `strobealign -r reference.fasta -i reads.fastq -o alignment.sam -q 20`
**Explanation:** Filter reads by quality score.

### Generate report
**Args:** `strobealign -r reference.fasta -i reads.fastq -o alignment.sam --report`
**Explanation:** Generate comprehensive HTML report.
