---
name: ucsc-fatotwobit
category: utility
description: UCSC faToTwoBit - Tool for converting FASTA to 2bit format.
tags: [ucsc-fatotwobit, ucsc, fasta, format-conversion, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC faToTwoBit - A tool for converting FASTA to 2bit format.
- **Core Function**: Compresses FASTA sequences into binary 2bit format.
- **Input**: FASTA file.
- **Output**: 2bit binary file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, data compression, genome browser.

## Pitfalls

- **Memory**: May require significant memory for large sequences.
- **Output Size**: Compressed format may not be suitable for all purposes.

## Examples

### Convert to 2bit
**Args:** `faToTwoBit input.fa output.2bit`
**Explanation:** Convert FASTA to 2bit format.

### With options
**Args:** `faToTwoBit -noMask input.fa output.2bit`
**Explanation:** Convert without masking.
