---
name: ncls
category: programming
description: NCLS (Nested Containment List) is a fast interval tree-like implementation in C, wrapped for Python, providing efficient interval queries.
tags: [ncls, programming, interval-tree, bioinformatics, python]
author: oxo-call-community
source_url: "https://github.com/endrebak/ncls"
---

## Concepts

- **Tool Overview**: NCLS is a fast interval tree implementation in C with Python bindings for efficient interval overlap queries.
- **Core Function**: Provides fast construction and lookup of genomic intervals for interval-based operations.
- **Algorithm**: Implements a nested containment list data structure optimized for genomic interval queries.
- **Input Format**: Accepts intervals as start and end coordinates with optional payload data.
- **Output**: Returns intervals that overlap with query regions in O(log n) time complexity.
- **Use Case**: Genomic interval operations, peak calling, feature annotation, and variant analysis.

## Pitfalls

- **Memory Requirements**: Large interval sets can consume significant memory.
- **Version Compatibility**: API may change between versions.
- **C Dependencies**: Requires C compiler for installation from source.
- **Static Structure**: Once built, the interval tree cannot be dynamically modified.
- **Python Version**: May require specific Python version for compatibility.
- **Documentation**: Limited documentation requires code exploration.

## Examples

### Display help
**Args:** `python -c "from ncls import NCLS; help(NCLS)"`
**Explanation:** Shows available methods and usage instructions.

### Create interval tree
**Args:** `from ncls import NCLS; ncls = NCLS(starts, ends, ids)`
**Explanation:** Creates interval tree from start, end coordinates and IDs.

### Query overlaps
**Args:** `results = ncls.query(query_start, query_end)`
**Explanation:** Finds all intervals overlapping with query region.

### Batch query
**Args:** `results = ncls.query_batch(query_starts, query_ends)`
**Explanation:** Queries multiple intervals in batch.

### Get count
**Args:** `count = ncls.count_overlaps(start, end)`
**Explanation:** Returns number of overlapping intervals.

### Interval intersection
**Args:** `intersections = ncls.intersection(other_ncls)`
**Explanation:** Finds intervals common to two interval trees.