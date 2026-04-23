---
name: bwise
category: assembly
description: De Bruijn assembly Workflow using Integral information of Short paired-End reads
tags: [bwise, assembly, debruijn, paired-end]
author: oxo-call-community
source_url: "https://github.com/Malfoy/BWISE"
---

## Concepts

- **Tool Overview**: BWISE is a de Bruijn graph assembler for short paired-end reads.
- **Core Function**: Assembles genomes using paired-end information for improved contiguity.
- **Algorithm**: De Bruijn graph approach with integrated paired-end information.
- **Input**: Paired-end FASTQ files.
- **Output**: Assembled contigs in FASTA format.
- **Installation**: Install via bioconda: `conda install -c bioconda bwise`

## Pitfalls

- **Paired-End Required**: Requires paired-end data; single-end not supported.
- **K-mer Selection**: Choose appropriate k-mer size based on coverage and genome complexity.
- **Memory Usage**: Large genomes require significant memory.
- **Coverage**: Low coverage reduces assembly quality.

## Examples

### Assemble paired-end reads
**Args:** `bwise -1 R1.fq -2 R2.fq -k 31 -o assembly.fa`
**Explanation:** Assembles paired-end reads using 31-mer size.

### Set k-mer size
**Args:** `bwise -1 R1.fq -2 R2.fq -k 41 -o assembly.fa`
**Explanation:** Uses 41-mer for assembly of complex genome.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
