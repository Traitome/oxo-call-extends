---
name: ucsc-axtsort
category: utility
description: UCSC axtSort - Tool for sorting axt format alignments.
tags: [ucsc-axtsort, ucsc, alignment-sorting, axt-format, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC axtSort - A tool for sorting axt format alignment files.
- **Core Function**: Sorts axt format alignments by position.
- **Input**: Unsorted axt format alignment file.
- **Output**: Sorted axt format alignment file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment processing, data organization, genome analysis.

## Pitfalls

- **Format Requirements**: Requires proper axt format.
- **Memory**: Large files may require significant memory.

## Examples

### Sort axt file
**Args:** `axtSort unsorted.axt sorted.axt`
**Explanation:** Sort axt format alignment file.

### With multiple files
**Args:** `axtSort -inputDir alignments/ -output sorted.axt`
**Explanation:** Sort multiple axt files.
