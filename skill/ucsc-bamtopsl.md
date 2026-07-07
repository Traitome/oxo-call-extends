---
name: ucsc-bamtopsl
category: utility
description: UCSC bamToPsl - Tool for converting BAM alignments to PSL format.
tags: [ucsc-bamtopsl, ucsc, format-conversion, bam, psl, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bamToPsl - A tool for converting BAM format alignments to PSL format.
- **Core Function**: Converts BAM alignments to PSL format for visualization.
- **Input**: BAM format alignment file.
- **Output**: PSL format alignment file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, genome browser visualization, alignment analysis.

## Pitfalls

- **BAM Index**: Requires indexed BAM file.
- **Memory**: Large BAM files may require significant memory.

## Examples

### Convert BAM to PSL
**Args:** `bamToPsl input.bam output.psl`
**Explanation:** Convert BAM alignment to PSL format.

### With filter
**Args:** `bamToPsl -minMapQ 30 input.bam output.psl`
**Explanation:** Convert with minimum mapping quality filter.
