---
name: ucsc-twobitinfo
category: utility
description: UCSC twoBitInfo - Tool for getting twoBit file information.
tags: [ucsc-twobitinfo, ucsc, twobit, info, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC twoBitInfo - A tool for getting information about twoBit files.
- **Core Function**: Retrieves metadata from twoBit files.
- **Input**: TwoBit file.
- **Output**: File information.
- **Installation**: Part of UCSC utilities
- **Use Case**: File inspection, metadata retrieval, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper twoBit format.

## Examples

### Get twoBit information
**Args:** `twoBitInfo input.2bit stdout`
**Explanation:** Get twoBit file info.

### With options
**Args:** `twoBitInfo -nBed=100 input.2bit stdout`
**Explanation:** Get first 100 sequences.
