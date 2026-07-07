---
name: sorted_nearest
category: utility
description: Sorted Nearest - Find nearest intervals in sorted files
tags: [sorted_nearest, utility, intervals, nearest, genomic]
author: oxo-call-community
source_url: "https://github.com/endrebak/sorted_nearest"
---

## Concepts

- **Tool Overview**: sorted_nearest (v0.0.41) - An interval nearest neighbor finder
- **Core Function**: Finds nearest intervals between sorted genomic files
- **Input/Output**: Accepts sorted BED files; outputs nearest interval pairs
- **Algorithm**: Efficient nearest neighbor search on sorted intervals
- **Installation**: `conda install -c bioconda sorted_nearest`
- **Key Features**: Nearest neighbor, sorted intervals, genomic regions

## Pitfalls

- **Input Requirements**: Requires properly sorted BED files
- **Sorting**: Files must be sorted by chromosome and position
- **Interval Format**: Intervals must be in BED format
- **Memory Usage**: Large interval files require significant memory
- **Distance Calculation**: Distance calculation depends on interval type
- **Output Format**: Output format depends on configuration

## Examples

### Display help
**Args:** `sorted_nearest --help`
**Explanation:** Shows available options and usage information.

### Basic nearest search
**Args:** `sorted_nearest -a intervals1.bed -b intervals2.bed -o nearest.txt`
**Explanation:** Find nearest intervals between files.

### With distance
**Args:** `sorted_nearest -a intervals1.bed -b intervals2.bed -o nearest.txt --distance`
**Explanation:** Output distance to nearest interval.

### With both directions
**Args:** `sorted_nearest -a intervals1.bed -b intervals2.bed -o nearest.txt --both`
**Explanation:** Find nearest in both directions.

### With overlap check
**Args:** `sorted_nearest -a intervals1.bed -b intervals2.bed -o nearest.txt --overlap`
**Explanation:** Check for overlapping intervals.

### Filter by distance
**Args:** `sorted_nearest -a intervals1.bed -b intervals2.bed -o nearest.txt --max-distance 1000`
**Explanation:** Filter by maximum distance.

### Output statistics
**Args:** `sorted_nearest -a intervals1.bed -b intervals2.bed -o nearest.txt --stats`
**Explanation:** Output search statistics.

### Generate report
**Args:** `sorted_nearest -a intervals1.bed -b intervals2.bed -o nearest.txt --report`
**Explanation:** Generate nearest search report.