---
name: ucsc-psltobed
category: utility
description: UCSC pslToBed - Tool for converting PSL to BED.
tags: [ucsc-psltobed, ucsc, psl, bed, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslToBed - A tool for converting PSL to BED format.
- **Core Function**: Converts PSL alignments to BED format.
- **Input**: PSL file.
- **Output**: BED file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, genome browser tracks, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Convert PSL to BED
**Args:** `pslToBed input.psl > output.bed`
**Explanation:** Convert PSL to BED format.

### With options
**Args:** `pslToBed -verbose input.psl > output.bed`
**Explanation:** Convert with verbose output.
