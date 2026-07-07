---
name: indelfixer
category: alignment
description: Sensitive sequence aligner using full Smith-Waterman alignment for 454, Illumina and PacBio data
tags: [indelfixer, sequence-alignment, Smith-Waterman, long-reads]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/InDelFixer"
---

## Concepts

- **Tool Overview**: InDelFixer (v1.1) is a sensitive sequence aligner that uses full Smith-Waterman alignment for accurate mapping of sequencing reads.
- **Core Function**: Specialized for handling insertion and deletion errors common in 454, Illumina, and PacBio sequencing data.
- **Algorithm**: Implements full Smith-Waterman dynamic programming for optimal local alignment.
- **Input/Output**: Accepts FASTA/FASTQ reads and reference sequences. Outputs SAM/BAM aligned files.
- **Accuracy**: Provides high sensitivity for detecting indels compared to heuristic aligners.

## Pitfalls

- **Computational Speed**: Full Smith-Waterman alignment is slower than heuristic approaches.
- **Memory Usage**: Requires significant memory for large datasets or long sequences.
- **Read Length**: May not be optimal for extremely long reads without chunking.
- **Parameter Tuning**: Gap penalties and scoring matrices require careful adjustment.
- **Reference Indexing**: Does not build index; performs direct alignment for each read.

## Examples

### Basic alignment
**Args:** `indelfixer -r reference.fasta -i reads.fastq -o aligned.sam`
**Explanation:** Aligns reads to reference using default parameters.

### Custom gap penalties
**Args:** `indelfixer -r ref.fasta -i reads.fastq -o aligned.sam -gopen 10 -gextend 2`
**Explanation:** Sets gap open penalty to 10 and gap extension penalty to 2.

### Output BAM format
**Args:** `indelfixer -r ref.fasta -i reads.fastq -b -o aligned.bam`
**Explanation:** Outputs aligned reads in BAM format (sorted and indexed).

### Quality filtering
**Args:** `indelfixer -r ref.fasta -i reads.fastq -o aligned.sam -q 20`
**Explanation:** Filters reads with quality score below 20 before alignment.

### PacBio data optimization
**Args:** `indelfixer -r ref.fasta -i pacbio.fastq -o aligned.sam -pacbio`
**Explanation:** Optimizes alignment parameters for PacBio sequencing data.

### Parallel processing
**Args:** `indelfixer -r ref.fasta -i reads.fastq -o aligned.sam -t 8`
**Explanation:** Uses 8 threads for parallel alignment.