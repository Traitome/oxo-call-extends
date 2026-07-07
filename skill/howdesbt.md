---
name: howdesbt
category: sequence_analysis
description: Sequence Bloom Tree, supporting determined/how split filters for efficient large-scale sequence database search
tags: [howdesbt, bloom_filter, sequence_search, k-mer, indexing]
author: oxo-call-community
source_url: "https://github.com/medvedevgroup/HowDeSBT/blob/2.00.15/README.md"
---

## Concepts

- **Sequence Bloom Tree**: Hierarchical data structure for efficient sequence presence queries
- **K-mer Indexing**: Uses k-mer based indexing for rapid sequence similarity searches
- **Split Filters**: Implements novel partitioning strategy to reduce index size and query time
- **Determined/How Splitting**: Two partitioning strategies for optimal index construction
- **Scalable Search**: Designed for large-scale sequence databases like SRA
- **Probabilistic Data Structure**: Uses Bloom filters for space-efficient storage with controlled false positives

## Pitfalls

- **False Positives**: Bloom filter-based approach can produce false positive results
- **K-mer Selection**: Optimal k-mer size depends on dataset characteristics (typically 31-71)
- **Index Construction Time**: Building indexes for very large databases can be time-consuming
- **Memory Requirements**: Large indexes require significant memory resources during construction
- **Query Batch Size**: Small query batches may not fully utilize the index's performance benefits
- **Sensitivity vs Specificity**: Adjusting filter parameters requires careful tuning

## Examples

### Build index from FASTA files
**Args:** `howdesbt build -i *.fasta -o sbt_index/ -k 31`
**Explanation:** Builds a Sequence Bloom Tree index from multiple FASTA files using k-mer size 31.

### Query the index
**Args:** `howdesbt query -i query.fasta -d sbt_index/ -o results.txt`
**Explanation:** Queries the SBT index with sequences from query.fasta and outputs presence/absence results.

### Build with "how" splitting
**Args:** `howdesbt build -i *.fasta -o sbt_index/ -k 31 --split how`
**Explanation:** Constructs the index using the "how" splitting strategy for improved query performance.

### Build with "determined" splitting
**Args:** `howdesbt build -i *.fasta -o sbt_index/ -k 51 --split determined`
**Explanation:** Uses "determined" splitting strategy for more balanced index construction.

### Batch query mode
**Args:** `howdesbt query -i queries/ -d sbt_index/ -o results/ --batch`
**Explanation:** Processes multiple query files in batch mode for increased throughput.