---
name: scrm
category: population-genomics
description: scrm - Coalescent simulator for genome-scale sequences
tags: ["scrm", "population-genomics", "coalescent", "simulation"]
author: oxo-call-community
source_url: "https://scrm.github.io/"
---

## Concepts

- **Tool Overview**: scrm (v1.7.4) is a coalescent simulator for genome-scale sequences.
- **Core Function**: Simulates genetic sequences under the coalescent model.
- **Algorithm**: Uses coalescent theory to simulate evolutionary history.
- **Input/Output**: Accepts simulation parameters and produces FASTA sequences.
- **Genome-Scale**: Designed for simulating large genomic regions.
- **Applications**: Population genetics, evolutionary biology, and method testing.

## Pitfalls

- **Computational Resources**: May require significant compute resources for large simulations.
- **Memory Usage**: High memory requirements for large population sizes.
- **Parameter Understanding**: Requires understanding of coalescent theory.
- **Simulation Time**: May have long run times for complex scenarios.
- **Output Size**: Large output files may require significant storage.
- **Model Assumptions**: Assumes idealized population models.

## Examples

### Basic simulation
**Args:** `scrm 10 1 -t 1000 -o seqs.fasta`
**Explanation:** Simulates 10 sequences of length 1000.

### Multiple loci
**Args:** `scrm 10 2 -t 1000 -r 1e-8 10000 -o seqs.fasta`
**Explanation:** Simulates 2 loci with recombination.

### Population growth
**Args:** `scrm 10 1 -t 1000 -eG 0.5 10 -o seqs.fasta`
**Explanation:** Simulates exponential population growth.

### Migration
**Args:** `scrm 10 10 2 -t 1000 -m 0.1 0.1 -o seqs.fasta`
**Explanation:** Simulates migration between 2 populations.

### Verbose logging
**Args:** `scrm 10 1 -t 1000 -v -o seqs.fasta`
**Explanation:** `-v` enables verbose output for debugging.

### Output VCF
**Args:** `scrm 10 1 -t 1000 --vcf -o variants.vcf`
**Explanation:** Outputs VCF format instead of FASTA.

### Seed for reproducibility
**Args:** `scrm 10 1 -t 1000 -seed 12345 -o seqs.fasta`
**Explanation:** `-seed` sets random seed for reproducibility.