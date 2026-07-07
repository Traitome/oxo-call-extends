---
name: ucsc-pslmap
category: utility
description: UCSC pslMap - Tool for mapping PSL alignments.
tags: [ucsc-pslmap, ucsc, psl, mapping, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslMap - A tool for mapping PSL alignments.
- **Core Function**: Maps alignments to reference coordinates.
- **Input**: PSL file, reference sequence.
- **Output**: Mapped alignments.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment mapping, genome analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Map PSL alignments
**Args:** `pslMap input.psl ref.fa > mapped.psl`
**Explanation:** Map PSL alignments.

### With options
**Args:** `pslMap -verbose input.psl ref.fa > mapped.psl`
**Explanation:** Map with verbose output.
