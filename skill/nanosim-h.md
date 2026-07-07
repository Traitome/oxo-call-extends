---
name: nanosim-h
category: utility
description: NanoSim-H is a simulator of Oxford Nanopore reads that captures the technology-specific features of ONT data with homopolymer-aware modeling.
tags: [nanosim-h, utility, simulation, nanopore, homopolymer]
author: oxo-call-community
source_url: "https://github.com/karel-brinda/NanoSim-H"
---

## Concepts

- **Tool Overview**: NanoSim-H v1.1.0.4 is a specialized Oxford Nanopore read simulator with enhanced homopolymer-aware error modeling.
- **Core Function**: Simulates Nanopore reads capturing ONT-specific features including accurate homopolymer length errors and strand bias.
- **Algorithm**: Uses a two-step approach - characterization of real reads to build error models, then simulation using those models.
- **Input Format**: Accepts FASTA reference sequences and trained model profiles from real Nanopore data.
- **Output**: Produces simulated FASTQ reads with realistic error profiles matching ONT sequencing characteristics.
- **Use Case**: Benchmarking assembly and variant calling pipelines, testing bioinformatics tools on controlled datasets.

## Pitfalls

- **Model Dependence**: Simulation accuracy depends heavily on the quality of the trained model.
- **Homopolymer Bias**: May over-represent homopolymer errors if model is not properly trained.
- **Computational Cost**: Characterization step can be computationally intensive for large datasets.
- **Version Compatibility**: Model files generated with different versions may not be compatible.
- **Reference Requirements**: Requires high-quality reference sequences for accurate simulation.
- **Memory Usage**: Can consume significant memory when simulating large genomes.

## Examples

### Display help
**Args:** `nanosim-h --help`
**Explanation:** Shows available options and parameters.

### Train model from real reads
**Args:** `nanosim-h train -i real_reads.fastq -r reference.fasta -o model_profile`
**Explanation:** Characterizes real Nanopore reads to build an error model.

### Basic simulation
**Args:** `nanosim-h simulate -c model_profile -r reference.fasta -o simulated_reads`
**Explanation:** Simulates Nanopore reads using trained homopolymer-aware model.

### Specify read count
**Args:** `nanosim-h simulate -c model_profile -r ref.fasta -n 5000 -o output`
**Explanation:** Simulates exactly 5,000 reads from the reference sequence.

### Quality filtering simulation
**Args:** `nanosim-h simulate -c model_profile -r ref.fasta -q 10 -o high_quality_reads`
**Explanation:** Simulates reads with minimum quality score of Q10.

### Paired-end simulation
**Args:** `nanosim-h simulate -c model_profile -r ref.fasta --paired -o paired_reads`
**Explanation:** Simulates paired-end reads with realistic insert sizes.