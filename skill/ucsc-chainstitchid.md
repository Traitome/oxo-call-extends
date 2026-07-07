---
name: ucsc-chainstitchid
category: utility
description: UCSC chainStitchId - Tool for stitching chain alignments.
tags: [ucsc-chainstitchid, ucsc, chain-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC chainStitchId - A tool for stitching together chain alignments.
- **Core Function**: Connects fragmented chain alignments.
- **Input**: Chain alignment file.
- **Output**: Stitched chain file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Alignment reconstruction, gap filling, genome comparison.

## Pitfalls

- **Overlap Requirement**: Requires overlapping alignments.
- **Memory**: May require significant memory for large files.

## Examples

### Stitch chains
**Args:** `chainStitchId input.chain > stitched.chain`
**Explanation:** Stitch together fragmented chain alignments.

### With tolerance
**Args:** `chainStitchId -tolerance=100 input.chain > stitched.chain`
**Explanation:** Stitch with position tolerance.
