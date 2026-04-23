---
name: bedops
category: annotation
description: BEDOPS - High-performance genomic feature operations
tags: [bed, genomic-intervals, set-operations, intersection, merge, complement]
author: oxo-call-community
source_url: "https://github.com/bedops/bedops"
---

## Concepts
- **Tool Overview**: BEDOPS is a suite of high-performance tools for genomic interval operations. The core `bedops` command performs boolean set operations (union, intersection, difference, complement, etc.) on sorted BED and Starch files with exceptional speed and memory efficiency.
- **Sorted Input Requirement**: All input files must be pre-sorted using `sort-bed`. Unsorted inputs will produce incorrect results silently.
- **Set Operations**: Supports union (`--everything`), intersection (`--intersect`), difference (`--difference`), symmetric difference (`--symmdiff`), complement (`--complement`), element-of (`--element-of`), merge (`--merge`), partition (`--partition`), and chop (`--chop`).
- **Starch Format**: BEDOPS introduces the Starch archive format for compressed BED data, which can be used directly as input without decompression.
- **Chain Operations**: Operations can be piped together for complex analyses, e.g., extend regions then merge then intersect.

## Pitfalls
- **Must Pre-sort Input**: Input files MUST be sorted with `sort-bed` (not `sort -k1,1 -k2,2n`). Using standard Unix sort will produce incorrect results.
- **Column Retention**: Only `--everything`, `--element-of`, and `--not-element-of` preserve all columns. Other operations output only the first 3 columns (chrom, start, end).
- **Coordinate System**: BEDOPS uses 0-based half-open coordinates consistent with BED format.
- **Memory Efficiency**: BEDOPS processes files in a streaming manner and can handle arbitrarily large files with minimal memory.

## Examples
### Union of multiple BED files
**Args:** `bedops --everything file1.bed file2.bed file3.bed > union.bed`
**Explanation:** Combines all elements from three BED files into a single sorted output.

### Find overlapping regions with minimum overlap
**Args:** `bedops --element-of 50% query.bed reference.bed > overlaps.bed`
**Explanation:** Returns elements from query.bed that overlap reference.bed by at least 50% of the query element's length.

### Subtract regions
**Args:** `bedops --difference genes.bed repeats.bed > genes_no_repeats.bed`
**Explanation:** Removes regions from genes.bed that overlap with repeats.bed.

### Complement (find gaps)
**Args:** `bedops --complement features.bed > gaps.bed`
**Explanation:** Reports genomic regions NOT covered by any feature in the input file.

### Merge overlapping regions
**Args:** `bedops --merge input.bed > merged.bed`
**Explanation:** Merges overlapping or adjacent regions into contiguous intervals.

### Extend regions and intersect
**Args:** `bedops --range 50 --merge peaks.bed | bedops --intersect - promoters.bed > extended_intersections.bed`
**Explanation:** Extends peaks by 50bp, merges them, then finds intersections with promoters.

### Filter by chromosome
**Args:** `bedops --chrom chr1 --everything input.bed > chr1_only.bed`
**Explanation:** Processes only data from chromosome 1.

### Chop regions into fixed-size bins
**Args:** `bedops --chop 1000 regions.bed > binned.bed`
**Explanation:** Divides regions into 1000bp non-overlapping bins.
