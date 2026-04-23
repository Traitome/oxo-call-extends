---
name: nanosim
category: utility
description: NanoSim is a fast and scalable read simulator for Nanopore sequencing data.
tags: [nanosim, utility, simulation, nanopore, reads]
author: oxo-call-community
source_url: "https://github.com/BirolLab/NanoSim"
---

## Concepts

- **Tool Overview**: NanoSim v3.2.3 - fast and scalable Nanopore read simulator.
- **Core Function**: Simulates Nanopore reads with realistic error profiles based on trained models.
- **Input/Output**: Takes reference genome and trained model; outputs simulated Nanopore FASTQ reads.
- **Installation**: `conda install -c bioconda nanosim`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Model Training**: Requires a trained model for realistic simulation.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Characterize reads
**Args:** `read_analysis.py characterize -i reads.fastq -r reference.fasta -o characterization`
**Explanation:** Characterizes Nanopore reads for model training.

### Simulate reads
**Args:** `simulator.py reads -c characterization -r reference.fasta -o simulated`
**Explanation:** Simulates Nanopore reads using trained model.
