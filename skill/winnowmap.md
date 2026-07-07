---
name: winnowmap
category: bioinformatics
description: Winnowmap - Long-read mapping tool.
tags: [winnowmap, sequence-alignment, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/marbl/Winnowmap"
---

## Concepts

- **Tool Overview**: Winnowmap - Long-read mapping tool.
- **Core Function**: Maps long reads to reference genome.
- **Input**: FASTQ reads.
- **Output**: SAM/BAM file.
- **Installation**: Install via conda or source
- **Use Case**: Sequence alignment, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Complexity**: May have steep learning curve.

## Examples

### Map reads
**Args:** `winnowmap -ax map-pb ref.fasta reads.fastq > alignment.sam`
**Explanation:** Map PacBio reads.

### With options
**Args:** `winnowmap -ax map-ont -t 8 ref.fasta reads.fastq > alignment.sam`
**Explanation:** Map ONT reads with 8 threads.
