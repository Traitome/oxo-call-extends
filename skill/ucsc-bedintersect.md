---
name: ucsc-bedintersect
category: utility
description: UCSC bedIntersect - Tool for intersecting BED files.
tags: [ucsc-bedintersect, ucsc, bed-analysis, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedIntersect - A tool for finding intersections between BED files.
- **Core Function**: Identifies overlapping regions between two or more BED files.
- **Input**: Multiple BED files.
- **Output**: BED file with overlapping regions.
- **Installation**: Part of UCSC utilities
- **Use Case**: Peak calling, region analysis, data integration.

## Pitfalls

- **File Order**: May produce different results based on file order.
- **Memory**: May require significant memory for large files.

## Examples

### Intersect BED files
**Args:** `bedIntersect file1.bed file2.bed > intersection.bed`
**Explanation:** Find overlapping regions between two BED files.

### With minimum overlap
**Args:** `bedIntersect -minOverlap 0.5 file1.bed file2.bed > intersection.bed`
**Explanation:** Find regions with minimum 50% overlap.
