---
name: nanosim
category: utility
description: NanoSim is a fast and scalable read simulator for Nanopore sequencing data with realistic error profiles.
tags: [nanosim, utility, simulation, nanopore, reads]
author: oxo-call-community
source_url: "https://github.com/BirolLab/NanoSim"
---

## Concepts

- **Tool Overview**: NanoSim v3.2.3 is a fast and scalable read simulator designed specifically for Oxford Nanopore sequencing data.
- **Core Function**: Generates simulated Nanopore reads with realistic error profiles based on trained machine learning models.
- **Algorithm**: Uses a two-stage process - first characterizes real reads to build statistical models, then simulates reads using these models.
- **Input Format**: Requires FASTA reference sequences and optional FASTQ reads for model training.
- **Output**: Produces simulated FASTQ reads with quality scores matching real Nanopore sequencing characteristics.
- **Use Case**: Validating bioinformatics pipelines, benchmarking assembly tools, generating training data for machine learning.

## Pitfalls

- **Model Training Time**: Characterizing large datasets can be time-consuming.
- **Version Compatibility**: Model files may not be compatible across different versions.
- **Reference Dependence**: Simulation quality depends heavily on reference sequence quality.
- **Computational Resources**: Large-scale simulations require significant memory and processing power.
- **Error Rate Variability**: Simulated error rates may not perfectly match specific sequencing runs.
- **Limited Platform Support**: May not fully simulate newer ONT platforms like PromethION.

## Examples

### Display help
**Args:** `nanosim --help`
**Explanation:** Shows available options and usage instructions.

### Characterize reads for model training
**Args:** `read_analysis.py characterize -i reads.fastq -r reference.fasta -o characterization_output`
**Explanation:** Analyzes real Nanopore reads to build error model parameters.

### Simulate reads with trained model
**Args:** `simulator.py reads -c characterization_output -r reference.fasta -o simulated_reads`
**Explanation:** Generates simulated Nanopore reads using the trained model.

### Simulate with specific read length
**Args:** `simulator.py reads -c char_output -r ref.fasta --avg-len 5000 -o long_reads`
**Explanation:** Simulates reads with average length of 5000bp.

### Generate paired-end reads
**Args:** `simulator.py reads -c char_output -r ref.fasta --paired -o paired_output`
**Explanation:** Simulates paired-end reads with realistic fragment sizes.

### Batch simulation
**Args:** `simulator.py reads -c char_output -r ref.fasta -n 100000 -o batch_output`
**Explanation:** Simulates 100,000 reads in a single batch.