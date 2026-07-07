---
name: ucsc-axtswap
category: utility
description: UCSC axtSwap - Tool for swapping target and query in axt alignments.
tags: [ucsc-axtswap, ucsc, alignment-processing, axt-format, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC axtSwap - A tool for swapping target and query sequences in axt alignments.
- **Core Function**: Transposes the alignment, making query the target and vice versa.
- **Input**: Axt format alignment file.
- **Output**: Axt format alignment with swapped sequences.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment processing, comparative genomics, data manipulation.

## Pitfalls

- **Format Requirements**: Requires proper axt format.
- **Strand Handling**: May require strand adjustment.

## Examples

### Swap alignment
**Args:** `axtSwap input.axt output.axt`
**Explanation:** Swap target and query in axt alignment.

### With strand
**Args:** `axtSwap -strand + input.axt output.axt`
**Explanation:** Swap alignment with strand consideration.
