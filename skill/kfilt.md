---
name: kfilt
category: qc
description: A fast, multi-threaded tool for filtering FASTA/FASTQ reads based on k-mer matching using BK-trees.
tags: [kfilt, qc, FASTQ, FASTA, k-mer, filtering]
author: oxo-call-community
source_url: "https://github.com/davidebolo1993/kfilt"
---

## Concepts

- **Tool Overview**: kfilt (v0.1.1) - Fast read filtering tool using k-mer matching with BK-trees.
- **BK-tree Index**: Uses BK-tree data structure for fast k-mer lookups.
- **Multi-threaded**: Supports parallel processing for speed.
- **Quality Control**: Filters reads based on k-mer content.
- **FASTA/FASTQ**: Works with both sequence formats.
- **Pattern Matching**: Matches reads against k-mer patterns.

## Pitfalls

- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Memory Usage**: Large k-mer databases require memory.
- **False Positives**: Can produce false positive filtering.
- **Input Size**: Very large files may cause issues.
- **Thread Management**: Too many threads may reduce performance.
- **Pattern Quality**: Poor patterns affect filtering accuracy.

## Examples

### Filter reads by k-mer
**Args:** `kfilt -i reads.fastq -k 21 -p patterns.txt -o filtered.fastq`
**Explanation:** Filters reads containing specified k-mers.

### Multiple patterns
**Args:** `kfilt -i reads.fastq -k 31 -p pattern1.txt pattern2.txt -o filtered.fastq`
**Explanation:** Filters reads matching any of multiple pattern files.

### Output rejected reads
**Args:** `kfilt -i reads.fastq -k 21 -p patterns.txt -o filtered.fastq -r rejected.fastq`
**Explanation:** Outputs both accepted and rejected reads.

### Use multiple threads
**Args:** `kfilt -i reads.fastq -k 21 -p patterns.txt -o filtered.fastq -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### FASTA input
**Args:** `kfilt -i sequences.fasta -k 21 -p patterns.txt -o filtered.fasta -f fasta`
**Explanation:** Processes FASTA format input.

### Verbose mode
**Args:** `kfilt -i reads.fastq -k 21 -p patterns.txt -o filtered.fastq -v`
**Explanation:** Shows verbose output during filtering.