---
name: dwgsim
category: utility
description: "Whole Genome Simulator for Next-Generation Sequencing."
tags: [dwgsim, utility, read-simulation, NGS, benchmarking]
author: oxo-call-community
source_url: "https://github.com/nh13/DWGSIM"
---

## Concepts

- **Tool Overview**: DWGSIM is a whole genome simulator for next-generation sequencing reads.
- **Core Function**: Simulates Illumina and SOLiD sequencing reads from a reference genome with realistic error models.
- **Input/Output**: Input: Reference genome (FASTA). Output: Simulated reads (FASTQ), mutation files.
- **Algorithm**: Uses empirical error models to generate realistic sequencing reads.
- **Key Features**: Paired-end simulation, indel simulation, base quality scores, customizable error rates.
- **Installation**: `conda install -c bioconda dwgsim`

## Pitfalls

- **Reference Quality**: Simulation accuracy depends on reference genome quality.
- **Error Models**: Default error models may not match specific sequencing platforms.
- **Coverage Depth**: High coverage simulations require significant disk space.
- **Random Seed**: Different random seeds produce different read sets.
- **Read Length**: Very long reads may not be supported for all platforms.

## Examples

### Basic read simulation
**Args:** `-d 30 -N 1000000 -1 100 -2 100 ref.fa output_prefix`
**Explanation:** Simulates 30x coverage paired-end 100bp reads from reference genome.

### With mutations
**Args:** `-d 30 -N 1000000 -1 100 -2 100 -r 0.001 -R 0.1 -X 0.1 ref.fa output_prefix`
**Explanation:** Simulates reads with SNP rate 0.1%, indel rate 0.1%, and structural variation rate 0.1%.

### Single-end reads
**Args:** `-d 30 -N 1000000 -1 150 ref.fa output_prefix`
**Explanation:** Simulates single-end 150bp reads.

### Custom error rate
**Args:** `-d 30 -N 1000000 -1 100 -2 100 -e 0.01 ref.fa output_prefix`
**Explanation:** Sets per-base error rate to 1%.

### Outer distance
**Args:** `-d 30 -N 1000000 -1 100 -2 100 -s 300 -o 1 ref.fa output_prefix`
**Explanation:** Sets outer distance to 300bp with standard deviation of 1.