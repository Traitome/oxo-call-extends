---
name: unimap
category: alignment
description: UniMap - Ultra-fast sequence aligner.
tags: [unimap, sequence-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/lh3/unimap"
---

## Concepts

- **Tool Overview**: UniMap - An ultra-fast sequence aligner for short reads.
- **Core Function**: Aligns sequencing reads to reference genome.
- **Input**: Reference genome (FASTA), reads (FASTQ).
- **Output**: Alignments (SAM/BAM).
- **Installation**: Install via conda or source
- **Use Case**: Read alignment, variant calling, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Index Building**: Requires indexed reference genome.

## Examples

### Align reads
**Args:** `unimap -d ref.mmi ref.fasta && unimap ref.mmi reads.fastq > alignments.sam`
**Explanation:** Build index and align reads.

### With options
**Args:** `unimap -t 8 ref.mmi reads.fastq > alignments.sam`
**Explanation:** Use 8 threads.
