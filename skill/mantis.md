---
name: mantis
category: formatting
description: "Mantis: A Fast, Small, and Exact Large-Scale Sequence-Search Index."
tags: [mantis, formatting, sequence-search, index]
author: oxo-call-community
source_url: "https://github.com/splatlab/mantis"
---
## Concepts

- **Tool Overview**: mantis v0.2 - Mantis is a fast, small, and exact large-scale sequence-search index for genomic sequence data.
- **Core Function**: Builds compact indexes for fast sequence searching in large genomic datasets.
- **Input/Output**: Input: Genomic sequences (FASTA); Output: Index files, search results.
- **Installation**: `conda install -c bioconda mantis`
- **Space-efficient**: Creates small index files for efficient storage.
- **Exact Matching**: Provides exact sequence matching capabilities.

## Pitfalls

- **Index Size**: Large genomes require significant storage for indexes.
- **Memory Usage**: Index building requires significant memory.
- **Query Length**: Short queries may have many matches.
- **Update Frequency**: Indexes require rebuilding when reference changes.
- **Query Complexity**: Complex queries may be slow.
- **Format Compatibility**: Requires specific input formats.

## Examples

### Build index
**Args:** `mantis build -i genome.fasta -o index/`
**Explanation:** Creates index from genomic sequences.

### Search index
**Args:** `mantis search -i index/ -q query.fasta -o results.txt`
**Explanation:** Searches index for query sequences.

### Batch search
**Args:** `mantis search -i index/ -q queries/ -o results/`
**Explanation:** Searches multiple query files.

### Quick search
**Args:** `mantis search -i index/ -q query.fasta -o results.txt --quick`
**Explanation:** Runs in quick search mode.

### Verbose mode
**Args:** `mantis search -i index/ -q query.fasta -o results.txt -v`
**Explanation:** Provides detailed logging during search.

### Index statistics
**Args:** `mantis stats -i index/ -o stats.txt`
**Explanation:** Generates statistics about the index.