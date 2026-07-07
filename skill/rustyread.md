---
name: rustyread
category: simulation
description: Rustyread - a long-read sequencing simulator.
tags: ["rustyread", "long reads", "simulation", "PacBio", "ONT"]
author: oxo-call-community
source_url: "https://github.com/natir/rustyread"
---

## Concepts

- **Tool Overview**: rustyread (v0.4.1) is a fast long-read sequencing simulator that generates synthetic reads from reference genomes. It simulates both PacBio and Oxford Nanopore sequencing technologies.
- **Core Function**: Generates realistic long reads with characteristic error profiles for different sequencing platforms. Supports various error models and read length distributions.
- **Algorithm**: Uses statistical models to simulate read errors (substitutions, insertions, deletions) and read length distributions based on real sequencing data characteristics.
- **Input Format**: FASTA reference genome sequence, optional configuration file for error models.
- **Output Format**: FASTQ files with simulated reads, optionally with read alignments in SAM format.
- **Use Case**: Testing assembly algorithms, benchmarking variant callers, validating bioinformatics pipelines, teaching and training purposes.

## Pitfalls

- **Reference requirements**: Requires complete reference genome for simulation.
- **Error model limitations**: Error models may not perfectly match real sequencing data.
- **Computational time**: Simulating large genomes with many reads can be time-consuming.
- **Memory usage**: Storing large reference genomes requires significant memory.
- **Read length distribution**: Default distributions may not match specific sequencing runs.
- **Coverage uniformity**: Simulated coverage may not perfectly match real sequencing coverage patterns.

## Examples

### Basic read simulation
**Args:** `rustyread -r reference.fasta -o reads.fastq -n 10000`
**Explanation:** `-r` reference genome; `-o` output FASTQ; `-n` number of reads to simulate.

### Simulate PacBio reads
**Args:** `rustyread -r reference.fasta -o reads.fastq -p pacbio -n 5000`
**Explanation:** `-p` platform type (pacbio/ont).

### Specify read length
**Args:** `rustyread -r reference.fasta -o reads.fastq -l 10000 -n 1000`
**Explanation:** `-l` mean read length.

### With error rate
**Args:** `rustyread -r reference.fasta -o reads.fastq -e 0.02 -n 5000`
**Explanation:** `-e` overall error rate.

### Output SAM alignments
**Args:** `rustyread -r reference.fasta -o reads.fastq --sam alignments.sam -n 1000`
**Explanation:** `--sam` outputs alignment information.

### Paired-end simulation
**Args:** `rustyread -r reference.fasta -o reads.fastq --paired -n 5000`
**Explanation:** `--paired` generates paired-end reads.

### Custom error model
**Args:** `rustyread -r reference.fasta -o reads.fastq --model custom.json -n 10000`
**Explanation:** `--model` uses custom error model from JSON file.
