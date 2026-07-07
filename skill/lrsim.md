---
name: lrsim
category: utility
description: Simulator for 10X Genomics Linked Reads
tags: [lrsim, utility, simulation, linked-reads]
author: oxo-call-community
source_url: "https://github.com/aquaskyline/LRSIM"
---

## Concepts

- **Tool Overview**: lrsim v1.0 simulates 10X Genomics linked-reads from a reference genome.
- **Core Function**: Generates synthetic barcoded reads mimicking the 10X Genomics library preparation process.
- **Barcode Simulation**: Creates realistic barcode distributions and attachment points.
- **Input/Output**: Input: Reference genome in FASTA format; Output: Simulated FASTQ reads with barcode information.
- **Installation**: `conda install -c bioconda lrsim`
- **Applications**: Testing linked-read analysis pipelines, benchmarking variant callers, and method development.

## Pitfalls

- **Reference Quality**: Simulation accuracy depends on reference genome quality.
- **Barcode Complexity**: Real-world barcode distributions may differ from simulation.
- **Read Length Distribution**: Default parameters may not match specific sequencing runs.
- **Memory Usage**: Simulating large genomes requires significant memory.
- **Computation Time**: Generating high-coverage simulations can be slow.
- **Error Model**: Does not perfectly replicate real sequencing errors and biases.

## Examples

### Simulate linked reads
**Args:** `lrsim -r reference.fasta -o simulated_reads.fastq`
**Explanation:** Simulates 10X Genomics linked reads from reference.

### Coverage
**Args:** `lrsim -r reference.fasta -o simulated_reads.fastq -c 30`
**Explanation:** Sets coverage to 30x.

### Read length
**Args:** `lrsim -r reference.fasta -o simulated_reads.fastq -l 150`
**Explanation:** Sets read length to 150bp.

### Number of barcodes
**Args:** `lrsim -r reference.fasta -o simulated_reads.fastq -b 100000`
**Explanation:** Uses 100,000 unique barcodes.

### Insert size
**Args:** `lrsim -r reference.fasta -o simulated_reads.fastq -i 500`
**Explanation:** Sets mean insert size to 500bp.

### Help documentation
**Args:** `lrsim --help`
**Explanation:** Displays all available options and parameters.