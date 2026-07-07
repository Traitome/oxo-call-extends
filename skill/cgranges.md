---
name: cgranges
category: genomics
description: High-performance C library for genomic interval overlap queries
tags: [cgranges, c-library, genomic-intervals, bioinformatics, interval-tree]
author: oxo-call-community
source_url: "https://github.com/lh3/cgranges"
---

## Concepts

- **Tool Overview**: cgranges is a small, fast C library designed for efficient genomic interval overlap queries.
- **Core Function**: Provides interval tree data structure for fast overlap queries on genomic intervals.
- **Algorithm**: Implements interval tree for O(log n) time complexity for overlap queries.
- **Input**: Genomic intervals (chromosome, start, end coordinates).
- **Output**: List of overlapping intervals for given query regions.
- **Application**: Genomic feature annotation, variant analysis, and interval-based queries.
- **Installation**: Install via bioconda: `conda install -c bioconda cgranges`

## Pitfalls

- **C Library**: Requires C programming knowledge for direct usage.
- **Memory Management**: Manual memory management required in C.
- **Coordinate System**: Zero-based vs one-based coordinate handling.
- **Sorting**: Intervals must be sorted for optimal performance.

## Examples

### Build index from BED file
**Args:** `cgranges-build -i intervals.bed -o index.cgr`
**Explanation:** Builds interval index from BED file.

### Query overlapping intervals
**Args:** `cgranges-query -i index.cgr -c chr1 -s 1000 -e 2000`
**Explanation:** Finds all intervals overlapping region chr1:1000-2000.

### Convert to BED format
**Args:** `cgranges-convert -i index.cgr -o intervals.bed`
**Explanation:** Converts index back to BED format.

### Display help
**Args:** `cgranges-build --help`
**Explanation:** Shows all available options and usage information.