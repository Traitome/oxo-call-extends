---
name: ucsc-chainantirepeat
category: utility
description: UCSC chainAntiRepeat - Tool for removing repeat elements from chain alignments.
tags: [ucsc-chainantirepeat, ucsc, chain-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chainAntiRepeat - A tool for filtering out repeat elements from chain alignments.
- **Core Function**: Removes alignments that map to repeat regions.
- **Input**: Chain alignment file, repeat mask file.
- **Output**: Filtered chain file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment filtering, repeat masking, genome comparison.

## Pitfalls

- **Repeat Mask Format**: Requires proper repeat mask format.
- **Memory**: May require significant memory for large files.

## Examples

### Filter repeats
**Args:** `chainAntiRepeat chain.txt repeats.bed > filtered.chain`
**Explanation:** Remove repeat-containing alignments.

### With soft mask
**Args:** `chainAntiRepeat -soft chain.txt repeats.bed > filtered.chain`
**Explanation:** Soft-mask repeat regions.
