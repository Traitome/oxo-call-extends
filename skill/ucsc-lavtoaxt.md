---
name: ucsc-lavtoaxt
category: utility
description: UCSC lavToAxt - Tool for converting LAV to AXT format.
tags: [ucsc-lavtoaxt, ucsc, lav, axt, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC lavToAxt - A tool for converting LAV to AXT format.
- **Core Function**: Converts LAV alignment format to AXT format.
- **Input**: LAV file.
- **Output**: AXT file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, alignment analysis, comparative genomics.

## Pitfalls

- **Format Requirements**: Requires proper LAV format.
- **Memory**: May require significant memory for large files.

## Examples

### Convert LAV to AXT
**Args:** `lavToAxt input.lav > output.axt`
**Explanation:** Convert LAV to AXT format.

### With options
**Args:** `lavToAxt -score input.lav > output.axt`
**Explanation:** Include score in output.
