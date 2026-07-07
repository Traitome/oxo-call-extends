---
name: simlord
category: utility
description: SimLoRD - Long read simulator for third-generation sequencing
tags: ["simlord", "utility", "simulation", "long-read"]
author: oxo-call-community
source_url: "https://bitbucket.org/genomeinformatics/simlord/"
---

## Concepts

- **Tool Overview**: SimLoRD (v1.0.4) simulates long reads from third-generation sequencing.
- **Core Function**: Generates synthetic long reads with realistic error models.
- **Algorithm**: Uses Pacific Biosciences SMRT error model for simulation.
- **Input/Output**: Accepts FASTA sequences and produces simulated FASTQ reads.
- **Read Simulation**: Specialized for long-read sequencing simulation.
- **Applications**: Algorithm testing, benchmarking, and method development.

## Pitfalls

- **Memory Usage**: High memory requirements for large genomes.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for realistic simulation.
- **Error Model**: Limited to specific sequencing technologies.
- **Version Compatibility**: Legacy software, may have compatibility issues.
- **Documentation**: Limited documentation available.

## Examples

### Simulate reads
**Args:** `simlord -g genome.fasta -o simulated_reads.fastq`
**Explanation:** `-g` input genome; `-o` output FASTQ.

### With coverage
**Args:** `simlord -g genome.fasta -c 30 -o simulated_reads.fastq`
**Explanation:** `-c 30` target coverage.

### With read length
**Args:** `simlord -g genome.fasta -l 10000 -o simulated_reads.fastq`
**Explanation:** `-l 10000` average read length.

### Help command
**Args:** `simlord --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `simlord --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `simlord -v -g genome.fasta -o simulated_reads.fastq`
**Explanation:** `-v` verbose output.

### Paired-end mode
**Args:** `simlord -g genome.fasta -p -o simulated/`
**Explanation:** `-p` paired-end simulation.
