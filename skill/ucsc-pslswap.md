---
name: ucsc-pslswap
category: utility
description: UCSC pslSwap - Tool for swapping query and target.
tags: [ucsc-pslswap, ucsc, psl, swap, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslSwap - A tool for swapping query and target in PSL alignments.
- **Core Function**: Swaps query and target coordinates.
- **Input**: PSL file.
- **Output**: Swapped PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Coordinate transformation, alignment processing, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Swap query and target
**Args:** `pslSwap input.psl > swapped.psl`
**Explanation:** Swap query and target.

### With options
**Args:** `pslSwap -verbose input.psl > swapped.psl`
**Explanation:** Swap with verbose output.
