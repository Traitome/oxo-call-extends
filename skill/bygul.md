---
name: bygul
category: utility
description: Amplicon read simulator with customizable sample proportions
tags: [bygul, simulation, amplicon, reads]
author: oxo-call-community
source_url: "https://github.com/andersen-lab/Bygul"
---

## Concepts

- **Tool Overview**: Bygul simulates amplicon sequencing reads with customizable sample proportions.
- **Core Function**: Generates simulated amplicon reads with user-defined abundance profiles.
- **Input**: Reference sequences and abundance/proportion specifications.
- **Output**: Simulated FASTQ reads with realistic error profiles.
- **Application**: Benchmarking amplicon analysis pipelines.
- **Installation**: Install via bioconda: `conda install -c bioconda bygul`

## Pitfalls

- **Amplicon Mode**: Designed for amplicon sequencing simulation.
- **Error Model**: Error profile may not match all sequencing platforms.
- **Random Seed**: Set seed for reproducible simulations.

## Examples

### Simulate amplicon reads
**Args:** `bygul -i references.fa -p proportions.tsv -o simulated.fq`
**Explanation:** Simulates amplicon reads with specified sample proportions.

### Set read length
**Args:** `bygul -i refs.fa -p props.tsv -l 250 -o sim.fq`
**Explanation:** Simulates 250bp amplicon reads.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
