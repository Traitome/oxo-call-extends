---
name: ucsc-pslrecalcmatch
category: utility
description: UCSC pslRecalcMatch - Tool for recalculating match counts.
tags: [ucsc-pslrecalcmatch, ucsc, psl, recalculate, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslRecalcMatch - A tool for recalculating match counts.
- **Core Function**: Recalculates match statistics for PSL alignments.
- **Input**: PSL file, sequence file.
- **Output**: Recalculated PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment analysis, quality control, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Recalculate match counts
**Args:** `pslRecalcMatch input.psl ref.fa > recalc.psl`
**Explanation:** Recalculate match statistics.

### With options
**Args:** `pslRecalcMatch -verbose input.psl ref.fa > recalc.psl`
**Explanation:** Recalculate with verbose output.
