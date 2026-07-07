---
name: ucsc-maskoutfa
category: utility
description: UCSC maskOutFa - Tool for masking FASTA sequences.
tags: [ucsc-maskoutfa, ucsc, fasta, masking, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC maskOutFa - A tool for masking regions in FASTA sequences.
- **Core Function**: Masks specified regions in FASTA sequences.
- **Input**: FASTA file, mask regions file.
- **Output**: Masked FASTA file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Sequence masking, repeat masking, genome analysis.

## Pitfalls

- **Memory**: May require significant memory for large sequences.
- **Format Requirements**: Requires proper coordinate format.

## Examples

### Mask FASTA regions
**Args:** `maskOutFa input.fa mask.bed > masked.fa`
**Explanation:** Mask specified regions in FASTA.

### With options
**Args:** `maskOutFa -hard input.fa mask.bed > masked.fa`
**Explanation:** Use hard masking (N's).
