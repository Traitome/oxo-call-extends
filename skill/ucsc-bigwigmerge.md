---
name: ucsc-bigwigmerge
category: utility
description: UCSC bigWigMerge - Tool for merging BigWig files.
tags: [ucsc-bigwigmerge, ucsc, bigwig, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bigWigMerge - A tool for merging multiple BigWig files.
- **Core Function**: Combines multiple BigWig signals into a single track.
- **Input**: Multiple BigWig files.
- **Output**: Merged BigWig or bedGraph file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data merging, track visualization, multi-sample analysis.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Signal Overlap**: Requires handling for overlapping signals.

## Examples

### Merge BigWig files
**Args:** `bigWigMerge file1.bw file2.bw file3.bw output.bw`
**Explanation:** Merge multiple BigWig files.

### Output bedGraph
**Args:** `bigWigMerge -bedGraph file*.bw output.bedgraph`
**Explanation:** Merge and output as bedGraph.
