---
name: ruranges
category: programming
description: Rust-backed interval kernels exposed to Python/NumPy.
tags: ["ruranges", "rust", "python", "interval", "genomics"]
author: oxo-call-community
source_url: "https://github.com/pyranges/ruranges"
---

## Concepts

- **Tool Overview**: ruranges (v0.1.3) is a Python package that provides high-performance interval operations using Rust-backed kernels. It exposes efficient interval arithmetic to Python/NumPy for genomic interval analysis.
- **Core Function**: Implements fast interval operations (intersection, union, difference, overlap detection) using Rust for computational efficiency while providing a Pythonic interface.
- **Algorithm**: Uses sorted interval trees and bitwise operations for efficient interval manipulation. Leverages Rust's memory safety and performance.
- **Input Format**: NumPy arrays or pandas DataFrames containing interval start and end positions.
- **Output Format**: NumPy arrays or pandas DataFrames with interval operation results.
- **Use Case**: Genomic interval analysis, peak calling, ChIP-seq analysis, variant filtering, genome annotation.

## Pitfalls

- **Python dependency**: Requires Python environment with NumPy.
- **Rust compilation**: First installation requires Rust toolchain for compilation.
- **Memory overhead**: Converting between Python and Rust data structures has overhead.
- **API stability**: May have breaking changes between versions.
- **Documentation**: Limited documentation for advanced usage.
- **Platform compatibility**: May not build on all platforms.

## Examples

### Intersect intervals
**Args:** `python -c "import ruranges; result = ruranges.intersect(a, b)"`
**Explanation:** Computes intersection of two interval arrays.

### Union intervals
**Args:** `python -c "import ruranges; result = ruranges.union(intervals)"`
**Explanation:** Merges overlapping or adjacent intervals.

### Find overlaps
**Args:** `python -c "import ruranges; hits = ruranges.overlap(query, target)"`
**Explanation:** Finds all intervals in target that overlap with query.

### Interval difference
**Args:** `python -c "import ruranges; result = ruranges.difference(a, b)"`
**Explanation:** Subtracts intervals in b from intervals in a.

### Interval complement
**Args:** `python -c "import ruranges; result = ruranges.complement(intervals, genome_size)"`
**Explanation:** Finds intervals not covered by input intervals.

### Sort intervals
**Args:** `python -c "import ruranges; sorted = ruranges.sort(intervals)"`
**Explanation:** Sorts intervals by start position.

### Interval statistics
**Args:** `python -c "import ruranges; stats = ruranges.stats(intervals)"`
**Explanation:** Computes statistics (total bases, interval count, mean length).
