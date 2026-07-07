---
name: ucsc-gff3topsl
category: utility
description: UCSC gff3ToPsl - Tool for converting GFF3 to PSL format.
tags: [ucsc-gff3topsl, ucsc, gff3, psl, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC gff3ToPsl - A tool for converting GFF3 to PSL format.
- **Core Function**: Converts GFF3 annotations to PSL format.
- **Input**: GFF3 file.
- **Output**: PSL format file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, alignment visualization, genome browser.

## Pitfalls

- **Format Requirements**: Requires proper GFF3 format.
- **Memory**: May require significant memory for large files.

## Examples

### Convert GFF3 to PSL
**Args:** `gff3ToPsl input.gff3 > output.psl`
**Explanation:** Convert GFF3 to PSL format.

### With options
**Args:** `gff3ToPsl -score input.gff3 > output.psl`
**Explanation:** Include score in output.
