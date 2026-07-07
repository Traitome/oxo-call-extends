---
name: ucsc-qacagplift
category: utility
description: UCSC qaCagpLift - Tool for lifting QAC to AGP.
tags: [ucsc-qacagplift, ucsc, qac, agp, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC qaCagpLift - A tool for lifting QAC to AGP format.
- **Core Function**: Converts QAC format to AGP format.
- **Input**: QAC file, chain file.
- **Output**: AGP file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, genome assembly, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper QAC/chain format.

## Examples

### Lift QAC to AGP
**Args:** `qaCagpLift input.qac chain.txt > output.agp`
**Explanation:** Convert QAC to AGP format.

### With options
**Args:** `qaCagpLift -verbose input.qac chain.txt > output.agp`
**Explanation:** Convert with verbose output.
