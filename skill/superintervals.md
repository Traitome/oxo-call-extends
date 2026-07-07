---
name: superintervals
category: utility
description: Rapid interval intersections for genomic regions analysis.
tags: [superintervals, interval-analysis, genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/kcleal/superintervals"
---

## Concepts

- **Tool Overview**: superintervals (v0.3.5) performs rapid interval intersections for genomic analysis.
- **Core Function**: Efficiently finds intersections between sets of genomic intervals.
- **Algorithm**: Uses interval tree data structure for fast intersection queries.
- **Input/Output**: Input: BED/GFF files with intervals; Output: Intersected intervals.
- **Applications**: Genomics, ChIP-seq analysis, peak calling, region analysis.
- **Installation**: `conda install -c bioconda superintervals` or download from GitHub.

## Pitfalls

- **Input Format**: Requires sorted intervals for optimal performance.
- **Memory Requirements**: Large interval sets require significant memory.
- **Performance**: Very large inputs can be slow.
- **Overlap Definition**: Different overlap definitions affect results.
- **Coordinate System**: Requires consistent coordinate system.
- **File Size**: Very large files may cause issues.

## Examples

### Display help
**Args:** `superintervals --help`
**Explanation:** Shows available options and usage information.

### Basic intersection
**Args:** `superintervals -a regions1.bed -b regions2.bed -o intersection.bed`
**Explanation:** Find intersections between two interval sets.

### With overlap threshold
**Args:** `superintervals -a regions1.bed -b regions2.bed -o intersection.bed -f 0.5`
**Explanation:** Require 50% overlap for intersection.

### Verbose mode
**Args:** `superintervals -a regions1.bed -b regions2.bed -o intersection.bed -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `superintervals -a regions1.bed -b regions2.bed -o intersection.bed --stats`
**Explanation:** Generate statistics about intersections.

### Batch processing
**Args:** `superintervals -a regions/ -b targets.bed -o results/`
**Explanation:** Intersect multiple interval files with target.

### Filter by size
**Args:** `superintervals -a regions1.bed -b regions2.bed -o intersection.bed -m 100`
**Explanation:** Minimum interval size of 100.

### Include non-overlapping
**Args:** `superintervals -a regions1.bed -b regions2.bed -o intersection.bed --non-overlapping`
**Explanation:** Include non-overlapping regions.

### Generate report
**Args:** `superintervals -a regions1.bed -b regions2.bed -o intersection.bed --report`
**Explanation:** Generate comprehensive HTML report.
