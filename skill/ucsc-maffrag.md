---
name: ucsc-maffrag
category: utility
description: UCSC mafFrag - Tool for fragmenting MAF alignments.
tags: [ucsc-maffrag, ucsc, maf, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafFrag - A tool for fragmenting MAF alignments.
- **Core Function**: Breaks MAF alignments into smaller fragments.
- **Input**: MAF file.
- **Output**: Fragmented MAF file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment processing, fragment analysis, comparative genomics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper MAF format.

## Examples

### Fragment MAF alignments
**Args:** `mafFrag input.maf > fragmented.maf`
**Explanation:** Fragment MAF alignments.

### With options
**Args:** `mafFrag -maxSize=1000 input.maf > fragmented.maf`
**Explanation:** Maximum fragment size.
