---
name: ucsc-pslcdnafilter
category: utility
description: UCSC pslCdnaFilter - Tool for filtering cDNA PSL alignments.
tags: [ucsc-pslcdnafilter, ucsc, psl, cdna, filtering, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslCdnaFilter - A tool for filtering cDNA PSL alignments.
- **Core Function**: Filters and processes cDNA alignments.
- **Input**: PSL file.
- **Output**: Filtered PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment filtering, gene prediction, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Filter cDNA PSL
**Args:** `pslCdnaFilter input.psl > filtered.psl`
**Explanation:** Filter cDNA alignments.

### With options
**Args:** `pslCdnaFilter -minIdentity=95 input.psl > filtered.psl`
**Explanation:** Minimum identity filter.
