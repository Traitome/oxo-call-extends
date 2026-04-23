---
name: last
category: alignment
description: LAST finds & aligns related regions of sequences.
tags: [last, alignment]
author: oxo-call-community
source_url: "https://gitlab.com/mcfrith/last"
---

## Concepts

- **Tool Overview**: last v1651 - LAST finds & aligns related regions of sequences. It is designed for moderately large data (e.g. genomes, DNA reads, proteomes).  It's especially good at: finding rearrangements and recombinations; finding DNA-versus-protein related regions; unusual data like AT-rich DNA; sensitive DNA-DNA search..
- **Core Function**: LAST finds & aligns related regions of sequences.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda last`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Index database
**Args:** `lastdb -uNEAR mydb reference.fasta`
**Explanation:** Builds LAST database with NEAR seeding scheme.

### Align reads
**Args:** `lastal -Q1 mydb reads.fastq > alignments.maf`
**Explanation:** Maps FASTQ reads against indexed database.

