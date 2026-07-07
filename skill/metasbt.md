---
name: metasbt
category: variant-calling
description: Microbial genomes characterization with Sequence Bloom Trees.
tags: [metasbt, variant-calling, sequence-bloom-trees]
author: oxo-call-community
source_url: "https://github.com/cumbof/MetaSBT"
---

## Concepts

- **Tool Overview**: MetaSBT v0.1.5 is a scalable framework for indexing microbial genomes and characterizing metagenome-assembled genomes using Sequence Bloom Trees.
- **Core Function**: Characterizes microbial genomes and MAGs (Metagenome-Assembled Genomes) using efficient indexing techniques.
- **Sequence Bloom Trees**: Uses Sequence Bloom Trees for fast and memory-efficient sequence indexing and querying.
- **Scalable Indexing**: Enables efficient indexing of large collections of microbial genomes.
- **Input/Output**: Accepts genome sequences and metagenomic data; outputs genome characterizations and comparisons.
- **Memory Efficiency**: Designed for bounded memory usage even with large inputs.

## Pitfalls

- **Index Size**: Building indexes for large genome collections may require significant storage.
- **Query Complexity**: Complex queries may require careful optimization.
- **Memory Management**: Although optimized, large datasets may still require substantial memory.
- **Database Completeness**: Analysis quality depends on reference database completeness.
- **False Positives**: May produce false positive matches.
- **Runtime**: Index construction can be time-consuming for large datasets.

## Examples

### Build Sequence Bloom Tree index
**Args:** `metasbt build -i genomes/ -o index/`
**Explanation:** Builds a Sequence Bloom Tree index from genome sequences.

### Query index
**Args:** `metasbt query -i index/ -q query.fasta -o results.txt`
**Explanation:** Queries the index with input sequences.

### Characterize MAGs
**Args:** `metasbt characterize -i mags.fasta -d index/ -o results/`
**Explanation:** Characterizes metagenome-assembled genomes.

### Compare genomes
**Args:** `metasbt compare -i genome1.fasta genome2.fasta -d index/`
**Explanation:** Compares two genomes using the indexed database.

### Batch processing
**Args:** `metasbt query -i index/ -q queries/ -o results/`
**Explanation:** Processes multiple query files in batch.