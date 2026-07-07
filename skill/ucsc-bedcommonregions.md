---
name: ucsc-bedcommonregions
category: utility
description: UCSC bedCommonRegions - Tool for finding common regions in multiple BED files.
tags: [ucsc-bedcommonregions, ucsc, bed-analysis, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedCommonRegions - A tool for finding overlapping regions across multiple BED files.
- **Core Function**: Identifies regions common to all input BED files.
- **Input**: Multiple BED files.
- **Output**: BED file with common regions.
- **Installation**: Part of UCSC utilities
- **Use Case**: Peak calling, region intersection, data integration.

## Pitfalls

- **File Format**: Requires consistent BED format across files.
- **Memory**: May require significant memory for many files.

## Examples

### Find common regions
**Args:** `bedCommonRegions file1.bed file2.bed file3.bed > common.bed`
**Explanation:** Find regions common to all BED files.

### With min overlap
**Args:** `bedCommonRegions -minOverlap 0.5 file*.bed > common.bed`
**Explanation:** Find regions with minimum 50% overlap.
