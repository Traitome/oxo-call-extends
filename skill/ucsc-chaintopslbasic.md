---
name: ucsc-chaintopslbasic
category: utility
description: UCSC chainToPslBasic - Tool for converting chains to basic PSL format.
tags: [ucsc-chaintopslbasic, ucsc, format-conversion, chain, psl]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chainToPslBasic - A tool for converting chain alignments to basic PSL format.
- **Core Function**: Converts chain format to simplified PSL format.
- **Input**: Chain alignment file.
- **Output**: Basic PSL format alignment file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, simplified alignment output.

## Pitfalls

- **Format Limitation**: Produces basic PSL without full features.
- **Memory**: May require significant memory for large files.

## Examples

### Convert to basic PSL
**Args:** `chainToPslBasic input.chain > output.psl`
**Explanation:** Convert chain to basic PSL format.

### With FASTA
**Args:** `chainToPslBasic -fasta target.fa input.chain > output.psl`
**Explanation:** Convert with FASTA sequence information.
