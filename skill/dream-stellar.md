---
name: dream-stellar
category: alignment
description: "DREAM-Stellar: a fast and accurate pairwise local aligner."
tags: [dream-stellar, alignment, pairwise-alignment, sequence-comparison]
author: oxo-call-community
source_url: "https://github.com/seqan/dream-stellar"
---

## Concepts

- **Tool Overview**: DREAM-Stellar is a fast and accurate pairwise local aligner for comparing large biological sequences.
- **Core Function**: Identifies conserved subsequences between pairs of large sequences efficiently.
- **Input/Output**: Input: Two sequences (FASTA). Output: Local alignments with scores.
- **Algorithm**: Uses advanced seed-and-extend strategy optimized for large sequence comparison.
- **Key Features**: Linear time complexity, handles very large sequences, high sensitivity, multi-threaded.
- **Installation**: `conda install -c bioconda dream-stellar`

## Pitfalls

- **Memory Usage**: Aligning very large sequences may require significant memory.
- **Parameter Tuning**: Seed size and scoring parameters affect sensitivity and speed.
- **Repeat Regions**: Highly repetitive sequences can produce spurious alignments.
- **Sequence Similarity**: Very divergent sequences may not produce meaningful alignments.
- **Time Complexity**: While linear on average, worst-case scenarios can be slower.

## Examples

### Basic pairwise alignment
**Args:** `--seq1 ref.fasta --seq2 query.fasta --output alignments.txt`
**Explanation:** Finds local alignments between two sequences.

### High sensitivity mode
**Args:** `--seq1 ref.fasta --seq2 query.fasta --output alignments.txt --sensitive`
**Explanation:** Uses more sensitive alignment parameters for divergent sequences.

### Fast mode
**Args:** `--seq1 ref.fasta --seq2 query.fasta --output alignments.txt --fast`
**Explanation:** Prioritizes speed over sensitivity for quick comparisons.

### Custom scoring matrix
**Args:** `--seq1 ref.fasta --seq2 query.fasta --output alignments.txt --matrix BLOSUM62`
**Explanation:** Uses BLOSUM62 scoring matrix for protein alignment.

### Parallel processing
**Args:** `--seq1 ref.fasta --seq2 query.fasta --output alignments.txt --threads 8`
**Explanation:** Uses 8 threads for parallel alignment computation.