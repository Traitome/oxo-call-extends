---
name: ucsc-pslsortacc
category: utility
description: UCSC pslSortAcc - Tool for sorting PSL by accession.
tags: [ucsc-pslsortacc, ucsc, psl, sorting, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslSortAcc - A tool for sorting PSL by accession.
- **Core Function**: Sorts PSL alignments by accession number.
- **Input**: PSL file.
- **Output**: Sorted PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data organization, accession-based sorting, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Sort PSL by accession
**Args:** `pslSortAcc input.psl > sorted.psl`
**Explanation:** Sort by accession number.

### With options
**Args:** `pslSortAcc -verbose input.psl > sorted.psl`
**Explanation:** Sort with verbose output.
