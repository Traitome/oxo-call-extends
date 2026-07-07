---
name: ucsc-maffetch
category: utility
description: UCSC mafFetch - Tool for fetching MAF alignments.
tags: [ucsc-maffetch, ucsc, maf, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafFetch - A tool for fetching MAF alignments.
- **Core Function**: Extracts alignments from MAF files.
- **Input**: MAF file, region coordinates.
- **Output**: MAF alignments for specified region.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment retrieval, region analysis, comparative genomics.

## Pitfalls

- **Coordinate Format**: Requires proper coordinate specification.
- **Memory**: May require significant memory for large files.

## Examples

### Fetch MAF alignments
**Args:** `mafFetch input.maf chr1:1000-2000 > region.maf`
**Explanation:** Fetch alignments for specified region.

### With options
**Args:** `mafFetch -species=hg38,panTro4 input.maf chr1:1000-2000 > region.maf`
**Explanation:** Fetch specific species only.
