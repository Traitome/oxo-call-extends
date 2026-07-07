---
name: kmindex
category: formatting
description: Large-scale k-mer indexing for comparative genomics
tags: [kmindex, formatting, k-mer, indexing, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/tlemane/kmindex"
---

## Concepts

- **K-mer Indexing**: Builds large-scale k-mer indices for genomic databases
- **Shared K-mer Analysis**: Computes shared k-mers between query and databases
- **Comparative Genomics**: Enables efficient comparative analysis across genomes
- **Database Support**: Handles multiple genomic datasets in single index
- **Memory Efficiency**: Optimized for large-scale indexing
- **Query Processing**: Supports fast querying against indexed databases

## Pitfalls

- **Index Size**: Large databases create large indices
- **Build Time**: Index construction can be time-consuming
- **Memory Requirements**: Building requires significant memory
- **Query Sensitivity**: K-mer size affects query sensitivity
- **Database Updates**: Re-indexing needed for database updates
- **Disk Space**: Index storage can require substantial disk space

## Examples

### Build index from database
**Args:** `kmindex index -d genomes/ -o index_dir`
**Explanation:** Builds k-mer index from genome database.

### Query shared k-mers
**Args:** `kmindex query -d index_dir -q reads.fastq -o shared_kmers.tsv`
**Explanation:** Finds shared k-mers between query and indexed database.

### Batch querying
**Args:** `kmindex batch -d index_dir -q queries/ -o results/`
**Explanation:** Queries multiple samples against index.

### Specify k-mer size
**Args:** `kmindex index -d genomes/ -k 31 -o index_dir`
**Explanation:** Uses k-mer size of 31 for indexing.

### Filter by frequency
**Args:** `kmindex query -d index_dir -q reads.fastq --min-freq 3 -o results.tsv`
**Explanation:** Only reports k-mers with frequency >= 3.

### Export statistics
**Args:** `kmindex stats -d index_dir -o statistics.tsv`
**Explanation:** Exports index statistics and summary.