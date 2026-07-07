---
name: ucsc-maftopsl
category: utility
description: UCSC mafToPsl - Tool for converting MAF to PSL format.
tags: [ucsc-maftopsl, ucsc, maf, psl, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafToPsl - A tool for converting MAF to PSL format.
- **Core Function**: Converts MAF alignments to PSL format.
- **Input**: MAF file.
- **Output**: PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, alignment visualization, genome browser.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper MAF format.

## Examples

### Convert MAF to PSL
**Args:** `mafToPsl input.maf > output.psl`
**Explanation:** Convert MAF to PSL format.

### With options
**Args:** `mafToPsl -verbose input.maf > output.psl`
**Explanation:** Convert with verbose output.
