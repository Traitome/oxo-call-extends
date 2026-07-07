---
name: ucsc-pslselect
category: utility
description: UCSC pslSelect - Tool for selecting PSL alignments.
tags: [ucsc-pslselect, ucsc, psl, selection, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslSelect - A tool for selecting PSL alignments.
- **Core Function**: Selects alignments based on criteria.
- **Input**: PSL file.
- **Output**: Selected PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment selection, filtering, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Filter Criteria**: Requires proper filter specification.

## Examples

### Select PSL alignments
**Args:** `pslSelect input.psl > selected.psl`
**Explanation:** Select alignments.

### With options
**Args:** `pslSelect -minScore=100 input.psl > selected.psl`
**Explanation:** Minimum score filter.
