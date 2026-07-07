---
name: ucsc-chopfalines
category: utility
description: UCSC chopFaLines - Tool for chopping FASTA lines.
tags: [ucsc-chopfalines, ucsc, fasta, sequence-manipulation, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chopFaLines - A tool for reformatting FASTA file line lengths.
- **Core Function**: Adjusts line lengths in FASTA sequences.
- **Input**: FASTA file.
- **Output**: Reformatted FASTA file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence formatting, file preparation, data standardization.

## Pitfalls

- **Line Length**: Requires appropriate line length specification.
- **Memory**: May require significant memory for large sequences.

## Examples

### Chop FASTA lines
**Args:** `chopFaLines -maxLineSize=60 input.fa > output.fa`
**Explanation:** Reformat FASTA lines to specified length.

### With padding
**Args:** `chopFaLines -maxLineSize=80 -pad input.fa > output.fa`
**Explanation:** Chop with padding.
