---
name: adas
category: alignment
description: Sequence database search engine for long sequences using Minimizer, MinHash, Coreset and HNSW
tags: [sequence-search, minimizer, minhash, hnsw, long-sequences, database]
author: oxo-call-community
source_url: "https://github.com/jianshu93/adas"
---

## Concepts

- **Tool Overview**: ADAS is an innovative sequence database search engine for long sequences, combining Minimizer, MinHash, Coreset, and Hierarchical Navigable Small World Graphs (HNSW).
- **Core Function**: Enables fast similarity search and clustering of long biological sequences using approximate nearest neighbor techniques.
- **Input/Output**: Input: FASTA sequence database and query sequences. Output: Search results with similarity scores and matched sequences.
- **Algorithm**: Uses minimizer-based sketching with MinHash for dimensionality reduction, then HNSW graphs for efficient approximate nearest neighbor search.
- **Installation**: Install via bioconda: `conda install -c bioconda adas`

## Pitfalls

- **Memory Usage**: Building HNSW index requires memory proportional to database size - plan accordingly for large databases.
- **Approximate Results**: Uses approximate nearest neighbor search - results may not include all exact matches.
- **Parameter Tuning**: Search accuracy depends on HNSW parameters (ef_construction, M) - higher values improve recall but slow indexing.
- **Sequence Length**: Optimized for long sequences - short sequences may not benefit from minimizer-based approaches.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available commands and options for ADAS.

### Build search index
**Args:** `build -i database.fasta -o index_dir`
**Explanation:** Builds HNSW index from sequence database for fast searching.

### Search query sequences
**Args:** `search -i index_dir -q queries.fasta -o results.tsv`
**Explanation:** Searches query sequences against pre-built index, outputting matches.

### Build with custom parameters
**Args:** `build -i database.fasta -o index_dir -M 32 --ef-construction 200`
**Explanation:** Builds index with HNSW M=32 and ef_construction=200 for better recall.

### Search with higher accuracy
**Args:** `search -i index_dir -q queries.fasta -o results.tsv --ef-search 500`
**Explanation:** Uses higher ef_search value for more accurate (but slower) search results.

### Cluster sequences
**Args:** `cluster -i database.fasta -o clusters.tsv --threshold 0.95`
**Explanation:** Clusters sequences at 95% similarity threshold using the search index.

### Direct search without index
**Args:** `search-direct -d database.fasta -q queries.fasta -o results.tsv`
**Explanation:** Performs direct search without building persistent index (slower for repeated searches).
