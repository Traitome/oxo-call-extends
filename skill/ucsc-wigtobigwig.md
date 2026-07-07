---
name: ucsc-wigtobigwig
category: utility
description: UCSC wigToBigWig - Tool for converting WIG to BigWig.
tags: [ucsc-wigtobigwig, ucsc, wig, bigwig, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC wigToBigWig - A tool for converting WIG to BigWig format.
- **Core Function**: Converts WIG format to compressed binary BigWig format.
- **Input**: WIG file, chrom.sizes file.
- **Output**: BigWig file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, genome browser tracks, bioinformatics.

## Pitfalls

- **Chromosome Sizes**: Requires chrom.sizes file.
- **Memory**: May require significant memory for large files.

## Examples

### Convert WIG to BigWig
**Args:** `wigToBigWig input.wig chrom.sizes output.bw`
**Explanation:** Convert WIG to BigWig format.

### With options
**Args:** `wigToBigWig -verbose input.wig chrom.sizes output.bw`
**Explanation:** Convert with verbose output.
