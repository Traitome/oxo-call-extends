---
name: ucsc-nettobed
category: utility
description: UCSC netToBed - Tool for converting net to BED format.
tags: [ucsc-nettobed, ucsc, net, bed, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC netToBed - A tool for converting net to BED format.
- **Core Function**: Converts net alignments to BED format.
- **Input**: Net file.
- **Output**: BED file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, genome browser tracks, visualization.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper net format.

## Examples

### Convert net to BED
**Args:** `netToBed input.net > output.bed`
**Explanation:** Convert net to BED format.

### With options
**Args:** `netToBed -verbose input.net > output.bed`
**Explanation:** Convert with verbose output.
