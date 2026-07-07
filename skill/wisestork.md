---
name: wisestork
category: bioinformatics
description: Wisestork - Structural variant detection.
tags: [wisestork, structural-variants, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/wisestork/"
---

## Concepts

- **Tool Overview**: Wisestork - Structural variant detection tool.
- **Core Function**: Detects structural variants.
- **Input**: BAM file.
- **Output**: SV calls.
- **Installation**: Install via pip or conda
- **Use Case**: Variant analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large BAM files.
- **Complexity**: May have steep learning curve.

## Examples

### Detect SVs
**Args:** `wisestork -i input.bam -o svs.vcf`
**Explanation:** Detect structural variants.

### With options
**Args:** `wisestork -i input.bam -o svs.vcf -t 8`
**Explanation:** Use 8 threads.
