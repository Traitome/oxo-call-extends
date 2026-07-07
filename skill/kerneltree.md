---
name: kerneltree
category: programming
description: Ultrafast interval tree implementation from Linux kernel, wrapped for Python.
tags: [kerneltree, programming, interval tree, Python, kernel]
author: oxo-call-community
source_url: "https://pypi.org/project/kerneltree/"
---

## Concepts

- **Tool Overview**: kerneltree (v0.0.5) - Fast interval tree implementation from Linux kernel.
- **Interval Tree**: Data structure for interval queries.
- **Kernel Implementation**: Based on Linux kernel's interval tree.
- **Python Wrapper**: Python interface for easy use.
- **Fast Queries**: O(log n) time complexity for queries.
- **Memory Efficient**: Optimized memory usage.

## Pitfalls

- **Interval Overlaps**: Requires understanding of interval overlaps.
- **Memory Management**: Large trees require memory.
- **Python GIL**: May be affected by Python GIL.
- **Version Compatibility**: May have version-specific issues.
- **Documentation**: Limited documentation available.
- **Error Handling**: Limited error handling.

## Examples

### Create interval tree
**Args:** `from kerneltree import IntervalTree; it = IntervalTree()`
**Explanation:** Creates empty interval tree.

### Add intervals
**Args:** `it.add(10, 20, "region1"); it.add(15, 25, "region2")`
**Explanation:** Adds intervals to tree.

### Query overlaps
**Args:** `results = it.find_overlapping(12, 18)`
**Explanation:** Finds all intervals overlapping [12, 18].

### Query point
**Args:** `results = it.find_containing(15)`
**Explanation:** Finds intervals containing position 15.

### Delete interval
**Args:** `it.remove(10, 20, "region1")`
**Explanation:** Removes specific interval.

### Iterate intervals
**Args:** `for interval in it: print(interval)`
**Explanation:** Iterates through all intervals.