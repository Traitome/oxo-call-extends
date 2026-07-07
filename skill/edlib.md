---
name: edlib
category: alignment
description: "C/C++ library and program for sequence alignment using edit (Levenshtein) distance"
tags: [edlib, alignment, edit-distance, sequence-comparison, Levenshtein]
author: oxo-call-community
source_url: "https://github.com/Martinsos/edlib"
---

## Concepts

- **Tool Overview**: Edlib is a lightweight C/C++ library for fast and accurate sequence alignment using edit distance (Levenshtein distance).
- **Core Function**: Calculates edit distance between sequences and finds optimal alignments with minimal computational overhead.
- **Input/Output**: Input: Query and target sequences (FASTA/FASTQ). Output: Alignment results, edit distance scores, CIGAR strings.
- **Algorithm**: Uses Myers' bit-vector algorithm for ultra-fast edit distance calculation with SIMD optimizations.
- **Key Features**: Extremely fast alignment, low memory footprint, exact and approximate matching, prefix/suffix/extension modes, CIGAR output.
- **Installation**: `conda install -c bioconda edlib`

## Pitfalls

- **Sequence Length**: Very long sequences may exceed bit-vector limitations.
- **Memory Constraints**: Large-scale alignments require careful memory management.
- **Alignment Mode**: Different modes (global, local, prefix) produce different results.
- **Error Threshold**: Setting appropriate error threshold is critical for performance.
- **Version Compatibility**: API may change between major versions.

## Examples

### Basic alignment
**Args:** `edlib-align query.fa target.fa`
**Explanation:** Aligns query sequence against target sequence.

### With edit distance threshold
**Args:** `edlib-align query.fa target.fa -k 5`
**Explanation:** Finds alignments with at most 5 edit operations.

### Output CIGAR format
**Args:** `edlib-align query.fa target.fa -c`
**Explanation:** Outputs alignment in CIGAR format.

### Prefix alignment mode
**Args:** `edlib-align query.fa target.fa -m PREFIX`
**Explanation:** Performs prefix alignment (query aligns to prefix of target).

### Batch processing
**Args:** `edlib-align queries.fa targets.fa -o results.txt`
**Explanation:** Aligns multiple query sequences against multiple targets.