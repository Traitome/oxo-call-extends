---
name: ucsc-gaptolift
category: utility
description: UCSC gapToLift - Tool for converting gaps to lift format.
tags: [ucsc-gaptolift, ucsc, lift-format, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC gapToLift - A tool for converting gap information to lift format.
- **Core Function**: Converts gap annotations to liftOver format.
- **Input**: Gap file.
- **Output**: Lift format file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Liftover preparation, genome alignment, coordinate conversion.

## Pitfalls

- **Gap Format**: Requires proper gap format.
- **Memory**: May require significant memory for large files.

## Examples

### Convert gaps
**Args:** `gapToLift gaps.bed > gaps.lift`
**Explanation:** Convert gaps to lift format.

### With options
**Args:** `gapToLift -minSize=1000 gaps.bed > gaps.lift`
**Explanation:** Minimum gap size threshold.
