---
name: rust-gtars
category: utility
description: Performance-critical tools to manipulate, analyze, and process genomic interval data.
tags: ["rust-gtars", "rust", "genomic", "interval", "bioinformatics"]
author: oxo-call-community
source_url: "https://docs.rs/crate/gtars/0.8.0"
---

## Concepts

- **Tool Overview**: rust-gtars (v0.8.0) is a high-performance toolkit for manipulating and analyzing genomic interval data. Built in Rust, it provides fast interval operations for genome analysis.
- **Core Function**: Implements efficient interval tree data structures and operations for genomic regions. Supports interval intersection, union, overlap detection, and genome arithmetic.
- **Algorithm**: Uses interval trees, segment trees, and bit-parallel operations for fast interval queries. Optimized for both speed and memory efficiency.
- **Input Format**: BED, GFF, BEDPE, and custom interval formats. Supports reading from files or standard input.
- **Output Format**: BED, GFF, TSV, and JSON formats. Can output statistics and summary reports.
- **Use Case**: ChIP-seq peak analysis, genome annotation, variant filtering, interval-based genome comparisons, feature counting.

## Pitfalls

- **Rust dependency**: Requires Rust toolchain for installation from source.
- **Format limitations**: May not support all edge cases of BED/GFF formats.
- **Memory requirements**: Large interval sets require significant memory.
- **Learning curve**: CLI interface may be unfamiliar to some users.
- **Documentation**: Limited examples for advanced usage.
- **Platform support**: Binary releases may not be available for all platforms.

## Examples

### Intersect two BED files
**Args:** `gtars intersect -a peaks.bed -b regions.bed -o intersections.bed`
**Explanation:** `-a` and `-b` input BED files; `-o` output intersections.

### Merge overlapping intervals
**Args:** `gtars merge -i peaks.bed -o merged.bed`
**Explanation:** Merges overlapping or adjacent intervals into single intervals.

### Count intervals per chromosome
**Args:** `gtars count -i intervals.bed -o counts.tsv`
**Explanation:** Counts intervals on each chromosome.

### Subtract intervals
**Args:** `gtars subtract -a all.bed -b exclude.bed -o remaining.bed`
**Explanation:** Removes intervals in exclude.bed from all.bed.

### Find unique intervals
**Args:** `gtars unique -a set1.bed -b set2.bed -o unique.bed`
**Explanation:** Finds intervals present in set1 but not in set2.

### Interval statistics
**Args:** `gtars stats -i intervals.bed -o stats.json`
**Explanation:** Computes statistics (total bases, interval count, distribution).

### Sort intervals
**Args:** `gtars sort -i unsorted.bed -o sorted.bed`
**Explanation:** Sorts intervals by chromosome and start position.
