---
name: ucsc-bedrestricttopositions
category: utility
description: UCSC bedRestrictToPositions - Tool for restricting BED regions to specific positions.
tags: [ucsc-bedrestricttopositions, ucsc, bed-manipulation, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedRestrictToPositions - A tool for restricting BED regions to specific positions.
- **Core Function**: Filters or clips BED regions based on specified positions.
- **Input**: BED file, position constraints.
- **Output**: Restricted BED file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Region filtering, target enrichment, data subsetting.

## Pitfalls

- **Coordinate Matching**: Requires exact position matching.
- **File Format**: Requires proper BED format.

## Examples

### Restrict to positions
**Args:** `bedRestrictToPositions -i input.bed -positions targets.bed > output.bed`
**Explanation:** Restrict BED regions to target positions.

### With padding
**Args:** `bedRestrictToPositions -i input.bed -positions targets.bed -padding 100 > output.bed`
**Explanation:** Restrict with padding around target positions.
