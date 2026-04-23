---
name: bigwig-nim
category: utility
description: Command-line querying and conversion of bigWig files
tags: [bigwig, query, conversion, genomics]
author: oxo-call-community
source_url: "https://github.com/brentp/bigwig-nim"
---

## Concepts
- **Tool Overview**: bigwig-nim is a fast command-line tool for querying and converting bigWig files, written in Nim for performance.
- **Query Operations**: Extract values at specific positions, regions, or across entire genome.
- **Conversion**: Convert bigWig to text format or other representations.
- **Performance**: Optimized for speed with minimal memory footprint.

## Pitfalls
- **Index Requirement**: Requires properly indexed bigWig files.
- **Output Format**: Output format may need post-processing for downstream tools.

## Examples
### Query value at position
**Args:** `bigwig-nim query input.bw chr1:1000000-1000100`
**Explanation:** Extracts signal values for a specific region.

### Convert to text
**Args:** `bigwig-nim to-wig input.bw > output.wig`
**Explanation:** Converts bigWig to wiggle text format.
