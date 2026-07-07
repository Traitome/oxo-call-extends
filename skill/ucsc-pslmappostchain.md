---
name: ucsc-pslmappostchain
category: utility
description: UCSC pslMapPostChain - Tool for mapping post-chain PSL alignments.
tags: [ucsc-pslmappostchain, ucsc, psl, mapping, chain, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslMapPostChain - A tool for mapping post-chain PSL alignments.
- **Core Function**: Maps PSL alignments after chain processing.
- **Input**: PSL file, chain file.
- **Output**: Mapped PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment mapping, liftover, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL/chain format.

## Examples

### Map post-chain PSL
**Args:** `pslMapPostChain input.psl chain.txt > mapped.psl`
**Explanation:** Map post-chain PSL alignments.

### With options
**Args:** `pslMapPostChain -verbose input.psl chain.txt > mapped.psl`
**Explanation:** Map with verbose output.
