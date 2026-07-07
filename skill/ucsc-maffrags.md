---
name: ucsc-maffrags
category: utility
description: UCSC mafFrags - Tool for extracting fragments from MAF.
tags: [ucsc-maffrags, ucsc, maf, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafFrags - A tool for extracting fragments from MAF alignments.
- **Core Function**: Extracts sequence fragments from MAF alignments.
- **Input**: MAF file.
- **Output**: Sequence fragments.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence extraction, fragment analysis, comparative genomics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper MAF format.

## Examples

### Extract fragments
**Args:** `mafFrags input.maf > fragments.txt`
**Explanation:** Extract fragments from MAF alignment.

### With options
**Args:** `mafFrags -species=hg38 input.maf > fragments.txt`
**Explanation:** Extract fragments for specific species.
