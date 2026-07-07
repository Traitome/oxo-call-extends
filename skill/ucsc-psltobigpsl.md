---
name: ucsc-psltobigpsl
category: utility
description: UCSC pslToBigPsl - Tool for converting PSL to bigPsl.
tags: [ucsc-psltobigpsl, ucsc, psl, bigpsl, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslToBigPsl - A tool for converting PSL to bigPsl format.
- **Core Function**: Converts PSL alignments to binary bigPsl format.
- **Input**: PSL file, chrom.sizes file.
- **Output**: bigPsl binary file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, genome browser tracks, data compression.

## Pitfalls

- **Chromosome Sizes**: Requires chrom.sizes file.
- **Memory**: May require significant memory for large files.

## Examples

### Convert PSL to bigPsl
**Args:** `pslToBigPsl input.psl chrom.sizes > output.bb`
**Explanation:** Convert PSL to bigPsl format.

### With options
**Args:** `pslToBigPsl -name=alignments input.psl chrom.sizes > output.bb`
**Explanation:** Add track name.
