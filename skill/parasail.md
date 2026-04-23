---
name: parasail
category: variant-calling
description: Pairwise Sequence Alignment Library
tags: [parasail, variant-calling]
author: oxo-call-community
source_url: "https://github.com/jeffdaily/parasail"
---

## Concepts
- **Tool Overview**: parasail is a SIMD C (C99) library containing implementations of the Smith-Waterman (local), Needleman-Wunsch (global), and various semi-global pairwise sequence alignment algorithms. Here, semi-global means insertions before the start or after the end of either the query or target sequence are optionally not penalized. parasail implements most known algorithms for vectorized pairwise sequence alignment, including diagonal [Wozniak, 1997], blocked [Rognes and Seeberg, 2000], striped [Farrar, 2007], and prefix scan [Daily, 2015]. Therefore, parasail is a reference implementation for these algorithms in addition to providing an implementation of the best-performing algorithm(s) to date on today's most advanced CPUs.
- **Core Function**: Pairwise Sequence Alignment Library
- **Input/Output**: FASTA/BAM/SAM
- **Installation**: `conda install -c bioconda parasail`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
