---
name: ucsc-chainmergesort
category: utility
description: UCSC chainMergeSort - Tool for merging and sorting chain alignments.
tags: [ucsc-chainmergesort, ucsc, chain-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chainMergeSort - A tool for merging and sorting chain alignments.
- **Core Function**: Merges multiple chain files and sorts by target coordinates.
- **Input**: Multiple chain alignment files.
- **Output**: Merged and sorted chain file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment merging, data organization, genome comparison.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Chromosome Consistency**: Requires matching chromosome names.

## Examples

### Merge and sort
**Args:** `chainMergeSort chain1.txt chain2.txt > merged.chain`
**Explanation:** Merge and sort chain alignments.

### With output file
**Args:** `chainMergeSort -output merged.chain chain*.txt`
**Explanation:** Merge multiple chain files.
