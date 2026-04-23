---
name: bedtk
category: annotation
description: A set of high-performance tools to process BED files
tags: [bed, intersection, merge, sort, coverage, performance]
author: oxo-call-community
source_url: "https://github.com/lh3/bedtk"
---

## Concepts
- **Tool Overview**: bedtk is a set of simple, high-performance tools for processing BED files, developed by Heng Li. It focuses on speed and memory efficiency, being several to tens of times faster than bedtools while using a fraction of the memory.
- **Core Operations**: Implements intersection, subtraction, sorting, merging, and coverage breadth computation.
- **Combined Operations**: Unlike bedtools, bedtk can perform sorting, merging, and intersection in one go without Unix pipes.
- **Performance**: Optimized for large genomic datasets, using efficient algorithms and minimal memory footprint.

## Pitfalls
- **Not a bedtools Replacement**: bedtk does not aim to match bedtools' full feature set. It provides a focused subset of operations with superior performance.
- **Input Requirements**: Input files should be properly formatted BED files. Some operations may require sorted input.
- **Limited Documentation**: bedtk has minimal documentation compared to bedtools.

## Examples
### Intersect two BED files
**Args:** `bedtk isec -i a.bed b.bed > intersect.bed`
**Explanation:** Finds overlapping regions between two BED files.

### Subtract regions
**Args:** `bedtk sub a.bed b.bed > subtracted.bed`
**Explanation:** Removes regions in b.bed from a.bed.

### Sort and merge in one step
**Args:** `bedtk merge input.bed > merged.bed`
**Explanation:** Sorts and merges overlapping/adjacent regions in one pass.

### Compute breadth of coverage
**Args:** `bedtk cov target.bed reads.bed`
**Explanation:** Computes the breadth of coverage of reads over target regions.

### Sort, merge, and intersect combined
**Args:** `bedtk isec -m -i a.bed b.bed > result.bed`
**Explanation:** Sorts, merges, and intersects both input files in one operation.
