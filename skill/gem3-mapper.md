---
name: gem3-mapper
category: alignment
description: GEM3 read mapper - High-performance sequence alignment tool for next-generation sequencing data.
tags: [gem3-mapper, sequence-alignment, NGS, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/smarco/gem3-mapper"
---

## Concepts
- **Read Mapping**: High-performance alignment of NGS reads to reference genomes.
- **Burrows-Wheeler Transform**: Uses BWT-based indexing for efficient mapping.
- **Seed-and-Extend**: Implements seed-and-extend strategy for sensitive alignment.
- **Multiple Alignment**: Supports mapping of paired-end and single-end reads.
- **Quality-aware**: Takes base quality scores into account during mapping.

## Pitfalls
- **Index Building**: Requires time and memory to build genome index.
- **Parameter Optimization**: Multiple parameters need optimization for specific datasets.
- **Memory Requirements**: Large genomes require significant memory for mapping.
- **Output Size**: Alignment files can be very large.
- **Version Compatibility**: Different versions may have different command-line options.

## Examples
### Build genome index
**Args:** `gem3-index -i genome.fasta -o genome`
**Explanation:** Builds a GEM3 index for the reference genome.

### Map paired-end reads
**Args:** `gem3-mapper -I genome.gem -1 reads_1.fastq -2 reads_2.fastq -o alignments.sam`
**Explanation:** Maps paired-end reads to the reference genome.

### Map single-end reads
**Args:** `gem3-mapper -I genome.gem -s reads.fastq -o alignments.sam`
**Explanation:** Maps single-end reads to the reference genome.

### Output BAM format
**Args:** `gem3-mapper -I genome.gem -1 reads_1.fastq -2 reads_2.fastq -o alignments.bam -f bam`
**Explanation:** Maps reads and outputs in BAM format.

### With quality filtering
**Args:** `gem3-mapper -I genome.gem -1 reads_1.fastq -2 reads_2.fastq -o alignments.sam -q 20`
**Explanation:** Maps reads with minimum quality score of 20.