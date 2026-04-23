---
name: nanosimh
category: utility
description: NanoSimH is a fork of NanoSim, a fast and scalable read simulator that captures the technology-specific features of ONT data.
tags: [nanosimh, utility, simulation, nanopore, reads]
author: oxo-call-community
source_url: "https://github.com/karel-brinda/NanoSimH"
---

## Concepts

- **Tool Overview**: NanoSimH v1.0.1.8 - fork of NanoSim for Nanopore read simulation.
- **Core Function**: Simulates Nanopore reads capturing ONT-specific features with improvements over original NanoSim.
- **Input/Output**: Takes reference and model; outputs simulated Nanopore reads.
- **Installation**: `conda install -c bioconda nanosimh`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Model Training**: Requires characterization step for model training.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-c model_profile -r reference.fasta -o simulated_reads`
**Explanation:** Simulates Nanopore reads using trained model.
