---
name: curesim
category: utility
description: CuReSim - Customized Read Simulator for synthetic sequencing reads
tags: [curesim, utility, read-simulation, sequencing, synthetic-data]
author: oxo-call-community
source_url: "http://www.pegase-biosciences.com/curesim-a-customized-read-simulator/"
---

## Concepts

- **Tool Overview**: curesim (v1.3+) is a customized read simulator that generates synthetic next-generation sequencing reads.
- **Core Function**: Simulates sequencing reads from reference genomes with customizable error profiles and sequencing parameters.
- **Input/Output**: Input: Reference FASTA, configuration file. Output: Synthetic FASTQ reads, alignment truth data.
- **Supported Platforms**: Illumina, Ion Torrent, PacBio, Oxford Nanopore sequencing simulations.
- **Key Features**: Customizable error models, supports paired-end and single-end reads, generates truth alignments.
- **Installation**: `conda install -c bioconda curesim`

## Pitfalls

- **Configuration Complexity**: Many parameters require careful tuning for realistic simulations.
- **Reference Indexing**: Reference genome must be indexed before simulation.
- **Error Models**: Default error models may not match specific sequencing platforms.
- **Memory Usage**: Simulating large genomes may require significant memory.
- **Output Size**: Generated read files can be large; manage disk space carefully.

## Examples

### Simulate Illumina reads
**Args:** `curesim -r reference.fasta -o reads/ --platform illumina --read-length 150`
**Explanation:** Simulate 150bp Illumina paired-end reads from reference genome.

### Simulate nanopore reads
**Args:** `curesim -r reference.fasta -o nanopore_reads/ --platform nanopore --coverage 30`
**Explanation:** Simulate 30x coverage nanopore reads with realistic error profile.

### Generate truth alignments
**Args:** `curesim -r reference.fasta -o reads/ --truth-alignments`
**Explanation:** Generate synthetic reads along with truth alignment information.
