---
name: minialign
category: alignment
description: Fast and accurate alignment tool for PacBio and Nanopore long reads.
tags: [minialign, alignment, long-read]
author: oxo-call-community
source_url: "https://github.com/ocxtal/minialign"
---

## Concepts

- **Tool Overview**: MiniAlign v0.6.0 aligns long-read sequences from PacBio and Nanopore.
- **Core Function**: Aligns long sequencing reads to reference sequences.
- **Minimizer Index**: Uses minimizer-based indexing for speed.
- **Seed Chaining**: Implements array-based seed chaining.
- **SIMD Parallelism**: Uses SIMD for parallel Smith-Waterman extension.
- **Long-read Support**: Optimized for PacBio and Oxford Nanopore reads.

## Pitfalls

- **Long-read Specific**: Designed for long sequencing reads.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large reference genomes.
- **Parameter Tuning**: May require parameter adjustment for optimal alignment.
- **Data Quality**: Alignment accuracy depends on read quality.
- **Reference Genome**: Requires appropriate reference sequences.

## Examples

### Align long reads
**Args:** `minialign -i reads.fastq -r reference.fasta -o alignments.sam`
**Explanation:** Aligns long reads to reference genome.

### With custom k-mer size
**Args:** `minialign -i reads.fastq -r reference.fasta -o alignments.sam -k 15`
**Explanation:** Uses k-mer size of 15 for minimizer index.

### Paired-end alignment
**Args:** `minialign -i reads_1.fastq -R reads_2.fastq -r reference.fasta -o alignments.sam`
**Explanation:** Processes paired-end long reads.

### Batch processing
**Args:** `minialign -i fastq/ -r reference.fasta -o alignments/`
**Explanation:** Processes multiple read files in batch mode.

### Generate statistics
**Args:** `minialign -i reads.fastq -r reference.fasta -o alignments.sam -s stats.txt`
**Explanation:** Generates alignment statistics.