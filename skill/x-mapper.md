---
name: x-mapper
category: bioinformatics
description: X-Mapper - Sequence mapping tool.
tags: [x-mapper, sequence-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/x-mapper/"
---

## Concepts

- **Tool Overview**: X-Mapper - Sequence mapping tool.
- **Core Function**: Maps sequences to reference.
- **Input**: FASTQ reads.
- **Output**: SAM/BAM file.
- **Installation**: Install via conda or source
- **Use Case**: Sequence alignment, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Complexity**: May have steep learning curve.

## Examples

### Map reads
**Args:** `x-mapper -i reads.fastq -r ref.fasta -o alignment.sam`
**Explanation:** Map reads to reference.

### With options
**Args:** `x-mapper -i reads.fastq -r ref.fasta -o alignment.sam -t 8`
**Explanation:** Use 8 threads.
