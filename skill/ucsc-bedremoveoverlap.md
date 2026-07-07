---
name: ucsc-bedremoveoverlap
category: utility
description: UCSC bedRemoveOverlap - Tool for removing overlapping regions from BED files.
tags: [ucsc-bedremoveoverlap, ucsc, bed-manipulation, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedRemoveOverlap - A tool for removing overlapping regions within a BED file.
- **Core Function**: Merges or removes overlapping regions to create non-overlapping sets.
- **Input**: BED file with potentially overlapping regions.
- **Output**: BED file with non-overlapping regions.
- **Installation**: Part of UCSC utilities
- **Use Case**: Peak merging, region simplification, data cleaning.

## Pitfalls

- **Strand Awareness**: May not consider strand by default.
- **Merge Strategy**: Requires appropriate merge strategy selection.

## Examples

### Remove overlaps
**Args:** `bedRemoveOverlap -i input.bed > output.bed`
**Explanation:** Remove overlapping regions from BED file.

### Merge overlapping
**Args:** `bedRemoveOverlap -merge -i input.bed > merged.bed`
**Explanation:** Merge overlapping regions.
