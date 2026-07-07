---
name: ucsc-bedclip
category: utility
description: UCSC bedClip - Tool for clipping BED file coordinates.
tags: [ucsc-bedclip, ucsc, bed-manipulation, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedClip - A tool for clipping BED file coordinates to chromosome boundaries.
- **Core Function**: Ensures BED coordinates are within valid chromosome ranges.
- **Input**: BED file, chromosome sizes file.
- **Output**: Clipped BED file.
- **Installation**: Part of UCSC utilities
- **Use Case**: BED file validation, coordinate normalization, data cleaning.

## Pitfalls

- **Chromosome Names**: Requires matching chromosome names.
- **Coordinate System**: Requires 0-based or 1-based consistency.

## Examples

### Clip BED file
**Args:** `bedClip input.bed chrom.sizes output.bed`
**Explanation:** Clip BED coordinates to chromosome boundaries.

### With padding
**Args:** `bedClip -padding 100 input.bed chrom.sizes output.bed`
**Explanation:** Clip with padding around boundaries.
