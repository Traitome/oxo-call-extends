---
name: ucsc-catdir
category: utility
description: UCSC catDir - Tool for concatenating files in a directory.
tags: [ucsc-catdir, ucsc, file-manipulation, bioinformatics, utilities]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC catDir - A tool for concatenating files in a directory.
- **Core Function**: Concatenates multiple files in a directory.
- **Input**: Directory path, optional file pattern.
- **Output**: Concatenated content.
- **Installation**: Part of UCSC utilities
- **Use Case**: File merging, data aggregation, batch processing.

## Pitfalls

- **File Order**: May concatenate in non-deterministic order.
- **Memory**: May require significant memory for large files.

## Examples

### Concatenate files
**Args:** `catDir /path/to/directory > output.txt`
**Explanation:** Concatenate all files in directory.

### With pattern
**Args:** `catDir -pattern="*.txt" /path/to/directory > output.txt`
**Explanation:** Concatenate files matching pattern.
