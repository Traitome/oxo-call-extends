---
name: ucsc-chainswap
category: utility
description: UCSC chainSwap - Tool for swapping target and query in chain alignments.
tags: [ucsc-chainswap, ucsc, chain-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chainSwap - A tool for swapping target and query sequences in chain alignments.
- **Core Function**: Transposes the alignment, making query the target and vice versa.
- **Input**: Chain alignment file.
- **Output**: Swapped chain file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment manipulation, comparative genomics, data analysis.

## Pitfalls

- **Strand Handling**: May require strand adjustment.
- **Coordinate Conversion**: Requires proper coordinate conversion.

## Examples

### Swap chains
**Args:** `chainSwap input.chain > swapped.chain`
**Explanation:** Swap target and query in chain alignments.

### With reverse complement
**Args:** `chainSwap -rc input.chain > swapped.chain`
**Explanation:** Swap with reverse complement.
