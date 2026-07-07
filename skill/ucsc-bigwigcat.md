---
name: ucsc-bigwigcat
category: utility
description: UCSC bigWigCat - Tool for concatenating BigWig files.
tags: [ucsc-bigwigcat, ucsc, bigwig, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bigWigCat - A tool for concatenating multiple BigWig files.
- **Core Function**: Merges multiple BigWig files into a single file.
- **Input**: Multiple BigWig files.
- **Output**: Combined BigWig file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data merging, track aggregation, multi-sample analysis.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Chromosome Consistency**: Requires matching chromosome names.

## Examples

### Concatenate BigWig files
**Args:** `bigWigCat -output combined.bw file1.bw file2.bw file3.bw`
**Explanation:** Merge multiple BigWig files.

### With override
**Args:** `bigWigCat -override -output combined.bw file*.bw`
**Explanation:** Concatenate with override for overlapping regions.
