---
name: ucsc-axttomaf
category: utility
description: UCSC axtToMaf - Tool for converting axt alignments to MAF format.
tags: [ucsc-axttomaf, ucsc, format-conversion, axt, maf, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC axtToMaf - A tool for converting axt format alignments to MAF (Multiple Alignment Format).
- **Core Function**: Converts pairwise axt alignments to multiple alignment format.
- **Input**: Axt format alignment file.
- **Output**: MAF format alignment file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, multiple sequence alignment, comparative genomics.

## Pitfalls

- **Format Requirements**: Requires proper axt format.
- **Coordinate Handling**: Requires correct coordinate systems.

## Examples

### Convert to MAF
**Args:** `axtToMaf input.axt output.maf`
**Explanation:** Convert axt alignment to MAF format.

### With chain file
**Args:** `axtToMaf -chain chain.txt input.axt output.maf`
**Explanation:** Convert with chain file for coordinate mapping.
