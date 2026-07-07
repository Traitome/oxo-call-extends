---
name: ucsc-bigwiginfo
category: utility
description: UCSC bigWigInfo - Tool for inspecting BigWig files.
tags: [ucsc-bigwiginfo, ucsc, bigwig, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bigWigInfo - A tool for inspecting BigWig file metadata.
- **Core Function**: Retrieves information about BigWig file structure and statistics.
- **Input**: BigWig file.
- **Output**: File metadata and statistics.
- **Installation**: Part of UCSC utilities
- **Use Case**: File inspection, quality control, data management.

## Pitfalls

- **File Integrity**: Requires valid BigWig format.
- **Index Check**: May fail if file is not properly indexed.

## Examples

### Get info
**Args:** `bigWigInfo input.bw`
**Explanation:** Display BigWig file information.

### Detailed info
**Args:** `bigWigInfo -detailed input.bw`
**Explanation:** Display detailed BigWig file information.
