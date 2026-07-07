---
name: ucsc-bigwigtobedgraph
category: utility
description: UCSC bigWigToBedGraph - Tool for converting BigWig to bedGraph format.
tags: [ucsc-bigwigtobedgraph, ucsc, format-conversion, bigwig, bedgraph]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bigWigToBedGraph - A tool for converting BigWig format to bedGraph format.
- **Core Function**: Converts indexed BigWig files to plain bedGraph format.
- **Input**: BigWig file.
- **Output**: bedGraph format file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, data extraction, analysis.

## Pitfalls

- **File Size**: Output may be significantly larger than input.
- **Memory**: May require significant memory for large files.

## Examples

### Convert to bedGraph
**Args:** `bigWigToBedGraph input.bw output.bedgraph`
**Explanation:** Convert BigWig to bedGraph format.

### With region
**Args:** `bigWigToBedGraph -chrom=chr1 -start=1 -end=1000000 input.bw output.bedgraph`
**Explanation:** Extract specific region from BigWig.
