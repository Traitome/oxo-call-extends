---
name: smithwaterman
category: alignment
description: Implementation of the Smith-Waterman-Gotoh local sequence alignment algorithm
tags: [smithwaterman, alignment, sequence-alignment, local-alignment, gotoh]
author: oxo-call-community
source_url: "https://github.com/ekg/smithwaterman"
---

## Concepts

- **Tool Overview**: smithwaterman (v1.0.0) - A tool implementing the Smith-Waterman-Gotoh local alignment algorithm
- **Core Function**: Performs optimal local sequence alignment with affine gap penalties
- **Input/Output**: Accepts FASTA sequences; outputs aligned sequences with scores
- **Algorithm**: Implements the Smith-Waterman-Gotoh algorithm with affine gap costs
- **Installation**: `conda install -c bioconda smithwaterman`
- **Key Features**: Local alignment, affine gap penalties, customizable scoring matrix

## Pitfalls

- **Sequence Length**: Not optimized for very long sequences
- **Computation Time**: O(n*m) complexity for sequences of length n and m
- **Memory Usage**: Requires O(n*m) memory for dynamic programming matrix
- **Scoring Matrix**: Default BLOSUM62 may not be optimal for all data
- **Gap Penalties**: Requires careful selection of gap open/extend parameters
- **Output Format**: May require post-processing for downstream analysis

## Examples

### Display help
**Args:** `smithwaterman --help`
**Explanation:** Shows available options and usage information.

### Basic local alignment
**Args:** `smithwaterman -a seq1.fasta -b seq2.fasta`
**Explanation:** Perform local alignment between two sequences.

### With custom scoring matrix
**Args:** `smithwaterman -a seq1.fasta -b seq2.fasta -m blosum80`
**Explanation:** Use BLOSUM80 scoring matrix instead of default.

### Specify gap penalties
**Args:** `smithwaterman -a seq1.fasta -b seq2.fasta -g -11 -e -1`
**Explanation:** Set gap open penalty to -11 and gap extend to -1.

### Output alignment only
**Args:** `smithwaterman -a seq1.fasta -b seq2.fasta -o alignment.txt`
**Explanation:** Save alignment to output file.

### Multiple sequence alignment
**Args:** `smithwaterman -a seq1.fasta -b seq2.fasta -c seq3.fasta`
**Explanation:** Align multiple sequences pairwise.

### Show score only
**Args:** `smithwaterman -a seq1.fasta -b seq2.fasta -s`
**Explanation:** Output only the alignment score.

### With FASTA input from stdin
**Args:** `cat seq1.fasta | smithwaterman -a - -b seq2.fasta`
**Explanation:** Read first sequence from standard input.