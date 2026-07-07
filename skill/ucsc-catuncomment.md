---
name: ucsc-catuncomment
category: utility
description: UCSC catUncomment - Tool for removing comments from files.
tags: [ucsc-catuncomment, ucsc, file-manipulation, bioinformatics, utilities]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC catUncomment - A tool for removing comments from text files.
- **Core Function**: Strips comment lines from input files.
- **Input**: Text file with comments.
- **Output**: Text file without comments.
- **Installation**: Part of UCSC utilities
- **Use Case**: File cleaning, configuration parsing, data processing.

## Pitfalls

- **Comment Syntax**: Requires correct comment character specification.
- **Embedded Comments**: May not handle embedded comments properly.

## Examples

### Remove comments
**Args:** `catUncomment input.txt > output.txt`
**Explanation:** Remove comments from file.

### With custom comment character
**Args:** `catUncomment -commentChar="#" input.txt > output.txt`
**Explanation:** Remove lines starting with custom comment character.
