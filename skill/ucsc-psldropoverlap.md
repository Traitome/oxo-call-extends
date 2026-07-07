---
name: ucsc-psldropoverlap
category: utility
description: UCSC pslDropOverlap - Tool for removing overlapping alignments.
tags: [ucsc-psldropoverlap, ucsc, psl, overlap, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslDropOverlap - A tool for removing overlapping alignments.
- **Core Function**: Removes overlapping regions from PSL alignments.
- **Input**: PSL file.
- **Output**: Filtered PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment processing, deduplication, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Drop overlapping alignments
**Args:** `pslDropOverlap input.psl > output.psl`
**Explanation:** Remove overlapping alignments.

### With options
**Args:** `pslDropOverlap -minCover=80 input.psl > output.psl`
**Explanation:** Minimum coverage threshold.
