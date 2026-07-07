---
name: ucsc-chainsort
category: utility
description: UCSC chainSort - Tool for sorting chain alignments.
tags: [ucsc-chainsort, ucsc, chain-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chainSort - A tool for sorting chain alignments by target coordinates.
- **Core Function**: Sorts chain alignments by chromosome and position.
- **Input**: Unsorted chain alignment file.
- **Output**: Sorted chain file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment sorting, data organization, genome comparison.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Sort Order**: Requires correct sort order specification.

## Examples

### Sort chains
**Args:** `chainSort input.chain > sorted.chain`
**Explanation:** Sort chain alignments by target coordinates.

### By query
**Args:** `chainSort -query input.chain > sorted.chain`
**Explanation:** Sort chains by query coordinates.
