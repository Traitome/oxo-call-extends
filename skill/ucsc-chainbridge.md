---
name: ucsc-chainbridge
category: utility
description: UCSC chainBridge - Tool for bridging chain alignments.
tags: [ucsc-chainbridge, ucsc, chain-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chainBridge - A tool for bridging gaps in chain alignments.
- **Core Function**: Connects fragmented chain alignments across gaps.
- **Input**: Chain alignment file.
- **Output**: Bridged chain file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment improvement, gap filling, genome comparison.

## Pitfalls

- **Gap Size**: May not handle large gaps properly.
- **Memory**: May require significant memory for large files.

## Examples

### Bridge chains
**Args:** `chainBridge input.chain > bridged.chain`
**Explanation:** Bridge gaps in chain alignments.

### With max gap
**Args:** `chainBridge -maxGap=1000 input.chain > bridged.chain`
**Explanation:** Bridge gaps up to specified size.
