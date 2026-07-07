---
name: intervals
category: programming
description: Python tools for handling intervals (ranges of comparable objects)
tags: [intervals, programming, python, ranges]
author: oxo-call-community
source_url: "https://github.com/kvesteri/intervals"
---

## Concepts

- **Tool Overview**: intervals (v0.6.0) is a Python library for working with interval ranges
- **Core Function**: Provides tools for interval arithmetic, comparison, and manipulation
- **Interval Types**: Supports closed, open, and half-open intervals
- **Operations**: Union, intersection, difference, and containment checks
- **Installation**: `conda install -c bioconda intervals`

## Pitfalls

- **Inclusive vs Exclusive**: Be careful with interval boundaries (inclusive vs exclusive endpoints)
- **Type Consistency**: All interval endpoints must be of the same comparable type
- **Empty Intervals**: Operations on empty intervals may produce unexpected results
- **Performance**: Large interval collections may require specialized data structures
- **Version Compatibility**: API may change between versions

## Examples

### Create an interval
**Args:** `python -c "from intervals import Interval; iv = Interval('[1, 10]'); print(iv)"`
**Explanation:** Creates a closed interval from 1 to 10 (inclusive).

### Check containment
**Args:** `python -c "from intervals import Interval; iv = Interval('[1, 10]'); print(5 in iv)"`
**Explanation:** Checks if value 5 is contained within the interval.

### Interval intersection
**Args:** `python -c "from intervals import Interval; iv1 = Interval('[1, 10]'); iv2 = Interval('[5, 15]'); print(iv1 & iv2)"`
**Explanation:** Computes the intersection of two intervals.

### Interval union
**Args:** `python -c "from intervals import Interval; iv1 = Interval('[1, 5]'); iv2 = Interval('[8, 12]'); print(iv1 | iv2)"`
**Explanation:** Computes the union of two intervals.

### Create empty interval
**Args:** `python -c "from intervals import Interval; iv = Interval.empty(); print(iv)"`
**Explanation:** Creates an empty interval.

### Parse interval string
**Args:** `python -c "from intervals import Interval; iv = Interval.parse('(1, 10]'); print(iv)"`
**Explanation:** Parses an interval from string representation (open start, closed end).