---
name: fulgor
category: formatting
description: A fast and space-efficient colored de Bruijn graph index.
tags: [fulgor, de Bruijn graph, sequence indexing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/jermp/fulgor"
---

## Concepts
- **Colored de Bruijn Graph**: Builds colored de Bruijn graph indexes.
- **Space-efficient**: Optimized for memory usage.
- **Fast Querying**: Enables fast sequence queries.
- **Multiple Colors**: Supports multiple datasets (colors) in a single index.
- **GGCAT Integration**: Powered by GGCAT for efficient graph construction.

## Pitfalls
- **Memory Requirements**: Index construction requires significant memory.
- **K-mer Size**: K-mer size selection affects performance.
- **Index Building Time**: Building index for large datasets is time-consuming.
- **Query Complexity**: Complex queries may be slow.
- **Format Limitations**: Specific input format requirements.

## Examples
### Build index from FASTA
**Args:** `fulgor build -i genome.fasta -k 31 -o index.fulgor`
**Explanation:** Builds colored de Bruijn graph index with k=31.

### Query index
**Args:** `fulgor query -i index.fulgor -q query.fasta -o results.txt`
**Explanation:** Queries index with sequences from query file.

### Build multi-color index
**Args:** `fulgor build -i genome1.fasta genome2.fasta -k 31 -o multi_index.fulgor`
**Explanation:** Builds index with multiple genomes (colors).

### Search for k-mers
**Args:** `fulgor search -i index.fulgor -k ATCGATCG -o matches.txt`
**Explanation:** Searches for specific k-mer in index.

### Statistics
**Args:** `fulgor stats -i index.fulgor -o stats.txt`
**Explanation:** Generates statistics about the index.