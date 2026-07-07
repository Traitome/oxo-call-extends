---
name: ucsc-genepredtobed
category: utility
description: UCSC genePredToBed - Tool for converting gene predictions to BED format.
tags: [ucsc-genepredtobed, ucsc, gene-prediction, bed, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC genePredToBed - A tool for converting gene predictions to BED format.
- **Core Function**: Converts genePred format to BED format.
- **Input**: Gene prediction file.
- **Output**: BED format file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, genome browser tracks, visualization.

## Pitfalls

- **Format Requirements**: Requires proper genePred format.
- **Memory**: May require significant memory for large files.

## Examples

### Convert to BED
**Args:** `genePredToBed genes.txt > genes.bed`
**Explanation:** Convert gene predictions to BED.

### With options
**Args:** `genePredToBed -type=bed12 genes.txt > genes.bed`
**Explanation:** Output BED12 format.
