---
name: ucsc-psltochain
category: utility
description: UCSC pslToChain - Tool for converting PSL to chain format.
tags: [ucsc-psltochain, ucsc, psl, chain, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslToChain - A tool for converting PSL to chain format.
- **Core Function**: Converts PSL alignments to chain format.
- **Input**: PSL file, target sequence, query sequence.
- **Output**: Chain file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, liftover, comparative genomics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Convert PSL to chain
**Args:** `pslToChain input.psl target.fa query.fa > output.chain`
**Explanation:** Convert PSL to chain format.

### With options
**Args:** `pslToChain -verbose input.psl target.fa query.fa > output.chain`
**Explanation:** Convert with verbose output.
