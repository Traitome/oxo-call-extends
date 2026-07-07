---
name: ucsc-bedgraphtobigwig
category: utility
description: UCSC bedGraphToBigWig - Tool for converting bedGraph to BigWig format.
tags: [ucsc-bedgraphtobigwig, ucsc, format-conversion, bedgraph, bigwig]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedGraphToBigWig - A tool for converting bedGraph format to BigWig format.
- **Core Function**: Converts bedGraph files to indexed BigWig format.
- **Input**: bedGraph file, chromosome sizes file.
- **Output**: BigWig format file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Genome browser visualization, data sharing, efficient access.

## Pitfalls

- **Sorted Input**: Requires sorted bedGraph input.
- **Chromosome Names**: Requires matching chromosome names in sizes file.

## Examples

### Convert to BigWig
**Args:** `bedGraphToBigWig input.bedgraph chrom.sizes output.bw`
**Explanation:** Convert bedGraph to BigWig format.

### With compression
**Args:** `bedGraphToBigWig -compress input.bedgraph chrom.sizes output.bw`
**Explanation:** Convert with compression.
