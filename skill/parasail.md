---
name: parasail
category: alignment
description: Parasail is a SIMD-accelerated pairwise sequence alignment library.
tags: [parasail, alignment, sequence-alignment, simd]
author: oxo-call-community
source_url: "https://github.com/jeffdaily/parasail"
---

## Concepts

- **Tool Overview**: Parasail provides high-performance sequence alignment.
- **Core Function**: Performs fast pairwise sequence alignment.
- **Algorithm**: Implements Smith-Waterman, Needleman-Wunsch, and semi-global alignment.
- **Input Format**: Accepts FASTA sequences.
- **Output**: Produces alignment scores and alignments.
- **Use Case**: Sequence comparison, alignment, bioinformatics analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequences require memory.
- **SIMD Support**: Performance depends on SIMD capabilities.
- **Parameter Sensitivity**: Results depend on scoring parameters.
- **Runtime**: Large-scale analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `parasail_aligner --help`
**Explanation:** Shows available options and usage instructions.

### Local alignment
**Args:** `parasail_aligner -a sw -q query.fasta -t target.fasta -o alignment.txt`
**Explanation:** Performs Smith-Waterman local alignment.

### Global alignment
**Args:** `parasail_aligner -a nw -q query.fasta -t target.fasta -o alignment.txt`
**Explanation:** Performs Needleman-Wunsch global alignment.

### Semi-global alignment
**Args:** `parasail_aligner -a sg -q query.fasta -t target.fasta -o alignment.txt`
**Explanation:** Performs semi-global alignment.

### Verbose mode
**Args:** `parasail_aligner -v -a sw -q query.fasta -t target.fasta`
**Explanation:** Runs with verbose output.

### Scoring matrix
**Args:** `parasail_aligner -a sw -m blosum62 -q query.fasta -t target.fasta`
**Explanation:** Uses BLOSUM62 scoring matrix.

### Gap penalties
**Args:** `parasail_aligner -a sw -g -10 -e -1 -q query.fasta -t target.fasta`
**Explanation:** Sets gap open (-10) and extend (-1) penalties.