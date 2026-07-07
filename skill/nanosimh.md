---
name: nanosimh
category: utility
description: NanoSimH is a fork of NanoSim, a fast and scalable read simulator that captures the technology-specific features of ONT data with improved performance.
tags: [nanosimh, utility, simulation, nanopore, reads]
author: oxo-call-community
source_url: "https://github.com/karel-brinda/NanoSimH"
---

## Concepts

- **Tool Overview**: NanoSimH v1.0.1.8 is a high-performance fork of the original NanoSim read simulator for Oxford Nanopore sequencing.
- **Core Function**: Simulates Nanopore reads with realistic error profiles, offering improved speed and scalability over the original.
- **Algorithm**: Implements optimized read simulation with Markov chain models for error generation and base quality scores.
- **Input Format**: Accepts FASTA reference sequences and optional trained model profiles from real sequencing data.
- **Output**: Produces simulated FASTQ reads with accurate quality scores matching real Nanopore characteristics.
- **Use Case**: Pipeline development, tool benchmarking, testing variant callers and assemblers on controlled data.

## Pitfalls

- **Version Differences**: Options may vary significantly between different versions.
- **Model Training**: Requires characterization step for optimal simulation accuracy.
- **Resource Intensive**: Large-scale simulations can require significant computational resources.
- **Reference Bias**: Simulation quality depends on reference sequence quality and completeness.
- **Memory Requirements**: May require substantial RAM for large genome simulations.
- **Learning Curve**: Understanding model parameters requires careful study of documentation.

## Examples

### Display help
**Args:** `nanosimh --help`
**Explanation:** Shows available options and usage instructions.

### Characterize reads for model training
**Args:** `nanosimh characterize -i real_reads.fastq -r reference.fasta -o model_output`
**Explanation:** Analyzes real Nanopore reads to generate error model parameters.

### Basic read simulation
**Args:** `nanosimh simulate -c model_output -r reference.fasta -o simulated_reads`
**Explanation:** Simulates Nanopore reads using the trained error model.

### Simulate with specific coverage
**Args:** `nanosimh simulate -c model_output -r ref.fasta -x 30 -o 30x_coverage`
**Explanation:** Simulates reads to achieve approximately 30x coverage of the reference.

### Single-end mode
**Args:** `nanosimh simulate -c model_output -r ref.fasta --single -o single_reads`
**Explanation:** Generates single-end reads instead of paired-end.

### Quality threshold filtering
**Args:** `nanosimh simulate -c model_output -r ref.fasta --min-q 8 -o filtered_reads`
**Explanation:** Filters simulated reads to minimum quality score of Q8.