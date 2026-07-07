---
name: kmtricks
category: utility
description: A k-mer matrix framework for large-scale read collections
tags: [kmtricks, utility, k-mer, matrix, bloom-filter, genomics]
author: oxo-call-community
source_url: "https://github.com/tlemane/kmtricks"
---

## Concepts

- **K-mer Matrix Construction**: Builds k-mer presence/absence matrices
- **Bloom Filter Integration**: Uses Bloom filters for memory efficiency
- **Large-scale Processing**: Handles massive read collections efficiently
- **Read Collections**: Processes multiple samples simultaneously
- **Matrix Export**: Exports k-mer matrices for downstream analysis
- **Parallel Processing**: Supports multi-threaded computation

## Pitfalls

- **Memory Usage**: Large matrices require significant memory
- **Disk Space**: Intermediate files can consume substantial space
- **K-mer Selection**: K-mer size affects matrix characteristics
- **Sample Number**: More samples increase matrix complexity
- **Threshold Selection**: Abundance thresholds affect results
- **Matrix Sparsity**: Very sparse matrices may be inefficient

## Examples

### Build k-mer matrix
**Args:** `kmtricks pipeline --file reads.list --run-dir output --kmer-size 31`
**Explanation:** Builds k-mer matrix from read list.

### Specify sample list
**Args:** `kmtricks pipeline --file samples.txt --run-dir results --kmer-size 25`
**Explanation:** Uses sample list file for matrix construction.

### With Bloom filter
**Args:** `kmtricks pipeline --file reads.list --run-dir output --bloom`
**Explanation:** Uses Bloom filter for memory efficiency.

### Filter by abundance
**Args:** `kmtricks pipeline --file reads.list --run-dir output --min-count 2`
**Explanation:** Only includes k-mers with count >= 2.

### Export matrix
**Args:** `kmtricks matrix --run-dir output -o matrix.tsv`
**Explanation:** Exports constructed k-mer matrix.

### Batch processing
**Args:** `kmtricks batch --config config.yaml --run-dir results/`
**Explanation:** Processes multiple configurations in batch mode.