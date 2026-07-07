---
name: ucsc-toupper
category: utility
description: UCSC toUpper - Tool for converting to uppercase.
tags: [ucsc-toupper, ucsc, uppercase, text-processing, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC toUpper - A tool for converting text to uppercase.
- **Core Function**: Converts lowercase letters to uppercase.
- **Input**: Text file.
- **Output**: Uppercase text.
- **Installation**: Part of UCSC utilities
- **Use Case**: Text processing, data normalization, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Encoding**: Requires proper encoding handling.

## Examples

### Convert to uppercase
**Args:** `toUpper input.txt > output.txt`
**Explanation:** Convert text to uppercase.

### With options
**Args:** `toUpper -verbose input.txt > output.txt`
**Explanation:** Convert with verbose output.
