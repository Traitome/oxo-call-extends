---
name: ucsc-overlapselect
category: utility
description: UCSC overlapSelect - Tool for selecting overlapping regions.
tags: [ucsc-overlapselect, ucsc, overlap, selection, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC overlapSelect - A tool for selecting overlapping regions.
- **Core Function**: Selects regions that overlap with query regions.
- **Input**: Query regions, target regions.
- **Output**: Overlapping regions.
- **Installation**: Part of UCSC utilities
- **Use Case**: Region analysis, annotation, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper BED format.

## Examples

### Select overlapping regions
**Args:** `overlapSelect queries.bed targets.bed > overlaps.bed`
**Explanation:** Find overlapping regions.

### With options
**Args:** `overlapSelect -minOverlap=50 queries.bed targets.bed > overlaps.bed`
**Explanation:** Minimum overlap percentage.
