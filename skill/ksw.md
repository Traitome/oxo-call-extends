---
name: ksw
category: alignment
description: Smith-Waterman sequence alignment in C
tags: [ksw, alignment, smith-waterman, sequence-alignment, C]
author: oxo-call-community
source_url: "https://github.com/nh13/ksw"
---

## Concepts

- **Smith-Waterman**: Implements Smith-Waterman local alignment algorithm
- **Fast C Implementation**: Highly optimized C implementation
- **Sequence Alignment**: Performs local sequence alignments
- **Gap Penalties**: Supports custom gap opening and extension penalties
- **Scoring Matrix**: Uses standard scoring matrices (BLOSUM, PAM)
- **Interactive Mode**: Provides interactive alignment mode

## Pitfalls

- **Scoring Parameters**: Requires proper scoring matrix selection
- **Gap Penalties**: Gap penalty tuning affects alignment quality
- **Sequence Length**: Very long sequences require more memory
- **Quality Scores**: Does not inherently use base quality scores
- **Input Format**: Requires correct input format
- **Memory Management**: Large alignments need careful memory management

## Examples

### Align two sequences
**Args:** `ksw -a sequence1.fasta -b sequence2.fasta -o alignment.txt`
**Explanation:** Aligns two sequences using Smith-Waterman.

### Specify scoring matrix
**Args:** `ksw -a seq1.fasta -b seq2.fasta -m BLOSUM62 -o results.txt`
**Explanation:** Uses BLOSUM62 scoring matrix.

### Set gap penalties
**Args:** `ksw -a seq1.fasta -b seq2.fasta -g 10 -e 1 -o results.txt`
**Explanation:** Sets gap open=10, gap extend=1.

### Paired-end alignment
**Args:** `ksw -1 reads_1.fastq -2 reads_2.fastq -o results.sam`
**Explanation:** Aligns paired-end reads.

### Batch processing
**Args:** `ksw batch -d reads/ -o alignments/`
**Explanation:** Processes multiple read files.

### Export alignments
**Args:** `ksw -a seq1.fasta -b seq2.fasta -o results.txt --format SAM`
**Explanation:** Exports alignments in SAM format.