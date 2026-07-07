---
name: ucsc-mafaddqrows
category: utility
description: UCSC mafAddQRows - Tool for adding Q rows to MAF.
tags: [ucsc-mafaddqrows, ucsc, maf, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafAddQRows - A tool for adding Q rows to MAF alignments.
- **Core Function**: Adds quality score rows to MAF alignment files.
- **Input**: MAF file, quality file.
- **Output**: Modified MAF file with Q rows.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment processing, quality scores, comparative genomics.

## Pitfalls

- **Format Requirements**: Requires proper MAF format.
- **Memory**: May require significant memory for large files.

## Examples

### Add Q rows to MAF
**Args:** `mafAddQRows input.maf quality.txt > output.maf`
**Explanation:** Add quality rows to MAF alignment.

### With options
**Args:** `mafAddQRows -verbose input.maf quality.txt > output.maf`
**Explanation:** Add with verbose output.
