---
name: boquila
category: utility
description: NGS read simulator to eliminate read nucleotide bias
tags: [boquila, simulation, ngs, reads, bias-correction]
author: oxo-call-community
source_url: "https://github.com/CompGenomeLab/boquila"
---

## Concepts

- **Tool Overview**: Boquila is an NGS read simulator designed to eliminate nucleotide bias.
- **Core Function**: Simulates sequencing reads with realistic error profiles and reduced bias.
- **Input**: Reference genome FASTA file.
- **Output**: Simulated FASTQ reads with quality scores.
- **Features**: Models sequencing errors and coverage bias.
- **Installation**: Install via bioconda: `conda install -c bioconda boquila`

## Pitfalls

- **Coverage Setting**: Adjust coverage depth based on simulation needs.
- **Read Length**: Choose appropriate read length for target sequencing platform.
- **Error Model**: Error profile should match intended sequencing technology.
- **Random Seed**: Set seed for reproducible simulations.

## Examples

### Simulate reads from genome
**Args:** `boquila -r genome.fa -o simulated.fq`
**Explanation:** Generates simulated reads from reference genome.

### Set coverage and read length
**Args:** `boquila -r genome.fa -c 30 -l 150 -o simulated.fq`
**Explanation:** Simulates 30x coverage of 150bp reads.

### Set random seed
**Args:** `boquila -r genome.fa -s 12345 -o simulated.fq`
**Explanation:** Uses fixed seed for reproducible read simulation.

### Output paired-end reads
**Args:** `boquila -r genome.fa --paired -o simulated`
**Explanation:** Generates paired-end simulated reads as R1 and R2 files.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
