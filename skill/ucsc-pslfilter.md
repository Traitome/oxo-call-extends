---
name: ucsc-pslfilter
category: utility
description: UCSC pslFilter - Tool for filtering PSL alignments.
tags: [ucsc-pslfilter, ucsc, psl, filtering, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslFilter - A tool for filtering PSL alignments.
- **Core Function**: Filters PSL alignments based on criteria.
- **Input**: PSL file.
- **Output**: Filtered PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment filtering, quality control, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Filter Criteria**: Requires proper filter specification.

## Examples

### Filter PSL alignments
**Args:** `pslFilter input.psl > filtered.psl`
**Explanation:** Filter PSL alignments.

### With options
**Args:** `pslFilter -minScore=100 input.psl > filtered.psl`
**Explanation:** Minimum alignment score filter.
