---
name: wgsim
category: bioinformatics
description: wgsim - Whole-genome sequencing read simulator.
tags: [wgsim, sequence-simulation, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/lh3/wgsim"
---

## Concepts

- **Tool Overview**: wgsim - Sequencing read simulator.
- **Core Function**: Simulates sequencing reads from reference genome.
- **Input**: Reference genome.
- **Output**: Simulated FASTQ reads.
- **Installation**: Install via conda or source
- **Use Case**: Simulation, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Complexity**: May have steep learning curve.

## Examples

### Simulate reads
**Args:** `wgsim -1 100 -2 100 ref.fasta read1.fq read2.fq`
**Explanation:** Simulate paired-end reads.

### With options
**Args:** `wgsim -e 0.01 -d 500 ref.fasta read1.fq read2.fq`
**Explanation:** Simulate with 1% error rate.
