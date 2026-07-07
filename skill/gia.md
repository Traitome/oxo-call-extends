---
name: gia
category: genomic-intervals
description: gia - Genomic Interval Arithmetic for interval operations and analysis.
tags: [gia, genomic-intervals, interval-operations, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/noamteyssier/gia"
---

## Concepts
- **Interval Operations**: Performs arithmetic on genomic intervals.
- **Bedtools Integration**: Extends bedtools functionality.
- **Set Operations**: Supports union, intersection, difference.
- **Coordinate Math**: Handles genomic coordinates.
- **Format Support**: Supports BED and similar formats.

## Pitfalls
- **Coordinate System**: Must handle chromosome naming consistently.
- **Strand Orientation**: Strand information may affect results.
- **Format Compatibility**: Requires correct input format.
- **Memory Usage**: Large files require memory.
- **Result Validation**: Results should be validated.

## Examples
### Intersect intervals
**Args:** `gia intersect -a intervals1.bed -b intervals2.bed -o intersect.bed`
**Explanation:** Finds intersecting intervals.

### Union intervals
**Args:** `gia union -i intervals.bed -o union.bed`
**Explanation:** Computes union of intervals.

### Subtract intervals
**Args:** `gia subtract -a intervals1.bed -b intervals2.bed -o diff.bed`
**Explanation:** Subtracts intervals.

### Find overlaps
**Args:** `gia overlap -a intervals1.bed -b intervals2.bed -o overlaps.bed`
**Explanation:** Finds overlapping regions.

### Generate statistics
**Args:** `gia stats -i intervals.bed -o stats.txt`
**Explanation:** Generates interval statistics.