---
name: ngsngs
category: utility
description: NGSNGS is a sequencing simulator for generating synthetic NGS data.
tags: [ngsngs, utility, simulation, sequencing]
author: oxo-call-community
source_url: "https://github.com/rahenriksen/ngsngs"
---

## Concepts

- **Tool Overview**: NGSNGS simulates next-generation sequencing data for testing and validation.
- **Core Function**: Generates synthetic sequencing reads with realistic characteristics.
- **Algorithm**: Models sequencing errors, biases, and coverage patterns.
- **Input Format**: Accepts reference genomes and simulation parameters.
- **Output**: Produces synthetic FASTQ files and variant data.
- **Use Case**: Pipeline testing, benchmarking, and method validation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Genome**: Requires FASTA reference genome.
- **Memory Usage**: Large genomes require memory.
- **Computational Cost**: Simulation can be computationally intensive.
- **Parameter Tuning**: Requires careful parameter optimization.
- **Realism**: Simulated data may not perfectly match real sequencing.

## Examples

### Display help
**Args:** `ngsngs --help`
**Explanation:** Shows available options and usage instructions.

### Basic simulation
**Args:** `ngsngs -r reference.fasta -o output/`
**Explanation:** Generates synthetic reads from reference.

### Specify coverage
**Args:** `ngsngs -r reference.fasta -c 30 -o output/`
**Explanation:** Generates 30x coverage.

### Paired-end reads
**Args:** `ngsngs -r reference.fasta -p -o output/`
**Explanation:** Generates paired-end reads.

### Error rate
**Args:** `ngsngs -r reference.fasta -e 0.01 -o output/`
**Explanation:** Sets error rate to 1%.

### Insert size
**Args:** `ngsngs -r reference.fasta -i 300 -o output/`
**Explanation:** Sets average insert size to 300bp.

### Threads
**Args:** `ngsngs -r reference.fasta -t 8 -o output/`
**Explanation:** Uses 8 threads for parallel processing.