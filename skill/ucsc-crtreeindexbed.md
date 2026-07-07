---
name: ucsc-crtreeindexbed
category: utility
description: UCSC crTreeIndexBed - Tool for indexing BED files with crTree.
tags: [ucsc-crtreeindexbed, ucsc, indexing, bed, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC crTreeIndexBed - A tool for creating crTree indexes for BED files.
- **Core Function**: Builds spatial index for fast BED file queries.
- **Input**: BED file.
- **Output**: Indexed BED file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Fast querying, genome browser, data indexing.

## Pitfalls

- **BED Format**: Requires proper BED format.
- **Memory**: May require significant memory for large files.

## Examples

### Index BED file
**Args:** `crTreeIndexBed input.bed output.index`
**Explanation:** Create crTree index for BED file.

### With options
**Args:** `crTreeIndexBed -blockSize=1000 input.bed output.index`
**Explanation:** Index with specified block size.
