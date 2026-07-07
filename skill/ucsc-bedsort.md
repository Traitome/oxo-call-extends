---
name: ucsc-bedsort
category: utility
description: UCSC bedSort - Tool for sorting BED files.
tags: [ucsc-bedsort, ucsc, bed-manipulation, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC bedSort - A tool for sorting BED files by chromosome and position.
- **Core Function**: Sorts BED file entries by genomic coordinates.
- **Input**: Unsorted BED file.
- **Output**: Sorted BED file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data organization, preparation for genome browser, file indexing.

## Pitfalls

- **Memory**: Large files may require significant memory.
- **Sort Order**: Requires correct sort order specification.

## Examples

### Sort BED file
**Args:** `bedSort input.bed output.bed`
**Explanation:** Sort BED file by chromosome and position.

### Sort by name
**Args:** `bedSort -name input.bed output.bed`
**Explanation:** Sort BED file by name field.
