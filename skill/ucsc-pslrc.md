---
name: ucsc-pslrc
category: utility
description: UCSC pslRc - Tool for reverse complementing PSL alignments.
tags: [ucsc-pslrc, ucsc, psl, reverse-complement, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslRc - A tool for reverse complementing PSL alignments.
- **Core Function**: Reverse complements PSL alignment coordinates.
- **Input**: PSL file.
- **Output**: Reverse complemented PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Strand conversion, alignment processing, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Reverse complement PSL
**Args:** `pslRc input.psl > rc.psl`
**Explanation:** Reverse complement PSL alignments.

### With options
**Args:** `pslRc -verbose input.psl > rc.psl`
**Explanation:** Reverse complement with verbose output.
