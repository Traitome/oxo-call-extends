---
name: deacon
category: alignment
description: Fast alignment-free sequence filter using k-mer matching.
tags: [deacon, alignment, k-mer, sequence-filtering, alignment-free]
author: oxo-call-community
source_url: "https://github.com/bede/deacon"
---

## Concepts

- **Tool Overview**: deacon (v0.15.0+) is a fast alignment-free sequence filtering tool that uses k-mer matching to quickly identify and filter sequences without performing full alignment.
- **Core Function**: Rapidly filters or categorizes sequences based on k-mer content, useful for removing contaminants, identifying sequences of interest, or pre-filtering before alignment.
- **Input/Output**: Input: FASTA/FASTQ sequences, k-mer database or reference sequences. Output: Filtered sequences, matching statistics.
- **Algorithm**: Uses k-mer indexing and counting for fast sequence comparison without performing computationally expensive alignments.
- **Key Features**: Fast filtering, memory-efficient, supports multiple filtering criteria, no alignment required.
- **Installation**: `conda install -c bioconda deacon`

## Pitfalls

- **K-mer Size**: K-mer size affects sensitivity and specificity.
- **False Positives**: May have false positives for sequences with shared k-mers.
- **Memory Usage**: Large k-mer databases may require significant memory.
- **Sequence Similarity**: Works best for sequences with clear k-mer differences.
- **Filtering Threshold**: Requires appropriate threshold for filtering decisions.

## Examples

### Filter sequences by k-mer content
**Args:** `deacon -i sequences.fasta -d reference.fasta -o filtered.fasta`
**Explanation:** Filter sequences based on k-mer similarity to reference.

### Specify k-mer size
**Args:** `deacon -i sequences.fasta -d reference.fasta -k 21 -o filtered.fasta`
**Explanation:** Use k-mer size of 21 for filtering.

### Set filtering threshold
**Args:** `deacon -i sequences.fasta -d reference.fasta --threshold 0.8 -o filtered.fasta`
**Explanation:** Filter sequences with at least 80% k-mer match.