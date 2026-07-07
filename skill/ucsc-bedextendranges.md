---
name: ucsc-bedextendranges
category: utility
description: UCSC bedExtendRanges - Tool for extending BED region coordinates.
tags: [ucsc-bedextendranges, ucsc, bed-manipulation, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedExtendRanges - A tool for extending BED region coordinates upstream and downstream.
- **Core Function**: Extends genomic regions by specified amounts.
- **Input**: BED file, extension parameters.
- **Output**: Extended BED file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Region expansion, promoter analysis, flanking regions.

## Pitfalls

- **Chromosome Boundaries**: May extend beyond chromosome boundaries.
- **Strand Consideration**: Requires strand awareness for directional extension.

## Examples

### Extend regions
**Args:** `bedExtendRanges -up=1000 -down=500 input.bed > extended.bed`
**Explanation:** Extend regions by 1000bp upstream and 500bp downstream.

### Symmetric extension
**Args:** `bedExtendRanges -extend=2000 input.bed > extended.bed`
**Explanation:** Extend regions symmetrically by 2000bp on each side.
