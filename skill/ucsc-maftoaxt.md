---
name: ucsc-maftoaxt
category: utility
description: UCSC mafToAxt - Tool for converting MAF to AXT format.
tags: [ucsc-maftoaxt, ucsc, maf, axt, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafToAxt - A tool for converting MAF to AXT format.
- **Core Function**: Converts MAF alignments to AXT format.
- **Input**: MAF file.
- **Output**: AXT file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, alignment analysis, comparative genomics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper MAF format.

## Examples

### Convert MAF to AXT
**Args:** `mafToAxt input.maf > output.axt`
**Explanation:** Convert MAF to AXT format.

### With options
**Args:** `mafToAxt -verbose input.maf > output.axt`
**Explanation:** Convert with verbose output.
