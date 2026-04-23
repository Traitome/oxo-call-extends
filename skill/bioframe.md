---
name: bioframe
category: annotation
description: Pandas utilities for tab-delimited and other genomic files
tags: [pandas, genomic-data, intervals, data-structures]
author: oxo-call-community
source_url: "https://github.com/mirnylab/bioframe"
---

## Concepts
- **Tool Overview**: bioframe provides Pandas-based utilities for working with tab-delimited and genomic interval files. It extends Pandas DataFrames for genomic operations.
- **Interval Operations**: Overlap, complement, coverage, closest, and other genomic interval operations using DataFrames.
- **File Support**: Reads BED, GFF, and other genomic formats directly into DataFrames.
- **Integration**: Works seamlessly with Pandas ecosystem for genomic data analysis.

## Pitfalls
- **Memory Usage**: Large genomic files loaded into DataFrames can consume significant memory.
- **Coordinate System**: Uses 0-based half-open coordinates (BED convention).

## Examples
### Load BED file
**Args:** `import bioframe as bf; df = bf.read_table('peaks.bed')`
**Explanation:** Loads BED file into a Pandas DataFrame.

### Find overlaps
**Args:** `overlaps = bioframe.overlap(df1, df2)`
**Explanation:** Finds overlapping intervals between two DataFrames.

### Compute complement
**Args:** `complement = bioframe.complement(df, 'hg38')`
**Explanation:** Computes genomic regions not covered by intervals.
