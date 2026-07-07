---
name: ucsc-beditemoverlapcount
category: analysis
description: UCSC bedItemOverlapCount - Tool for counting overlaps in BED files.
tags: [ucsc-beditemoverlapcount, ucsc, overlap-analysis, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedItemOverlapCount - A tool for counting overlaps between BED items.
- **Core Function**: Counts how many items in one BED file overlap with items in another.
- **Input**: Two BED files.
- **Output**: Overlap counts.
- **Installation**: Part of UCSC utilities
- **Use Case**: Peak analysis, region annotation, overlap statistics.

## Pitfalls

- **Strand Consideration**: May not consider strand information by default.
- **Memory**: May require significant memory for large datasets.

## Examples

### Count overlaps
**Args:** `bedItemOverlapCount regions.bed annotations.bed > counts.txt`
**Explanation:** Count overlaps between regions and annotations.

### With strand
**Args:** `bedItemOverlapCount -strand + regions.bed annotations.bed > counts.txt`
**Explanation:** Count overlaps considering strand.
