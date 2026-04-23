---
name: nanosim-h
category: utility
description: NanoSim-H is a simulator of Oxford Nanopore reads that captures the technology-specific features of ONT data.
tags: [nanosim-h, utility, simulation, nanopore, homopolymer]
author: oxo-call-community
source_url: "https://github.com/karel-brinda/NanoSim-H"
---

## Concepts

- **Tool Overview**: NanoSim-H v1.1.0.4 - Nanopore read simulator with homopolymer-aware modeling.
- **Core Function**: Simulates Nanopore reads capturing ONT-specific features including homopolymer errors.
- **Input/Output**: Takes reference and trained model; outputs simulated Nanopore reads.
- **Installation**: `conda install -c bioconda nanosim-h`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Model Training**: Requires characterization step for model training.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-c model_profile -r reference.fasta -o simulated_reads`
**Explanation:** Simulates Nanopore reads with homopolymer-aware error model.
