---
name: unikmer
category: bioinformatics
description: UniKmer - K-mer based sequence analysis tool.
tags: [unikmer, k-mer, sequence-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/unikmer/"
---

## Concepts

- **Tool Overview**: UniKmer - A tool for k-mer based sequence analysis.
- **Core Function**: Analyzes k-mer frequencies and patterns in sequences.
- **Input**: Sequence files (FASTA/FASTQ).
- **Output**: K-mer statistics and analysis.
- **Installation**: Install via pip or conda
- **Use Case**: Sequence analysis, genome comparison, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large k-mer sets.
- **K-mer Size**: Results depend on k-mer size choice.

## Examples

### Count k-mers
**Args:** `unikmer count -i input.fasta -k 21 -o kmers.txt`
**Explanation:** Count k-mers of size 21.

### Compare k-mers
**Args:** `unikmer compare -i1 sample1.kmers -i2 sample2.kmers -o comparison.txt`
**Explanation:** Compare k-mer profiles.
