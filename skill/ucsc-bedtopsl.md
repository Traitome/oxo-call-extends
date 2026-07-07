---
name: ucsc-bedtopsl
category: utility
description: UCSC bedToPsl - Tool for converting BED to PSL format.
tags: [ucsc-bedtopsl, ucsc, format-conversion, bed, psl]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedToPsl - A tool for converting BED format alignments to PSL format.
- **Core Function**: Converts BED alignments to PSL format for visualization.
- **Input**: BED format alignment file.
- **Output**: PSL format alignment file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, genome browser visualization.

## Pitfalls

- **Format Requirements**: Requires proper BED format with alignment info.
- **Strand Handling**: Requires correct strand information.

## Examples

### Convert BED to PSL
**Args:** `bedToPsl input.bed output.psl`
**Explanation:** Convert BED alignment to PSL format.

### With quality
**Args:** `bedToPsl -q input.bed output.psl`
**Explanation:** Convert with quality scores.
