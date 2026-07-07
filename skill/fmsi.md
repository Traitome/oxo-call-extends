---
name: fmsi
category: formatting
description: FMSI - memory efficient k-mer set index based on masked superstrings and Burrows-Wheeler transform.
tags: [fmsi, k-mer, indexing, BWT, sequence analysis]
author: oxo-call-community
source_url: "https://github.com/OndrejSladky/fmsi"
---

## Concepts
- **Masked Superstrings**: Compresses k-mer sets into superstrings with masking to reduce memory usage.
- **BWT Integration**: Uses Burrows-Wheeler Transform for efficient pattern matching on the compressed index.
- **Memory Efficiency**: Significantly reduces memory footprint compared to traditional k-mer indexes.
- **Set Operations**: Supports efficient union, intersection, and difference operations on k-mer sets.
- **Query Performance**: Enables fast membership queries and set comparisons across large datasets.

## Pitfalls
- **Index Building Time**: Construction of the masked superstring index can be time-consuming for large k-mer sets.
- **K-mer Size Limits**: Performance degrades with very large k-mer sizes (>64).
- **Compression Trade-off**: Higher compression ratios may reduce query speed.
- **Reference Genome Dependence**: Index quality depends on the diversity of the input k-mer sets.
- **Output Format Limitations**: May require conversion for downstream tools expecting standard formats.

## Examples
### Build k-mer index from FASTA
**Args:** `fmsi build -i genome.fasta -k 31 -o index.fmsi`
**Explanation:** Builds an FMSI index from a genome FASTA file using k-mer size 31.

### Query k-mer membership
**Args:** `fmsi query -i index.fmsi -k ATCGATCGATCG`
**Explanation:** Checks if the specified k-mer exists in the indexed set.

### Compute intersection of two indexes
**Args:** `fmsi intersect -i index1.fmsi -j index2.fmsi -o common_kmers.txt`
**Explanation:** Finds common k-mers between two indexed k-mer sets.

### Build from multiple FASTA files
**Args:** `fmsi build -i genome1.fasta genome2.fasta -k 27 -o combined.fmsi`
**Explanation:** Builds a combined index from multiple genome sequences.

### Export k-mers to text file
**Args:** `fmsi export -i index.fmsi -o kmers.txt`
**Explanation:** Exports all k-mers in the index to a text file.