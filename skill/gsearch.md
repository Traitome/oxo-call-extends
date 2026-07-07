---
name: gsearch
category: bioinformatics
description: gsearch is an ultra-fast microbial genome search tool using MinHash-like metrics and graph-based approximate nearest neighbor search.
tags: [gsearch, genome-search, metagenomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/jean-pierreBoth/gsearch"
---

## Concepts

- **Genome Search**: gsearch performs fast search of microbial genomes.

- **MinHash Algorithm**: Uses MinHash-like metrics for efficient similarity estimation.

- **Graph-Based Search**: Implements graph-based approximate nearest neighbor search.

- **Scalability**: Designed for scalable search of large genome databases.

- **Database Indexing**: Creates indexes for fast search operations.

- **Similarity Scoring**: Calculates similarity scores between genomes.

## Pitfalls

- **Database Size**: Large databases require significant storage.

- **Index Time**: Index generation can be time-consuming for large datasets.

- **Memory Usage**: Loading large indexes may require significant memory.

- **Parameter Tuning**: Adjust parameters based on dataset characteristics.

- **Result Interpretation**: Interpret similarity scores carefully.

## Examples

### Build database index
**Args:** `gsearch index -i genomes/ -o index/`
**Explanation:** Creates an index for a genome database.

### Search database
**Args:** `gsearch search -q query.fasta -d index/ -o results.txt`
**Explanation:** Searches for similar genomes in the database.

### Adjust sensitivity
**Args:** `gsearch search -q query.fasta -d index/ -s high -o results.txt`
**Explanation:** Sets high sensitivity mode for more accurate search.

### Batch search
**Args:** `gsearch batch -q queries/ -d index/ -o results/`
**Explanation:** Searches multiple query genomes.

### Generate statistics
**Args:** `gsearch stats -d index/ -o stats.txt`
**Explanation:** Generates statistics about the database index.

### Compare genomes
**Args:** `gsearch compare -i genome1.fasta genome2.fasta -o comparison.txt`
**Explanation:** Compares two genomes directly.

### Help command
**Args:** `gsearch --help`
**Explanation:** Shows available options and usage information.