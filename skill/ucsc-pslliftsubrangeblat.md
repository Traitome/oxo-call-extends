---
name: ucsc-pslliftsubrangeblat
category: utility
description: UCSC pslLiftSubrangeBlat - Tool for lifting subrange BLAT alignments.
tags: [ucsc-pslliftsubrangeblat, ucsc, psl, lift, blat, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslLiftSubrangeBlat - A tool for lifting subrange BLAT alignments.
- **Core Function**: Lifts subrange alignments to target coordinates.
- **Input**: PSL file, chain file.
- **Output**: Lifted PSL file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Liftover, coordinate conversion, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL/chain format.

## Examples

### Lift subrange BLAT
**Args:** `pslLiftSubrangeBlat input.psl chain.txt > lifted.psl`
**Explanation:** Lift subrange BLAT alignments.

### With options
**Args:** `pslLiftSubrangeBlat -verbose input.psl chain.txt > lifted.psl`
**Explanation:** Lift with verbose output.
