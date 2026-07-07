---
name: cycsim
category: qc
description: A context-based long-read simulator
tags: [cycsim, qc, long-reads, simulation, nanopore]
author: oxo-call-community
source_url: "https://github.com/BioEarthDigital/CycSim/blob/main/README.md"
---

## Concepts

- **Tool Overview**: cycsim (v1.0.4+) is a context-based long-read simulator for generating realistic sequencing reads.
- **Core Function**: Simulates long reads with context-dependent error profiles mimicking real sequencing data.
- **Input/Output**: Input: Reference FASTA, configuration files. Output: Simulated FASTQ reads, truth data.
- **Algorithm**: Uses context-aware error models to generate more realistic sequencing errors.
- **Key Features**: Context-dependent errors, supports multiple sequencing platforms, generates truth alignments.
- **Installation**: `conda install -c bioconda cycsim`

## Pitfalls

- **Reference Quality**: Requires high-quality reference sequences for accurate simulation.
- **Parameter Tuning**: Error model parameters require adjustment for specific use cases.
- **Performance**: Generating large datasets can be computationally intensive.
- **Realism vs Speed**: Higher realism may require longer computation time.
- **Validation**: Simulated data should be validated against real sequencing data.

## Examples

### Simulate long reads
**Args:** `cycsim -i reference.fasta -o simulated_reads.fastq`
**Explanation:** Generate context-aware simulated long reads from reference.

### Specify coverage
**Args:** `cycsim -i reference.fasta -o reads.fastq --coverage 30`
**Explanation:** Generate 30x coverage of simulated reads.

### Output truth alignments
**Args:** `cycsim -i reference.fasta -o reads.fastq --truth truth.bam`
**Explanation:** Generate reads along with truth alignment file.
