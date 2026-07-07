---
name: ushuffle
category: bioinformatics
description: uShuffle - Nucleic acid sequence shuffling tool.
tags: [ushuffle, sequence-shuffling, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/ushuffle/"
---

## Concepts

- **Tool Overview**: uShuffle - A tool for shuffling nucleic acid sequences.
- **Core Function**: Generates shuffled sequences while preserving k-mer frequencies.
- **Input**: Sequence file (FASTA).
- **Output**: Shuffled sequences.
- **Installation**: Install via conda or source
- **Use Case**: Sequence analysis, background modeling, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large sequences.
- **K-mer Size**: Results depend on k-mer size parameter.

## Examples

### Shuffle sequences
**Args:** `ushuffle -i input.fasta -o shuffled.fasta`
**Explanation:** Shuffle sequences preserving k-mer frequencies.

### With options
**Args:** `ushuffle -i input.fasta -o shuffled.fasta -k 3`
**Explanation:** Preserve 3-mer frequencies.
