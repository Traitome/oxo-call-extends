---
name: ucsc-bedweedoverlapping
category: utility
description: UCSC bedWeedOverlapping - Tool for removing overlapping regions from BED files.
tags: [ucsc-bedweedoverlapping, ucsc, bed-manipulation, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedWeedOverlapping - A tool for removing or merging overlapping regions in BED files.
- **Core Function**: Identifies and removes redundant overlapping regions.
- **Input**: BED file with overlapping regions.
- **Output**: BED file with non-overlapping regions.
- **Installation**: Part of UCSC utilities
- **Use Case**: Peak calling, region simplification, data cleaning.

## Pitfalls

- **Strand Awareness**: May not consider strand by default.
- **Weed Strategy**: Requires appropriate strategy selection.

## Examples

### Remove overlapping
**Args:** `bedWeedOverlapping -i input.bed > output.bed`
**Explanation:** Remove overlapping regions from BED file.

### With minimum score
**Args:** `bedWeedOverlapping -minScore 100 -i input.bed > output.bed`
**Explanation:** Remove overlaps keeping highest scoring regions.
