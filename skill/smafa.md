---
name: smafa
category: sequence-analysis
description: smafa is a tool for querying and clustering pre-aligned small sequences
tags: [smafa, sequence-analysis, clustering, small-rna, alignment]
author: oxo-call-community
source_url: "https://github.com/wwood/smafa"
---

## Concepts

- **Tool Overview**: smafa (v0.8.0) - A tool for querying and clustering pre-aligned small sequences
- **Core Function**: Efficiently searches and clusters short, pre-aligned sequences
- **Input/Output**: Accepts FASTA/FASTQ files; outputs clustered sequences and alignments
- **Algorithm**: Uses suffix array indexing for fast sequence queries
- **Installation**: `conda install -c bioconda smafa`
- **Key Features**: Fast querying, clustering support, handles small RNA data

## Pitfalls

- **Pre-alignment Requirement**: Requires pre-aligned input sequences
- **Sequence Length**: Optimized for small sequences (50-200bp)
- **Memory Usage**: Large databases may require significant memory
- **Index Building**: Index creation can be time-consuming
- **Database Format**: Requires specific database format
- **Query Size**: Query sequences must match database characteristics

## Examples

### Display help
**Args:** `smafa --help`
**Explanation:** Shows available options and usage information.

### Build database
**Args:** `smafa build -i sequences.fasta -o smafa_db`
**Explanation:** Build smafa database from input sequences.

### Query database
**Args:** `smafa query -d smafa_db -q queries.fasta -o results.txt`
**Explanation:** Query sequences against smafa database.

### Cluster sequences
**Args:** `smafa cluster -i sequences.fasta -o clusters.txt`
**Explanation:** Cluster pre-aligned sequences.

### Search with mismatches
**Args:** `smafa query -d smafa_db -q queries.fasta -m 2 -o results.txt`
**Explanation:** Allow up to 2 mismatches in search.

### Extract subset
**Args:** `smafa extract -d smafa_db -l list.txt -o subset.fasta`
**Explanation:** Extract specific sequences from database.

### Batch query
**Args:** `smafa batch -d smafa_db -i query_dir/ -o results_dir/`
**Explanation:** Process multiple query files in batch.