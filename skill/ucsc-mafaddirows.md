---
name: ucsc-mafaddirows
category: utility
description: UCSC mafAddIRows - Tool for adding I rows to MAF.
tags: [ucsc-mafaddirows, ucsc, maf, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafAddIRows - A tool for adding I (insertion) rows to MAF alignments.
- **Core Function**: Adds insertion rows to MAF alignment files.
- **Input**: MAF file.
- **Output**: Modified MAF file with I rows.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment processing, gap handling, comparative genomics.

## Pitfalls

- **Format Requirements**: Requires proper MAF format.
- **Memory**: May require significant memory for large files.

## Examples

### Add I rows to MAF
**Args:** `mafAddIRows input.maf > output.maf`
**Explanation:** Add insertion rows to MAF alignment.

### With options
**Args:** `mafAddIRows -verbose input.maf > output.maf`
**Explanation:** Add with verbose output.
