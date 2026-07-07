---
name: ucsc-headrest
category: utility
description: UCSC headRest - Tool for header manipulation.
tags: [ucsc-headrest, ucsc, text-processing, bioinformatics, utilities]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC headRest - A tool for manipulating file headers.
- **Core Function**: Extracts or removes headers from files.
- **Input**: Text file.
- **Output**: Modified file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Text processing, data manipulation, file preparation.

## Pitfalls

- **Header Detection**: Requires proper header format.
- **Encoding**: May require proper character encoding.

## Examples

### Remove header
**Args:** `headRest -remove input.txt > output.txt`
**Explanation:** Remove header from file.

### Extract header
**Args:** `headRest -extract input.txt > header.txt`
**Explanation:** Extract header lines.
