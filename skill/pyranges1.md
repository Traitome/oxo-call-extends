---
name: pyranges1
category: programming
description: PyRanges provides GenomicRanges-like functionality for Python for genomic interval operations.
tags: [pyranges1, programming, genomics, intervals]
author: oxo-call-community
source_url: "https://github.com/pyranges/pyranges_1.x"
---

## Concepts

- **Tool Overview**: pyranges1 manipulates genomic ranges.
- **Core Function**: Interval operations.
- **Algorithm**: Uses range trees.
- **Input Format**: Accepts BED/GFF files.
- **Output**: Produces range operations.
- **Use Case**: Genomics analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Coordinate System**: Must be correct.
- **Overlap Detection**: May have edge cases.
- **Runtime**: Operations may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyranges1 --help`
**Explanation:** Shows available options and usage instructions.

### Run operations
**Args:** `pyranges1 intersect -a ranges1.bed -b ranges2.bed -o result.bed`
**Explanation:** Finds overlapping ranges.

### With parameters
**Args:** `pyranges1 intersect -a ranges1.bed -p params.yaml -o result.bed`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyranges1 -v intersect -a ranges1.bed -b ranges2.bed -o result.bed`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyranges1 -t 4 intersect -a ranges1.bed -b ranges2.bed -o result.bed`
**Explanation:** Uses 4 threads for parallel processing.

### Merge ranges
**Args:** `pyranges1 merge -i ranges.bed -o merged.bed`
**Explanation:** Merges overlapping ranges.

### Generate report
**Args:** `pyranges1 intersect -a ranges1.bed -b ranges2.bed -o result.bed --report report.html`
**Explanation:** Generates HTML report.