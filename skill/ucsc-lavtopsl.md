---
name: ucsc-lavtopsl
category: utility
description: UCSC lavToPsl - Tool for converting LAV to PSL format.
tags: [ucsc-lavtopsl, ucsc, lav, psl, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC lavToPsl - A tool for converting LAV to PSL format.
- **Core Function**: Converts LAV alignment format to PSL format.
- **Input**: LAV file.
- **Output**: PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, alignment visualization, genome browser.

## Pitfalls

- **Format Requirements**: Requires proper LAV format.
- **Memory**: May require significant memory for large files.

## Examples

### Convert LAV to PSL
**Args:** `lavToPsl input.lav > output.psl`
**Explanation:** Convert LAV to PSL format.

### With options
**Args:** `lavToPsl -score input.lav > output.psl`
**Explanation:** Include score in output.
