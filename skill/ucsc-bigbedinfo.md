---
name: ucsc-bigbedinfo
category: utility
description: UCSC bigBedInfo - Tool for inspecting BigBed files.
tags: [ucsc-bigbedinfo, ucsc, bigbed, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bigBedInfo - A tool for inspecting BigBed file metadata.
- **Core Function**: Retrieves information about BigBed file structure.
- **Input**: BigBed file.
- **Output**: File metadata and statistics.
- **Installation**: Part of UCSC utilities
- **Use Case**: File inspection, quality control, data management.

## Pitfalls

- **File Integrity**: Requires valid BigBed format.
- **Index Check**: May fail if file is not properly indexed.

## Examples

### Get info
**Args:** `bigBedInfo input.bb`
**Explanation:** Display BigBed file information.

### Detailed info
**Args:** `bigBedInfo -detailed input.bb`
**Explanation:** Display detailed BigBed file information.
