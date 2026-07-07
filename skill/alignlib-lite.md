---
name: alignlib-lite
category: alignment
description: Python wrapper around alignlib C++ library for sequence alignment
tags: [alignlib-lite, sequence-alignment, C++, python-bindings, bioinformatics]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/alignlib"
---

## Concepts

- **Tool Overview**: alignlib-lite is a Python wrapper around the alignlib C++ library, providing sequence alignment functionality for bioinformatics applications.
- **Core Function**: Enables pairwise sequence alignment with support for various alignment algorithms through Python bindings to a high-performance C++ library.
- **Alignment Types**: Supports global alignment, local alignment, and semi-global alignment strategies.
- **Scoring Models**: Implements various scoring matrices (BLOSUM, PAM) and gap penalty schemes.
- **Input/Output**: Input: Sequence data as Python strings or BioPython objects. Output: Alignment objects with scores and aligned sequences.
- **Installation**: Install via bioconda: `conda install -c bioconda alignlib-lite` or via pip: `pip install alignlib-lite`
- **Author**: Andreas Heger
- **License**: BSD license

## Pitfalls

- **Version Differences**: Library is in alpha development stage (version 0.3), API may change.
- **Documentation**: Limited official documentation available; refer to source code for details.
- **Python Version**: May require specific Python versions for compatibility.
- **C++ Dependencies**: Requires compatible C++ compiler for building from source.
- **Memory Management**: Be cautious with memory usage for very large sequence alignments.

## Examples

### Display help information
**Args:** `-h`
**Explanation:** Shows available options and usage instructions.

### Basic pairwise alignment (Python API)
**Args:** `from alignlib_lite import Aligner; a = Aligner(); result = a.align(seq1, seq2)`
**Explanation:** Performs pairwise sequence alignment using default parameters.

### Global alignment
**Args:** `aligner = Aligner(mode='global'); result = aligner.align(seq1, seq2)`
**Explanation:** Performs global alignment (Needleman-Wunsch style).

### Local alignment
**Args:** `aligner = Aligner(mode='local'); result = aligner.align(seq1, seq2)`
**Explanation:** Performs local alignment (Smith-Waterman style).

### Semi-global alignment
**Args:** `aligner = Aligner(mode='semiglobal'); result = aligner.align(seq1, seq2)`
**Explanation:** Performs semi-global alignment (free end gaps).

### Custom scoring matrix
**Args:** `aligner = Aligner(matrix='BLOSUM62'); result = aligner.align(seq1, seq2)`
**Explanation:** Uses BLOSUM62 scoring matrix for protein alignment.

### Custom gap penalties
**Args:** `aligner = Aligner(gap_open=-10, gap_extend=-2); result = aligner.align(seq1, seq2)`
**Explanation:** Sets custom gap opening (-10) and extension (-2) penalties.

### Get alignment score
**Args:** `score = result.getScore()`
**Explanation:** Retrieves the alignment score from the result object.

### Get aligned sequences
**Args:** `aligned_seq1, aligned_seq2 = result.getSequences()`
**Explanation:** Retrieves the aligned sequences with gaps.

### Multiple sequence alignment preparation
**Args:** `for seq in sequences: aligner.align(reference, seq)`
**Explanation:** Aligns multiple sequences to a reference sequence.

### Command line basic usage
**Args:** `alignlib-lite -i seq1.fasta -j seq2.fasta -o alignment.txt`
**Explanation:** Aligns two sequences from FASTA files and outputs result.

### Show alignment statistics
**Args:** `alignlib-lite -i seq1.fasta -j seq2.fasta --stats`
**Explanation:** Outputs detailed alignment statistics including score and identity.
