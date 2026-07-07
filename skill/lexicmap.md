---
name: lexicmap
category: alignment
description: Efficient sequence alignment against millions of prokaryotic genomes
tags: [lexicmap, alignment, prokaryotic, genome-search, large-scale]
author: oxo-call-community
source_url: "https://github.com/shenwei356/LexicMap"
---

## Concepts

- **Large-scale Search**: Aligns sequences against millions of genomes
- **Prokaryotic Focus**: Optimized for prokaryotic genome databases
- **Efficient Indexing**: Uses efficient indexing for fast searches
- **K-mer Based**: K-mer based sequence comparison
- **Multi-genome**: Handles very large genome collections
- **Rapid Alignment**: Fast alignment to large databases

## Pitfalls

- **Memory Usage**: Indexing millions of genomes requires significant memory
- **Database Size**: Very large databases increase search time
- **K-mer Selection**: K-mer size affects sensitivity/speed
- **Sequence Length**: Very short sequences may not align
- **Database Updates**: Requires regular database updates
- **Computational Resources**: Significant resources needed for indexing

## Examples

### Index references
**Args:** `lexicmap index -k 31 -s reference.fasta -o index_dir`
**Explanation:** Builds LexicMap index from reference sequences.

### Search queries
**Args:** `lexicmap search -i index_dir -q queries.fasta -o results.tsv`
**Explanation:** Searches query sequences against indexed references.

### Batch search
**Args:** `lexicmap search -i index_dir -q queries.txt -o results.tsv`
**Explanation:** Searches multiple query files.

### Set k-mer size
**Args:** `lexicmap index -k 25 -s reference.fasta -o index_dir`
**Explanation:** Uses k-mer size of 25.

### Filter results
**Args:** `lexicmap search -i index_dir -q queries.fasta -t 0.9 -o results.tsv`
**Explanation:** Filters by similarity threshold of 90%.

### Index statistics
**Args:** `lexicmap stats -i index_dir`
**Explanation:** Shows index statistics.