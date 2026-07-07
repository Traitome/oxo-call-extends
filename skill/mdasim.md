---
name: mdasim
category: utility
description: MDAsim simulates whole genome amplification (WGA) processes for sequencing data.
tags: [mdasim, simulation, whole-genome-amplification]
author: oxo-call-community
source_url: "https://github.com/hzi-bifo/mdasim"
---

## Concepts

- **Tool Overview**: MDAsim simulates whole genome amplification processes.
- **Core Function**: Models MDA (Multiple Displacement Amplification).
- **Amplification Simulation**: Simulates DNA amplification bias.
- **Error Modeling**: Models amplification errors and biases.
- **Input/Output**: Accepts reference genomes, produces simulated reads.
- **Installation**: `conda install -c bioconda mdasim`

## Pitfalls

- **Parameter Complexity**: Many parameters require careful tuning.
- **Simulation Accuracy**: Results depend on parameter choices.
- **Memory Requirements**: Large genomes require memory.
- **Computation Time**: Slow for complex simulations.
- **Model Assumptions**: Simplified models may not capture all complexities.
- **Output Size**: Large output files for high coverage simulations.

## Examples

### Simulate MDA
**Args:** `mdasim -r ref.fasta -o simulated.fastq`
**Explanation:** Simulates MDA from reference genome.

### With coverage
**Args:** `mdasim -r ref.fasta -c 30 -o simulated.fastq`
**Explanation:** Simulates with 30x coverage.

### Error rate
**Args:** `mdasim -r ref.fasta -e 0.001 -o simulated.fastq`
**Explanation:** Sets error rate to 0.001.

### Paired-end reads
**Args:** `mdasim -r ref.fasta -p -o simulated_`
**Explanation:** Generates paired-end reads.

### Help documentation
**Args:** `mdasim --help`
**Explanation:** Displays available options.
