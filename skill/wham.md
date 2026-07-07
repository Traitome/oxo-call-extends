---
name: wham
category: bioinformatics
description: WHAM - Structural variant caller.
tags: [wham, structural-variants, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/zeeev/wham"
---

## Concepts

- **Tool Overview**: WHAM - Whole-genome alignment-based SV caller.
- **Core Function**: Calls structural variants from alignment data.
- **Input**: BAM file.
- **Output**: SV calls.
- **Installation**: Install via conda or source
- **Use Case**: Variant analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large BAM files.
- **Complexity**: May have steep learning curve.

## Examples

### Call SVs
**Args:** `whamg -f ref.fasta -b input.bam -o svs.vcf`
**Explanation:** Call structural variants.

### With options
**Args:** `whamg -f ref.fasta -b input.bam -o svs.vcf -t 8`
**Explanation:** Use 8 threads.
