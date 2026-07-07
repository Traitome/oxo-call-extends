---
name: yaha
category: bioinformatics
description: YAHA - Sequence aligner.
tags: [yaha, sequence-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/yaha/"
---

## Concepts

- **Tool Overview**: YAHA - Fast sequence aligner.
- **Core Function**: Aligns sequences to reference.
- **Input**: FASTQ reads.
- **Output**: SAM/BAM file.
- **Installation**: Install via conda or source
- **Use Case**: Sequence alignment, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Complexity**: May have steep learning curve.

## Examples

### Align reads
**Args:** `yaha -i reads.fastq -r ref.fasta -o alignment.sam`
**Explanation:** Align reads.

### With options
**Args:** `yaha -i reads.fastq -r ref.fasta -o alignment.sam -t 8`
**Explanation:** Use 8 threads.
