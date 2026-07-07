---
name: ucsc-pslsort
category: utility
description: UCSC pslSort - Tool for sorting PSL alignments.
tags: [ucsc-pslsort, ucsc, psl, sorting, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslSort - A tool for sorting PSL alignments.
- **Core Function**: Sorts PSL alignments by various criteria.
- **Input**: PSL file.
- **Output**: Sorted PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data organization, sorting, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Sort PSL alignments
**Args:** `pslSort input.psl > sorted.psl`
**Explanation:** Sort PSL alignments.

### With options
**Args:** `pslSort -query input.psl > sorted.psl`
**Explanation:** Sort by query name.
